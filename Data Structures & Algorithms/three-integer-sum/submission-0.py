class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[List[int]]:
        left = 0
        right = len(numbers) - 1
        pairs = []

        while left < right:
            canidate = numbers[left] + numbers[right]
            if canidate == target:
                pairs.append([numbers[left], numbers[right]])
                left += 1
                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1
            elif canidate < target:
                left += 1
            else:
                right -= 1

        return pairs

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if nums[0] > 0:
            return []
        
        res = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = 0 - nums[i]
            pairs = self.twoSum(nums[i + 1:], target)
            for pair in pairs:
                res.append([nums[i], pair[0], pair[1]])
        
        return res