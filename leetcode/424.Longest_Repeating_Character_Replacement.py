class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        cnt = {}
        n = len(s)
        start = 0
        cnt[s[start]] = 1
        res = 1
        for i in range(1, n):
            cnt[s[i]] = cnt.get(s[i], 0) + 1
            while ((i - start + 1) - max(cnt.values()) > k):
                cnt[s[start]] -= 1
                start += 1
            res = max(res, i - start + 1)
        return res
