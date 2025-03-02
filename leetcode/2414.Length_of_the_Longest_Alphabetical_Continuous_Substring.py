class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        start = 0
        n = len(s)
        res = 0
        for i in range(n):
            index = ord(s[start]) - ord('a')
            if index + i - start >= len(alphabet):
                start = i
                continue
            if s[i] == alphabet[index + i - start]:
                res = max(res, i - start + 1)
            else:
                start = i
        return res
