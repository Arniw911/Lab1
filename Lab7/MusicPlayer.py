import pygame 
from pygame import mixer

pygame.init()
mixer.init()
width = 700
length = 500
screen = pygame.display.set_mode((width, length))
running = True
clock = pygame.time.Clock()
pygame.display.set_caption("Music Player")
current_track = 0
screen.fill((180, 180, 180))

font = pygame.font.Font(None, 36)
text = font.render('Hello this is a music player: ', True, (0, 0, 0))
command1 = font.render('To play current song please press "up arrow key". ', True, (0, 0, 0))
command2 = font.render('To stop the song please press "down arrow key". ', True, (0, 0, 0))
command3 = font.render('To skip to the next track please press "right arrow key". ', True, (0, 0, 0))
command4 = font.render('To get to the previous track please press "left arrow key". ', True, (0, 0, 0))
screen.blit(text, (width/4, length/3))
screen.blit(command1, (0, length/2.6))
screen.blit(command2, (0, length/2.325))
screen.blit(command3, (0, length/2.1))
screen.blit(command4, (0, length/1.9))
pygame.display.flip()

playlist = ["C:/Users/user/Desktop/labpygames/Star Wars - Cantina Song.mp3",
    "C:/Users/user/Desktop/labpygames/Dos-muqasan - Toy jyry.mp3",
    "C:/Users/user/Desktop/labpygames/Daft Punk - Around The World.mp3"]

def play_music(track_index):
    if 0 <= track_index < len(playlist):
        mixer.music.load(playlist[track_index])
        mixer.music.play()
    else:
        print("Track index out of range.")

def stop_music():
    mixer.music.stop()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_music(current_track)

def previous_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play_music(current_track)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_UP:
                play_music(current_track)
            if event.key == pygame.K_RIGHT:
                next_track()
            if event.key == pygame.K_DOWN:
                stop_music()
            if event.key == pygame.K_LEFT:
                previous_track()
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()