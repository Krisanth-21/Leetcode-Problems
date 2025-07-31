class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        hash = {}
        for i , num in enumerate(nums):
            needed = target - num
            if needed in hash:
                return [hash[needed], i]
            hash[num] = i