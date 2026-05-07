class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        ROW, COL = len(image), len(image[0])
        paint = set()
        def dfs(r, c, clr):
            if (min(r, c) < 0 or
                r == ROW or c == COL or
                image[r][c] != clr or 
                (r, c) in paint):
                return
            else:
                paint.add((r, c))
            dfs(r + 1, c, clr)
            dfs(r - 1, c, clr)
            dfs(r, c + 1, clr)
            dfs(r, c - 1, clr)
            return
        dfs(sr, sc, image[sr][sc])
        for cell in paint:
            image[cell[0]][cell[1]] = color
        return image

"""
[1, 1, 1]
[1, 1, 0]
[1, 0, 1]
"""