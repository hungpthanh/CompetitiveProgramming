class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = set()
        ans = []
        nums = sorted(nums)
        def backtrack(index: int) -> None:
            if index == len(nums):
                subsets.add(tuple(ans))
                return 
            for select in range(2):
                if select == 1:
                    ans.append(nums[index])
                backtrack(index + 1)
                if select == 1:
                    ans.pop()
        backtrack(0)
        return list(subsets)
