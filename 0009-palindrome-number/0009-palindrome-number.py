class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False

        # x = str(x)
        # return x == x[::-1] 
        
        
        #[start, stop, step], [hello - olleh - (-1)]
        # if( x == reverse ):
        #     return True
        # else:
        #     return False