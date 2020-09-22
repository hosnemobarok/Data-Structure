# Python program to
# demonstrate stack implementation
# using collections.deque


from collections import deque

stack = deque()

# append() function to push
# element in the stack
stack.append('1->mobarok')
stack.append('2->arman')
stack.append('3->asraful')
stack.append('4->araf')
stack.append('5->abul bashar')


print('Initial stack:')
print(stack)

print()
print('popleft',stack.popleft())

# pop() fucntion to pop
# element from stack in
# LIFO order
print('\nElements poped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are poped:')
print(stack)

# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty
