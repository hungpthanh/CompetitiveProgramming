class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        digits = list(map(int, digits))
        m = len(digits)    
        numbers = list(map(int, str(n)))[::-1]
        sz = len(numbers)
        dp = [0] * sz
        for item in digits:
            if item <= numbers[0]:
                dp[0] += 1
        pw = 1
        sum_pw = 0
        for i in range(1, sz):
            pw = pw * m
            sum_pw += pw
            for digit in digits:
                if digit < numbers[i]:
                    dp[i] += pw
            if numbers[i] in digits:
                dp[i] += dp[i - 1]
        
        return dp[sz - 1] + sum_pw