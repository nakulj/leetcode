from collections import Counter
from heapq import heappush, heappushpop


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = iter((freq, value) for value, freq in Counter(nums).items())
        top_k: list[tuple[int, int]] = []
        for _ in range(k):
            heappush(top_k, next(counts))
        for count in counts:
            heappushpop(top_k, count)
        return [value for _, value in top_k]
