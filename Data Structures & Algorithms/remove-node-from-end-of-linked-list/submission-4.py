# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr1 = curr2 = head
        for i in range(n):
            curr1 = curr1.next
    
        if not curr1:
            return head.next
        
        prev = None
        while curr1:
            curr1 = curr1.next
            prev = curr2
            curr2 = curr2.next
        prev.next = curr2.next
        return head