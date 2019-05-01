class StackLinked_list():
	def __init__(self, x):
		self.headval = ListNode(x)
		self.minstack = ListNode(x)

	def Push(self, x):
		newnode = ListNode(x)
		newnode.next = self.headval
		self.headval = newnode
		if newnode.val < self.minstack.val:
			self.minstack = newnode
		else:
			self.minstack = ListNode(self.minstack.val)

	def Pop(self):
		if self.IsEmpty():
			return
		self.headval = self.headval.next
		self.minstack = self.minstack.next

	def Top(self):
		if self.IsEmpty():
			return
		print (self.headval.val)

	def IsEmpty(self):
		if self.headval == None:
			print ("The stack is empty!")
			return (True)
		return (False)

	def getSize(self):
		count = 0
		current = self.headval
		while current != None:
			count += 1
			current = current.next
		print ("The stack have %d elements!" % (count))

	def getmin(self):
		if self.IsEmpty():
			return
		print (self.minstack.val)

class ListNode():
	def __init__(self, x):
		self.val = x
		self.next = None