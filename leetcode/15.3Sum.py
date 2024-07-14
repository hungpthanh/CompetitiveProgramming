class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        pair_set = set()
        const = 2 * int(1e5) + 1
        M = {}
        for idx, e in enumerate(nums):
            M[e] = idx
        for i in range(len(nums) - 2):
            if (i > 1) and (nums[i] == nums[i - 1]):
                continue
            for j in range(i + 1, len(nums) - 1):
                if (j > i + 1) and (nums[j] == nums[j - 1]):
                    continue
                if ((0 - nums[i] - nums[j]) in M) and (M[0 - nums[i] - nums[j]] > j):
                    mi, ma = nums[i] + int(1e5), nums[j] + int(1e5)
                    k = mi * const + ma
                    if k in pair_set:
                        continue
                    results.append([nums[i], nums[j], 0 - nums[i] - nums[j]])
                    pair_set.add(k)
        return results
