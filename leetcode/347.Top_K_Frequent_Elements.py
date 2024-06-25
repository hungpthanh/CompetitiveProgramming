class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = Counter(nums)
        results = [e[0] for e in mp.most_common(k)]
        return results
