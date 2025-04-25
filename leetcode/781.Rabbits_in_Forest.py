# IDEA: TBD
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        M = Counter(answers)
        cnt = 0
        while len(M) > 0:
            first_key = next(iter(M))
            value = M[first_key]
            if value > first_key + 1:
                M[first_key] = value - first_key - 1
            else:
                del M[first_key]
            cnt += (first_key + 1)
        return cnt
