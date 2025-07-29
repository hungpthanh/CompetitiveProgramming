class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def get_result(a, b, ops):
            a, b = float(a), float(b)
            if ops == '*':
                return str(a * b)
            if ops == '-':
                return str(a - b)
            if ops == '+':
                return str(a + b)
            if ops == '/':
                return str(int(a / b))

        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(token)
            elif len(stack) >= 2:
                b = stack.pop()
                a = stack.pop()
                stack.append(get_result(a, b, token))
        return int(float(stack[0]))