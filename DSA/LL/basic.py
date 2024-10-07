class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, value):
        newnode = Node(value)
        self.head = newnode
        self.tail = newnode
        self.length = 1

    def addNode(self, value):
        newnode = Node(value)
        self.tail.next = newnode
        self.tail = newnode
        self.length += 1

    def popitem(self):
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

    def printLL(self):
        self.temp = self.head
        while self.temp is not None:
            print(self.temp.value)
            self.temp = self.temp.next


ll = LinkedList(5)
ll.addNode(1)
ll.addNode(2)
ll.addNode(3)
ll.addNode(4)
ll.printLL()

def getNode(ll, positionFromTail):
    # Write your code here
    temp = ll
    # print(temp.head)
    n = 0
    while temp:
        n += 1
        temp = temp.next
        
    des = n-positionFromTail-1
    temp = ll
    t = 0
    
    for _ in range(des):
        temp = temp.next
    return temp.value

print("value from position is ",getNode(ll.head, 2))
