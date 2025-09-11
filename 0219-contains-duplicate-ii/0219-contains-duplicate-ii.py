class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dup = set()  # store last values that we've seen last
        for i in range(len(nums)):
            if i > k:
                dup.remove(nums[i-k-1])  # current - last seen - 1
            
            if nums[i] in dup: # If current number already in the set → duplicate found
                return True

            dup.add(nums[i])
        return False
