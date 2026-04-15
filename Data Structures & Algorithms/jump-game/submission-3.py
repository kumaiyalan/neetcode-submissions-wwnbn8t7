class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = nums[0]
        for i in range(1, len(nums)):
            if jump == 0:
                return False
            jump = max(jump - 1, nums[i])
        return True

        

        