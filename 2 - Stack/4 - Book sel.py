'''
    Complexity:-
            push()----O(1)
            pop() ----O(1)

'''

class Book_Stack:

    def __init__(self):
        self.items = [] # Book sel

    def push(self, item):
        self.items.append(item) # Book sell er moddo Book raka kora holo

    def pop(self):
        return self.items.pop()


    def Book_sel_empty(self):
        if self.items == []:
            return 'sorry Book sel empty!'
        return False




if __name__=="__main__":
    book = Book_Stack()

    book.push('1. Bangla')
    book.push('2. English')
    book.push('3. Math')
    book.push('4. Programming')
    book.push('5. Oparating System')

    book.pop()

    while not book.Book_sel_empty():
        item = book.pop()
        print(item)
