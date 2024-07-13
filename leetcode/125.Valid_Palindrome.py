class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        print(s)
        s = "".join([c for c in s if ('a' <= c <= 'z') or ('0' <= c <= '9')])
        print(s)
        return s == s[::-1]
