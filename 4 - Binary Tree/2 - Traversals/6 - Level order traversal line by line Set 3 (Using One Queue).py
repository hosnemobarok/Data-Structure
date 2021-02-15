# Python program to

class Node:
    def __init__(self, data):
        self.val = data
        self.left_child = None
        self.right_child = None


def printLevelLineByLine(root):
    if root is None:
        return

    queue = []

    queue.append(root)
    queue.append(None)


    while len(queue) > 1:
        # root node store
        current_node = queue.pop(0)


        if current_node == None:
            queue.append(None)
            print()

        else:
            if current_node.left_child:
                queue.append(current_node.left_child)


            if current_node.right_child:
                queue.append(current_node.right_child)

            print(current_node.val, end=" ")


# Driver Code
if __name__ == '__main__':
    """
                            ____10____
                          /            \
                      ___20___      ___30___
                     /        \    /        \
                   40         50  60        70
                  /  \
                100  None

    """
    # root node
    root = Node(10)

    root.left_child = Node(20)
    root.right_child = Node(30)

    root.left_child.left_child = Node(40)
    root.left_child.right_child = Node(50)

    root.right_child.left_child = Node(60)
    root.right_child.right_child = Node(70)

    root.left_child.left_child.left_child = Node(100)

    printLevelLineByLine(root)