class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        indices = {}
        for i,num in enumerate(nums):
            if num in indices:
                last = indices[num]
                if i - last <= k:
                    return True
            indices[num] = i
        return False
        
