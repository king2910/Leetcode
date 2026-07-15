class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        z=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    z.append([i,j])
        for x in z:
            i=x[0]
            j=x[1]
            a=0
            while a<len(matrix[0]):
                matrix[i][a]=0
                a+=1
            a=0
            while a<len(matrix):
                matrix[a][j]=0
                a+=1