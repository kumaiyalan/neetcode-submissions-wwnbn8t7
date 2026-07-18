class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = set()
        cols = set()

        for row in board:
            rows = set()
            for i in range(0, 9):
                if row[i] != '.':
                    if row[i] in rows:
                        return False
                    else:
                        rows.add(row[i])
        print("ROW CHECK PASSED")

        for i in range(0, 9):
            cols = set()
            for row in board:
                if row[i] != '.':
                    if row[i] in cols:
                        return False
                    else:
                        cols.add(row[i])
        print("COL CHECK PASSED")


        startPoints = [[0, 0], [0, 3], [0, 6],
                       [3, 0], [3, 3], [3, 6],
                       [6, 0], [6, 3], [6, 6]]
        square = set()

        for start in startPoints:
            square = set()
            for x in range(start[0], start[0] + 3):
                for y in range(start[1], start[1] + 3):
                    if board[x][y] != '.':
                        if board[x][y] in square:
                            return False
                        else:
                            square.add(board[x][y])

        return True    