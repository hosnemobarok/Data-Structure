# Python program to introduce Binary Tree

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


if __name__ == '__main__':
    # create root
    root = Node(1)
    ''' 
        following is the tree after above statement
                 ___1___
                /       \
              None      None
    
    '''

    root.left = Node(2)
    root.right = Node(3)

    '''
        2 and 3 become left and right children of 1
                 ____1____
                /         \
             __2__       __3__
            /     \     /     \
         None    None None    None
    
    '''

    root.left.left = Node(4)
    '''
        4 becomes left child of 2
                 ____1____
                /         \
             __2__       __3__
            /     \     /     \
           4    None None    None
    
    '''

    # root node
    print(root.val)

    print(root.left.val)
    print(root.right.val)

    print(root.left.left.val)

