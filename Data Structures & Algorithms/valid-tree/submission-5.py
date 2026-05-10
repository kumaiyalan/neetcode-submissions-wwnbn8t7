class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = {i: [] for i in range(n)}
        for root, child in edges:
            graph[root].append(child)
            graph[child].append(root)
        seen = set()
        q = deque()
        q.append(0)

        while q:
            root = q.popleft()
            for children in graph[root]:
                if children not in seen:
                    q.append(children)
            seen.add(root)

        if len(seen) != n:
            return False

        return True        