class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        original = x
        result = 0

        while x > 0:
            reminder = x % 10
            result = result * 10 + reminder
            x = x // 10
        
        if original == result:
            return True
        else:
            return False


        # x = str(x)
        # if x == x[::-1]:
        #     return True
        # else:
        #     return False




        # x = str(x)
        # return x == x[::-1] 
        
        
        #[start, stop, step], [hello - olleh - (-1)]
        # if( x == reverse ):
        #     return True
        # else:
        #     return False