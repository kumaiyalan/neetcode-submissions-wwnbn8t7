class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def dfs(n):
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            nString = str(n)
            new = 0
            for c in nString:
                new += int(c) ** 2
            return dfs(new)
        
        return dfs(n)