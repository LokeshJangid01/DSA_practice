class Node:
    def __init__(self,value):
        self.value = value
        self.pre = None
        self.next = None
class doublylinkedlist:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def add_node(self,value):
        
        new_node = Node(value)
        self.tail.next = new_node
        new_node.pre = self.tail
        self.tail = new_node

    def dll_pop(self):
        temp = self.head
        pre = None
        while temp:
            p = temp
            temp = temp.next
        p.next = None

    def print_dll(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next


dll = doublylinkedlist(1)
dll.add_node(2)
dll.add_node(3)
dll.add_node(4)
dll.add_node(5)
dll.print_dll()

dll.dll_pop()
dll.print_dll()