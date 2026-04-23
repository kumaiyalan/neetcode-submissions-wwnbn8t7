class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for num in nums:
            subsets += [subset + [num] for subset in subsets]
        seen = set()
        unique = []
        for subset in subsets:
            subset.sort()
            if tuple(subset) not in seen:
                unique.append(subset)
                seen.add(tuple(subset))
        return unique
        