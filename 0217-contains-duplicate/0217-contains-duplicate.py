class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = set(nums)
        if len(nums) == len(duplicate):
            return False
        else:
            return True