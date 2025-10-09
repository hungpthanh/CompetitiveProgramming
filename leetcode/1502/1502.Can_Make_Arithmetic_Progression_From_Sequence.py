class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        n = len(arr)
        c = arr[1] - arr[0]
        for i in range(n):
            if arr[i] - arr[0] != i* c:
                return False
        return True