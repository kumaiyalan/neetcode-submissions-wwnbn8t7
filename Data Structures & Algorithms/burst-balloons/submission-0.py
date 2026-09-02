class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def reward(i, nums):
            if i == 0:
                return nums[i] * nums[i + 1]
            if i == len(nums) - 1:
                return nums[i - 1] * nums[i]
            else:
                return nums[i - 1] * nums[i] * nums[i + 1]
        
        cache = {}

        def memo(nums):
            if len(nums) == 1:
                return nums[0]
            if tuple(nums) in cache:
                return cache[tuple(nums)]
            best = -1
            for i in range(len(nums)):
                best = max(best, reward(i, nums) + memo(nums[:i] + nums[i + 1:]))
            cache[tuple(nums)] = best
            return best
        
        return memo(nums)
