class Stats():
	def __init__(self, st):
		self.st=st
		self.reset_stats()
		self.game_active=False
		self.top_score=1
		self.endtime=0

	def reset_stats(self):
		self.score=1
		self.start=0
		self.current=0

		self.timeleft=15