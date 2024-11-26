class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        product = 1
        min_neg, max_neg, min_pos, max_pos = 1, int(-3e5), int(3e5), -1
        res = -int(4e5)
        for e in nums:
            if e == 0:
                min_neg, max_neg, min_pos, max_pos = 1, int(-3e5), int(3e5), -1
                product = 1
            else:
                product *= e
                res = max(res, product)
                if product > 0:
                    if min_pos != -int(3e5):
                        res = max(res, product // min_pos)
                    elif min_neg != 1:
                        res = max(res, product // min_neg)
                    min_pos = min(min_pos, product)
                    max_pos = max(max_pos, product)
                else:
                    if max_neg != int(-3e5):
                        res = max(res, product // max_neg)
                    elif max_pos != -1:
                        res = max(res, product // max_pos)
                    min_neg = min(min_neg, product)
                    max_neg = max(max_neg, product)
        if 0 in nums:
            res = max(res, 0)
        return res
