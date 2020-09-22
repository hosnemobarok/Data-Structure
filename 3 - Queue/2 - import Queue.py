from queue import Queue

Q = Queue(maxsize=4)

Q.put('1<- Md Hosne Mobarok')
Q.put('2<- Md Arman')
Q.put('4<- Md Asraful')
Q.put('5<- Md Araf')


#Queue Size
print(f'Queue Size-> {Q.qsize()}')

#Queue Empty
print(f'\nQueue is Empty:-> {Q.empty()}')

#Queue Full
print(f'\nQueue is Full-> {Q.full()}')

#Queue deque
all_men =[]
for deque in range(Q.maxsize):
    all_men.append(Q.get())
print(all_men)

#Queue Full
print(f'\nQueue is Full-> {Q.full()}')
