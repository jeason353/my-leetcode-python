# 24ms, faster than 96.93%
# 12.6MB, less than 100%
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        s = str(x)
        while s[-1] == '0':
            s = s[:-1]
        if s[0] == '-':
            s = s[1:] + '-'
        res = int(s[::-1])
        if res < 2147483648 and res >= -2147483648:
            return res
        else:
            return 0
