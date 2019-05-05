from ImplementTree import BinaryTree, TreeNode

Tree = ["A", "B", "C", "D", "E", "F", "x", "x", "x", "G", "H", "x", "I"]

T = BinaryTree(Tree)

"""
a = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")
e = TreeNode("E")
f = TreeNode("F")
g = TreeNode("G")
h = TreeNode("H")
i = TreeNode("I")

T = BinaryTree(a)

a.leftchild = b
a.rightchild = c

b.leftchild = d
b.rightchild = e

e.leftchild = g
e.rightchild = h

c.leftchild = f
f.rightchild = i

b.parent = a
c.parent = a

d.parent = b
e.parent = b

g.parent = e
h.parent = e

f.parent = c
i.parent = f

T.pre_order(a)
print ("")
T.in_order(a)
print ("")
T.post_order(a)
print ("")
T.level_order()
print ("")
"""

T.Inorder_by_Parent()
print("")
T.Inorder_Reverse()
print ("")

T.InsertLevelorder("K")
T.InsertLevelorder("L")
T.InsertLevelorder("M")
T.InsertLevelorder("N")

T.Inorder_by_Parent()
print("")
T.Inorder_Reverse()