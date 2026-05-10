class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for s, e in prerequisites:
            if s not in graph:
                graph[s] = []
            if e not in graph:
                graph[e] = []
            graph[e].append(s)
        completed = set()
        seen = set()
        def dfs(course):
            if course in completed:
                return True
            if course not in graph:
                return True
            if course in seen:
                return False
            seen.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            seen.remove(course)
            completed.add(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True