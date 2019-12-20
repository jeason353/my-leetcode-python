class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for i, num in enumerate(nums):
            if target - num not in nums_dict:
                nums_dict[num] = i
            else:
                return [nums_dict[target-num], i]
