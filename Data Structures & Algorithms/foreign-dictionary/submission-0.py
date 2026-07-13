class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        inDegree = {}
        for word in words:
            for char in word:
                adj[char] = set()
                inDegree[char] = 0
         
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        inDegree[w2[j]] += 1
                    break
        
        queue = deque([char for char in inDegree if inDegree[char] == 0])
        res = []

        while queue:
            char = queue.popleft()
            res.append(char)
            for neighbour in adj[char]:
                inDegree[neighbour] -= 1
                if inDegree[neighbour] == 0:
                    queue.append(neighbour)
            
        if len(res) == len(adj):
            return "".join(res)
        else:
            return ""
