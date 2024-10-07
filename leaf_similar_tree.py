"""
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
"""
# class TreeNode:
#     def __init__(self, value=0, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right

# class BST:
#     def __init__(self):
#         self.root = None

#     def insert(self, value):
#         if self.root is None:
#             self.root = TreeNode(value)
#         else:
#             self._insert(self.root, value)

#     def _insert(self, node, value):
#         if value < node.value:
#             if node.left is None:
#                 node.left = TreeNode(value)
#             else:
#                 self._insert(node.left, value)
#         else:
#             if node.right is None:
#                 node.right = TreeNode(value)
#             else:
#                 self._insert(node.right, value)

#     def get_leaf_nodes(self):
#         leaves = []
#         self._get_leaf_nodes(self.root, leaves)
#         return leaves

#     def _get_leaf_nodes(self, node, leaves):
#         if node is not None:
#             if node.left is None and node.right is None:
#                 leaves.append(node.value)
#             self._get_leaf_nodes(node.left, leaves)
#             self._get_leaf_nodes(node.right, leaves)

# # Example usage:
# # bst = BST()
# # bst.insert(5)
# # bst.insert(3)
# # bst.insert(8)
# # bst.insert(1)
# # bst.insert(4)
# # bst.insert(7)
# # bst.insert(9)
# # print(bst.get_leaf_nodes())  # Output: [1, 4, 7, 9]
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node, leaf_sequence):
            if not node:
                return
            if not node.left and not node.right:
                leaf_sequence.append(node.val)
            dfs(node.left, leaf_sequence)
            dfs(node.right, leaf_sequence)

        leaf_sequence1 = []
        leaf_sequence2 = []
        
        dfs(root1, leaf_sequence1)
        dfs(root2, leaf_sequence2)
        
        return leaf_sequence1 == leaf_sequence2
    
obj = Solution()

