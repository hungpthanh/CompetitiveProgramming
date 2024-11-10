class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = [0] * (n + 1)
        mark = [False] * (n + 1)
        results = []
        def check(ans, i, j):
            for k in range(1, i):
                if abs(i - k) == abs(ans[k] - j):
                    return False
            return True

        def backtrack(i):
            if i == n + 1:
                tmp = []
                for k in range(1, n + 1):
                    row = ""
                    for t in range(0, n):
                        if t == ans[k] - 1:
                            row += 'Q'
                        else:
                            row += '.'
                    tmp.append(row)
                results.append(tmp)
                return

            for j in range(1, n + 1):
                if not mark[j] and check(ans, i, j):
                    mark[j] = True
                    ans[i] = j
                    backtrack(i + 1)
                    mark[j] = False
        backtrack(1)
        return results
