class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def transpose(matrix):
            for i in range(len(matrix)):
                for j in range(i+1, len(matrix)):
                    matrix[j][i], matrix[i][j] = matrix[i][j],matrix[j][i]
                    
        def reverse(matrix):
            for i in range(len(matrix)):
                matrix[i] = matrix[i][::-1]
        
        transpose(matrix)
        reverse(matrix)
        
        
        