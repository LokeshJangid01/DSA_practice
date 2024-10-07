"""
You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k. You must choose a subsequence of indices from nums1 of length k.

For chosen indices i0, i1, ..., ik - 1, your score is defined as:

The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.
It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).
Return the maximum possible score.

A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1} by deleting some or no elements.

 

Example 1:

Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
Output: 12
Explanation: 
The four possible subsequence scores are:
- We choose the indices 0, 1, and 2 with score = (1+3+3) * min(2,1,3) = 7.
- We choose the indices 0, 1, and 3 with score = (1+3+2) * min(2,1,4) = 6. 
- We choose the indices 0, 2, and 3 with score = (1+3+2) * min(2,3,4) = 12. 
- We choose the indices 1, 2, and 3 with score = (3+3+2) * min(1,3,4) = 8.
Therefore, we return the max score, which is 12.
Example 2:

Input: nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1
Output: 30
Explanation: 
Choosing index 2 is optimal: nums1[2] * nums2[2] = 3 * 10 = 30 is the maximum possible score.

"""

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Sort the pairs of nums1 and nums2 based on nums2 values in descending order
        pairs = sorted(zip(nums1, nums2), key=lambda x: -x[1])
        
        # Initialize a min-heap to keep track of the smallest elements
        min_heap = []
        
        # Initialize variables to keep track of the current sum and result
        current_sum = 0
        result = 0
        
        # Iterate through the pairs
        for num1, num2 in pairs:
            # Add the current num1 to the sum
            current_sum += num1 
            
            # Push the current num1 onto the min-heap
            heapq.heappush(min_heap, num1)
            
            # If the heap size exceeds k, remove the smallest element
            if len(min_heap) > k:
                current_sum -= heapq.heappop(min_heap)
            
            
            # Update the result with the maximum of the current sum and the current result
            result = max(result, current_sum * num2)
        
        # Return the maximum possible score
        return result



