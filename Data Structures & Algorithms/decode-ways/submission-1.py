class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
            
        dp = [0] * len(s)
        length = len(s)
        
        if s[-1] == "0":
            dp[-1] = 0
        else:
            dp[-1] = 1

        if s[-2] == "0":
            dp[-2] = 0
        elif 10 <= int(s[-2: ]) <= 26:
            dp[-2] = 1 + dp[-1]
        else:
            dp[-2] = dp[-1]
        
        for i in range(length - 3, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            elif 10 <= int(s[i:i + 2]) <= 26:
                dp[i] = dp[i + 1] + dp[i + 2]
            else:
                dp[i] = dp[i + 1]

        return dp[0]
