import pygame
import random
from gallery.globals import GameData


gd = GameData()


# sprite classes have functions update and draw which already built to them
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('gallery/img/pipe.png')
        self.rect = self.image.get_rect()
        # position 1 is from the top. -1 is from the bottom
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(gd.pipe_gap/2)]
        if position == -1:
            self.rect.topleft = [x, y + int(gd.pipe_gap/2)]

    # update the animation - delete passed pipes
    def update(self, game_over):
        if game_over is False:
            self.rect.x -= gd.scroll_speed
            if self.rect.right < 0:
                self.kill()

    # generate new random pipes
    @staticmethod
    def getpipe(pipe_group, scr_width, scr_height):
        pipe_height = random.randint(-100, 100)
        btm_pipe = Pipe(scr_width, int(scr_height / 2) + pipe_height, -1)
        top_pipe = Pipe(scr_width, int(scr_height / 2) + pipe_height, 1)
        pipe_group.add(btm_pipe)
        pipe_group.add(top_pipe)
