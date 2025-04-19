# IDEA: The operations are Euclean GCD algorithm
# Gradually, sub value to each start pair
# from (a, b) -> (c, d) then have multile (c, d) but from a (c, d) -> (a, b) only one path
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:

        def gcd(sx: int, sy: int, tx: int, ty: int) -> bool:
            if not (sx <= tx and sy <= ty):
                return False
            if tx < ty:
                return gcd(sy, sx, ty, tx)
            if tx % ty >= sx:
                return gcd(sx, sy, tx % ty, ty)
            if (tx - sx) % ty == 0:
                return ty == sy
            return False
        return gcd(sx, sy, tx, ty)
        
