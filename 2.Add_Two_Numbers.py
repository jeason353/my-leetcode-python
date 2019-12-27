# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        num1 = l1.val
        flag = 1
        while l1.next is not None:
            l1 = l1.next
            num1 = num1 + l1.val * 10**flag
            flag += 1
            
        num2 = l2.val
        flag = 1
        while l2.next is not None:
            l2 = l2.next
            num2 += l2.val * 10**flag
            flag += 1
            
        sum = num1 + num2
        l = ListNode(sum%10)
        sum = sum//10
        if sum != 0:
            t = ListNode(sum%10)
            l.next = t
            sum = sum//10
        while sum != 0:
            t.next = ListNode(sum%10)
            sum = sum // 10
            t = t.next
        return l