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