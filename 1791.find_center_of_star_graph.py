from collections import Counter


class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        return next(iter(set(edges[0]) & set(edges[1])))
