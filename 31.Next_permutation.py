# 32ms, faster than 97.36%
# 12.6MB, less than 100%

class Solution:
    def nextPermutation(self, nums:List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(-2, -len(nums)-1, -1):
            if nums[i] < nums[i+1]:
                l = - i - 1
                val = nums[i]
                for j in range(1, l+1):
                    if nums[-1] > val:
                        nums.insert(i+1, nums.pop())
                        break
                    else:
                        nums.insert(i+j, nums.pop())
                for k in range(-2, j-l-1, -1):
                    nums.append(nums.pop(k))
                break
            if i == -len(nums):
                nums.sort()
