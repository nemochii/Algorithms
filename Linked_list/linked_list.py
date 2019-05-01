class HeadNode:
	def __init__(self, x):
		self.headval = ListNode(x)

	def PrintList(self):
		current = self.headval
		while current != None:
			print (current.val)
			current = current.next

	def Push_front(self, x):
		newnode = ListNode(x)
		newnode.next = self.headval
		self.headval = newnode

	def Push_back(self, x):
		newnode = ListNode(x)
		current = self.headval
		if current == None:
			current = newnode
			return

		while current.next != None:
			current = current.next
		current.next = newnode

	def Delete(self, x):
		current = self.headval
		if current.val == x:
			self.headval = self.headval.next
			return

		while current.next != None:
			if current.next.val == x:
				current.next = current.next.next
				return
			current = current.next

		while current.next != None:
			if current.next.val == x:
				current.next = current.next.next

	def Clear(self):
		while self.headval != None:
			current = self.headval
			self.Delete(current.val)
			self.headval = current.next

	def Reverse(self):
		previous = None
		current = self.headval
		preceding = current.next
		while preceding != None:
			current.next = previous
			previous = current
			current = preceding
			preceding = current.next
		current.next = previous
		self.headval = current

class ListNode():
	def __init__(self, val):
		self.val = val
		self.next = None