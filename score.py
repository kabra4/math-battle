import pygame
class Scoreboard():
	def __init__(self, st, screen, stat):
		self.screen=screen
		self.screen_rect=screen.get_rect()
		self.st=st
		self.stat=stat
		self.text_color=(220, 240, 240)
		self.font=pygame.font.SysFont('Berlin Sans FB', 48)
		self.prep_score()
		self.prep_top()

	def prep_top(self):
		top_score=str(self.stat.top_score)
		self.topfont=pygame.font.SysFont('Berlin Sans FB', 68)
		self.top_image=self.topfont.render(top_score, True, self.text_color, self.st.bg)
		self.top_rect=self.top_image.get_rect()
		self.top_rect.right=self.screen_rect.right-20
		self.top_rect.top=20

	def prep_score(self):
		score_str=str(self.stat.score)
		self.score_image=self.font.render(score_str, True, self.text_color, self.st.bg)
		self.score_rect=self.score_image.get_rect()
		self.score_rect.right=self.screen_rect.centerx
		self.score_rect.top=20

	def show_score(self):
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.top_image, self.top_rect)