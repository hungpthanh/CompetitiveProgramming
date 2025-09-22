class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            a, b = b, a
        while len(a) < len(b):
            a = '0' + a
        n = len(a)
        result = ""
        store = 0
        for i in range(n - 1, -1, -1):
            add = int(a[i]) + int(b[i]) + store
            result = str(add % 2) + result
            store = 1 if add >= 2 else 0
        if store > 0:
            result = '1' + result
        return result
        