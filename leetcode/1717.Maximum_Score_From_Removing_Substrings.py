# TODO: Prove greendy solution
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove(s, t, point):
            score = 0
            stack = []
            for c in s:
                if len(stack) > 0:
                    top = stack[-1]
                    if top + c == t:
                        stack.pop()
                        score += point
                    else:
                        stack.append(c)
                else:
                    stack.append(c)
            return "".join(stack), score
        if x > y:
            s, score1 = remove(s, "ab", x)
            s, score2 = remove(s, "ba", y)

        else:
            s, score1 = remove(s, "ba", y)
            s, score2 = remove(s, "ab", x)

        return score1 + score2
