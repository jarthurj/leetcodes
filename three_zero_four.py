class NumMatrix:

    def __init__(self, matrix):
       ROWS, COLS = len(matrix), len(matrix[0])
       self.sumMat = [[0] * (COLS + 1) for r in range(ROWS + 1)]
       for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sumMat[r][c+1]
                self.sumMat[r+1][c+1] = prefix + above

    def __str__(self):
        stringer = ""
        for row in self.sumMat:
            stringer += str(row) + "\n"
        print(stringer)
        return stringer
    def sumRegion(self, row1, col1, row2, col2):
        big_square = self.sumMat[col2+1][row2+1]
        top = self.sumMat[row2+1][col1]
        left = self.sumMat[row1][col2+1]
        overlap = self.sumMat[col1][row1]
        return big_square + top + left - overlap
         

# d = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
d = NumMatrix([[3,0,1],[5,6,3],[1,2,0]])
print(d)