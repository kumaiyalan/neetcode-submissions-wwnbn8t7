class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        cache = {}

        def memo(i, j, k):
            if k == len(s3):
                return i == len(s1) and j == len(s2)
            if (i, j) in cache:
                return cache[(i, j)]

            res = False
            if i < len(s1) and s1[i] == s3[k]:
                res = memo(i + 1, j, k + 1)
            if not res and j < len(s2) and s2[j] == s3[k]:
                res = memo(i, j + 1, k + 1)
            
            cache[(i, j)] = res
            return res
        
        return memo(0, 0, 0)
                
            
        