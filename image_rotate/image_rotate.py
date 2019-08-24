from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for i in range(len(matrix)): #transpose of matrix
            for j in range(i, len(matrix[0])):
                if i != j:
                	matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
               
        m = len(matrix)
        n = len(matrix[0])
        for i in range(n//2): #swaping counter outer columns
            for j in range(m):
            	matrix[j][i],matrix[j][n-i-1] = matrix[j][n-i-1], matrix[j][i]