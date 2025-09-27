class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        def devide(numbers: List[int]):
            remains = 0
            ans = []
            for number in numbers:
                k = remains * 10 + number
                c = k // 2
                ans.append(k // 2)
                remains = k - c * 2
            return ans