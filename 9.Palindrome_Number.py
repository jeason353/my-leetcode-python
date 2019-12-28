# 52ms, faster than 93.54%
# 12.7MB, less than 100%
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        l = len(s)
        half = l // 2
        if s[:half] == s[l-1:l-half-1:-1]:
            return True
        else:
            return False
