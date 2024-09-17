class Node:
	def __init__(self,item):
		self.data = item
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

lkl = LinkedList()
lkl.head = Node(1)
second = Node(2)
third = Node(3)
forth = Node(4)
fifth = Node(5)

lkl.head.next = second
second.next = third
third.next = forth
forth.next = fifth

while lkl.head!= None:
	print(lkl.head.data,end=' ')
	lkl.head = lkl.head.next