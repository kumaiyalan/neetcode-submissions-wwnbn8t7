"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if intervals == []:
            return 0
        re = []
        for interval in intervals:
            curr = [interval.start, interval.end]
            re.append(curr)
        intervals = re
        intervals.sort()
        rooms = {}
        rooms[0] = [intervals[0]]
        res = 1

        for i in range(1, len(intervals)):
            placed = False
            curr = intervals[i]
            for room in rooms:
                if curr[0] >= rooms[room][-1][1]:
                    rooms[room].append(curr)
                    placed = True
                    break
            if not placed:
                rooms[res] = [curr]
                res += 1
        return res