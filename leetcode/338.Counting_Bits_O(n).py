class Solution:
    def countBits(self, n: int) -> List[int]:
        next2 = 1
        ans = [0]
        for i in range(1, n + 1):
            if i == next2:
                ans.append(1)
                next2 = next2 * 2
            else:
                ans.append(ans[i - next2 // 2] + 1)
        return ans
