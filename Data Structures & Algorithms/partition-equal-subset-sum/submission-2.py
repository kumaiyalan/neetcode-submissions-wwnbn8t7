class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) / 2

        memo = {}

        def sub(index, target):
            if (index, target) in memo:
                return memo[(index, target)]
            if target == 0:
                memo[(index, target)] = True
                return True
            if index >= len(nums) or target < 0:
                memo[(index, target)] = False
                return False
            memo[(index, target)] = sub(index + 1, target - nums[index]) or sub(index + 1, target)
            return memo[(index, target)]
        
        return sub(0, target)