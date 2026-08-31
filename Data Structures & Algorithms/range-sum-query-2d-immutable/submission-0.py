class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matriks=[[] for i in range(0,len(matrix)+1)]
        self.summers=[[] for i in range(0,len(self.matriks))]
        for i in range(0,len(matrix)+1):
            for o in range(0,len(matrix[0])+1):
                if i==0 or o==0:
                    self.matriks[i].append(0)
                    self.summers[i].append(0)
                else:
                    self.matriks[i].append(matrix[i-1][o-1])
                    self.summers[i].append(self.summers[i-1][o]+self.summers[i][o-1]+self.matriks[i][o]-self.summers[i-1][o-1])
                



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.summers[row2+1][col2+1]+self.summers[row1][col1]-self.summers[row1][col2+1]-self.summers[row2+1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)