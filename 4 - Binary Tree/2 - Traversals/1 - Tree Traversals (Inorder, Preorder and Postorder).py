''''
    Inorder (Left, Root, Right) : 4 2 5 1 3
    Preorder (Root, Left, Right) : 1 2 4 5 3
    Postorder (Left, Right, Root) : 4 5 2 3 1
    
    
    
    
    Inorder function	:->  time complexity	: O(n)
    Preorder function	:->  time complexity	: O(n)
    Postorder function	:->  time complexity	: O(n)
'''
# Python program to Binary Tree Inorder Traversals
class Node:

    def __init__(self, data):
        self.left_child = None
        self.right_child = None
        self.val = data


# Preorder tree traversal
def printPreorder(root):
    if root:
        # First print teh data of node
        print(root.val, end=" ")
        # Then recur on left child
        printPreorder(root.left_child)
        # Finally recur on right child
        printPreorder(root.right_child)


# Inorder tree traversal
def prntInorder(root):
    if root:
        # First recur on left child
        prntInorder(root.left_child)
        # then print the data of node
        print(root.val, end=" ")
        # now recur on right child
        prntInorder(root.right_child)


# PostOrder tree tree traversal
def printPostorder(root):
    if root:
        # First recur on left child
        printPostorder(root.left_child)
        # teh recur on right child
        printPostorder(root.right_child)
        # now print the data of node
        print(root.val, end=" ")


if __name__ == '__main__':
    # root node
    root = Node(10)

    root.left_child = Node(20)
    root.right_child = Node(30)

    root.left_child.left_child = Node(40)

    # call print Preorder function
    print("Print Preorder Tree Traversal:")
    printPreorder(root)

    # call print Inorder function
    print("\n\nPrint Inorder Tree Traversal:")
    prntInorder(root)

    # call print Postorder function
    print("\n\nPrint Postorder function:")
    printPostorder(root)

"""
    1. root = Node(10)

                ____10____
              /            \
            None          None



    2. root.left_child = Node(20)

                    ____10____
                  /            \
              ___20___        None


    3. root.right_child = Node(30)

                    ____10____
                  /            \
              ___20___      ___30___
             /        \    /        \
          None       None None      None

    4. root.left_child.right_child = Node(40)

                    ____10____
                  /            \
              ___20___      ___30___
             /        \    /        \
           40       None None      None


    preorder    : 10->20->40->30
    inorder     : 40->20->10->30
    postorder   : 40->20->30->10

"""


