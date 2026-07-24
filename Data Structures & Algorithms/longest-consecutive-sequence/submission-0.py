class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        contains = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in contains:
                count = 1
                curr = num
                while curr + 1 in contains:
                    count += 1
                    curr += 1
                res = max(res, count)
        return res