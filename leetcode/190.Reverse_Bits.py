class Solution:
    def reverseBits(self, n: int) -> int:
        binary = ""
        for i in range(32):
            bit = n & (1 << i)
            if bit:
                binary = "1" + binary
            else:
                binary = "0" + binary
        res = 0
        for i, bit in enumerate(binary[::-1]):
            if bit == "1":
                res += (1 << (31 - i))
        return res
