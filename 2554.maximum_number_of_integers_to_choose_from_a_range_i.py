class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        candidates = (i for i in range(1, n + 1) if i not in banned_set)
        s = 0
        num_candidates = 0
        for candidate in candidates:
            if s + candidate > maxSum:
                break
            s += candidate
            num_candidates += 1
        return num_candidates
