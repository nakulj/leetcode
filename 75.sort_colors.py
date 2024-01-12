from collections import Counter
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = Counter(nums)
        cursor = iter(range(len(nums)))
        for color in range(3):
            for _ in range(counts[color]):
                nums[next(cursor)] = color
        
