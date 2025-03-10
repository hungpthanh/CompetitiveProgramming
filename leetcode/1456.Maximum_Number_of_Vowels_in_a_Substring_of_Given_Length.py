class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        res = 0
        cnt = 0
        for i in range(n):
            if s[i] in vowels:
                cnt += 1
            if i - k >= 0 and s[i - k] in vowels:
                cnt -= 1
            res = max(res, cnt)
        return res
  
