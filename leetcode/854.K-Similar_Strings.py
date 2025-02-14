class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        n = len(s1)
        Q = deque()
        Q.append((s1, 0))
        mark = set()
        mark.add(s1)
        def gen(s):
            def swap_chars(s, i, j):
                if i == j:
                    return s  # No need to swap if indices are the same
                s_list = list(s)  # Convert to list (since strings are immutable)
                s_list[i], s_list[j] = s_list[j], s_list[i]  # Swap
                return ''.join(s_list)  # Convert back to string
            res = []
            for i in range(n - 1):
                for j in range(i + 1, n):
                    # print(f"ss = {s}")
                    # print(f"{i} {j}")
                    if s[i] != s[j]:
                        # print(f"s = {s}")
                        s = swap_chars(s, i, j)
                        # print(f"s = {s}")
                        if not s in mark:
                            # print("passs")
                            mark.add(s)
                            res.append(s)
                            # print(f"res = {res}")
                        s = swap_chars(s, i, j)
                        # print(f"sss = {s}")
                        # print(f"res = {res}")
            return res

        while len(Q) > 0:
            top, k = Q.popleft()
            if top == s2:
                return k
            gen_s = gen(top)
            # print("gens")
            # print(gen_s)
            for item in gen_s:
                Q.append((item, k + 1))
        return -1
