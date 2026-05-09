class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        pacificQ, atlanticQ = deque(), deque()

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    pacificQ.append((r, c))
                    pacific.add((r, c))
                if r == ROWS - 1 or c == COLS - 1:
                    atlanticQ.append((r, c))
                    atlantic.add((r, c))

        while pacificQ:
            node = pacificQ.popleft()
            r, c = node[0], node[1]
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for nr, nc in directions:
                if (r + nr < 0 or c + nc < 0 or
                    r + nr == ROWS or c + nc == COLS or
                    (r + nr, c + nc) in pacific or
                    heights[r + nr][c + nc] < heights[r][c]):
                    continue
                pacificQ.append((r + nr, c + nc))
                pacific.add((r + nr, c + nc))  

        while atlanticQ:
            node = atlanticQ.popleft()
            r, c = node[0], node[1]
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for nr, nc in directions:
                if (r + nr < 0 or c + nc < 0 or
                    r + nr == ROWS or c + nc == COLS or
                    (r + nr, c + nc) in atlantic or
                    heights[r + nr][c + nc] < heights[r][c]):
                    continue
                atlanticQ.append((r + nr, c + nc))
                atlantic.add((r + nr, c + nc))  
        res = []
        for r, c in (pacific & atlantic):
            res.append([r, c])
        return res      