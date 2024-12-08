"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        new_intervals = []
        for interval in intervals:
            new_intervals.append((interval.start, 1))
            new_intervals.append((interval.end, 0))
        new_intervals = sorted(new_intervals, key=lambda x: (x[0], x[1]))
        cnt = 0
        res = 0
        for new_interval in new_intervals:
            if new_interval[1] == 0:
                cnt -= 1
            else:
                cnt += 1
            res = max(res, cnt)
        return res
