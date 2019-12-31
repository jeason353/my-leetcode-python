# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 24ms, faster than 97.26%
# 12.6MB, less than 100%
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        tmp = head
        now = head
        cnt = 0
        while now.next is not None:
            if cnt < n:
                now = now.next
                cnt += 1
            else:
                tmp = tmp.next
                now = now.next
        if cnt < n:
            return tmp.next
        if tmp.next.next is None:
            tmp.next = None
        else:
            tmp.next = tmp.next.next
        return head