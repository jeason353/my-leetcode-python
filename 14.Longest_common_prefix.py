# 32ms, 81.85%
# 12.8MB, less than 100%
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        lenght = len(strs[0])
        for s in strs:
            if len(s) < lenght:
                lenght = len(s)
        for i in range(lenght):
            tmp_s = strs[0][:i+1]
            for s in strs:
                if tmp_s != s[:i+1]:
                    return strs[0][:i]
        return strs[0][:lenght]
