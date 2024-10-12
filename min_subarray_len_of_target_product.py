"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
"""
class Solution:
    def minSubArrayLen(self, target,nums):
        min_length = float('inf')
        left = 0
        current_sum = 0  # Initialize current_sum to track the sum of the window
        
        for right, num in enumerate(nums):
            current_sum += num  # Add the current number to the sum
            
            # Check if the current sum meets or exceeds the target
            while current_sum >= target:  # Shrink the window from the left
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]  # Subtract the leftmost number
                left += 1  # Move the left pointer to the right
        
        return min_length if min_length != float('inf') else 0
    

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0

        left = 0
        result = len(nums)+1
        curr = 0

        for right in range(len(nums)):
            curr += nums[right]
            
            # Shrink the window as long as current sum is >= target
            while curr >= target:
                result = min(result, right-left+1)
                curr -= nums[left]
                left += 1
        
        # If result was never updated, return 0, else return result
        return result if result != len(nums)+1 else 0


            
        
        
o = Solution()
print(o.minSubArrayLen(7,[2,3,1,2,4,3]))
