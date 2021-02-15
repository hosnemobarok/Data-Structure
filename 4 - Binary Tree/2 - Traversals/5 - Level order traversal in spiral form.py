# Python program for recursive level oreder

class Node:

    def __init__(self, data):
        self.val = data
        self.left_child = None
        self.right_child = None


def height(root):
    if root is None:
        return 0

    else:

        lheight = height(root.left_child)
        rheight = height(root.right_child)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1

def printGivenLevel(root, level, ltr):
    if root is None:
        return
    if level == 1:
        print(root.val, end=" ")

    elif level > 1:

        if ltr:
            printGivenLevel(root.left_child, level-1, ltr)
            printGivenLevel(root.right_child, level-1, ltr)

        else:
            printGivenLevel(root.right_child, level-1, ltr)
            printGivenLevel(root.left_child, level-1, ltr)

def printSpital(root):
    h = height(root)

    ltr = False
    for i in range(1, h+1):
        printGivenLevel(root, i, ltr)

        ltr = not ltr


if __name__ == '__main__':
    """

                        ____10____
                      /            \
                  ___20___      ___30___
                 /        \    /        \
               40         50  60        70
              /  \
            100  None
               
        Output: 10->20->30->70->60->50->40->100
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

    printSpital(root)