class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(min(n, limit) + 1):
            subn = n - i
            l, r = max(0, subn - limit), min(limit, subn)
            if r >= l:
                ans += (r - l + 1)
        return ans
