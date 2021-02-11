# Queue implementation in Python

class Queue:

    def __init__(self):
        self.queue = []
        self.size = 0

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)
        self.size += 1

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None

        self.size -= 1
        return self.queue.pop(0)

    # Display  the queue
    def display(self):
        print(self.queue)


if __name__ == '__main__':

    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    q.display()

    q.dequeue()
    q.dequeue()

    print("After removing an element")
    q.display()
    print('\nQueue size:->', q.size)
