class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {}
        for point in points:
            adj[tuple(point)] = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                xi, yi = points[i]
                xj, yj = points[j]
                distance = abs(xi - xj) + abs(yi - yj)
                adj[tuple(points[i])].append([distance, xj, yj])
                adj[tuple(points[j])].append([distance, xi, yi])
        minHeap = [(0, points[0])]
        seen = set()
        res = 0
        while len(seen) != len(points):
            weight, point = heapq.heappop(minHeap)
            if tuple(point) in seen:
                continue
            seen.add(tuple(point))
            res += weight
            for neighbour in adj[tuple(point)]:
                heapq.heappush(minHeap, (neighbour[0], [neighbour[1], neighbour[2]]))
        return res