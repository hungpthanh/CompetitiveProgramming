class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        mp = Counter(nums)
        for (key, value) in mp.items():
            freq[value].append(key)
        res = []
        for i in range(len(nums), 0, -1):
            for e in freq[i]:
                res.append(e)
                if len(res) == k:
                    return res
        return res
        
