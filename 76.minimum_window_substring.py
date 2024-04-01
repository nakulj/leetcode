from collections import Counter
from typing import Iterable

def windows(s:str, n:int)->Iterable[tuple[str, Counter[str]]]:
    if len(s) <= n:
        return
    l = 0
    r = n
    window_ctr = Counter(s[:n])
    while True:
        yield s[l:r], window_ctr
        if r == len(s):
            return
        window_ctr[s[l]] -= 1
        window_ctr[s[r]] += 1
        l += 1
        r += 1


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        for substr, counts in windows(s, len(t)):
            if counts == target:
                return substr
            else:
                print(counts, target)
        return ""
