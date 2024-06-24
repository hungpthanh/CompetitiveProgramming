class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Map = defaultdict(list)
        for e in strs:
            ana = str(sorted(e))
            Map[ana].append(e)
        return Map.values()
