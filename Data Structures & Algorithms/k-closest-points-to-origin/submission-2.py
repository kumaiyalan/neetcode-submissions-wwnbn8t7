class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        close = []
        for point in points:
            x1 = point[0]
            y1 = point[1]
            distance = math.sqrt((x1 ** 2) + (y1 ** 2))
            heapq.heappush(close, (-distance, point))
            if len(close) > k:
                heapq.heappop(close)
        ans = []
        for point in close:
            ans.append(point[1])
        return ans 