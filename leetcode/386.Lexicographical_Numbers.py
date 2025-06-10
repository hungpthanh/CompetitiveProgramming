class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        def dfs(number):
            if number != "" and int(number) > n:
                return
            ans.append(number)
            st = 1 if number == "" else 0
            for c in range(st, 10):
                dfs(number + str(c))
        dfs("")
        return [int(item) for item in ans[1:]]
