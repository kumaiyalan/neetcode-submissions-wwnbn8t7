class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sys.setrecursionlimit(30000)
        cache = {}

        def memo(i):
            if i == len(nums) - 1:
                cache[i] = (nums[i], nums[i])
                return cache[i]
            if i in cache:
                return cache[i]
            big, small = memo(i + 1)
            cache[i] = (max(nums[i], nums[i] * big, nums[i] * small),
                        min(nums[i], nums[i] * big, nums[i] * small))
            return cache[i]
            
        memo(0)
        return max(x[0] for x in cache.values())