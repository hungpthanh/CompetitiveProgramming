class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        M = {}
        for idx, v in enumerate(numbers):
            M.setdefault(v, []).append(idx + 1)
        for idx, v in enumerate(numbers):
            if v > target // 2:
                break
            sub = target - v
            if not sub in M:
                continue
            if v == sub:
                if len(M[v]) > 1:
                    return [idx + 1, M[v][1]]
            else:
                return [idx + 1, M[sub][0]]
