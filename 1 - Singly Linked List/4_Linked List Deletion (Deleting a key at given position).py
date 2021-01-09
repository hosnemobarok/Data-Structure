# Node class
class Node:

	def __init__(self, data):
		self.data = data
		self.next = None


# Linkedlist Class
class Linkedlist:
	def __init__(self):
		self.head = None


	def push(self, new_data):
		current_node = Node(new_data)
		current_node.next = self.head
		self.head = current_node


	def deletePositionNode(self, position):
		current_node = self.head

		if position == 1:
			self.head = self.head.next
			current_node = None
			return

		i = 1
		while position-1 > i:
			current_node = current_node.next
			i += 1

		temp = current_node.next
		current_node.next = temp.next

		return self.head



	def printlist(self):
		current_node = self.head
		while current_node:
			print(current_node.data, end=" ")
			current_node = current_node.next


if __name__ == '__main__':

	llist = Linkedlist()
	llist.push(2)
	llist.push(9)
	llist.push(5)
	llist.push(4)
	llist.push(1)

	llist.deletePositionNode(1)

	llist.printlist()