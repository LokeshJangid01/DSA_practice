# class Solution:
#     def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
#         # Find the k largest elements from nums
#         largest_k_elements = sorted(nums, reverse=True)[:k]
        
#         # To preserve the order in the original array, use indices
#         result = []
#         for num in nums:
#             if num in largest_k_elements:
#                 result.append(num)
#                 largest_k_elements.remove(num)  # Remove the first occurrence from largest_k_elements
        
#         return result[:k]  # Return the subsequence of length k
        
from itertools import combinations

def find_subsequences(nums, k):
    # Use combinations to find all subsequences of length k
    return list(combinations(nums, k))

print(find_subsequences([-1,-2,3,4],2))

# def find_subsequences(nums, k):
#     result = []
    
#     # Helper function to generate subsequences recursively
#     def backtrack(start, path):
#         # If the length of the current path is equal to k, add it to the result
#         if len(path) == k:
#             result.append(path[:])  # Make a copy of path
#             return
        
#         # Recur over the remaining elements
#         for i in range(start, len(nums)):
#             # Include nums[i] in the current subsequence
#             path.append(nums[i])
#             # Move to the next element
#             backtrack(i + 1, path)
#             # Backtrack: remove the last added element
#             path.pop()
    
#     # Start the backtracking process
#     backtrack(0, [])
#     return result
