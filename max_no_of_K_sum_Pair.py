"""
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations
"""

def max_operations(nums, k):
    count_map = {}
    operations = 0
    
    for num in nums:
        complement = k - num
        
        # Check if complement exists in the count map
        if count_map.get(complement, 0) > 0:
            # Perform an operation: use the complement and current number
            operations += 1
            count_map[complement] -= 1
        else:
            # Add the current number to the map for future pairings
            count_map[num] = count_map.get(num, 0) + 1
            
    return operations
