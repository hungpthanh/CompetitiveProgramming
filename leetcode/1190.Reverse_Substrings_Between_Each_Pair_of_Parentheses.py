class Solution:
    def reverseParentheses(self, s: str) -> str:
        def reverse(i, j, s):
            return s[:i] + s[i: j + 1][::-1] + s[j + 1:]

        stack = []
        s2 = s
        for idx, c in enumerate(s):
            if c == ')':
                l, r = stack[-1] + 1, idx - 1
                stack.pop()
                s2 = reverse(l, r, s2)
            elif c == '(':
                stack.append(idx)
        return "".join([c for c in s2 if c != '(' and c != ')'])
