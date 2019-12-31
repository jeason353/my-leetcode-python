# 32ms, faster than 61.79%
# 12.7MB, less than 100%
class Solution:
    def isValid(self, s: str) -> bool:
        dicts = {'(':')', '[':']', '{':'}'}
        lst = ''
        for i in range(len(s)):
            if s[i] in dicts:
                lst += s[i]
            else:
                if len(lst) == 0:
                    return False
                if dicts[lst[-1]] == s[i]:
                    lst = lst[:-1]
                else:
                    return False
        if len(lst) == 0:
            return True
        else:
            return False
                