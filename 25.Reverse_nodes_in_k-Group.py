# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 48ms, faster than 56.07%
# 13.6MB, less than 100%
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None or k == 1:
            return head
        left, right = head, head
        cnt = 0
        val_lst = []
        while right is not None:
            val_lst.append(right.val)
            right = right.next
            cnt += 1
            if cnt == k:
                for i in range(cnt):
                    left.val = val_lst.pop()
                    left = left.next
                cnt = 0
        return head