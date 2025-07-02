# TLE, sol: binary search results, i.e., the value of k-th
# Using BS to counting number of element 
import heapq
from typing import List

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def check(mid, nums1, nums2):
            counting = 0
            for item in nums1:
                count = 0
                if item > 0:
                    expected_value = mid / item
                    count = bisect.bisect_right(nums2, expected_value)
                elif item == 0:
                    if mid >= 0:
                        count = len(nums2)
                else:
                    expected_value = mid / item
                    index = bisect.bisect_left(nums2, expected_value)
                    count = len(nums2) - index
                counting += count

            return counting >= k
        MAX_INT = 10**10  # much bigger than any product
        l, r = -MAX_INT, MAX_INT

        while l <= r:
            mid = (l + r) // 2
            if check(mid, nums1, nums2):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
