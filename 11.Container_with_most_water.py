# 132ms, faster than 82.55%
# 14.5MB, less than 38.95%
class Solution:
    def maxArea(self, height: List[int]) -> int:
        min_num = min(height[0], height[-1])
        max_area = (len(height) - 1) * min_num
        left, right = 0, len(height)-1
        while left < right:
            if height[left] <= height[right]:
                left += 1
                if left == right:
                    break
                if height[left] > min_num:
                    min_num = min(height[left], height[right])
                    max_area = max(max_area, min_num*(right-left))
            else:
                right -= 1
                if left == right:
                    break
                if height[right] > min_num:
                    min_num = min(height[left], height[right])
                    max_area = max(max_area, min_num*(right-left))
        return max_area
