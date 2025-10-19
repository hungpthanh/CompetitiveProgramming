# TODO: Write solution for this problem
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        cnt = Counter([item % value for item in nums])
        n = len(nums)
        for i in range(n):
            if (i % value) in cnt and cnt[i % value] > 0:
                cnt[i % value] -= 1
                continue
            else:
                return i
        return n