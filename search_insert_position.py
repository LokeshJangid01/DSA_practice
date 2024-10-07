"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
"""
def searchInsert( nums,target):
    if target in nums:
        return nums.index(target)
    else:
        if target >max(nums):
            return len(nums)
        else:

            i = 0
            for n in nums:
                if target < n:
                    return i
                    break
                else:
                    i += 1

print(searchInsert([1,3,5,6],2))

#   Simple Binary search
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return left