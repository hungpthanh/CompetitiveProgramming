class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        k = 4 * k
        n = len(s)
        s = "." + s
        presum = [0] * (n + 1)
        vowels = "aeiou"
        groups = defaultdict(list)
        groups[0].append(0)
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + 1 if s[i] in vowels else presum[i - 1] -1
            groups[presum[i]].append(i)
        k_new = k
        for t in range(int(sqrt(k)), k + 1):
            if (t * t) % k == 0:
                k_new = t
                break
        res = 0
        for _, positions in groups.items():
            cnt = defaultdict(int)
            for position in positions:
                res += cnt[position % k_new]
                cnt[position % k_new] += 1
        return res
