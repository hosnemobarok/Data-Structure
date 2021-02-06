# Python program for implementation of stack
class Stack:

    def __init__(self):
        self.stack = []
        self.size = 0

    def _push(self, item):
        self.stack.append(item)
        self.size += 1

    def _pop(self):
        self.size -= 1
        return self.stack.pop()

    def isEmpty(self):
        if len(self.stack) == 0:
            return 'Stack is Empty'

        return f"Stack total element:-> {len(s.stack)}"


    def stack_top_element(self):
        if len(self.stack) > 0:
            stack_top_element = self.stack[len(self.stack)-1]
            return stack_top_element

        return 'sorry stack is empty'


if __name__ == '__main__':
    s = Stack()

    arr = [100, 10, 5, 500]
    for i in arr:
        s._push(i)

    # push stack 50
    s._push(50)

    # Stack all element print
    print("Stack:->:", s.stack)

    # pop stack element
    print('\nStack pop element:')
    print(s._pop())
    print(s._pop())

    # call isEmpty function
    print()
    print(s.isEmpty())

    print('\nStack:->', end=" ")
    print(s.stack)

    print("\nStack Size:->", s.size)

    # Stack top element print
    print('\nTop Element:->', s.stack_top_element())
