class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        n = len(s1)
        Q = deque()
        Q.append((s1, 0))
        mark = set()
        mark.add(s1)
        
        def gen(s):
            res = []
            index = 0
            while index < n and s[index] == s2[index]: index += 1
            for i in range(index + 1, n):
                if s[i] == s2[index]:
                    tmp = s[:index] + s[i] + s[index + 1: i] + s[index] + s[i + 1:]
                    if s[index] == s2[i]:
                        res = [tmp] + res
                    else:
                        res.append(tmp)
            return res

        while len(Q) > 0:
            top, k = Q.popleft()
            if top == s2:
                return k
            gen_s = gen(top)
            for item in gen_s:
                if item == s2:
                    return k + 1
                if item in mark:
                    continue
                mark.add(item)
                Q.append((item, k + 1))
        return -1
