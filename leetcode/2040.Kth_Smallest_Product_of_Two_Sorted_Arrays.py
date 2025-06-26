class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n, m = len(nums1), len(nums2)
        i, j = 0, 0
        cnt = 0
        while i < n and j < m:
            cnt += 1
            if cnt == k:
                return nums1[i] * nums2[j]
            if (j < m - 1) and (nums1[i]
