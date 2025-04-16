# IDEA: The operations are Euclean GCD algorithm
# Gradually, sub value to each start pair
# from (a, b) -> (c, d) then have multile (c, d) but from a (c, d) -> (a, b) only one path
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        
