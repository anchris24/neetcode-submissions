# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        start, end = head, head            
        grouphead, grouptail, prevgroup = None, None, None
        while start:
            for _ in range(k):
                if end == None:
                    return dummy.next
                end = end.next

            grouptail = start

            prev, curr, currnext = None, start, start.next
            for _ in range(k):
                curr.next = prev
                prev = curr
                curr = currnext
                if curr:
                    currnext = curr.next
            grouphead = prev
            
            grouptail.next = end
            if not prevgroup:
                dummy.next = grouphead
            else:
                prevgroup.next = grouphead
            prevgroup = grouptail

            start = end
        
        return dummy.next




