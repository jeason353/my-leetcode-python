# 6384ms, 12.8MB
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ''
        else:
            max_len = 1
        left, right = 0, 1
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                half = (j - i + 1) // 2
                if s[i: i+half] == s[j:j-half:-1] and j-i+1 > max_len:
                    max_len = j-i+1
                    left, right = i, j+1

        print(left, right)
        return s[left:right]
