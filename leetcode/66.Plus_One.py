class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        n = len(digits)
        for i in range(n - 1, -1 , -1):
            digits[i] = (digits[i] + carry) 
            if digits[i] < 10:
                carry = 0
            else:
                carry = 1
                digits[i] = digits[i] % 10
        if carry > 0:
            digits.insert(0, carry)
        return digits
