# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        curr1 = curr2 = head
        while curr1:
            sz += 1
            curr1 = curr1.next
        
        if sz == 1:
            return None

        i = 0
        curr3 = curr2.next
        while curr2 and curr3:
            i += 1
            if i == sz - n:
                curr2.next = curr3.next
                break
            
            curr2 = curr2.next
            curr3 = curr3.next
        
        return head
