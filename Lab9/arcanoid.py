import pygame
import random

pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

# Game states
MAIN_MENU = 0
GAME = 1
PAUSE_MENU = 2
SETTINGS = 3
game_state = MAIN_MENU

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
def draw_menu(screen, items, selected):
    for i, item in enumerate(items):
        if i == selected:
            text = menu_font.render(item, True, (255, 0, 0))
        else:
            text = menu_font.render(item, True, (255, 255, 255))
        text_rect = text.get_rect(center=(W // 2, H // 2 + i * 60))
        screen.blit(text, text_rect)

def draw_pause_menu(screen):
    text = menu_font.render("Paused", True, (255, 255, 255))
    text_rect = text.get_rect(center=(W // 2, H // 2))
    screen.blit(text, text_rect)

def draw_settings(screen, items, selected, speed, width):
    for i, item in enumerate(items):
        if i == selected:
            text_color = (255, 0, 0)
        else:
            text_color = (255, 255, 255)
        if item == 'Ball Speed':
            text = menu_font.render(f'{item}: {speed}', True, text_color)
        elif item == 'Paddle Width':
            text = menu_font.render(f'{item}: {width}', True, text_color)
        else:
            text = menu_font.render(item, True, text_color)
        text_rect = text.get_rect(center=(W // 2, H // 2 + i * 60))
        screen.blit(text, text_rect)

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

def update_game(screen):
    global game_score, dx, dy, time_elapsed, paddleW, ballSpeed

    # Drawing blocks
    [pygame.draw.rect(screen, color_list[color], block) for color, block in enumerate(block_list)]
    [pygame.draw.rect(screen, (128, 128, 128), block) for block in unbreakable_blocks]  # Drawing unbreakable blocks
    [pygame.draw.rect(screen, (255, 255, 0), block) for block in bonus_blocks]  # Drawing bonus blocks
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
        paddleW = 150  # Reset paddle width to normal
        pygame.time.set_timer(pygame.USEREVENT, 0)  # Stop the timer

    # Update paddle with new width
    paddle.width = paddleW
    paddle.clamp_ip(screen.get_rect())

    # Game score
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)

    # Win/lose screens
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list) and not len(bonus_blocks):
        screen.fill((255, 255, 255))
        screen.blit(wintext, wintextRect)

    # Increase ball speed and shrink paddle with time
    time_elapsed += 1 / FPS
    if time_elapsed >= 30:  # Every 30 seconds
        ballSpeed = min(20, ballSpeed + 1)
        paddleW = max(50, paddleW - 10)
        time_elapsed = 0



# Block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
color_list = [(random.randrange(0, 255), random.randrange(0, 255),  random.randrange(0, 255)) for i in range(10) for j in range(4)]
unbreakable_blocks = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(2, 8) for j in range(1, 3)]  # Unbreakable blocks

# Bonus blocks
bonus_blocks = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(4, 6) for j in range(2, 3)]  # Bonus blocks

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

# Menu fonts
menu_font = pygame.font.SysFont('comicsansms', 60)
menu_items = ['Start', 'Settings', 'Quit']
selected_item = 0

# Settings
settings_items = ['Ball Speed', 'Paddle Width', 'Back']
selected_setting = 0

time_elapsed = 0  # For increasing ball speed and shrinking paddle

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if game_state == MAIN_MENU:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_item = max(0, selected_item - 1)
                elif event.key == pygame.K_DOWN:
                    selected_item = min(len(menu_items) - 1, selected_item + 1)
                elif event.key == pygame.K_RETURN:
                    if selected_item == 0:  # Start
                        game_state = GAME
                    elif selected_item == 1:  # Settings
                        game_state = SETTINGS
                    elif selected_item == 2:  # Quit
                        done = True
        elif game_state == GAME:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_state = PAUSE_MENU
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if ball.colliderect(paddle) and dy > 0:
                            dx, dy = detect_collision(dx, dy, ball, paddle, False)  # False because paddle is unbreakable
                elif event.type == pygame.MOUSEMOTION:
                    paddle.centerx = event.pos[0]
                    paddle.clamp_ip(screen.get_rect())
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_state = PAUSE_MENU
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if ball.colliderect(paddle) and dy > 0:
                        dx, dy = detect_collision(dx, dy, ball, paddle, False)  # False because paddle is unbreakable
            elif event.type == pygame.MOUSEMOTION:
                paddle.centerx = event.pos[0]
                paddle.clamp_ip(screen.get_rect())
        elif game_state == PAUSE_MENU:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_state = GAME
        elif game_state == SETTINGS:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_setting = max(0, selected_setting - 1)
                elif event.key == pygame.K_DOWN:
                    selected_setting = min(len(settings_items) - 1, selected_setting + 1)
                elif event.key == pygame.K_LEFT:
                    if selected_setting == 0:  # Ball Speed
                        ballSpeed = max(1, ballSpeed - 1)
                    elif selected_setting == 1:  # Paddle Width
                        paddleW = max(50, paddleW - 10)
                elif event.key == pygame.K_RIGHT:
                    if selected_setting == 0:  # Ball Speed
                        ballSpeed = min(20, ballSpeed + 1)
                    elif selected_setting == 1:  # Paddle Width
                        paddleW = min(300, paddleW + 10)
                elif event.key == pygame.K_RETURN:
                    if selected_setting == 2:  # Back
                        game_state = MAIN_MENU

    screen.fill(bg)

    if game_state == MAIN_MENU:
        draw_menu(screen, menu_items, selected_item)
    elif game_state == GAME:
        update_game(screen)
    elif game_state == PAUSE_MENU:
        draw_pause_menu(screen)
    elif game_state == SETTINGS:
        draw_settings(screen, settings_items, selected_setting, ballSpeed, paddleW)

    pygame.display.flip()
    clock.tick(FPS)

