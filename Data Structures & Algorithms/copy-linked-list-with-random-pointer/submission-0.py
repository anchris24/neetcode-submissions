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
        
        if head is None:
            return None
        
        pointer = head
        i = 0
        newmap = {None:None}
        while pointer:
            newhead = Node(pointer.val)
            newmap[pointer] = newhead
            pointer = pointer.next
        
        pointer = head
        while pointer:
            newmap[pointer].next = newmap[pointer.next]
            newmap[pointer].random = newmap[pointer.random]
            pointer = pointer.next
        
        return newmap[head]


