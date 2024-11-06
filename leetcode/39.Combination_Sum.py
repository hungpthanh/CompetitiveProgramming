class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        results = []
        def backtrack(target: int, index: int, sum_ans: int):
            if target == sum_ans:
                results.append(list(ans))
                return
            for idx in range(index, len(candidates)):
                if target - sum_ans < candidates[idx]:
                    continue    
                sum_ans += candidates[idx]
                ans.append(candidates[idx])
                backtrack(target, idx, sum_ans)
                sum_ans -= candidates[idx]
                ans.pop()
        backtrack(target, 0, 0)
        return results
        
                
