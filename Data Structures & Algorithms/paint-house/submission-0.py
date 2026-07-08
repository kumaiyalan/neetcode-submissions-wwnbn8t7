class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = costs[0]
        
        for i in range(1, len(costs)):
            house = costs[i]
            new = [0] * 3
            new[0] = house[0] + min(dp[1], dp[2])
            new[1] = house[1] + min(dp[0], dp[2])
            new[2] = house[2] + min(dp[0], dp[1])
            dp = new

        return min(dp) 