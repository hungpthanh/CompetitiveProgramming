class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []
        n = int(sqrt(finalSum))
        if n * (n + 1) > finalSum:
            n -= 1
        remains = finalSum // 2 - n * (n + 1) // 2
        result = [i for i in range(1, n + 1)]
        for i in range(remains):
            result[-i - 1] += 1
        result = [2 * item for item in result]
        return result
        

