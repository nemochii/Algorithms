class StackLinked_list():
	def __init__(self, x):
		self.headval = ListNode(x)

	def Push(self, x):
		newnode = ListNode(x)
		newnode.next = self.headval
		self.headval = newnode

	def Pop(self):
		if self.headval == None:
			print ("The stack is empty!")
			return
		self.headval = self.headval.next

	def Top(self):
		if self.headval == None:
			print ("The stack is empty!")
			return
		print (self.headval.val)

	def IsEmpty(self):
		if self.headval == None:
			print ("The stack is empty!")
			return
		print ("The stack is not empty!")

	def getSize(self):
		count = 0
		current = self.headval
		while current != None:
			count += 1
			current = current.next
		print ("The stack have %d elements!" % (count))

class ListNode():
	def __init__(self, x):
		self.val = x
		self.next = None