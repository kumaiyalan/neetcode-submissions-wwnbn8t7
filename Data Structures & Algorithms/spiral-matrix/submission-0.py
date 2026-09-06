class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        ROWS = len(matrix)
        COLS = len(matrix[0])
        total = ROWS * COLS

        def spiral(rows, cols):
            for i in range(cols, COLS - cols):
                res.append(matrix[rows][i])
            if len(res) == total:
                return
 
            for j in range(rows + 1, ROWS - rows):
                res.append(matrix[j][COLS - cols - 1])
            if len(res) == total:
                return

            for i in range(COLS - cols - 2, cols - 1, -1):
                res.append(matrix[ROWS - rows - 1][i])
            if len(res) == total:
                return

            for j in range(ROWS - rows - 2, rows, -1):
                res.append(matrix[j][cols])
            if len(res) == total:
                return
    
            if len(res) != total:
                spiral(rows + 1, cols + 1)
        
        spiral(0, 0)
        return res