def is_sorted(nums):
    return all(a<=b for a,b in zip(nums, nums[1:]))

class Solution:
    def check(self, nums: list[int]) -> bool:
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                peak = i
                break
        else:
            return True
        return is_sorted(nums[peak+1:]) and nums[-1] <=nums[0]


