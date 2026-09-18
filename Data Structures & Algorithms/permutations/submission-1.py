class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(curr, available):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for i in range(len(available)):
                curr.append(available[i])
                dfs(curr, available[:i] + available[i + 1:])
                curr.pop()

        dfs([], nums)
        return res