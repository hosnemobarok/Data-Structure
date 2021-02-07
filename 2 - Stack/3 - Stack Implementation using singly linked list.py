# Stack Implementation using singly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node('head')
        self.size = 0

    def print_stack_using_linkedlist(self):
        temp = self.head.next
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next

    def isEmpty(self):
        return self.size == 0

    def stack_top_val(self):
        if self.isEmpty():
            return 'Stack is Empty'
        return self.head.next.data


    def push(self, data):
        node = Node(data)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return 'Sorry Stack is Empty'

        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1

        return remove.data


if __name__ == '__main__':
    s = Stack()
    # stack push
    stack = [1, 2, 3, 4, 5]
    for i in stack:
        s.push(i)

    print('Before Stack:->', end=" ")
    s.print_stack_using_linkedlist()

    # stack pop
    s.pop()
    s.pop()
    s.pop()



    print('\n\nAfter Stack:->', end=" ")
    s.print_stack_using_linkedlist()

    # Stack Top value
    print("\n\nStack Top Value:->", end=" ")
    print(s.stack_top_val())

    # stack size
    print('Current Stack Size:->', s.size)