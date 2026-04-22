class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()
        def builder(i):
            if sum(subset) == target:
                res.append(subset.copy())
                return
            if i >= len(candidates) or sum(subset) > target:
                return
            
            subset.append(candidates[i])
            builder(i + 1)

            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            builder(i + 1)
        
        builder(0)
        return res