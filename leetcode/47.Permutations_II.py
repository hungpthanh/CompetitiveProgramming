class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        mark = [False for _ in range(n)]
        ans = [None for _ in range(n)]
        mark_ans = set()
        results = []
        def backtrack(i):
            if i == n:
                if ".".join(ans) not in mark_ans:
                   results.append([int(item) for item in ans]) 
                   mark_ans.add(".".join(ans))
                return
            for j in range(n):
                if not mark[j]:
                    mark[j] = True
                    ans[i] = str(nums[j])
                    backtrack(i + 1)
                    mark[j] = False
        backtrack(0)
        return results
