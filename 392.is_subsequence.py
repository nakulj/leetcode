from collections import defaultdict
from bisect import bisect_right




class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        indices = defaultdict(list)
        for i, c in enumerate(t):
            indices[c].append(i)
        i = -1
        for c in s:
            try:
                i = next(j for j in indices[c] if j > i)
            except ValueError:
                return False
        return True
