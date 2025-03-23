class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        start = -1
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                start = i
                break
        last = start
        while start >= 0 and s[start] != ' ':
            start -= 1
        return last - start
