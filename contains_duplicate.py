class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Time Complexity: O(n) - single pass through the array
        # Space Complexity: O(n) - hash map to store elements
        seen={}
        for i,num in enumerate(nums):
            if num in seen:
                return True
            seen[num]=i
        return False
