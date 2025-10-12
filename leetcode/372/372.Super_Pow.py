# Update: TODO with math knowledge, reading Euler theorem
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        def devide(numbers: List[int]):
            remains = 0
            ans = []
            for number in numbers:
                k = remains * 10 + number
                c = k // 2
                if not (len(ans) == 0 and c == 0):
                    ans.append(k // 2)
                remains = k - c * 2
            
            return ans

        def sub_one(numbers: List[int]):
            index = len(numbers) - 1
            ans = []
            while index > 0 and numbers[index] == 0:
                ans.append(0)
                index -= 1
            ans.append(numbers[index] - 1)
            for i in range(index - 1, -1, -1):
                ans.append(numbers[i])
            return ans[::-1]

        def is_zero(numbers: List[int]):
            return ((len(numbers) == 1) and (numbers[0] == 0))

        def is_odd(numbers: List[int]):
            return (numbers[-1] % 2 == 1)

        if is_zero(b):
            return 1
        if is_odd(b):
            b[-1] = b[-1] - 1
            return (self.superPow(a, b) * (a % 1337)) % 1337
        p = self.superPow(a, devide(b))
        return (p * p) % 1337
    
class Solution2:
    def superPow(self, a: int, b: List[int]) -> int:
        if a % 1337 == 0:
            return 0
        p = 0
        for i in b:
            p = (p * 10 + i) % 1140
        if p == 0:
            p += 1140
        return pow(a, p, 1337)

# Studying Chinese remainder theorem
class Solution:
    def power(self, a, n, MOD):
        if n == 0:
            return 1
        if n % 2:
            return ((a % MOD) * self.power(a, n -1, MOD)) % MOD
        pw = self.power(a, n // 2, MOD)
        return (pw * pw) % MOD
    
    def superPow(self, a: int, b: List[int]) -> int: