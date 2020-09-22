
class queue:

    def __init__(self):
        self.queue = []

    def enQueue(self, item):
        self.queue.append(item)

    def deQueue(self):
        return self.queue.pop()


    def isEmpty(self):
        if self.queue == []:
            return True
        return False


    def queue_size(self):
        return len(self.queue)


if __name__ == '__main__':
    q = queue()
    q.enQueue('1-> arman')
    q.enQueue('2-> asraful')
    q.enQueue('3-> araf')
    q.enQueue('4-> mobarok')

    q.deQueue()

    print('queue size:', q.queue_size())
    print()

    while not q.isEmpty():
        person = q.deQueue()
        print(person)
