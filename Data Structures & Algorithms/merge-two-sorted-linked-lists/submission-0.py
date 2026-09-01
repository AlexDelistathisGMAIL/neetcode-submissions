# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        else:
            dum = list3 = None
            curr1 = None
            curr2 = None
            if list1.val <= list2.val:
                dum = list3 = ListNode(val=list1.val)
                curr1 = list1.next
                curr2 = list2
            else:
                dum = list3 = ListNode(val=list2.val)
                curr1 = list1
                curr2 = list2.next

            while curr1 and curr2:
                if curr1.val <= curr2.val:
                    list3.next = ListNode(val=curr1.val)
                    curr1 = curr1.next
                    list3 = list3.next
                else:
                    list3.next = ListNode(val=curr2.val)
                    curr2 = curr2.next
                    list3 = list3.next

            while curr1:
                list3.next = ListNode(val=curr1.val)
                curr1 =curr1.next
                list3 = list3.next
            
            while curr2:
                list3.next = ListNode(val=curr2.val)
                curr2 = curr2.next
                list3 = list3.next

            return dum