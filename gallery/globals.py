import pygame

pygame.mixer.init()


class GameData:
    # set up the game window
    scr_width, scr_height = 864, 936
    fps = 60

    # define colors
    white = (255, 255, 255)

    # define game variables
    ground_scroll = 0                    # Ox of the ground
    scroll_speed = 4                     # moving speed of the ground
    pipe_gap = 150                       # the distance between the two pipes
    pipe_frequency = 1500                # 1500ms - pipe spawn time

    sound = {}
    # Game sounds
    sound['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    sound['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
    sound['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
    sound['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')
