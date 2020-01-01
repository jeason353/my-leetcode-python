
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 24 ms, faster than 99.56%
# 12.8 MB, less than 100.00% 
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            if l1.val < l2.val:
                l3 = ListNode(l1.val)
                l1 = l1.next
            else:
                l3 = ListNode(l2.val)
                l2 = l2.next
        
        now = l3
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                now.next = l1
                l1 = l1.next
                now = now.next
                now.next = None
            else:
                now.next = l2
                l2 = l2.next
                now = now.next
                now.next = None
        if l1 is None and l2 is None:
            return l3
        elif l1 is None:
            now.next = l2
            return l3
        else:
            now.next = l1
            return l3
