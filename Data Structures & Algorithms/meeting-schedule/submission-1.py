"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        previous_end = 0

        for i in intervals:
            if i.end < previous_end or i.start < previous_end:
                return False
            previous_end = i.end
        
        return True