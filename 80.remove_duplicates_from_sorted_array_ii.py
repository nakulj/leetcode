class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        dest = (i for i in range(len(nums) + 1))
        i = 0
        while i < len(nums):
            num = nums[i]
            nums[next(dest)] = num
            if i < len(nums) - 1 and nums[i + 1] == num:
                nums[next(dest)] = num
            while i < len(nums) and nums[i] == num:
                i += 1
        return next(dest)
