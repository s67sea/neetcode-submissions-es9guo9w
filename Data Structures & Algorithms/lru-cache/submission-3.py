class Node:
    def __init__(self,key=0,val=0,prev=None,next=None):
        #we have to store the key so that we can update the hashmap
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.hm = {} #key: Node
        self.capacity = capacity

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def removeFromList(self, node: Node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

    def moveToFront(self, node: Node):
        ###
        prevnext = self.head.next
        prevnext.prev = node
        node.next = prevnext
        node.prev = self.head
        self.head.next = node

    def get(self, key: int) -> int:
        #if the value doesn't exist in the hm, return -1
        if key not in self.hm:
            return -1
        
        #return the value, and also move the Node to the beginning of the list
        res = self.hm[key].val
        node = self.hm[key]

        self.removeFromList(node)
        self.moveToFront(node)

        return res
        

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            #update the value, move to front
            node = self.hm[key]
            node.val = value
            self.removeFromList(node)
            self.moveToFront(node)

        else:
            #make new value, put at front
            node = Node(key,value,None,None)
            self.moveToFront(node)
            self.hm[key] = node
        
        if len(self.hm) > self.capacity:
            toremove = self.tail.prev
            self.removeFromList(toremove)
            del self.hm[toremove.key]

        

        

        
