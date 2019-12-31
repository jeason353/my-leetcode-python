# 24ms, 93.58%
# 12.6MB, less than 100%
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        strList = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs',
            'tuv', 'wxyz']
        out = []
        if len(digits) == 0:
            return out
        out = [s for s in strList[int(digits[0])-2]]
        for digit in digits[1:]:
            out = [s+d for s in out for d in strList[int(digit)-2]]
        return out
