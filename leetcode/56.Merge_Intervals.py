class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        new_intervals = []
        st, en = 3e4, -1
        for interval in intervals:
            if interval[0] > en:
                if en != -1:
                    new_intervals.append([st, en])
                st, en = interval[0], interval[1]
            else:
                en = max(en, interval[1])
                st = min(st, interval[0])
        if en != -1:
            new_intervals.append([st, en])
        return new_intervals
