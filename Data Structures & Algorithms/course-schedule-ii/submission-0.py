class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        
        degree = [0] * numCourses

        for prereq in prerequisites:
            a, b = prereq[0], prereq[1]
            adj[b].append(a)
            degree[a] += 1

        queue = deque()
        for i in range(len(degree)):
            if degree[i] == 0:
                queue.append(i)

        topSort = []

        while queue:
            nxt = queue.popleft()
            topSort.append(nxt)
            for course in adj[nxt]:
                degree[course] -= 1
                if degree[course] == 0:
                    queue.append(course)

        if len(topSort) == numCourses:
            return topSort
        else:
            return []
