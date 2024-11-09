class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i, j, index):
            if index == len(word) - 1:
                return True
            for k in range(4):
                x = i + cx[k]
                y = j + cy[k]
                if (index < len(word) - 1) and (0 <= x < m) and (0 <= y < n) and (not mark[x][y]) and (board[x][y] == word[index + 1]):
                    mark[x][y] = True
                    ans = backtrack(x, y, index + 1)
                    mark[x][y] = False
                    if ans:
                        return True
            return False

        cx = [-1, 1, 0, 0]
        cy = [0, 0, -1, 1]
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    mark = [[False] * n for _ in range(m)]
                    mark[i][j] = True
                    ans = backtrack(i, j, 0)
                    if ans:
                        return True
        return False
      
