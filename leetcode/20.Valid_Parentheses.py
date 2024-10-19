class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for c in s:
            if c in mapping.keys():
                stack.append(c)
            elif (len(stack) > 0) and (c == mapping[stack[-1]]):
                stack.pop()
            else:
                return False

        return not (len(stack) > 0)
        
