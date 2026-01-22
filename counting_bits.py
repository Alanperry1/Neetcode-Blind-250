class Solution:
    def countBits(self, n: int) -> List[int]:
        # Time Complexity: O(n * log n) - iterating n times, bin() and count() take log n
        # Space Complexity: O(n) - two result arrays each storing n+1 elements
        result=[]
        new=[]
        for i in range(n+1):
            result.append(bin(i)[2:])
        for i in result:
            new.append(i.count("1"))
        return new
