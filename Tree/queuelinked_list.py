class QueueLinked_list():
	def __init__(self, x):
		self.headval = ListNode(x)
		self.backval = self.headval

	def Push(self, x):
		newnode = ListNode(x)
		current = self.headval
		while current.next != None:
			current = current.next
		current.next = newnode
		self.backval = newnode

	def Pop(self):
		if self.IsEmpty():
			return
		self.headval = self.headval.next

	def getFront(self):
		if self.IsEmpty():
			return
		#print (self.headval.val)
		return (self.headval.val)

	def getBack(self):
		if self.IsEmpty():
			return
		print (self.backval.val)

	def IsEmpty(self):
		if self.headval == None:
			#print ("The queue is empty!")
			return (True)
		return (False)

	def getSize(self):
		count = 0
		current = self.headval
		while current != None:
			count += 1
			current = current.next
		print (count)

class ListNode():
	def __init__(self, x):
		self.val = x
		self.next = None