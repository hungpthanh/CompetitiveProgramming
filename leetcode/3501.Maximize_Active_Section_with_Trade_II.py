class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        st, en = -1, -1
        n = len(s)
        segments = []
        print(f"n = {n}")
        fsum = [0] * n
        # if s[0] == '1':
        #     fsum[0] = 1 
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
        print(segments)
        m = len(segments)
        def find_right(m, k):
            print(f"right: {m} {k}")
            l, r = 0, m - 1
            ans = -1
            while l <= r:
                mid = (l + r) // 2
                print(f"mid: {mid}, segments: {segments[mid]}")
                if segments[mid][1] < k:
                    ans = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return ans

        def find_left(m, k):
            l, r = 0, m - 1
            ans = -1
            while l <= r:
                mid = (l + r) // 2
                if segments[mid][0] > k:
                    ans = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return ans
        res = []
        print("fsum")
        print(fsum)
        for q_st, q_en in queries:
            print(f"query: {q_st} {q_en}")
            index1 = find_left(m, q_st)
            index2 = find_right(m, q_en)
            print(f"index: {index1} {index2}")
            ans = (fsum[q_st - 1] if q_st - 1 >= 0 else 0) + fsum[n - 1] - fsum[q_en]
            print(f"ans = {ans}")
            if index1 != -1 and index2 != -1 and index1 <= index2:
                ans += q_en - q_st + 1
            else:
                ans = fsum[n - 1]
            print(f"final ans = {ans}")
            res.append(ans)
        return res
