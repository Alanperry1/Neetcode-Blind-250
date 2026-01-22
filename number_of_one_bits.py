class Solution:
    def hammingWeight(self, n: int) -> int:
        # Time Complexity: O(1) - always 32 iterations (constant)
        # Space Complexity: O(1) - only using constant extra space
        count=0
        for i in range(32):
            if n&1==1:
                count+=1
            n>>=1

        return count
