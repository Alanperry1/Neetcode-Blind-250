class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time Complexity: O(n) - single pass through the array
        # Space Complexity: O(n) - hash map to store elements
        seen={}
        for i,num in enumerate(nums):
            dif=target-num
            if dif in seen:
                return [seen[dif],i]
            
            seen[num]=i
        return []
