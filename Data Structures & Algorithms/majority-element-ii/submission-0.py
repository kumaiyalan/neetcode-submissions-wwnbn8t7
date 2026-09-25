class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        limit  = len(nums) // 3
        counter = {}
        res = []

        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        for num in counter:
            if counter[num] > limit:
                res.append(num)
        
        return res