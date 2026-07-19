class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            canidate = numbers[left] + numbers[right]
            if canidate == target:
                return [left + 1, right + 1]
            if canidate < target:
                left += 1
            if canidate > target:
                right -= 1
            