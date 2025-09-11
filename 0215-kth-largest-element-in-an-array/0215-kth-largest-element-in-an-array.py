class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        return nums[k-1] # k-1 => if k=2 -> 2-1=1 (i.e) 1 as index (0,1) value is in 1 index.