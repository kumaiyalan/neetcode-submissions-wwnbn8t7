class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = nums[0]
        if len(nums) == 1:
            return True
        for i in range(len(nums)):
            if jump == 0:
                return False
            jump = max(jump - 1, nums[i])
        return True

        

        