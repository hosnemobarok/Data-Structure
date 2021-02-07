# Python3 program to implement Queue using Stack

class Queue:
    def __init__(self):
        self.queue = []
        self.stack = []


    def enQueue(self, data):
        self.queue.append(data)

    def print_qeue(self):
        return self.queue

    def deQueue(self):
        if len(self.queue) == 0 and len(self.stack) == 0:
            print('Queue is Empty!')

        elif len(self.stack) == 0 and len(self.queue) > 0:

            while len(self.queue):
                # Queue last element store
                q_last_val = self.queue.pop()

                # stack insert queue last element
                self.stack.append(q_last_val)

            return self.stack.pop()

        else:
            return self.stack.pop()


# Driver code
if __name__ == '__main__':
    q = Queue()
    q.enQueue('Mobarok')
    q.enQueue('Arman')
    q.enQueue('Asraful')
    q.enQueue('Araf')

    print("Queue:->", q.print_qeue())

    print('\nDQ:->', q.deQueue(), q.deQueue())


