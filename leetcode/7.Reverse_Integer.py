class Solution:
    def reverse(self, x: int) -> int:
        Min = - (1<<31)
        Max = (1 << 31) - 1
        if x < Min or x > Max:
            return 0
        if x < 0:
            x = -x
            x = -int(str(x)[::-1])
        else:
            x = int(str(x)[::-1])
        if x < Min or x > Max:
            return 0
        return x
