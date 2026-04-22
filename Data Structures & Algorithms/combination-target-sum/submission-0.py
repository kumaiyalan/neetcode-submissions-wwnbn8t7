class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def builder(i):
            if sum(subset) == target:
                res.append(subset.copy())
                return
            if i >= len(nums) or sum(subset) > target:
                return
            
            subset.append(nums[i])
            builder(i)

            subset.pop()
            builder(i + 1)
        
        builder(0)
        return res
        