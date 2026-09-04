# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dum = l3 = ListNode()

        curr1 = l1
        curr2 = l2
        carry = False
        while curr1 and curr2:
            l3.next = ListNode()

            if carry:
                l3.next.val += 1

            if curr1.val + curr2.val >= 10:
                carry = True
            else:
                carry = False
            
            l3.next.val = (curr1.val + curr2.val) % 10
            
            curr1 = curr1.next
            curr2 = curr2.next
            l3 = l3.next

        if curr1:
            while curr1:
                l3.next = ListNode()
                if carry:
                    l3.next.val += 1
                
                if l3.next.val + curr1.val >= 10:
                    carry = True
                else:
                    carry = False
            
                l3.next.val = (l3.next.val + curr1.val) % 10
            
                curr1 = curr1.next
                l3 = l3.next
        else:
            while curr2:
                l3.next = ListNode()
                if carry:
                    l3.next.val += 1
                
                if l3.next.val + curr2.val >= 10:
                    carry = True
                else:
                    carry = False
            
                l3.next.val = (l3.next.val + curr2.val) % 10
                
                curr2 = curr2.next
                l3 = l3.next
        
        if carry:
            l3.next = ListNode(val=1)

        return dum.next
