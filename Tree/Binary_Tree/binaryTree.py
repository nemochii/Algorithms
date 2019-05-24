from queuelinked_list import QueueLinked_list

class BinaryTree():
	def __init__(self, x):
		#self.root = x

		self.root = TreeNode(x[0])
		self.LevelorderConstruct(x)

	def LevelorderConstruct(self, x):
		q = QueueLinked_list(self.root)
		current = self.root

		for i in range(1, len(x), 2):
			if x[i] != "x":
				newnode = TreeNode(x[i])
				newnode.parent = current
				current.leftchild = newnode
				q.Push(newnode)

			if i + 1 == len(x):
				return

			if x[i + 1] != "x":
				newnode = TreeNode(x[i + 1])
				newnode.parent = current
				current.rightchild = newnode
				q.Push(newnode)

			q.Pop()
			current = q.getFront()

	def InsertLevelorder(self, x):
		q = QueueLinked_list(self.root)
		current = self.root

		while current:
			if current.leftchild == None:
				newnode = TreeNode(x)
				newnode.parent = current
				current.leftchild = newnode
				return
			q.Push(current.leftchild)
			
			if current.rightchild == None:
				newnode = TreeNode(x)
				newnode.parent = current
				current.rightchild = newnode
				return
			q.Push(current.rightchild)

			q.Pop()
			current = q.getFront()

	def pre_order(self, current):
		if current:
			print (current.data, end = ' ')
			self.pre_order(current.leftchild)
			self.pre_order(current.rightchild)

	def in_order(self, current):
		if current:
			self.in_order(current.leftchild)
			print (current.data, end = ' ')
			self.in_order(current.rightchild)

	def post_order(self, current):
		if current:
			self.post_order(current.leftchild)
			self.post_order(current.rightchild)
			print (current.data, end = ' ')

	def level_order(self):
		current = self.root
		q = QueueLinked_list(current)

		while not q.IsEmpty():
			current = q.getFront()

			print (current.data, end = ' ')

			if current.leftchild != None:
				q.Push(current.leftchild)
			if current.rightchild != None:
				q.Push(current.rightchild)

			q.Pop()

	def InorderSuccessor(self, current):
		if current.rightchild != None:
			current = current.rightchild
			result = self.leftmost(current)
			#print (result.data)
			return (result)

		while current.parent != None:
			if current.parent.leftchild != current:
				current = current.parent
			else:
				#print (current.parent.data)
				return (current.parent)

	def leftmost(self, current):
		while current.leftchild != None:
			current = current.leftchild
		return (current)

	def Inorder_by_Parent(self):
		current = self.root
		current = self.leftmost(current)

		while current:
			print (current.data, end = ' ')
			current = self.InorderSuccessor(current)

	def InorderPredecessor(self, current):
		if current.leftchild != None:
			current = current.leftchild
			result = self.rightmost(current)
			#print (result.data)
			return (result)

		while current.parent != None:
			if current.parent.rightchild != current:
				current = current.parent
			else:
				#print (current.parent.data)
				return (current.parent)

	def rightmost(self, current):
		while current.rightchild != None:
			current = current.rightchild
		return (current)

	def Inorder_Reverse(self):
		current = self.root
		current = self.rightmost(current)

		while current:
			print (current.data, end = ' ')
			current = self.InorderPredecessor(current)

class TreeNode():
	def __init__(self, x):
		self.leftchild = None
		self.rightchild = None
		self.parent = None
		self.data = x