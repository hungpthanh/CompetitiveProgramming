class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        results = [[1]]
        for numRow in range(1, numRows):
            row = [1]
            for j in range(1, numRow):
                row.append(results[-1][j - 1] + results[-1][j])
            row.append(1)
            results.append(row)
        return results