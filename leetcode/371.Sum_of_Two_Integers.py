class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask  # keep 32-bit format
            b = carry & mask # keep 32-bit format

        return a if a <= max_int else ~(a ^ mask) # two complement
