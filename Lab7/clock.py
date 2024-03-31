import pygame 
import datetime

pygame.init()

width = 1200
length = 850
screen = pygame.display.set_mode((width, length))
running = True
clock = pygame.time.Clock()

right = pygame.image.load("Pics and music/leftarm.png")
left = pygame.image.load("Pics and music/rightarm.png")
layer = pygame.image.load("Pics and music/mainclock.png")

minutes = 0
seconds = -45


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    date = str(datetime.datetime.now())
    time = date.split(":")
    minutesnow = time[1]
    secondsnow = time[2].split(".")
    minutes = -(int(minutesnow) * 6) - (int(secondsnow[0])* 0.1)
    seconds = -int(secondsnow[0]) * 6 
    minrotate = pygame.transform.rotate(left, minutes)
    secrotate = pygame.transform.rotate(right, seconds)


    screen.fill((0, 0, 0))

    rect = minrotate.get_rect(center = (width/2, length/2))
    rebt = secrotate.get_rect(center = (width/2, length/2))


    screen.blit(layer, (0-(-width + 1400)/2, 0-(-length + 1050)/2))
    screen.blit(minrotate, rect.topleft)
    screen.blit(secrotate, rebt.topleft) 
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

