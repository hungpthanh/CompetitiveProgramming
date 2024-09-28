class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        height = [(v, idx) for idx, v in enumerate(height)]
        height = sorted(height)
        res = 0
        max_index = -1
        min_index = int(1e5 + 5)
        for h, idx in height[::-1]:
            if max_index != -1:
                water_volumn = max(max_index - idx, idx - min_index) * h
                res = max(res, water_volumn)
            max_index = max(max_index, idx)
            min_index = min(min_index, idx)
        return res
