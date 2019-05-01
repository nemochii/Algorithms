class SetArray():
	def __init__(self, x):
		self.set = [-1] * x

	def FindCollapsing(self, i):
		parent = i
		while parent > -1:
			root = parent
			parent = self.set[parent]

		while i != root:
			parent = self.set[i]
			self.set[i] = root
			i = parent

		return (root)

	def Union(self, x, y):
		xroot = self.FindCollapsing(x)
		yroot = self.FindCollapsing(y)

		if self.set[xroot] <= self.set[yroot]:
			self.set[xroot] += self.set[yroot]
			self.set[yroot] = xroot
			return (self.set)
		self.set[yroot] += self.set[xroot]
		self.set[xroot] = yroot
		return (self.set)

	def Printout(self):
		for i in range(len(self.set)):
			print ("{0:4}".format(i), end = '')
		print ("")
		for i in self.set:
			print ("{0:4}".format(i), end = '')
		print ("\n")