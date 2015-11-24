'''
Given a 2D matrix matrix, find the sum of the elements
inside the rectangle defined by its upper left corner 
(row1, col1) and lower right corner (row2, col2).

This solution uses a tuple to keep track of the DP array.
We could instead fill out the DP array in the __init__ by 
using the formula used in sumRegion.
'''

def print2d(matrix):
    for row in matrix:
        print row

class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.sum_matrix = matrix
        for y, row in enumerate(matrix):
            for x, item in enumerate(row):
                left = 0 if x==0 else self.sum_matrix[y][x-1][0]
                top = 0 if y==0 else  self.sum_matrix[y-1][x][1]
                mid = 0 if x==0 or y==0 else self.sum_matrix[y-1][x-1][2]
                
                self.sum_matrix[y][x] = (left+self.sum_matrix[y][x], 
                            top+self.sum_matrix[y][x], 
                            mid+left+top+self.sum_matrix[y][x])
                        
    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        A = self.sum_matrix[row2][col2][2]
        B = 0 if (row1==0 or col1==0) else self.sum_matrix[row1-1][col1-1][2]
        C = 0 if row1==0 else self.sum_matrix[row1-1][col2][2]
        D = 0 if col1==0 else self.sum_matrix[row2][col1-1][2]
        return A-C-D+B


if __name__ == '__main__':
    matrix = [
      [3, 0, 1, 4, 2],
      [5, 6, 3, 2, 1],
      [1, 2, 0, 1, 5],
      [4, 1, 0, 1, 7],
      [1, 0, 3, 0, 5]
    ]
    
    numMatrix = NumMatrix(matrix)
    assert 3 == numMatrix.sumRegion(0, 0, 0, 1)
    assert 4 == numMatrix.sumRegion(0, 0, 0, 2)
    assert 8 == numMatrix.sumRegion(0, 0, 0, 3)
    assert 10 == numMatrix.sumRegion(0, 0, 0, 4)

    assert 14 == numMatrix.sumRegion(0, 0, 1, 1)
    assert 18 == numMatrix.sumRegion(0, 0, 1, 2)
    assert 24 == numMatrix.sumRegion(0, 0, 1, 3)

    assert 9 == numMatrix.sumRegion(0, 0, 2, 0)
    assert 17 == numMatrix.sumRegion(0, 0, 2, 1)

    assert 11 == numMatrix.sumRegion(1, 1, 2, 2)
    assert 14 == numMatrix.sumRegion(1, 1, 2, 3)

    assert 28 == numMatrix.sumRegion(0, 0, 2, 3)
    assert 19 == numMatrix.sumRegion(0, 1, 2, 3)
    assert 20 == numMatrix.sumRegion(1, 0, 2, 3)
    assert 20 == numMatrix.sumRegion(1, 2, 3, 4)
    
    assert 3 == numMatrix.sumRegion(1,3,2,3)
    assert 9 == numMatrix.sumRegion(3,1,3,4)

