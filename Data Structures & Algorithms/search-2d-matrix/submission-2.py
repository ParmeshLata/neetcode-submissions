class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)-1
        n=len(matrix[0])-1
        row_low=0
        row_high=len(matrix)-1
        while row_low<=row_high:
            row_mid=(row_low+row_high)//2
            if target<matrix[row_mid][0]:
                row_high=row_mid-1
            elif target>matrix[row_mid][n]:
                row_low=row_mid+1
            else:
                col_low=0
                col_high=len(matrix[0])-1
                while col_low<=col_high:
                    col_mid=(col_low+col_high)//2
                    if matrix[row_mid][col_mid]==target:
                        return True
                    if matrix[row_mid][col_mid]>target:
                        col_high=col_mid-1
                    else:
                        col_low=col_mid+1
                return False
        return False
            