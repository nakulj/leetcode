from collections import defaultdict
from typing import Counter


class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        counts = Counter(nums)
        max_f = max(counts.values())
        return sum(f for f in counts.values() if f == max_f)


