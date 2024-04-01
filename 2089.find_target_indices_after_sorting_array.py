from collections import Counter

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
       counts = Counter(nums) 
       if target not in counts:
           return []
       offset = sum(freq for num, freq in counts.items() if num < target)
       return [offset + i for i in range(counts[target])]
