class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        mark = [[False for t in range(n)] for _ in range(m)]
        def dfs(x, y):
            mark[x][y] = True
            for k in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = x + k[0] 
                ny = y + k[1]
                if (0 <= nx < m) and (0 <= ny < n) and (board[nx][ny] == 'O') and not mark[nx][ny]:
                    dfs(nx, ny)
        for i in range(0, m):
            if mark[i][0] == False and board[i][0] == 'O':
                dfs(i, 0)
            if mark[i][n - 1] == False and board[i][n - 1] == 'O':
                dfs(i, n - 1)
        for i in range(0, n):
            if mark[0][i] == False and board[0][i] == 'O':
                dfs(0, i)
            if mark[m - 1][i] == False and board[m - 1][i] == 'O':
                dfs(m - 1, i)
        for i in range(m):
            for j in range(n):
                if not mark[i][j]:
                    board[i][j] = 'X'
        
