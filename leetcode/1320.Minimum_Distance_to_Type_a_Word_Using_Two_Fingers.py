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
