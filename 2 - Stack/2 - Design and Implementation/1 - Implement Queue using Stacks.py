# Python3 program to implement Queue using Stack

class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []


    def enQueue(self, data):
        self.s1.append(data)

    def print_stack(self):
        return self.s1

    def deQueue(self):
        if len(self.s1) == 0 and len(self.s2) == 0:
            print('Queue is Empty!')

        elif len(self.s2) == 0 and len(self.s1) > 0:

            while len(self.s1):
                # Queue last element store
                q_last_val = self.s1.pop()

                # stack insert queue last element
                self.s2.append(q_last_val)

            return self.s2.pop()

        else:
            return self.s2.pop()


# Driver code
if __name__ == '__main__':
    q = Queue()
    q.enQueue('Mobarok')
    q.enQueue('Arman')
    q.enQueue('Asraful')
    q.enQueue('Araf')

    print("Stack:->", q.print_stack())

    print('\nDQ:->', q.deQueue(), q.deQueue())

