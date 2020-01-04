# 24ms, faster than 94.88%
# 12.8MB, less than 100%

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = dividend // divisor
        if result < 0 and dividend % divisor != 0:
            result += 1
        if result > 2147483647 or result < -2147483648:
            return 2147483647
        return result