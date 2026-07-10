class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counts = [0] * len(nums)
        for num in nums:
            counts[num - 1] += 1
        print(counts)
        return [counts.index(2) + 1, counts.index(0) + 1]
