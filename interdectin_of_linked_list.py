# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp1 = headA
        temp2 = headB
        List1 = []
        List2 = []
        while temp1:
            List1.append(temp1.val)
            temp1 = temp1.next
        while temp2:
            List2.append(temp2.val)
            temp2 = temp2.next
        set1 = set(List1)
        set2 = set(List2)
        common_element = list(set1.intersection(set2))[0]
        Skip1 = 0
        Skip2 = 0
        while temp1:

            Skip1.append(temp1.val)
            if temp1.val == common_element:
                break
            else:
                temp1 = temp1.next
                Skip1 += 1

        while temp2:
            Skip2.append(temp2.val)
            if temp2.val == common_element:
                break
            else:
                temp2 = temp2.next
                Skip2 += 1

        return common_element,List1,List2,Skip1,Skip2

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        pA, pB = headA, headB
        
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        
        return pA

            

        
        
        