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
        
        for i, interval in enumerate(sorted_intervals):
            if i >= len(sorted_intervals) - 1:
                continue
            
            next_interval = sorted_intervals[i + 1]
            if interval.end > next_interval.start:
                return False
            
        return True