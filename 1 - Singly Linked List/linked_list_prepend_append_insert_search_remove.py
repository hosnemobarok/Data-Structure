''''
        # printllist()      Time complexity   : O(n)
                            space complexity  : O(1)

        # push()            Time complexity   : O(1)
                            Space complexity  : O(1)

        # append()          Time complexity   : O(n)
                            space complexity  : O(1)

        # prepend()         Time complexity   : O(1)
                            space complexity  : O(1)

        # searching()       Time complexity   : O(n)
                            space complexity  : O(1)


        # inserting()       Time complexity   : O(n)
                            space complexity  : O(1)

        # remove()          Time complexity   : O(n)
                            space complexity  : O(1)

'''

# Node class
class Node:
    def __init__(self,data=None, next=None):
        self.data = data # Assign data
        self.next = next # Initialize next as null


# Linked List class contains a Node object
class Linkedlist:
    def __init__(self):
        
        # Function to initialize head
        self.head = None

    # linked list traverse
    def printllist(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next


    # linked list Insert at the end
    def append(self, data):
        current_node = Node(data)
        if self.head == None:
            self.head = current_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = current_node


    # linked list Insert after a node
    def prepend(self, data):
        current_node = Node(data)
        current_node.next = self.head
        self.head = current_node

    # linked list searching node
    def searching(self, item):
        current_node = self.head
        while current_node:
            if current_node.data == item:
                return True
            current_node = current_node.next

        return False

    # linked list Insert at the beginning
    def inserting(self, prev, new_data):
        if prev is None:
            print('The given previous node must in LinkedList.')
            return

        node = Node(new_data)
        node.next = prev.next
        prev.next = node


    # linked list remove node
    def remove(self, item):
        # Store head node
        temp = self.head
        if temp == None:
            return

        # If head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == item:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == item:
                break
            prev = temp
            temp = temp.next


        prev.next = temp.next
        temp = None


# Code execution starts here
if __name__ == '__main__':

    # Start with the empty list
    llist = Linkedlist()
    llist.append('a')
    llist.append('b')
    llist.prepend('1')
    llist.append(100)
    llist.printllist()

    #inserting
    llist.inserting(llist.head.next.next, 'mobarok')
    llist.printllist()

    #remove
    llist.remove('b')

    llist.printllist()


    #searching
    print()
    if llist.searching('1'):
        print("Yes")
    else:
        print("No")
