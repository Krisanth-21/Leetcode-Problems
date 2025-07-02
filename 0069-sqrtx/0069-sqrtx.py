class Solution:
    def mySqrt(self, x: int) -> int:
        a = math.sqrt(x)
        return int(a) 
        #The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.