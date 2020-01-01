# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 3864ms, faster than 12.73%
# 15.6MB, less than 100%
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        i = 0
        while i < len(lists):
            if lists[i] is None:
                lists.pop(i)
            else:
                i += 1
        if len(lists) == 0:
            return None
        
        min_num = lists[0].val
        loc = 0
        for i in range(len(lists)):
            if lists[i].val < min_num:
                min_num = lists[i].val
                loc = i

        l = ListNode(min_num)
        now = l
        lists[loc] = lists[loc].next
        if lists[loc] is None:
            lists.pop(loc)
        
        while len(lists) > 0:
            min_num = lists[0].val
            loc = 0
            for i in range(len(lists)):
                if lists[i].val < min_num:
                    min_num = lists[i].val
                    loc = i
            now.next = lists[loc]
            lists[loc] = lists[loc].next
            if lists[loc] is None:
                lists.pop(loc)
            now = now.next
        return l