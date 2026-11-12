class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cache = {}

        def memo(i):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            
            cache[i] = max(nums[i], nums[i] + memo(i + 1))
            return cache[i]
        
        memo(0)
        return max(cache.values())
        