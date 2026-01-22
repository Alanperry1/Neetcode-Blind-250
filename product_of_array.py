import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time Complexity: O(n^2) - for each element, calculate product of remaining elements
        # Space Complexity: O(n) - storing product array and temporary arrays
        product=[]
        for i in range(len(nums)):
            temp=nums[:i]+nums[i+1:]
            product.append(math.prod(temp))

        return product
