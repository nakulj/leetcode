from random import shuffle

class Solution:

    def __init__(self, nums: list[int]):
        self.nums = nums
        

    def reset(self) -> list[int]:
        return self.nums
        

    def shuffle(self) -> list[int]:
        nums = [num for num in self.nums ]
        shuffle(nums)
        return nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
