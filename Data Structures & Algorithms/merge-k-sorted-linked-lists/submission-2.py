# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []
        prevdummy = ListNode()
        listptr = prevdummy

        for i, li in enumerate(lists):
            if li:
                heapq.heappush(q,(li.val,i,li)) #i is the listnum

        while q:
            val, listidx, ptr = heapq.heappop(q)
            listptr.next = ptr
            listptr = listptr.next
            if ptr.next:
                ptr = ptr.next
                heapq.heappush(q,(ptr.val,listidx,ptr))
        
        return prevdummy.next


