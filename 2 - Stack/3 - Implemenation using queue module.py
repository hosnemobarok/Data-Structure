from queue import LifoQueue

stack = LifoQueue(maxsize=5)
print(f'stack size-> {stack.qsize()}')

# stack push
stack.put('1->mobarok')
stack.put('2->arman')
stack.put('3->asraful')
stack.put('4->araf')
stack.put('5->abul bashar')

print(f'stack full:->{stack.full()}')
print(f'stack size-> {stack.qsize()}')

print('\nElements Poped From The Stack:')
print(stack.get())
print(stack.get())
print(stack.get())
print(stack.get())
print(stack.get())

print('\nstack is empty->',stack.empty())
print(f'stack max-size:-> {stack.maxsize}')
print(f'stack size:-> {stack.qsize()}')
