class DetectSquares:

    def __init__(self):
        self.cols, self.rows = {}, {}

    def add(self, point: List[int]) -> None:
        x, y = point
        if x not in self.rows:
            self.rows[x] = {}
        if y not in self.cols:
            self.cols[y] = {}
        if y not in self.rows[x]:
            self.rows[x][y] = 0
        self.rows[x][y] += 1

        if x not in self.cols[y]:
            self.cols[y][x] = 0
        self.cols[y][x] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0
        if y not in self.cols:
            return 0
        for c, cnt in self.cols[y].items():
            edge_d = abs(x - c) # c is x cooridate
            if edge_d == 0:
                continue
            if x in self.rows and (y - edge_d in self.rows[x]) and (y - edge_d in self.rows[c]):
                res += self.rows[x][y - edge_d] * self.rows[c][y - edge_d] * self.cols[y][c]
            if x in self.rows and (y + edge_d in self.rows[x]) and (y + edge_d in self.rows[c]):
                res += self.rows[x][y + edge_d] * self.rows[c][y + edge_d] * self.cols[y][c]
        return res



# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
