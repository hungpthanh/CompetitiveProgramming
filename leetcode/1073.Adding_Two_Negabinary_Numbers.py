class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n = max(len(arr1), len(arr2))
        arr1 = [0] * (n - len(arr1)) + arr1
        arr2 = [0] * (n - len(arr2)) + arr2
        carry = 0
        arr = [0] * n
        def add(a, b):
            if 0 <= a + b <= 1:
                return a + b, 0
            if a + b > 1:
                return 0, -1
            if a + b < 0:
                return 1, 1

        for i in range(1, n + 1):
            nb, carry1 = add(arr1[-i], arr2[-i])
            nb2, carry2 = add(nb, carry)
            arr[-i] = nb2
            carry = carry1 + carry2
        if carry == 1:
            arr = [1] + arr
        if carry == -1:
            arr = [1, 1] + arr
        while len(arr) > 1 and (arr[0] == 0):
            arr = arr[1:]
        return arr
            
