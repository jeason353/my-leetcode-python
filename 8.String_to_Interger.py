# 32ms, faster than 84.12%
# 12.8MB, less than 100%
class Solution:
    def myAtoi(self, str: str) -> int:
        flag = False
        str = str.strip()
        strings = '-+0123456789'
        if len(str) == 0:
            return 0
        if str[0] not in strings:
            return 0
        if str[0] in '-+':
            flag = True
        for i in range(1, len(str)):
            if str[i] not in strings[2:]:
                str = str[:i]
                break
            flag = False
        if flag:
            return 0
        num = int(str)
        if num >= 2147483648:
            num = 2147483647
        if num < -2147483648:
            num = -2147483648
        return num
