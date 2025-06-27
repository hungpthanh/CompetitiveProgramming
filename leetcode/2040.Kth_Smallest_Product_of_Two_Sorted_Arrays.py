class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        MAX_INT = int(1e10 + 5)
        def gen(a, b):
            n, m = len(a), len(b)
            i, j = 0, 0
            while (i < n) and (j < m):
                yield a[i] * b[j]
                if i == n - 1 and j == m - 1:
                    break
                if i == n - 1:
                    j += 1
                    continue
                if j == m - 1:
                    i += 1
                    continue
                if (a[i + 1] * b[j] < a[i] * b[j + 1]):
                    i += 1
                else:
                    j += 1
            
        n, m = len(nums1), len(nums2)
        i, j = 0, 0
        cnt = 0
        while i < n and j < m:
            cnt += 1
            if cnt == k:
                return nums1[i] * nums2[j]
            if (j < m - 1) and (nums1[i]
