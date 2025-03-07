class Solution:
    def convert(self, s: str, numRows: int) -> str:
        steps = [(1, 0), (-1, 1)]
        results = ["" for _ in range(numRows)]
        def move(x, y, k, direction):
            if k >= len(s):
                return "".join(results)
            results[x] += s[k]
            nx = x + steps[direction][0]
            ny = y + steps[direction][1]
            if (0 <= nx < numRows):
                return move(nx, ny, k + 1, direction)
            else:
                nx = x + steps[1 - direction][0]
                ny = y + steps[1 - direction][1]
                return move(nx, ny, k + 1, 1 - direction)
        return move(0, 0, 0, 0)
