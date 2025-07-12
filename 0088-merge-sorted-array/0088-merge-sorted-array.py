class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        #return None -> no return, sort the same array
        a = nums1[:m] #p1
        b = nums2 #p2
        merged = a + b #merge 2 array
        nums1[:] =  sorted(merged) #sort and return in the same array
