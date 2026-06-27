class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        res = {}
        adj = {i: [] for i in range(n)}
        for edge in edges:
            adj[edge[0]].append((edge[1], edge[2]))
        
        minHeap = [(0, src)]
        while minHeap:
            curr_w, curr_v = heapq.heappop(minHeap)
            if curr_v in res:
                continue
            res[curr_v] = curr_w
            
            for neighbour_v, neighbour_w in adj[curr_v]:
                if neighbour_v not in res:
                    heapq.heappush(minHeap, (curr_w + neighbour_w, neighbour_v))
        
        for i in range(n):
            if i not in res:
                res[i] = -1
        return res