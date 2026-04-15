class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        left = 0
        right = 0

        while right < len(nums) - 1:
            end = 0
            for i in range(left, right + 1):
                end = max(end, i + nums[i])
            left = right + 1
            right = end
            ans += 1
        
        return ans

