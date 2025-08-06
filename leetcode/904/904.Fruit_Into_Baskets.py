class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        m = 0
        res = 0
        st = 0
        cnt = defaultdict(int)
        for i in range(n):
            cnt[fruits[i]] += 1
            if cnt[fruits[i]] == 1:
                m += 1
            while m > 2:
                cnt[fruits[st]] -= 1
                if cnt[fruits[st]] == 0:
                    m -= 1
                st = st + 1
            res = max(res, i - st + 1)
        return res
