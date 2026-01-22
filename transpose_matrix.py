class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Time Complexity: O(m * n) - visit each element once where m, n are dimensions
        # Space Complexity: O(m * n) - result matrix storing all elements
        rows=len(matrix)
        cols=len(matrix[0])
        result=[[0]*rows for i in range(cols)]
        for x in range(rows):
            for j in range(cols):
                result[j][x]=matrix[x][j]

        return result
