# 28ms, faster than 83.26%
# 12.7MB, less than 100%

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[l] = nums[i]
                l += 1
        return l