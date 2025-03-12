class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        pairs = []
        link = {}
        for idx, c in enumerate(s):
            if c == '(':
                stack.append(idx)
            elif c == ')':
                link[idx] = stack[-1]
                link[stack[-1]] = idx
                stack.pop()
        curIndex = 0
        direction = 1
        result = ""
        while 0 <= curIndex < len(s):
            if s[curIndex] == '(' or s[curIndex] == ')':
                curIndex = link[curIndex]
                direction = -direction
            else:
                result += s[curIndex]
            curIndex += direction
        return result
