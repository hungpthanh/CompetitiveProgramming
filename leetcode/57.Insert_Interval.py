class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = []
        new_start = newInterval[0]
        new_end = newInterval[1]
        for idx, interval in enumerate(intervals):
            if newInterval[0] > interval[1]:
                new_intervals.append(interval)
                continue
            if newInterval[1] < interval[0]:
                new_intervals.append([new_start, new_end])
                new_intervals += intervals[idx:]
                return new_intervals
            new_start = min(new_start, interval[0])
            new_end = max(new_end, interval[1])
        new_intervals.append([new_start, new_end])
        return new_intervals
