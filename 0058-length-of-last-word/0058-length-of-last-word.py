class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.strip().split()

        if not a:
            return 0
        else:
            return len(a[-1])