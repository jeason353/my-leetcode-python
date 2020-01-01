# 52ms, faster than 91.19%
# 13.2kb, less than 62.76%
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ''
        out = 0
        for c in s:
            if c not in substr:
                substr += c
            else:
                out = len(substr) if len(substr) > out else out
                substr = substr[substr.find(c) + 1:] + c
        out = len(substr) if len(substr) > out else out
        return out