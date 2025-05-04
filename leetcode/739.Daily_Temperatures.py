class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        answers = [0] * n
        for i in range(n):
            while (len(stack) > 0) and (temperatures[i] > temperatures[stack[-1]]):
                answers[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return answers
