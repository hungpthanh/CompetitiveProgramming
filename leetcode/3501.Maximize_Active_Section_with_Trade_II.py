# IDEA: convert one of 1 blocks to 0 / the sum 2 adj 0 block is max -> using RMQ
class Solution:

    def create_segments(self, n, s):
        segments = [[0, 0]]
        add = True
        for i in range(1, n + 1):
            if s[i] == '0':
                add = True
            else:
                if add:
                    segments.append([i, i])
                    add = False
                else:
                    segments[-1][1] = i
        segments.append([n + 1, n + 1])
        return segments

    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        s = '1' + s + '1'
        segments = self.create_segments(n, s)
        print(segments)
        res = []
        return res
