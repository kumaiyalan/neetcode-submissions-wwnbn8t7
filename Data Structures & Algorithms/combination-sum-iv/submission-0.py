class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {}

        def memo(target):
            if target == 0:
                return 1
            if target in cache:
                return cache[target]
            #2 choices
            total = 0
            for num in nums:
                if target - num >= 0:
                    total += memo(target - num)
            cache[target] = total
            return total
        
        return memo(target)