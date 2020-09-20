class Node:
    def __init__(self,data=None, next=None):
        self.data = data
        self.next = next


class Linkedlist:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(repr(current_node.data))
            current_node = current_node.next

        return ' '.join(nodes)


    def append(self, data):
        current_node = Node(data)
        if self.head == None:
            self.head = current_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = current_node



    def prepend(self, data):
        current_node = Node(data)
        current_node.next = self.head
        self.head = current_node


    def searching(self, item):
        current_node = self.head
        while current_node:
            if current_node.data == item:
                return True
            current_node = current_node.next

        return False


    def inserting(self, prev, new_data):
        if prev is None:
            print('The given previous node must in LinkedList.')
            return

        node = Node(new_data)
        node.next = prev.next
        prev.next = node


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



if __name__ == '__main__':
    llist = Linkedlist()
    llist.append('a')
    llist.append('b')
    llist.prepend('1')
    llist.append(100)


    #inserting
    llist.inserting(llist.head.next.next, 'mobarok')

    print(llist)
    #remove
    remov = input('Remove:')
    llist.remove(remov)

    print(llist)


    #searching
    #for _ in range(int(input('Test Case:'))):
    s = input('searching:')
    if llist.searching(s):
        print("Yes")
    else:
        print("No")