class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        reverse = x[::-1] #[start, stop, step], [hello - olleh - (-1)]
        if( x == reverse ):
            return True
        else:
            return False