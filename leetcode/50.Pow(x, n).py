class Solution:

    def myPow(self, x: float, n: int) -> float:
        def pow(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            if n % 2 == 0:
                k = pow(x, n // 2)
                return k * k
            return x * pow(x, n - 1)
        if n == 0:
            return 1
        if n > 0:
            return pow(x, n)
        return 1 / pow(x, -n)
