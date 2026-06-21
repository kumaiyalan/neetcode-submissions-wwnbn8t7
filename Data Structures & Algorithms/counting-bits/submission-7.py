class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * max(5, n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        dp[3] = 2
        dp[4] = 1
        offset = 4

        for i in range(5, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp[:n + 1]