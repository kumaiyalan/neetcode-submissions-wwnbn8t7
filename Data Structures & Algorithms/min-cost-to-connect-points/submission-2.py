class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = [(0, (points[0][0], points[0][1]))]
        seen = set()
        res = 0
        while len(seen) != len(points):
            weight, curr = heapq.heappop(minHeap)
            if tuple(curr) in seen:
                continue
            seen.add(tuple(curr))
            res += weight
            for point in points:
                if tuple(point) not in seen:
                    distance = abs(point[0] - curr[0]) + abs(point[1] - curr[1])
                    heapq.heappush(minHeap, (distance, (point[0], point[1])))
        return res