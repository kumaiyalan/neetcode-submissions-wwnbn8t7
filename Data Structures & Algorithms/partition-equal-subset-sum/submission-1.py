class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) / 2

        def sub(nums, target):
            if target == 0:
                return True
            if nums == [] or target < 0:
                return False
            return sub(nums[1:], target - nums[0]) or sub(nums[1:], target)
        
        return sub(nums, target)