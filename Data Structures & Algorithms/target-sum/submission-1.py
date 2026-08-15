class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def memo(curr, index):
            if (curr, index) in cache:
                return cache[(curr, index)]
            if index == len(nums):
                if curr == target:
                    return 1
                else:
                    return 0

            ways = 0
            # 2 options, add or substract
            ways += memo(curr + nums[index], index + 1)
            ways += memo(curr - nums[index], index + 1)
            cache[(curr, index)] = ways
            return ways
        
        return memo(0, 0)