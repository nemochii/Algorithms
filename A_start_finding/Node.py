class Node:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.reset()

	def reset(self):
		self.status = 0
		self.text_status = False
		self.parent = None
		self.G = 0
		self.H = 0
		self.F = 0

	def compute_F(self):
		self.F = self.G + self.H