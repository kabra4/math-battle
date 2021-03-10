import pygame
class Question():
	def __init__(self, screen, st):
		self.screen=screen
		self.st=st
		self.screen_rect=screen.get_rect()
		self.text_color=(250, 250, 250)
		self.font=pygame.font.SysFont('Berlin Sans FB', 66)
		self.reset()

	def reset(self):
		self.e1=0
		self.e2=0
		self.ans=0
		self.sign=''
		self.tans=0
		self.q=True
		self.yesno=True
		self.fintim=0

	def prep(self):
		self.ques_str=str(self.e1)+' '+self.sign+' '+str(self.e2)+' = '+str(self.ans)
		self.ques_image=self.font.render(self.ques_str, True, self.text_color, self.st.bg)
		self.ques_rect=self.ques_image.get_rect()
		self.ques_rect.centerx=self.screen_rect.centerx
		self.ques_rect.centery=self.screen_rect.height/3

	def show_q(self):
		self.screen.blit(self.ques_image, self.ques_rect)