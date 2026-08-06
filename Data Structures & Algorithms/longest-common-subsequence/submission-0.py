class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def dp(text1, text2, i, j, memo):
            if i >= len(text1) or j >= len(text2):
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            
            if text1[i] == text2[j]:
                memo[i][j] = 1 + dp(text1, text2, i + 1, j + 1, memo)
            else:
                memo[i][j] = max(dp(text1, text2, i + 1, j, memo),
                                 dp(text1, text2, i, j + 1, memo))
            
            return memo[i][j]

        N, M = len(text1), len(text2)
        i, j = 0, 0
        memo = [[-1] * M for _ in range(N)]
        return dp(text1, text2, i, j, memo)