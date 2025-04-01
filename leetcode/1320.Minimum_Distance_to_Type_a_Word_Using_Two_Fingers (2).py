# O(n * 32 * 32)
# IDEA: When we type a new charactor, we only care the last charactor in both hands
class Solution:
    def minimumDistance(self, word: str) -> int:
        inf = int(1e8)
        def get_location(index):
            row = index // 6 
            col = index % 6 
            return [row, col]

        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        d = [[0] * 27 for _ in range(27)]
        for i in range(27):
            for j in range(27):
                if i == 0 or j == 0:
                    d[i][j] = 0
                else:
                    d[i][j] = distance(get_location(i - 1), get_location(j - 1))
        
        n = len(word)
        word = '.' + word

        dp = [[inf] * 27 for _ in range(27)]
        
        dp[0][0] = 0
        for k in range(1, n + 1):
            idx = ord(word[k]) - ord('A') + 1
            next_dp = [[inf] * 27 for _ in range(27)]
            for i in range(27):
                for j in range(27):
                    next_dp[i][idx] = min(next_dp[i][idx], dp[i][j] + d[j][idx])
                    next_dp[idx][j] = min(next_dp[idx][j], dp[i][j] + d[i][idx])
            dp = next_dp
        ans = min(min(row) for row in dp)
        return ans
