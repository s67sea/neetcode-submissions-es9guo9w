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
        if not head:
            return None
        #hashmap old node: new node
        hm = {}
        curr = head
        while curr:
            copy = Node(curr.val)
            hm[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            copy = hm[curr]
            if curr.next:
                copy.next = hm[curr.next]
            if curr.random:
                copy.random = hm[curr.random]
            curr = curr.next
        return hm[head]
        