class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        value = 0
        for i in range(len(nums)):
            if nums[i] == target:
                value = i
                break
            else:
                nums.append(target)
                nums.sort()
                value = nums.index(target)
        return value