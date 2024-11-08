class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        mark = set()
        perm = []
        ans = []
        def backtrack(index: int) -> None:
            if index == len(nums):
                perm.append(list(ans))
                return 
            for item in nums:
                if not item in mark:
                    ans.append(item)
                    mark.add(item)
                    backtrack(index + 1)
                    ans.pop()
                    mark.remove(item)
        backtrack(0)
        return perm
