class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) // 3
        count = Counter(nums)
        result = []
        for nums, count in count.items():
            if count > n:
                result.append(nums)
        return result
