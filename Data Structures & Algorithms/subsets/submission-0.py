class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def builder(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            builder(i + 1)
            subset.pop()
            builder(i + 1)
        
        builder(0)
        return res
        