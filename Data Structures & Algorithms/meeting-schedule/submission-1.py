"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if intervals == []:
            return True
        intervals.sort(key=lambda x:x.start)
        last = intervals[0]

        for interval in intervals[1:]:
            if last.start <= interval.start < last.end:
                return False
            last = interval
        
        return True