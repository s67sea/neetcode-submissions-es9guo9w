"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        copies = {}
        headcopy = Node(head.val,None,None) #leave the randoms as none for now
        copies[head] = headcopy

        curr = head
        currcopy = headcopy
        while curr.next:
            curr = curr.next
            currcopy.next = Node(curr.val,None,None)
            currcopy = currcopy.next
            copies[curr] = currcopy
        
        curr = head
        currcopy = headcopy
        while currcopy:
            currcopy.random = copies[curr.random] if curr.random else None
            currcopy = currcopy.next
            curr = curr.next
        
        return headcopy

