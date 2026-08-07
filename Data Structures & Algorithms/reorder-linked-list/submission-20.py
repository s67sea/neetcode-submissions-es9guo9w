# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: return


        slow = fast = head
        while fast.next:
            fast = fast.next
            if not fast.next:
                break
            fast = fast.next
            slow = slow.next
        
        #slow should be the last element of the previous side
        #fast should be the last element of the one to reverse
        prev = None; curr = slow.next
        slow.next = None #disconnect the two halves
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        #now we need to assemble the new list
        headcopy = head
        head2 = prev
        curr = head

        while head and head2:
            temp = head.next #save the ptr to node 2

            curr.next = head2
            head2 = head2.next
            curr = curr.next

            curr.next = temp
            head = temp
            curr = curr.next        


            
            