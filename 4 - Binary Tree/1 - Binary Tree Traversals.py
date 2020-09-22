''''
    Inorder (Left, Root, Right) : 4 2 5 1 3
    Preorder (Root, Left, Right) : 1 2 4 5 3
    Postorder (Left, Right, Root) : 4 5 2 3 1

'''
# Python program to for tree traversals
# Binary Tree
class Node:
	def __init__(self,key):
		self.left = None
		self.right = None
		self.val = key


# A function to do inorder tree traversal
def printInorder(root):

	if root:

		# First recur on left child
		printInorder(root.left)

		# then print the data of node
		print(root.val),

		# now recur on right child
		printInorder(root.right)



# A function to do postorder tree traversal
def printPostorder(root):

	if root:

		# First recur on left child
		printPostorder(root.left)

		# the recur on right child
		printPostorder(root.right)

		# now print the data of node
		print(root.val),


# A function to do preorder tree traversal
def printPreorder(root):

	if root:

		# First print the data of node
		print(root.val),

		# Then recur on left child
		printPreorder(root.left)

		# Finally recur on right child
		printPreorder(root.right)


# Driver code
if __name__ == '__main__':

    # root node-> 1st
    root = Node(1)

    # root->left node-> 2nd
    root.left	 = Node(2)

    # root->right node-> 3rd
    root.right	 = Node(3)

    # root-left-left node-> 4th
    root.left.left = Node(4)

    # root-left-right node-> 5th
    root.left.right = Node(5)
    
    print("Preorder traversal of binary tree is:")
    printPreorder(root)

    print("\nInorder traversal of binary tree is:")
    printInorder(root)

    print("\nPostorder traversal of binary tree is:")
    printPostorder(root)
