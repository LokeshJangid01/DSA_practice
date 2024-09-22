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

    def contains(self,value):
        if self.root is None:
            return False
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    
    def pre_order_dfs(self,node):
        if node is None:
            return
        print(node.value,end=' ')
        self.pre_order_dfs(node.left)
        self.pre_order_dfs(node.right)

    
    def in_order_dfs(self,node):
        
        if node is None:
            return
        self.in_order_dfs(node.left)
        print(node.value, end=' ')
        self.in_order_dfs(node.right)

    def post_order_dfs(self,node):
        if node is None:
            return
        self.post_order_dfs(node.left)
        self.post_order_dfs(node.right)
        print(node.value,end=' ')

    def bfs(self,node):
        if node is None:
            return 
        queue = [node]
        while len(queue) > 0:
            print(queue[0].value,end=' ')
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)



    # In-order DFS: Left, Root, Right
# def in_order_dfs(node):
#     if node is None:
#         return        
#     in_order_dfs(node.left)
#     print(node.value, end=' ')
#     in_order_dfs(node.right)

# def post_order_dfs(node):
#     if node is None:
#         return
#     post_order_dfs(node.left)
#     post_order_dfs(node.right)
#     print(node.value,end=' ')




bt = BinarySearchTree()
bt.insert(2)
bt.insert(1)
bt.insert(3)
bt.insert(4)
bt.insert(5)
bt.in_order_dfs(bt.root)
print(" \n")
bt.post_order_dfs(bt.root)
print(" \n")
bt.pre_order_dfs(bt.root)
print(" \n")
bt.bfs(bt.root)
# print(bt.root.value)
# print(bt.root.left.value)
# print(bt.root.right.value)

# print(bt.contains(3))
# print(bt.contains(4))

                