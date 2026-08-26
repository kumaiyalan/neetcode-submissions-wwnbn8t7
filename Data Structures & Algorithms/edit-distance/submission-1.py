class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}

        def memo(i, j):
            if j == len(word2):
                return len(word1) - i
            if i == len(word1):
                return len(word2) - j
            if (i, j) in cache:
                return cache[(i, j)]
            
            # 4 choices insert, delete, replace, or nothing
            if word1[i] == word2[j]:
                cache[(i, j)] = memo(i + 1, j + 1)
                return cache[(i, j)]
            
            # inserting advances j but not i
            insert = 1 + memo(i, j + 1)
            #delete
            delete = 1 + memo(i + 1, j)
            # replace advances both
            replace = 1 + memo(i + 1, j + 1)

            cache[(i, j)] = min(insert, delete, replace)
            return cache[(i, j)]
        
        return memo(0, 0)
