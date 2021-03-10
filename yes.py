import pygame
class Yes():
    def __init__(self, screen):
        self.screen=screen
        self.image=pygame.image.load('images/yes.png')
        self.rect =self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.right=self.screen_rect.centerx-50
        self.rect.centery=self.screen_rect.height/6*5

    def blitme(self):
        self.screen.blit(self.image, self.rect)