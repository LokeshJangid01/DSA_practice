#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

#Note that you must do this in-place without making a copy of the array.

def moveZeroes(nums):
    # c = nums.count(0)
    # print(c)
    # l_z = [0]*c
    # print(l_z)
    # ln_z = [x for x in nums if x != 0]
    # print(ln_z)
    # return ln_z+l_z
    # for n in nums:
    #     if n == 0:
    #         nums.remove(0).append(0)
    # return nums
    non_zero_index = 0  # Initialize a pointer for the position of non-zero elements

    # First pass: Move all non-zero elements to the front, maintaining their order
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index] = nums[i]
            non_zero_index += 1

        # Second pass: Fill the rest of the list with zeroes
    for i in range(non_zero_index, len(nums)):
        nums[i] = 0
    return nums


print(moveZeroes([0,1,0,3,12]))