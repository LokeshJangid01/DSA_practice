"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked-list:
1->1->2->3->4->4->5->6
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        R = []
        for l in lists:
            temp = l
            while temp:
                R.append(temp.val)
                temp = temp.next
            

        R.sort()
        head = temp = None
        for e in R:
            if head is None:

                new = ListNode(e)
                head = temp =  new
            else:
                new = ListNode(e)
                temp.next = new
                temp = new
        return head


        