# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 28ms, faster than 70.59%
# 12.9MB, less than 98.48%
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        now = head
        while now.next is not None:
            tmp = now.val
            now.val = now.next.val
            now.next.val = tmp
            if now.next.next is None:
                break
            now = now.next.next
        return head