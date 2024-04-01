def it(mat):
    for row in mat:
        for e in row:
            yield e

class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])
        if m*n != r*c:
            return mat
        mat_it = it(mat)
        out = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                out[i][j] = next(mat_it)
        return out
        
