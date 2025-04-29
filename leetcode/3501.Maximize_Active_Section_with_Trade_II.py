class Solution:

    def create_segments(s):
        st, en = -1, -1
        n = len(s)
        segments = []
        print(f"n = {n}")
        fsum = [0] * n
 
        print(fsum)
        for i in range(n):
            if i > 0:
                print(f"i = {i}")
                fsum[i] = fsum[i - 1]
            if s[i] == '1':
                fsum[i] += 1
                if st == -1:
                    st = i
                    en = i
                else:
                    en = i
            else:
                if en != -1:
                    segments.append([st, en])
                    st = -1
                    en = -1
        
        if st != -1:
            segments.append([st, en])
        
        return segments

    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        segments = create_segments()
        m = len(segments)
        
        actives = [0] * m
        for i in range(m):
            p = segments[i - 1][1] if i - 1 >= 0 else -1
            q = segments[i + 1][1] if i + 1 < m else n
            actives[i] = q - p
        return res
