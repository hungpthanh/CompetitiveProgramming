# Poor my code :(
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        m = len(str(n))
        ans = []
        r = [""] + [str(k) for k in range(10)]
        tmp = ""

        def backtrack(i):
            nonlocal tmp
            if i == m:
                if (len(tmp) > 0) and int(tmp) <= n:
                    ans.append(tmp)
                return
            st = 2 if i == 0 else 0
            for j in r[st:]:    
                tmp = tmp + j
                backtrack(i + 1)
                if j != "":
                    tmp = tmp[:-1]
        backtrack(0)
        return [int(x) for x in ans if int(x) > 0]
