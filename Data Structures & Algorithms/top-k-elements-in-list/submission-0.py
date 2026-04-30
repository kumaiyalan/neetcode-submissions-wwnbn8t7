class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        elements = freq.most_common(k)
        res = []
        for element in elements:
            res.append(element[0])
        return res
        