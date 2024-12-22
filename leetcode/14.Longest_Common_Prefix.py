class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        index = 0
        n = len(strs)
        m = min([len(str) for str in strs])
        for i in range(m):
            c = strs[0][i]
            same = True    
            for j in range(1, n):
                if strs[j][i] != c:
                    same = False
                    break
            if not same:
                return strs[0][:i]
        return strs[0][:m]
