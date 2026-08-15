# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyhead = ListNode()
        dummyhead.next = head
        listptr = dummyhead

        while head:
            endoflastsubsection = listptr
            #advance the listptr by k
            #this gives the last element of the reversing section
            for _ in range(k):
                listptr = listptr.next
                if not listptr: return dummyhead.next

            #its next element is the first one after the reversing section
            #the section goes from head to listptr
            pickup = listptr.next
            listptr.next = None
            prev, curr = None, head
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            #prev is the end o the current section we just reversed (old end, new beginning)
            endoflastsubsection.next = prev
            head.next = pickup
            listptr = head
            head = head.next
        
        return dummyhead.next

