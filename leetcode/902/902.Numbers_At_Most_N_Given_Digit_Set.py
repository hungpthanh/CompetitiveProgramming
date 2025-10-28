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
        pw = [0] * (sz + 1)
        pw[0] = 1
        pw[1] = m
        sum_pw = 0
        for i in range(1, sz):
            pw[i + 1] = pw[i] * m
            sum_pw += pw[i]
            if numbers[i] == 0:
                dp[i] = dp[i - 1]
            else:
                cnt = len([item for item in digits if item < numbers[i]])
                dp[i] = sum_pw + cnt * pw[i] + (0 if (numbers[i] not in digits) else dp[i - 1])
        print(dp)
        return dp[sz - 1]