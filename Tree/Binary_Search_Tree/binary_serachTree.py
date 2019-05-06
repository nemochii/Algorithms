class BinarySearchTree():
	def __init__(self, x):
		self.root = x

	def Insert(self, x, p):
		current, exist = self.Search(x)

		if exist:
			print ("The node is already exist!")
			return
		else:
			newnode = TreeNode(x, p)
			if x < current.data:
				current.leftchild = newnode
				newnode.parent = current
			else:
				current.rightchild = newnode
				newnode.parent = current

	def Search(self, x):
		current = self.root
		while current:
			if x == current.data:
				return (current, True)

			front = current
			if x < current.data:
				current = current.leftchild
			else:
				current = current.rightchild
		return (front, False)

	def Sort(self):
		self.in_order()

	def Delete(self, x):
		current, exist = self.Search(x)

		#y = really going to delete
		#x = the child of the deleted node

		if exist:
			if current.leftchild == None or current.rightchild == None:
				y = current
			else:
				y = self.Successor(current)

			if y.leftchild:
				x = y.leftchild
			else:
				x = y.rightchild

			if x:
				x.parent = y.parent
			if y.parent == None:
				self.root = x

			if y == y.parent.leftchild:
				y.parent.leftchild = x
			else:
				y.parent.rightchild = x

			if y != current:
				current.data = y.data
				current.element = y.element

		del y

	def in_order(self):
		current = self.root
		current = self.leftmost(current)
		while current:
			print (current.element, current.data)
			current = self.Successor(current)

	def Successor(self, current):
		if current.rightchild:
			current = current.rightchild
			result = self.leftmost(current)
			return (result)

		while current.parent:
			if current.parent.leftchild == current:
				return (current.parent)
			current = current.parent
		return (None)

	def leftmost(self, current):
		while current.leftchild != None:
			current = current.leftchild
		return (current)

class TreeNode():
	def __init__(self, x, p):
		self.data = x
		self.element = p
		self.leftchild = None
		self.rightchild = None
		self.parent = None