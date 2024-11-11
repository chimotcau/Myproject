import pygame
from gallery.globals import GameData


gd = GameData()
# load the animations
back_ground = pygame.image.load('gallery/img/bg.png')
ground = pygame.image.load('gallery/img/ground.png')


screen = pygame.display.set_mode((gd.scr_width, gd.scr_height))
score = 0               # score - how many times the bird's passed the pipes?
pass_pipe = False       # if the bird has passed the left site of the pipe


# scroll all the ground
def screen_roll(bird_group, pipe_group, game_over, flying):
    global score, pass_pipe
    # draw background
    screen.blit(back_ground, (0, 0))
    # draw the bird
    bird_group.draw(screen)
    bird_group.update(game_over, flying)
    # draw pipes
    pipe_group.draw(screen)
    pipe_group.update(game_over)
    # draw ground
    screen.blit(ground, (gd.ground_scroll, 768))

    # if the bird pass the pipe, then score +1
    if len(pipe_group) > 0:
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left \
                and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right \
                and pass_pipe is False:
            pass_pipe = True
        if pass_pipe is True:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                gd.sound['point'].play()
                score += 1
                pass_pipe = False

    if game_over is False:
        # scroll the ground
        gd.ground_scroll -= gd.scroll_speed
        if gd.ground_scroll < -35:
            gd.ground_scroll = 0

    # draw score appearance
    draw_text(str(score), gd.white, int(gd.scr_width / 2), 20)


# output the score
def draw_text(text, text_col, x, y):
    # define font
    pygame.font.init()
    font = pygame.font.SysFont(None, 60)

    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
