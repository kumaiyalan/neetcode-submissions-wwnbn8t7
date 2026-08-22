class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        first, last = 0, len(matrix) - 1

        while first < last:
            for i in range(len(matrix[first])):
                matrix[first][i], matrix[last][i] = matrix[last][i], matrix[first][i]
            first += 1
            last -= 1
        
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]