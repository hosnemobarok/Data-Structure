# python program for nth node of inorder traversal
class Node:

    def __init__(self, data):
        self.val = data
        self.left_child = None
        self.right_child = None


count = [0]


# Given binary tree, print the nth node of inorder tree traversal

def Nth_node_inorder(root, n):
    if root is None:
        return

    if count[0] <= n:
        print('c', count[0], '<=', n)
        Nth_node_inorder(root.left_child, n)
        count[0] += 1

        if count[0] == n:
            print(root.val)

        Nth_node_inorder(root.right_child, n)


# Driver Code
if __name__ == '__main__':
    # root node
    root = Node(10)
    """
        1. root = Node(10)

                ____10____
              /            \
            None          None

    """
    root.left_child = Node(20)
    """
        2. root.left_child = Node(20)

                    ____10____
                  /            \
              ___20___        None
    """
    root.right_child = Node(30)
    """
        3. root.right_child = Node(30)

                    ____10____
                  /            \
              ___20___      ___30___
             /        \    /        \
          None       None None      None
    """
    root.left_child.left_child = Node(40)
    """
        4. root.left_child.right_child = Node(40)

                    ____10____
                  /            \
              ___20___      ___30___
             /        \    /        \
           40       None None      None
    """

    # call Nth_node_inorder tree traversal
    # n = int(input())
    n = 3
    Nth_node_inorder(root, n)
