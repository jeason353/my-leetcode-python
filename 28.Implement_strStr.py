# 24ms, faster than 91.62%
#12.9MB, less than 100%

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(needle)
        for i in range(len(haystack) - l + 1):
            if haystack[i:i+l] == needle:
                return i
        return -1