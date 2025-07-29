from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextgreater = defaultdict(int)

        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                nextgreater[prev] = num
            stack.append(num)

        while stack:
            nextgreater[stack.pop()] = -1
        
        return [nextgreater[num] for num in nums1]