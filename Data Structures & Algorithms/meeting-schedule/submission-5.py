"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda interval: interval.start)
        
        for i in range(1, len(sorted_intervals)):
            prev_interval = sorted_intervals[i - 1]
            curr_interval = sorted_intervals[i]

            if prev_interval.end > curr_interval.start:
                return False
        
        return True

        
        