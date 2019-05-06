from binary_serachTree import BinarySearchTree, TreeNode

a = TreeNode(8, "A")
T = BinarySearchTree(a)

T.Insert(2, "B")
T.Insert(1000, "C")
T.Insert(513, "D")

T.in_order()

T.Delete(8)

T.in_order()