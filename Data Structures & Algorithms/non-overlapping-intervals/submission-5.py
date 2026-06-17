class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)
        res = [intervals[0]]
        remove = []
        merges = 0

        for i in range(1, len(intervals)):
            curr = intervals[i]
            if res[-1][0] <= curr[0] < res[-1][1]:
                if res[-1][1] >= curr[1]:
                    res.pop()
                    res.append(curr)
                remove.append(curr)
                merges += 1
            else:
                res.append(curr)
        return merges