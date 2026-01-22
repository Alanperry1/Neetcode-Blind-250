class Solution:
    def reverseBits(self, n: int) -> int:
        # Time Complexity: O(1) - always 32 iterations (constant)
        # Space Complexity: O(1) - only using constant extra space
        result=0
        for i in range(32):
            last_dig=n&1
            result=(result<<1)|last_dig
            n>>=1

        return result
