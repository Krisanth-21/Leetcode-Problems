class Solution:
    def reverseWords(self, s: str) -> str:        
        a = s.split()
        reverse = a[::-1]
        return " ".join(reverse)