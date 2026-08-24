class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        first, second = 0, 0
        n = len(mat)
        for i in range(n):
            first += mat[i][i]
            second += mat[i][n - 1 - i]
        if n % 2 != 0:
            first -= mat[n // 2][n // 2]
        return first + second