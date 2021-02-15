# python program to find n-th node of binary tree traversal
class Node:

    def __init__(self, data):
        self.val = data
        self.left_child = None
        self.right_child = None



flag = [0]
def Nth_node_postorder(root, n):

    if root is None:
        return

    if flag[0] <= n:
        # left child recursion
        Nth_node_postorder(root.left_child, n)
        # right child recursion
        Nth_node_postorder(root.right_child, n)

        flag[0] += 1

        if flag[0] == n:
            print(root.val)


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
    n = 2
    Nth_node_postorder(root, n)