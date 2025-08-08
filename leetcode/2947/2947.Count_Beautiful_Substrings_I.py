class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        counting = [0] * (n + 1)
        results = 0
        for i in range(1, n + 1):
            counting[i] = counting[i - 1] + (1 if s[i - 1] in vowels else 0)
            for j in range(i):
                vowel = counting[i] - counting[j]
                consonant = i - j - vowel
                if (vowel == consonant) and (((vowel * vowel) % k) == 0):
                    results += 1
        return results
