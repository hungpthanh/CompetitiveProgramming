class Solution:
    def isPalindrome(self, x: int) -> bool:
        rv = str(x)[::-1]
        return str(x) == rv
        
