class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Time Complexity: O(n) - iterate through string twice (filtering + checking)
        # Space Complexity: O(n) - storing filtered string
        new=''
        for string in s:
            if string.isalnum():
                new+=string
        new=new.lower()
        left,right=0,len(new)-1
        while left<right:
            if new[left] != new[right]:
                return False
            left += 1
            right -= 1
        return True
