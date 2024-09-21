class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            if new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

bt = BinarySearchTree()
bt.insert(2)
bt.insert(1)
bt.insert(3)
print(bt.root.value)
print(bt.root.left.value)
print(bt.root.right.value)
                