# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr1 = dummy = ListNode(0,head) #starts 1 behind the head
        ptr2 = head

        for i in range(n):
            ptr2 = ptr2.next
        
        while ptr2:
            ptr2 = ptr2.next
            ptr1 = ptr1.next
        
        ptr1.next = ptr1.next.next
        return dummy.next
