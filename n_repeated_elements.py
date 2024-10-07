"""
You are given an integer array nums with the following properties:

nums.length == 2 * n.
nums contains n + 1 unique elements.
Exactly one element of nums is repeated n times.
Return the element that is repeated n times.
"""
def repeatedN(nums):
    # d = {f"{x}":nums.count(x) for x in nums}
    # v = [ x for x in d.values()]
    # print(v)
    L = sorted(nums,reverse=True)
    i = nums.index(L[0])
    return nums[i]


print(repeatedN([2,1,2,5,3,2]))

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # d = {f"{x}":nums.count(x) for x in nums}
        # v = d.values()
        # L = sorted(nums)
        # L = sorted(nums,reverse=True)
        # i = nums.index(L[0])
        # return nums[i]
        count = {}
    
    # Count the occurrences of each element
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            
            # If any number appears n times, return it
            if count[num] == len(nums) // 2:
                return num



        

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        list1 = []
        for i in nums :
            if i in list1 :
                return i
            else :
                list1.append(i)

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        set1 = set()
        for i in nums :
            if i in set1 :
                return i
            else :
                set1.add(i)
