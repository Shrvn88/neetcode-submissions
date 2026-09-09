class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        colLen = len(matrix[0])-1
        rowLen = len(matrix)-1
        rowStart, rowEnd = 0, rowLen
        colStart, colEnd = 0, colLen        

        while rowStart <= rowEnd:
            rowMid = (rowStart + rowEnd) // 2
            if matrix[rowMid][colStart] > target:
                rowEnd = rowMid - 1
            elif matrix[rowMid][colEnd] < target:
                rowStart = rowMid + 1
            else:
                while colStart <= colEnd:
                    colMid = (colStart + colEnd) // 2
                    if matrix[rowMid][colMid] > target:
                        colEnd = colMid - 1
                    elif matrix[rowMid][colMid] < target:
                        colStart = colMid + 1
                    else:
                        return True
                
        return False

