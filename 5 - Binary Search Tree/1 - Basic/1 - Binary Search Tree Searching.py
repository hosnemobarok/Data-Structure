class Node:

    def __init__(self, data):
        self.val = data
        self.left_child = None
        self.right_child = None


def Inorder_Tree_Traversal(root):
    if root:
        Inorder_Tree_Traversal(root.left_child)
        print(root.val, end=" ")
        Inorder_Tree_Traversal(root.right_child)


def search_node(root, key):
    if root is None or root.val == key:
        return root

    # key is greater than root's key
    if root.val < key:
        return search_node(root.right_child, key)

    # key is smaller than root's key
    return search_node(root.left_child, key)



if __name__ == '__main__':
    """
    Before Binary Tree:
     
                     ____50____
                   /            \
               ___20___      ___60___
              /        \    /        \ 
            10         25  45        70
           /  \
          1  None

    """
    root = Node(50)

    root.left_child = Node(20)
    root.right_child = Node(60)

    root.left_child.left_child = Node(10)
    root.left_child.right_child = Node(25)

    root.right_child.left_child = Node(45)
    root.right_child.right_child = Node(70)

    root.left_child.left_child.left_child = Node(1)

    # call inorder function
    print("Print Binary Tree Inorder Traversal:")
    Inorder_Tree_Traversal(root)

    """
    After Binary Tree:
    
                         ____50____
                       /            \
                   ___20___      ___60___
                  /        \    /        \
                10         25  50        70
               /  \            /
              1  None         45

    """

    # call search function
    print("\nSearching node:")
    if search_node(root, 70):
        print('yes')
    else:
        print('no')