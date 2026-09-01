# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        traversed = {}
        count = 0
        
        while head:
            if traversed.get(head, None) is not None:
                return True
            else:
                traversed[head] = count
                head = head.next
                count += 1
        
        return False
        