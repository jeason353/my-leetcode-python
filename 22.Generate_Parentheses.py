# 24ms, faster than 98.71%
# 13MB, less than 100%
class Solution:
    def back(self, lst, s, left, right ,n):
        if len(s) == n*2:
            lst.append(s)
            return
        
        if left < n:
            self.back(lst, s+'(', left+1, right, n)
        if right < n and left > right:
            self.back(lst, s+')', left, right+1, n)

    def generateParenthesis(self, n: int) -> List[str]:
        lst = []
        self.back(lst, '', 0, 0, n)
        return lst
