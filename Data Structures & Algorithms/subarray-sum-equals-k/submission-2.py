class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixFreq = {}
        prefixFreq[0] = 1
        prefix = 0
        res = 0
        for i in range(len(nums)):
            prefix += nums[i]
            if prefix - k in prefixFreq:
                res += prefixFreq[prefix - k]
            prefixFreq[prefix] = 1 + prefixFreq.get(prefix, 0)
        return res