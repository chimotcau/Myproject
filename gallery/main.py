import pygame
from pygame.locals import *
from gallery.globals import GameData
from gallery.bird import Bird
from gallery.pipe import Pipe
from gallery.button import Button
from gallery.reset import reset_game
import gallery.draw


gd = GameData()

# set up the game window
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()


def main():
    # creat a group of birds animation
    bird_group = pygame.sprite.Group()
    flappy = Bird(100, int(gd.scr_height / 2))
    bird_group.add(flappy)
    # creat a group of pipes animation
    pipe_group = pygame.sprite.Group()
    # create restart button instance
    button = Button(gd.scr_width // 2 - 50, gd.scr_height // 2 - 100)
    # the last time when a pipe was created
    last_pipe = pygame.time.get_ticks() - gd.pipe_frequency

    run = True
    flying = False        # if the bird's still flying (no collision)
    game_over = False     # if the game's still working
    beat = False         # if the sound's still not beating
    while run:
        clock.tick(gd.fps)                      # set up frame rate

        if game_over is False and flying is True:
            time_now = pygame.time.get_ticks()
            if time_now - last_pipe > gd.pipe_frequency:
                Pipe.getpipe(pipe_group, gd.scr_width, gd.scr_height)     # generate new pipes
                last_pipe = time_now

        # look for collision
        if (pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0) and beat is False:
            game_over = True
            gd.sound['hit'].play()
            beat = True

        # check if bird has hit the ground
        if flappy.rect.bottom >= 768 and beat is False:
            gd.sound['hit'].play()
            game_over = True
            flying = False
            beat = True

        gallery.draw.screen_roll(bird_group, pipe_group, game_over, flying)  # update screen

        # check for game over and reset
        if game_over is True:
            if button.draw() is True:
                game_over = False
                beat = False
                gallery.draw.score = reset_game(pipe_group, flappy, gd.scr_height)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and flying is False and game_over is False:
                flying = True

        pygame.display.update()
