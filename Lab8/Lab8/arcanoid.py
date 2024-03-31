import pygame
import random
pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

# Paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

# Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

# Catching sound
collision_sound = pygame.mixer.Sound('audio/catch.mp3')

# Function to detect collision
def detect_collision(dx, dy, ball, rect, is_breakable):
    if dx > 0:  # Ball is moving right
        delta_x = ball.right - rect.left
    else:  # Ball is moving left
        delta_x = rect.right - ball.left
    if dy > 0:  # Ball is moving down
        delta_y = ball.bottom - rect.top
    else:  # Ball is moving up
        delta_y = rect.bottom - ball.top

    if is_breakable:
        if abs(delta_x - delta_y) < 10:
            dx, dy = -dx, -dy
        elif delta_x > delta_y:
            dy *= -1
        else:
            dx *= -1
    else:  # Collision with unbreakable block
        if delta_x > delta_y:
            dy *= -1
        else:
            dx *= -1

    return dx, dy



# Block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
color_list = [(random.randrange(0, 255), random.randrange(0, 255),  random.randrange(0, 255)) for i in range(10) for j in range(4)]
unbreakable_blocks = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(2, 8) for j in range(1, 3)]  # Unbreakable blocks

# Game over screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# Win screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

time_elapsed = 0  # For increasing ball speed and shrinking paddle

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(bg)

    # Drawing blocks
    [pygame.draw.rect(screen, color_list[color], block) for color, block in enumerate(block_list)]
    [pygame.draw.rect(screen, (128, 128, 128), block) for block in unbreakable_blocks]  # Drawing unbreakable blocks
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    # Ball movement
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    # Collision with walls
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    if ball.centery < ballRadius + 50:
        dy = -dy

    # Collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle, False)  # False because paddle is unbreakable

    # Collision with blocks
    hitIndex = ball.collidelist(block_list)
    if hitIndex != -1:
        hitRect = block_list.pop(hitIndex)
        hitColor = color_list.pop(hitIndex)
        dx, dy = detect_collision(dx, dy, ball, hitRect, True)  # True because block is breakable
        game_score += 1
        collision_sound.play()

    # Collision with unbreakable blocks
    unbreakable_collision_index = ball.collidelist(unbreakable_blocks)
    if unbreakable_collision_index != -1:
        unbreakable_rect = unbreakable_blocks[unbreakable_collision_index]
        dx, dy = detect_collision(dx, dy, ball, unbreakable_rect, False)  # False because unbreakable block

    # Game score
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)

    # Win/lose screens
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255, 255, 255))
        screen.blit(wintext, wintextRect)

    # Paddle control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    # Increase ball speed and shrink paddle with time
    time_elapsed += 1
    if time_elapsed % (FPS * 30) == 0:  # Every 30 seconds
        ballSpeed += 1
        paddleW = max(50, paddleW - 10)
        paddle = pygame.Rect(paddle.left, paddle.top, paddleW, paddleH)

    pygame.display.flip()
    clock.tick(FPS)