from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        a = []
        for k, v in c.items():
            if v==1:
                a.append(k)
        return a