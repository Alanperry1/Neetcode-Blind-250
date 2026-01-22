class Solution:
    def climbStairs(self, n: int) -> int:
        # Time Complexity: O(n) - iterate from 0 to n
        # Space Complexity: O(n) - dp array of size n
        if n<=2:
            return n
        else:
            dp=[0]*n 
            dp[0],dp[1]=1,2
            for i in range(2,n):
                    dp[i]=dp[i-1]+dp[i-2]
            return dp[n-1]
