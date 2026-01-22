class Solution:

    def encode(self, strs: List[str]) -> str:
        # Time Complexity: O(n * k) - n strings, each of average length k
        # Space Complexity: O(n * k) - result string storing all characters
        res=''
        for string in strs:
            res+=str(len(string))+"#"+string
        
        return res
    
    def decode(self, s: str) -> List[str]:
        # Time Complexity: O(n) - single pass through string
        # Space Complexity: O(n) - result array storing decoded strings
        res,i=[],0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            res.append(s[j+1:length+1+j])
            i=length+1+j
        return res
