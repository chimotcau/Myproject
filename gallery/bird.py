import pygame
from gallery.globals import GameData


gd = GameData()


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # set up animations
        self.images = []        # list of animation
        self.number = 0         # animation serial number
        self.counter = 0        # velocity of the wings
        for numb in range(1, 5):
            anm = pygame.image.load(f'gallery/img/bird_{numb}.png')
            self.images.append(anm)
        self.image = self.images[self.number]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]      # position of the bird
        self.vel = 0                   # jumping velocity
        self.clicked = False           # drive the bird

    # update the animation about movements of the wings and the bird itself
    def update(self, game_over, flying):
        if flying is True:
            # gravity
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 768:
                self.rect.y += int(self.vel)

        if game_over is False:
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                gd.sound['wing'].play()
                self.clicked = True
                self.vel = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            self.counter += 1
            flap_cooldown = 5  # 5ms/frame
            if self.counter > flap_cooldown:
                self.counter = 0
                self.number += 1
                if self.number >= len(self.images):
                    self.number = 0

            self.image = self.images[self.number]
            # make the animation more smooth
            self.image = pygame.transform.rotate(self.images[self.number], self.vel * -2)
        else:
            self.image = pygame.transform.rotate(self.images[self.number], -90)
