class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Time Complexity: O(n) - single pass with two pointers
        # Space Complexity: O(1) - only using constant extra space
        l,r=0,len(heights)-1
        result=0
        while l<r:
            area=min(heights[l],heights[r])*(r-l)
            if area>result:
                result=area
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        

        return result


