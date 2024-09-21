"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""
def three_sum(nums):
    # Sort the array to make it easier to avoid duplicates and use two-pointer technique
    nums.sort()
    result = []

    for i in range(len(nums)):
        # Skip the same element to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Use two pointers to find pairs that sum to -nums[i]
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Move the left pointer to the right, avoiding duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Move the right pointer to the left, avoiding duplicates
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # Move both pointers
                left += 1
                right -= 1
            elif total < 0:
                left += 1  # We need a larger sum
            else:
                right -= 1  # We need a smaller sum

    return result
