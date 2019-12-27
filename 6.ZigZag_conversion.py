# 60ms, faster than 76.89%
# 12.9MB, less than 100%
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        string_list = ['' for i in range(numRows)]
        idx = 0
        down = True
        while idx < len(s):
            if down:
                for i in range(numRows):
                    string_list[i] += s[idx]
                    idx += 1
                    if idx >= len(s):
                        break
                down = False
            else:
                for i in range(numRows-1, 1, -1):
                    string_list[i-1] += s[idx]
                    idx += 1
                    if idx >= len(s):
                        break
                down = True
        return ''.join(string_list)
