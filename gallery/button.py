import pygame
from gallery.draw import screen
from gallery.globals import GameData


gd = GameData()
button_img = pygame.image.load('gallery/img/restart.png')


class Button:
    def __init__(self, x, y):
        self.image = button_img
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    # draw the restart button
    def draw(self):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check if mouse is over the button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                gd.sound['swoosh'].play()
                action = True

        # draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action
