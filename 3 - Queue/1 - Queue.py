Queue = []

# Adding elements to the queue
Queue.append(1)
Queue.append(2)
Queue.append(3)
Queue.append(4)
print("Initial queue")
print(Queue)
print()


# Removing elements from the queue
print("\nElements dequeued from queue")
print(Queue.pop(0))
print(Queue.pop(0))
print(Queue.pop(0))

print("\nQueue after removing elements")
print(Queue)



#2nd code-----------------------------------------------
# using collections.dequeue
from collections import deque

# Initializing a queue
q = deque()

# Adding elements to a queue
q.append('a')
q.append('b')
q.append('c')
q.append('c')


print("Initial queue")
print(q)

# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)
