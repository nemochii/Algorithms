class RedBlackTree():
	def __init__(self):
		self.root = None
		self.nil = False

	def Search(self, x):
		current = self.root

		if not current:
			return (None)

		while current:
			if x == current.data:
				return (current)

			front = current
			if x < current.data:
				current = current.leftchild
			else:
				current = current.rightchild

		return (front)

	def InsertRBT(self, x, p):
		current = self.Search(x)
		newnode = TreeNode(x, p)

		if not current:
			self.root = newnode
			return

		newnode.parent = current
		if x < current.data:
			current.leftchild = newnode
		else:
			current.rightchild = newnode

		newnode.leftchild = self.nil
		newnode.rightchild = self.nil

		self.InsertFixedUpRBT(newnode)

	def InsertFixedUpRBT(self, current):
		while current.parent.color:
			if current.parent.parent.leftchild == current.parent:
				uncle = current.parent.parent.rightchild
				parent = current.parent
				if uncle.color:
					parent.color = False
					uncle.color = False
					parent.parent.color = True
					current = parent.parent
				else:
					if current == parent.rightchild:
						current = parent
						self.LeftRotation(current)
					parent.color = False
					parent.parent.color = True
					self.RightRotation(parent.parent)

			else:
				uncle = current.parent.parent.leftchild
				parent = current.parent
				if uncle.color:
					parent.color = False
					uncle.color = False
					parent.parent.color = True
					current = parent.parent
				else:
					if current == parent.rightchild:
						current = parent
						self.RightRotation(current)
					parent.color = False
					parent.parent.color = True
					self.LeftRotation(parent.parent)

		self.root.color = False

	def DeleteRBT(self, x):
		current = self.Search(x)

		if current:
			if current.leftchild == self.nil or current.rightchild == self.nil:
				y = current
			else:
				y = self.Successor(current)

			if y.leftchild:
				x = y.leftchild
			else:
				x = y.rightchild

			if x:
				x.parent = y.parent
			if not y.parent:
				self.root = x

			if y == y.parent.leftchild:
				y.parent.leftchild = x
			else:
				y.parent.rightchild = x

			if y != current:
				current.data = y.data
				current.element = y.element

			if not y.color:
				self.DeleteFixedUpRBT(x)

	def DeleteFixedUpRBT(self, current):
		while current != self.root and not current.color:
			if current == current.parent.leftchild:
				sibling = current.parent.rightchild
				parent = current.parent
				if sibling.color:
					siblng.color = False
					parent.color = True
					self.LeftRotation(parent)
					sibling = parent.rightchild

				if not sibling.leftchild.color and not sibling.rightchild.color:
					sibling.color = True
					current = parent
				else:
					if not sibling.rightchild.color:
						sibling.leftchild.color = False
						sibling.color = True
						self.RightRotation(sibling)
						sibling = parent.rightchild
					sibling.color = parent.color
					parent.color = False
					sibling.rightchild.color = False
					self.LeftRotation(parent)
					current = self.root

			else:
				sibling = current.parent.rightchild
				parent = current.parent
				if sibling.color:
					siblng.color = False
					parent.color = True
					self.RightRotation(parent)
					sibling = parent.rightchild

				if not sibling.leftchild.color and not sibling.rightchild.color:
					sibling.color = True
					current = parent
				else:
					if not sibling.rightchild.color:
						sibling.leftchild.color = False
						sibling.color = True
						self.LeftRotation(sibling)
						sibling = parent.rightchild
					sibling.color = parent.color
					parent.color = False
					sibling.rightchild.color = False
					self.RightRotation(parent)
					current = self.root

		current.color = False

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
		while current.leftchild:
			current = current.leftchild
		return (current)

	def LeftRotation(self, current):
		y = current.rightchild

		current.rightchild = y.leftchild
		if y.leftchild != self.nil:
			y.leftchild.parent = current

		y.parent = current.parent

		if current.parent == self.nil:
			self.root = y
		elif current == current.parent.leftchild:
			current.parent.leftchild = y
		else:
			current.parent.rightchild = y

		y.leftchild = current
		current.parent = y

	def RightRotation(self, current):
		y = current.leftchild

		current.leftchild = y.rightchild
		if y.rightchild != self.nil:
			y.rightchild.parent = current

		y.parent = current.parent

		if current.parent == self.nil:
			self.root = y
		elif current == current.parent.leftchild:
			current.parent.leftchild = y
		else:
			current.parent.rightchild = y

		y.rightchild = current
		current.parent = y

class TreeNode():
	def __init__(self, x, p):
		self.data = x
		self.element = p
		self.leftchild = None
		self.rightchild = None
		self.parent = None
		self.color = True