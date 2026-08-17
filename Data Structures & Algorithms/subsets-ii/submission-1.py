class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            offset = 1
            while i + offset < len(nums) and nums[i] == nums[i + offset]:
                offset += 1
            dfs(i + offset)

        
        dfs(0)
        return res