class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        for i in range(ROWS):
            zero = False
            for j in range(COLS):
                if matrix[i][j] == 0:
                    matrix[i][j] = "X"
                    zero = True
                    break
            if zero:
                for j in range(COLS):
                    if matrix[i][j] != "X" and matrix[i][j] != 0:
                        matrix[i][j] = "O"
        
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == "X":
                    matrix[i][j] = 0
                
        for j in range(COLS):
            zero = False
            for i in range(ROWS):
                if matrix[i][j] == 0:
                    matrix[i][j] = "X"
                    zero = True
                    break
            if zero:
                for i in range(ROWS):
                    if matrix[i][j] != "X":
                        matrix[i][j] = "0"
        
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == "X" or matrix[i][j] == "O":
                    matrix[i][j] = 0