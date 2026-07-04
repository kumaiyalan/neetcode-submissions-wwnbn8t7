class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []
        for u, v, t in times:
            adj[u].append((v, t))
        heap = [(0, k)]
        time = [-1] * n
        while heap:
            t, n = heapq.heappop(heap)
            if time[n - 1] != -1:
                continue
            time[n - 1] = t
            for nn, nt in adj[n]:
                heapq.heappush(heap, (t + nt, nn))
        if -1 in time:
            return -1
        else:
            return max(time)