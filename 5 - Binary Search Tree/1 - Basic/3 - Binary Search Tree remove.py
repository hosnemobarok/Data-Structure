class Node:
    def __init__(self, data):
        self.val = data
        self.left_child = None
        self.right_child = None


def inorder_tree_traversal(root):
    if root:
        inorder_tree_traversal(root.left_child)
        print(root.val, end=" ")
        inorder_tree_traversal(root.right_child)


def findMin(root):
    while root.left_child is not None:
        root = root.left_child

    return root

def remove_node(root, key):
    if root is None: return None

    if root.val < key:
        root.right_child = remove_node(root.right_child, key)

    elif root.val > key:
        root.left_child = remove_node(root.left_child, key)

    else:
        if root.left_child is None:
            return root.right_child

        elif root.right_child is None:
            return root.left_child


        minNode = findMin(root.right_child)
        root.val = minNode.val
        root.right_child = remove_node(root.right_child, root.val)

    return root



if __name__ == '__main__':
    """
    Before Binary Tree:

                     ____50____
                   /            \
               ___30___      ___70___
              /        \    /        \
            20         40  60        80

    """
    root = Node(50)

    root.left_child = Node(30)
    root.right_child = Node(70)

    root.left_child.left_child = Node(20)
    root.left_child.right_child = Node(40)

    root.right_child.left_child = Node(60)
    root.right_child.right_child = Node(80)

    print('Inorder Tree Traversal:')
    inorder_tree_traversal(root)

    remove_node(root, 20)
    remove_node(root, 50)

    print("After Tree:\n")
    inorder_tree_traversal(root)


