"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        # res = 0
        # n = len(height)

        # # For every element of the array
        # for i in range(1, n - 1):

        #     # Find the maximum element on its left
        #     left = height[i]
        #     for j in range(i):
        #         left = max(left, height[j])

        #     # Find the maximum element on its right
        #     right = height[i]

        #     for j in range(i + 1, n):
        #         right = max(right, height[j])

        #     # Update the maximum water
        #     res = res + (min(left, right) - height[i])

        # return res
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water_trapped = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water_trapped += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water_trapped += right_max - height[right]
        
        return water_trapped
        