import pygame

pygame.init()
width = 400
height = 400
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("A BALL")
done = False
is_blue = True
x = 150
y = 150



clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        width = pygame.display.get_window_size()[0]
        height = pygame.display.get_window_size()[1]
        if event.type == pygame.QUIT:
            exit()
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_RIGHT]: x += 20
        if x + 20 > width - 25: x = x + (width - x) - 25
        if pressed[pygame.K_LEFT]: x -= 20
        if x - 20 < 25: x = 25
        if pressed[pygame.K_UP]: y -= 20
        if y - 20 < 25: y = 25
        if pressed[pygame.K_DOWN]: y += 20
        if y + 20 > height - 25: y = y + (height - y) - 25
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_ESCAPE]:quit()



    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255,0,0), (x,y), 25)



    pygame.display.flip()
    clock.tick(60)

pygame.quit()