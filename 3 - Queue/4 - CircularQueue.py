class circular_Queue:

    def __init__(self, size):
        self.items = [0]*size

        self.max_size = size    #total queue size
        self.head = 0           #head 0 number index
        self.tail = 0           #tail 0 number index
        self.size = 0           #queue size 0


    # Data Add------------------------------------------------
    def enqueue(self, item):
        if self.is_full():
            print("Queue is Full!")
            return

        print('Inserting', item)
        self.items[self.tail] = item                #items tail er moddo item raka holo
        self.tail = (self.tail + 1) % self.max_size # tail er (tail + 1) queue er max size data % kora holo
        self.size = self.size + 1                   # size er man 1 kore baranu holo


    # Data remove--------------------------------------------
    def dequeue(self):
        item = self.items[self.head] # item er moddo queue er head 0 number index raka holo
        self.head = (self.head + 1) % self.max_size # head er moddo (head+1) % max size dara % kora holo
        self.size -= 1 # size er man 1 kore - kora holo

        return item     # item return kora holo


    # Data Empty-----------------------------------------------
    def is_empty(self):
        if self.size == 0:  # queue size jodi 0 hoy
            return 'Queue is empty!'   #print(Queue empyt)
        return False    # Queue er moddo data ache


    # Data Full------------------------------------------------
    def is_full(self):
        if self.size == self.max_size:  # queue size == jodi queue max size == hoy
            return 'Queue is Full!'     # queue size full
        return False        # queue size full na



if __name__=="__main__":
    # Queue total size 5
    q = circular_Queue(5)   #queue er moddo 5 ta memorey boraddo kora holo

    # Data Add
    q.enqueue('1. kamal')
    q.enqueue('2. rofiq')
    q.enqueue('3. Hosne Mobarok')
    q.enqueue('4. pervej')
    q.enqueue('5. rabikul')


    print(f'\nQueue size:-> {q.is_full()}')

    # Data remove
    print('\nqueue remove element:')
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

    print(f'\nQueue size:-> {q.is_full()}')