class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        cnt = 0
        pos = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                pos.append(i)
        if len(pos) == 0:
            return True
        if len(pos) != 2:
            return False
        return s1[pos[0]] == s2[pos[1]] and s1[pos[1]] == s2[pos[0]]
        
