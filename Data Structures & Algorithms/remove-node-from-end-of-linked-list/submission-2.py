# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        curr1 = curr2 = curr3 = head
        while curr1:
            curr1 = curr1.next
            sz += 1
        
        if sz == 1:
            return None
        elif sz - n == 0:
            return head.next

        x = 1
        curr3 = curr2.next
        while curr2 and curr3:
            if x == sz - (n - 1) - 1:
                curr2.next = curr3.next
                break
            
            curr2 = curr2.next
            curr3 = curr3.next
            x += 1
        
        return head
