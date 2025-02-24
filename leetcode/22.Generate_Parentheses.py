class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        n *= 2
        count = 0
        results = []
        parenthese = ""
        def gen(i: int):
            nonlocal count, parenthese
            if i == n + 1:
                if count == 0:
                    results.append(parenthese)
                return
            for k in [("(", 1), (")", -1)]:
                count += k[1]
                parenthese += k[0]
                if count >= 0:
                    gen(i + 1)
                count -= k[1]
                parenthese = parenthese[:-1]
        gen(1)
        return results
