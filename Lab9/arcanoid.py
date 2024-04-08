import pygame
import random

pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)
n = 15  # the medium speed
change_hard = 0  # variable for difficulty change

# Game states
GAME = 0
PAUSE_MENU = 1
SETTINGS_MENU = 2
game_state = GAME

# Paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle_color = (255, 255, 255)
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

# Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('georgia', 40)
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
unbreakable_blocks = [pygame.Rect(10 + 120 * random.randint(0, 9), 50 + 70 * random.randint(0, 3), 100, 50) for _ in range(5)]  # 5 random unbreakable blocks

block_list = []  # Start with an empty list for breakable blocks
for i in range(10):
    for j in range(4):
        new_block = pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50)
        # Only add the new block if it doesn't intersect with any unbreakable block
        if not any(new_block.colliderect(ub_block) for ub_block in unbreakable_blocks):
            block_list.append(new_block)

color_list = [(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)) for _ in range(len(block_list))]

# Bonus blocks
bonus_blocks = [pygame.Rect(10 + 120 * random.randint(0, 9), 50 + 70 * random.randint(0, 3), 100, 50) for _ in range(3)]  # 3 random bonus blocks

# Game over screen
losefont = pygame.font.SysFont('georgia', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# Win screen
winfont = pygame.font.SysFont('georgia', 40)
wintext = winfont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

# Menu fonts
menu_font = pygame.font.SysFont('georgia', 60)
pause_menu_items = ['Resume', 'Settings', 'Quit']
selected_item = 0

# Settings fonts
settings_font = pygame.font.SysFont('georgia', 60)
settings_menu_items = ['Back', 'Change paddle color to random', 'Change the difficulty mode']
selected_item = 0

# Difficulty font
diff_font = pygame.font.SysFont('georgia', 60)
diff = "Medium"
diff_font = pygame.font.SysFont('georgia', 40)
diff_text = diff_font.render(f'{diff}', True, (255, 255, 255))
diff_rect = diff_text.get_rect()
diff_rect.center = (600, 20)

# Color text
color_font = pygame.font.SysFont('georgia', 60)
color = "Color"
color_font = pygame.font.SysFont('georgia', 40)
color_text = color_font.render('Color', True, paddle_color)
color_rect = color_text.get_rect()
color_rect.center = (900, 20)

time_elapsed = 0  # For increasing ball speed and shrinking paddle

def draw_pause_menu(screen, items, selected):
    for i, item in enumerate(items):
        if i == selected:
            text = menu_font.render(item, True, (255, 0, 0))
        else:
            text = menu_font.render(item, True, (255, 255, 255))
        text_rect = text.get_rect(center=(W // 2, H // 2.5 + i * 60))
        screen.blit(text, text_rect)

def draw_settings_menu(screen, items, selected):
    for i, item in enumerate(items):
        if i == selected:
            text = settings_font.render(item, True, (255, 0, 0))
        else:
            text = settings_font.render(item, True, (255, 255, 255))
        text_rect = text.get_rect(center=(W // 2, H // 2.5 + i * 60))
        screen.blit(text, text_rect)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if game_state == PAUSE_MENU:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_item = max(0, selected_item - 1)
                elif event.key == pygame.K_DOWN:
                    selected_item = min(len(pause_menu_items) - 1, selected_item + 1)
                elif event.key == pygame.K_RETURN:
                    if selected_item == 0:  # Resume
                        game_state = GAME
                    elif selected_item == 1:  # Settings
                        game_state = SETTINGS_MENU
                    elif selected_item == 2:  # Quit
                        done = True
                        
        elif game_state == SETTINGS_MENU:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_item = max(0, selected_item - 1)
                elif event.key == pygame.K_DOWN:
                    selected_item = min(len(settings_menu_items) - 1, selected_item + 1)
                elif event.key == pygame.K_RETURN:
                    if selected_item == 0:  # Back to Pause menu
                        game_state = PAUSE_MENU
                    elif selected_item == 1:  # Change Paddle Color
                        paddle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    elif selected_item == 2:  # Change the difficulty
                        if n == 7.5:
                            n = 15
                            diff = "Medium"
                            paddleW = 150
                        elif change_hard == 1:
                            n = 7.5
                            paddleW = 100
                            diff = "Hard"
                        elif n == 15:
                            n = 20
                            paddleW = 200
                            diff = "Easy"
                            change_hard = 1
    screen.fill(bg)


    if game_state == GAME:
        # Paddle control
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and paddle.left > 0:
            paddle.left -= paddleSpeed
        if key[pygame.K_RIGHT] and paddle.right < W:
            paddle.right += paddleSpeed

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

        # Collision with bonus blocks
        bonus_collision_index = ball.collidelist(bonus_blocks)
        if bonus_collision_index != -1:
            bonus_rect = bonus_blocks.pop(bonus_collision_index)
            dx, dy = detect_collision(dx, dy, ball, bonus_rect, True)  # True because bonus block is breakable
            paddleW = 300  # Make paddle super wide
            pygame.time.set_timer(pygame.USEREVENT, 5000)  # Set a timer for 5 seconds

        # Event to reset paddle size after 5 seconds
        if event.type == pygame.USEREVENT:
            if diff == "Hard":
                paddleW = 100  # Reset paddle width to normal
                pygame.time.set_timer(pygame.USEREVENT, 0)  # Stop the timer
            elif diff == "Medium":
                paddleW = 150  # Reset paddle width to normal
                pygame.time.set_timer(pygame.USEREVENT, 0)  # Stop the timer
            elif diff == "Easy":
                paddleW = 200  # Reset paddle width to normal
                pygame.time.set_timer(pygame.USEREVENT, 0)  # Stop the timer

        # Update paddle with new width
        paddle = pygame.Rect(paddle.left, paddle.top, paddleW, paddleH)

        # Drawing blocks
        [pygame.draw.rect(screen, color_list[color], block) for color, block in enumerate(block_list)]
        [pygame.draw.rect(screen, (255, 255, 0), block) for block in bonus_blocks]  # Drawing bonus blocks
        pygame.draw.rect(screen, paddle_color, paddle)
        pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)
        [pygame.draw.rect(screen, (128, 128, 128), block) for block in unbreakable_blocks]

        # Game score
        game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
        screen.blit(game_score_text, game_score_rect)

        # Game diff
        diff_text = diff_font.render(f'{diff}', True, (255, 255, 255))
        screen.blit(diff_text, diff_rect)
        # Paddle color
        color_text = color_font.render("Color", True, paddle_color)
        screen.blit(color_text, color_rect)

        # Win/lose screens
        if ball.bottom > H:
            screen.fill((0, 0, 0))
            screen.blit(losetext, losetextRect)
        elif not len(block_list) and not len(bonus_blocks):
            screen.fill((255, 255, 255))
            screen.blit(wintext, wintextRect)

        # Increase ball speed and shrink paddle with time
        time_elapsed += clock.get_time()  # Increment time_elapsed by the number of milliseconds since last tick
        if time_elapsed >= n * 1000:  # Every n seconds (n*1000 milliseconds)
            ballSpeed += 1  # Increase ball speed by a smaller value
            paddleW = max(50, paddleW - 10)  # Shrink paddle width
            paddle = pygame.Rect(paddle.left, paddle.top, paddleW, paddleH)  # Update paddle rect
            time_elapsed = 0  # Reset time_elapsed

        if key[pygame.K_ESCAPE]:
            game_state = PAUSE_MENU

    elif game_state == PAUSE_MENU:
        draw_pause_menu(screen, pause_menu_items, selected_item)
        # Game diff
        diff_text = diff_font.render(f'{diff}', True, (255, 255, 255))
        screen.blit(diff_text, diff_rect)
        # Paddle color
        color_text = color_font.render("Color", True, paddle_color)
        screen.blit(color_text, color_rect)
    elif game_state == SETTINGS_MENU:
        draw_settings_menu(screen, settings_menu_items, selected_item)
        # Game diff
        diff_text = diff_font.render(f'{diff}', True, (255, 255, 255))
        screen.blit(diff_text, diff_rect)
        # Paddle color
        color_text = color_font.render("Color", True, paddle_color)
        screen.blit(color_text, color_rect)

    pygame.display.flip()
    clock.tick(FPS)
