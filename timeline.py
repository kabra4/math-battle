import pygame
class Timeline():
	def __init__(self, screen, stat):
		self.screen=screen
		self.stat=stat
		self.screen_rect=screen.get_rect()
		self.rect=pygame.Rect(0, 0, self.screen_rect.width, 20)
		self.rect.left=0
		self.rect.bottom=self.screen_rect.height/3*2
		self.color=(70, 50, 200)
	def prep(self):
		self.time=self.stat.timeleft/15*self.screen_rect.width
		self.rect.right=self.time
	def draw(self):
		pygame.draw.rect(self.screen, self.color, self.rect)