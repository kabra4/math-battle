import pygame

class Bg2():
	def __init__(self, screen):
		self.screen=screen
		self.screen_rect=screen.get_rect()
		self.rect=pygame.Rect(0, 0, self.screen_rect.width, int(self.screen_rect.height/3))
		self.rect.left=0
		self.rect.bottom=self.screen_rect.bottom
		self.color=(230, 230, 230)
	def bg2draw(self):
		pygame.draw.rect(self.screen, self.color, self.rect)

class YesNo():
    def __init__(self, screen, yesNo):
        self.screen=screen
        self.image=pygame.image.load(f'images/{yesNo}.png')
        self.rect =self.image.get_rect()
        self.screen_rect=screen.get_rect()
        if yesNo == 'yes':
            self.rect.right=self.screen_rect.centerx-50
        else:
            self.rect.left=self.screen_rect.centerx+50
        self.rect.centery=self.screen_rect.height/6*5

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Play():
    def __init__(self, screen):
        self.screen=screen
        self.image=pygame.image.load('images/play.png')
        self.rect =self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.centery=self.screen_rect.centery

    def blitme(self):
        self.screen.blit(self.image, self.rect)