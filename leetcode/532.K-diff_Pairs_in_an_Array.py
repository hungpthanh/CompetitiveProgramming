class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        nums = sorted(list(set(nums)))
        cnt = 0
        for e in nums:
            r = k + e
            if r == e:
                if counter[r] > 1:
                    cnt += 1
            elif counter[r] > 0:
                cnt += 1
        return cnt
        
