class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for n in nums:
            nPerm = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    modify = perm.copy()
                    modify.insert(i, n)
                    nPerm.append(modify)
            perms = nPerm
        return perms