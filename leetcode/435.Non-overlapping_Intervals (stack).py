class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        n = len(intervals)
        new_intervals = [intervals[0]]
        for interval in intervals[1:]:
            if (interval[1] < new_intervals[-1][1]):
                new_intervals[-1] = interval
            elif interval[0] >= new_intervals[-1][1]:
                new_intervals.append(interval)
        return n - len(new_intervals)
