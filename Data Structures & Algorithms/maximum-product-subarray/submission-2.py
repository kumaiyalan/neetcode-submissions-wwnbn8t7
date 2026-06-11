class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        bigDp, smallDp = [0] * len(nums), [0] * len(nums)
        bigDp[0], smallDp[0] = nums[0], nums[0]
        curr = nums[0]

        for i in range(1, len(nums)):
            bigDp[i] = max(bigDp[i - 1] * nums[i], nums[i], smallDp[i - 1] * nums[i])
            smallDp[i] = min(smallDp[i - 1] * nums[i], nums[i], bigDp[i - 1] * nums[i])
            curr = max(curr, bigDp[i], smallDp[i])

        return curr