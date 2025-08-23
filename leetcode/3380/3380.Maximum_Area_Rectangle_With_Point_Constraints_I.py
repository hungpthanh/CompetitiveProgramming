class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        xs = defaultdict(list)
        ys = defaultdict(list)
        for idx, point in enumerate(points):
            xs[point[0]].append(idx)
            ys[point[1]].append(idx)
        
        n = len(points)
        res = -1
        for idx in range(n):
            for i in xs[points[idx][0]]:
                for j in ys[points[idx][1]]:
                    nx = points[i][0] + points[j][0] - points[idx][0]
                    ny = points[i][1] + points[j][1] - points[idx][1]

                    minx = min([points[idx][0], points[i][0], points[j][0], nx])
                    miny = min([points[idx][1], points[i][1], points[j][1], ny])
                    maxx = max([points[idx][0], points[i][0], points[j][0], nx])
                    maxy = max([points[idx][1], points[i][1], points[j][1], ny])

                    if [nx, ny] in points:
                        valid = True
                        for k in range(n):
                            if k != idx and k != i and k != j and points[k] != [nx, ny] and (minx <= points[k][0] <= maxx) and (miny <= points[k][1] <= maxy):
                                valid = False
                                break
                        if valid:
                            area = (maxx - minx) * (maxy - miny)
                            if area > 0:
                                res = max(res, area)
        return res
