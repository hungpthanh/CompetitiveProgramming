class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        ans = [0] * n
        for i in range(n):
            ans[i] = len(set(A[:i + 1]) & set(B[:i + 1]))
        return ans
