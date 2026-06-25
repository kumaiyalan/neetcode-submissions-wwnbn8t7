class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        if sum(nums) == target:
            return len(nums)
        
        window = 0
        L = 0
        length = len(nums)

        for R in range(0, len(nums)):
            window += nums[R]

            while window >= target:
                length = min(length, R - L + 1)
                window -= nums[L]
                L += 1

        return length