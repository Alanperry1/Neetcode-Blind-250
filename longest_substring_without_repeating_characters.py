class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time Complexity: O(n) - each character visited at most twice
        # Space Complexity: O(min(n, m)) - set size limited by string length n or charset size m
        seen=set()
        result=0
        l=0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            result=max(result,r-l+1)

        return result
