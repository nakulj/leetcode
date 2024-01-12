class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        dest = iter(range(len(nums) + 1))
        i = 0
        while i < len(nums):
            num = nums[i]
            nums[next(dest)] = num
            while i < len(nums) and nums[i] == num:
                i += 1
        return next(dest)
