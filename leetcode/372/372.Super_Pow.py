class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        print("b = ", b)
        def devide(numbers: List[int]):
            remains = 0
            ans = []
            # print("numbers = ", numbers)
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
            return (self.superPow(a, sub_one(b)) * (a % 1337)) % 1337
        p = self.superPow(a, devide(b))
        return (p * p) % 1337