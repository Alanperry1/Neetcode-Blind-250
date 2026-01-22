class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Time Complexity: O(n^2) - iterate through all n*n elements
        # Space Complexity: O(1) - in-place rotation
        matrix.reverse()
        n=len(matrix)
        for x in range(n):
            for j in range(x+1,n):
                matrix[x][j],matrix[j][x]=matrix[j][x],matrix[x][j]

        
