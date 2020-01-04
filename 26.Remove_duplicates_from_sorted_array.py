# 100ms, 31.65%
# 14.3MB, less than 100%

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)