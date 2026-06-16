class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            curr = intervals[i]
            if res[-1][0] <= curr[0] <= res[-1][1]:
                merge = res.pop()
                new = [min(curr[0], merge[0]), max(curr[1], merge[1])]
                res.append(new)
            else:
                res.append(curr)
                
        return res