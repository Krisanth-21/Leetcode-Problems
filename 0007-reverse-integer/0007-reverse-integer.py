class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        negative = False

        if x < 0:
            negative = True
            x = -x
        
        while x > 0:
            remainder = x % 10
            rev = rev * 10 + remainder
            x = x // 10
        
        if negative:
            rev = -rev

        # Overflow check (32-bit signed integer)
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        
        return rev