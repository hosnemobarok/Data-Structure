# Python Program to Stack Middle element

class Stack:

    def __init__(self):
        self.stack = []
        self.size = 0

    def print_stack(self):
        print("Before Stack:->", self.stack)

    def isEmpty(self):
        return self.size == 0

    def push(self, new_data):
        self.stack.append(new_data)
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return 'Stack is Empty!'
        self.size -= 1
        print("Stack Pop:->",self.stack.pop())




    # create stack middle value
    def stack_middle_val(self):
        return self.stack[self.size // 2]

# Driver Code
if __name__ == '__main__':
    s = Stack()
    s.push('mobarok')
    s.push('arman')
    s.push('asraful')
    s.push('araf')
    s.push('rayhan')
    s.push('kamal')

    # call print_stack function
    s.print_stack()
    print()

    # call pop function
    s.pop()
    s.pop()

    # call print_stack function
    print()
    s.print_stack()

    print("\nStack Middle Val:->", s.stack_middle_val())
    print("\nCurrent Stack Size:->", s.size)
