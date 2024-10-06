class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        M = {}
        start = 0
        res = 0
        for idx in range(len(s)):
            if not (s[idx] in M):
                M[s[idx]] = 0
            M[s[idx]] += 1
            while (start < idx) and (M[s[idx]] > 1):
                M[s[start]] -= 1
                start += 1
            res = max(res, idx - start + 1)
        return res
                
        
