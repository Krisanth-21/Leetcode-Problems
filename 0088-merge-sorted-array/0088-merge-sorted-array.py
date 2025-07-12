class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        a = nums1[:m]
        b = nums2
        merged = a + b
        nums1[:] =  sorted(merged)
