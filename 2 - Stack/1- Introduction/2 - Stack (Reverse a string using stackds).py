class Stack:

    def __init__(self):
        self.stack = []


    def _push(self, item):
        self.stack.append(item)

    def _pop(self):
        return self.stack.pop()

    def isEmpty(self):
        if len(self.stack) == 0:
            return 'Stack is Empty'
        return True

    def reversed_stack(self):
        s = self.stack
        print(s[::-1])

        """for i in range(len(s)-1, -1, -1):
            print(self.stack[i], end=' ')"""



if __name__ == '__main__':
    s = Stack()
    # Stack push
    s._push(10)
    s._push(500)
    s._push(3)
    s._push(1000)

    # Stack all element
    print('Stack:->', s.stack)
    print('Pop Stack:->', s._pop())


    print('\nStack:->', s.stack)

    print('Reversed Stack:->', end=' ')
    s.reversed_stack()