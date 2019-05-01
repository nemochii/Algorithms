class CircularQueueArray():
	def __init__(self, x):
		self.front = 0
		self.back = 0
		self.capacity = x
		self.queue = [None] * self.capacity
		self.count = 0

	def Push(self, x):
		self.back = (self.back + 1) % self.capacity
		if self.back == self.front:
			self.DoubleCapacity()
		self.queue[self.back] = x
		self.count += 1

	def Pop(self):
		if self.IsEmpty():
			return
		self.front = (self.front + 1) % self.capacity
		self.count -= 1

	def getFront(self):
		if self.IsEmpty():
			return
		print (self.queue[self.front + 1])

	def getBack(self):
		if self.IsEmpty():
			return
		print (self.queue[self.back])

	def IsEmpty(self):
		if self.front == self.back:
			print ("The queue is empty!")
			return (True)
		return (False)

	def getSize(self):
		print ("The queue have %d element!" % (self.count))

	def DoubleCapacity(self):
		newqueue = [None] * self.capacity * 2
		for i in range(1, self.count + 1):
			self.front = (self.front + 1) % self.capacity
			newqueue[i] = self.queue[self.front]
		self.queue = newqueue
		self.front = 0
		self.back = self.count + 1