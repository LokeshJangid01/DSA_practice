"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        max_sum = float('-inf')
        max_level = 0
        current_level = 1
        queue = [(root, 1)]
        
        while queue:
            node, level = queue.pop(0)
            
            if level > current_level:
                current_level = level
                max_sum = node.val
            else:
                max_sum += node.val
                
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
                
        return max_level

obj = Solution()
