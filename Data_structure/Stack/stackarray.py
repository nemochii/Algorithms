class StackArray():
	def __init__(self, capacity = 1):
		self.top = -1
		self.capacity = capacity
		self.stack = [None] * capacity

	def Push(self, x):
		if self.capacity == self.top:
			DoubleCapacity()
		self.top += 1
		self.stack[self.top] = x

	def Pop(self):
		if self.top == -1:
			print ("The stack is empty!")
			return
		self.top -= 1

	def Top(self):
		if self.top == -1:
			print ("The stack is empty!")
			return
		print (self.stack[self.top])

	def IsEmpty(self):
		if self.top == -1:
			print ("The stack is empty!")
			return
		print ("The stack is not empty!")

	def getSize(self):
		print ("The stack have %d elements!" % (self.top + 1))

	def DoubleCapacity(self):
		newstack = [None] * self.capacity * 2
		for i in range(self.top + 1):
			newstack[i] = self.stack[i]
		self.stack = newstack