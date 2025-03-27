# TODO
# idea: split into 2 unique sub array
# Let dp[i][j] = optimal results with last finger 1 at i and last finger 2 at j
# Let's consider the letter at position k
# If type char at k by finger 1:
# -- If char at k - 1 type by finger 1: dp[k][j] = min(dp[k - 1][j] + d[k - 1][k])
# -- If char at k - 1 type by finger 2: dp[k][k - 1] = min(dp[i][k - 1] + d[i][k])
# If type char at k by finger 2:
# -- If char at k - 1 type by finger 1: dp[k - 1][j] = min(dp[k - 1][j] + d[j][k])
# -- If char at k - 1 type by finger 2: dp[i][k] = min(dp[i][k - 1] + d[k - 1][k])

# Answer = min(dp[n - 1][j], dp[i][n - 1])

class Solution:
    def minimumDistance(self, word: str) -> int:
        inf = int(1e8)
        def get_location(c):
            index = ord(c) - ord('A')
            row = index // 6 
            col = index % 6 
            return [row, col]

        def distance(p1, p2):
            if p2 == [-1, -1] or p1 == [-1, -1]:
                return 0
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        n = len(word)
        word = '.' + word

        location = [get_location(word[i]) for i in range(1, n + 1)]
        location = [[-1, -1]] + location

        dp = [[inf] * (n + 1) for _ in range(n + 1)]
        dp[1][0] = 0
        dp[0][1] = 0
        for k in range(2, n + 1):
            for j in range(k - 1):
                dp[k][j] = min(dp[k][j], dp[k - 1][j] + distance(location[k - 1], location[k]))
                dp[k - 1][k] = min(dp[k - 1][k], dp[k - 1][j] + distance(location[j], location[k]))
            for i in range(k - 1):
                dp[k][k - 1] = min(dp[k][k - 1], dp[i][k - 1] + distance(location[i], location[k]))
                dp[i][k] = min(dp[i][k], dp[i][k - 1] + distance(location[k - 1], location[k]))
        ans = inf
        for i in range(n):
            ans = min(ans, min(dp[n][i], dp[i][n]))
        return ans
