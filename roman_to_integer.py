class Solution:
    def romanToInt(self, s: str) -> int:
        # Time Complexity: O(n) - single pass through string where n is length
        # Space Complexity: O(1) - constant size hash map with 7 elements
        total=0
        roman={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000 
        }
        for i in range(len(s)-1):
            if roman[s[i]]<roman[s[i+1]]:
                total-=roman[s[i]]
            else:
                total+=roman[s[i]]
        total+=roman[s[-1]]
        return total
