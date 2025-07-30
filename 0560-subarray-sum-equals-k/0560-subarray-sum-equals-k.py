class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict

        prefixsum = 0 #(0+1)
        count = 0 #if both prefix sum and k is same increase count to 1
        freq = defaultdict(int)

        for i in nums:
            prefixsum = prefixsum + i
            
            if (prefixsum == k):
                count = count + 1
            count = count + freq[prefixsum - k]
            freq[prefixsum] = freq[prefixsum] + 1

        return count                