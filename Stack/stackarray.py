class StackArray():
	def __init__(self, capacity = 1):
		self.top = -1
		self.capacity = capacity
		self.stack = [None] * capacity
		self.minstack = [None] * capacity

	def Push(self, x):
		if self.capacity == self.top:
			self.DoubleCapacity()
		self.top += 1
		if self.top == 0:
			self.minstack[self.top] = x
		else:
			if x < self.minstack[self.top - 1]:
				self.minstack[self.top] = x
			else:
				self.minstack[self.top] = self.minstack[self.top - 1]
		self.stack[self.top] = x

	def Pop(self):
		if self.IsEmpty():
			return
		self.top -= 1

	def Top(self):
		if self.IsEmpty():
			return
		print (self.stack[self.top])

	def IsEmpty(self):
		if self.top == -1:
			print ("The stack is empty!")
			return (True)
		return (False)

	def getSize(self):
		print ("The stack have %d elements!" % (self.top + 1))

	def DoubleCapacity(self):
		newstack = [None] * self.capacity * 2
		newminstack = [None] * self.capacity * 2
		for i in range(self.top + 1):
			newstack[i] = self.stack[i]
			newminstack[i] = self.minstack[i]
		self.stack = newstack
		self.minstack = newminstack

	def getmin(self):
		if self.IsEmpty():
			return
		print (self.minstack[self.top])