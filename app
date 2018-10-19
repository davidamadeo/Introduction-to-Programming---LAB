# import pygame with all the special sub-modules
from pygame import *

# import menu.py
import menu

# import 'random' api to create random asteroid
import random

# import classes.py with all the class
from classes import *


def run_game():

    # create screen resolution
    screen = pygame.display.set_mode((800, 600))

    # create program name
    display.set_caption("Dank Mission")

    # initialize score
    scores = 0

    # initialize all imported pygame modules
    pygame.init()

    # create jet object group
    jet1 = Jet(screen)
    Jet_sprites = Group(jet1)

    # create asteroid object group
    asteroid_group = Group()

    # create bullets object Group
    bullets = Group()

    # set how fast the game phase
    theClock = pygame.time.Clock()
    Fps = 40
    asteroid_timer = pygame.time.get_ticks()
    while True:
        theClock.tick(Fps)
        Fps += 0.01  # game phase goes faster after every frame

        # create score board
        font = pygame.font.Font("Minecraft.ttf", 36)  # create font
        score_board = font.render("score:" + str(scores), True, (255, 255, 255))

        # update referred to the word's method
        screen.blit(score_board, (10, 550))

        # load bg image for game
        screen.fill(pygame.Color(15, 77, 143))

        # create jet
        Jet_sprites.draw(screen)

        # create bullets
        bullets.draw(screen)

        # create asteroid
        asteroid_group.draw(screen)

        # update current frame with all the above changes
        display.update()

        # get events from the queue
        pygame.event.get()

        """moving the jet according to key pressed"""
        key = pygame.key.get_pressed()

        # moving LEFT
        if key[K_LEFT] and jet1.rect.x > 0:
            jet1.moveleft()

        # moving RIGHT
        if key[K_RIGHT] and jet1.rect.x <= 700:
            jet1.moveright()

        # moving DOWN
        if key[K_DOWN] and jet1.rect.y <= 500:
            jet1.movedown()

        # moving UP
        if key[K_UP] and jet1.rect.y > 0:
            jet1.moveup()

        # SPACE to spawn the bullets
        if key[K_SPACE] and len(bullets) <= jet1.firerates+(scores/4000):
            bullet = Bullet(screen, jet1.rect.x + 50, jet1.rect.y + 42)
            bullets.add(bullet)
            pygame.mixer.music.load("LaserBlast.wav")
            pygame.mixer.music.play()

        # ESC to break
        if key[K_ESCAPE]:
            menu.pause_menu(Button, run_game)

        # P ro pause
        if key[K_p]:
            menu.pause_menu(Button, run_game)

        """generate asteroid randomly"""
        if pygame.time.get_ticks() - asteroid_timer >= 200:
            asteroid = Asteroid(screen, 50, 50, random.randint(1, 4) * 6, 800, (random.randint(1, 28) * 20))
            asteroid_group.add(asteroid)
            asteroid_timer = pygame.time.get_ticks()

        """update the movement of asteroid"""
        for asteroid in asteroid_group:
            asteroid.movement()
            if asteroid.rect.right <= 0:
                asteroid_group.remove(asteroid)  # remove after screen
            if groupcollide(Jet_sprites, asteroid_group, dokilla=True, dokillb=True):  # collition check
                menu.lose_menu(Button, run_game, scores)

        """update bullet movement on screen"""
        for bullet in bullets:
            bullet.movement()
            if bullet.rect.left > 800:
                bullets.remove(bullet)
            if groupcollide(bullets, asteroid_group, dokilla=True, dokillb=True):
                scores += 100
                pygame.mixer.music.load('oof.mp3')
                pygame.mixer.music.play(0)


# run the game
menu.menu_screen(Button, run_game)
