"""
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
"""

"""
To delete the middle node of a singly linked list, we can use the two-pointer technique:

We use two pointers, slow and fast. The fast pointer moves two steps at a time, while the slow pointer moves one step at a time.
By the time the fast pointer reaches the end of the list, the slow pointer will be at the middle node.
Once we find the middle node, we adjust the pointers to skip over the middle node, thereby deleting it.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteMiddle(head: ListNode) -> ListNode:
    # Edge case: If there's only one node, return None (empty list)
    if not head or not head.next:
        return None
    
    # Initialize slow and fast pointers
    slow = head
    fast = head
    prev = None  # To keep track of the node before slow
    
    # Move fast pointer two steps and slow pointer one step
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    # Now slow is at the middle node, and prev is the node before it
    prev.next = slow.next  # Delete the middle node
    
    return head
