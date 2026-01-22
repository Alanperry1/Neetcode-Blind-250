class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Time Complexity: O(log n) - binary search
        # Space Complexity: O(1) - only using constant extra space
        left,right=0,len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]<nums[right]:
                right=mid
            else:
                left=mid+1


        return nums[left]




        
