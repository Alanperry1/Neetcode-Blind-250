class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Time Complexity: O(n^2) - for each character, expand around center
        # Space Complexity: O(1) - only storing result string (not counting output)
        #check for even or odd length palindromes 
        # Using the expand around center
        res=''
        LongRes=0
        for i in range(len(s)):
            #odd length
            l,r=i,i #starting from the center
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>LongRes:
                    res=s[l:r+1]
                    LongRes=r-l+1
                l-=1
                r+=1

            #odd length
            l,r=i,i+1 #starting from the center
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>LongRes:
                    res=s[l:r+1]
                    LongRes=r-l+1
                l-=1
                r+=1
        return res
