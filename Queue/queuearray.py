class QueueArray():
	def __init__(self, capacity = 1):
		self.front = -1
		self.back = -1
		self.capacity = capacity
		self.queue = [None] * capacity

	def Push(self, x):
		self.back += 1
		if self.back == self.capacity - 1:
			self.DoubleCapacity()
		self.queue[self.back] = x

	def Pop(self):
		if self.IsEmpty():
			return
		self.front += 1 

	def getFront(self):
		if self.IsEmpty():
			return
		print (self.queue[self.front + 1])

	def getBack(self):
		if self.IsEmpty():
			return
		print (self.queue[self.back])

	def IsEmpty(self):
		if self.back == -1:
			print ("The queue is empty!")
			return (True)
		return (False)

	def getSize(self):
		print (self.back - self.front)

	def DoubleCapacity(self):
		newqueue = [None] * self.capacity * 2
		for i in range(front + 1, back + 1):
			newqueue[i] = self.queue[i]
		self.queue = newqueue
		size = getSize()
		self.front = -1
		self.back = size