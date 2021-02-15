# Python program for level order

class Node:

    def __init__(self, data):
        self.val = data
        self.left_child = None
        self.right_child = None

def height(root):
    if root is None:
        return 0
    else:
        l_height = height(root.left_child)
        r_height = height(root.right_child)

        if l_height > r_height:
            return l_height+1
        else:
            return r_height+1

# print nodes at a given level
def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.val, end=" ")
    elif level > 1:
        printGivenLevel(root.left_child, level-1)
        printGivenLevel(root.right_child, level-1)


# Function to print level order traversal of tree
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printGivenLevel(root, i)


if __name__ == '__main__':
    """         
                    ____10____
                  /            \
              ___20___      ___30___
             /        \    /        \
           40         50 None      None
    """

    # root node
    root = Node(10)

    root.left_child = Node(20)
    root.right_child = Node(30)

    root.left_child.left_child = Node(40)
    root.left_child.right_child = Node(50)

    print("Print Binary Tree Level Height:")
    print(height(root))

    print('\nPrint Given Level:')
    printGivenLevel(root, level=height(root))

    print("\n\nPrint Level Order Tree Traversal:")
    printLevelOrder(root)



