class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        s = s + "."
        ans = [0] * (n + 1)
        ans[n] = 1
        res = 1
        def backtrack(i: int):
            nonlocal res
            if i == n:
                strs = []
                ss = ""
                for k in range(n + 1):
                    if ans[k] == 1:
                        if len(ss) > 0:
                            strs.append(ss)
                        ss = s[k]
                    else:
                        ss += s[k]
                if len(set(strs)) == len(strs):
                    res = max(res, len(strs))
                return
            for j in range (2):
                ans[i] = j
                backtrack(i + 1)
        backtrack(0)
        return res
