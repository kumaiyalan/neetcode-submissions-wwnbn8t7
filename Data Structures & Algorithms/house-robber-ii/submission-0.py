class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        house1, house2 = nums[:-1], nums[1:]
        dp1, dp2 = [0] * len(house1), [0] * len(house2)
        dp1[0], dp2[0] = house1[0], house2[0]
        dp1[1], dp2[1] = max(house1[1], dp1[0]), max(house2[1], dp2[0])

        for i in range(2, len(house1)):
            dp1[i] = max(dp1[i - 1], house1[i] + dp1[i - 2])
            dp2[i] = max(dp2[i - 1], house2[i] + dp2[i - 2])
        
        return max(dp1[-1], dp2[-1])