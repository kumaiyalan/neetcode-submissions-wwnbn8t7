class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        q = deque()
        seen = set()
        count = 0

        for i in range(n):
            if i not in seen:
                count += 1
                q.append(i)
                seen.add(i)
                while q:
                    node = q.popleft()
                    for neighbor in graph[node]:
                        if neighbor not in seen:
                            q.append(neighbor)
                            seen.add(neighbor)
        
        return count