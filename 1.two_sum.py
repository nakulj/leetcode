class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indices = {num: i for i, num in enumerate(nums)}
        return next(
            [i, ci]
            for i, num in enumerate(nums)
            if (ci := indices.get(target-num,None)) is not None and ci != i
        )
