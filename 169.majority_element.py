class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        e = None
        count = 0
        for num in nums:
            if count == 0:
                e, count = num, 1
                continue
            if num == e:
                count += 1
            else:
                count -=1
        return e


        
