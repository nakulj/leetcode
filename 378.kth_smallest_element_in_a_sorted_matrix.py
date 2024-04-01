class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        r = k // n
        c = k % n
        return matrix[r][c]
        
