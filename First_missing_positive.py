"""
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        M = max(nums)
        n = 1

        for _ in range(M):
            if n in nums:
                n += 1
                continue
            else:
                
                break
        return n
    