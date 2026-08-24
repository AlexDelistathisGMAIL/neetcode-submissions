class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowToSearch = -1
        for row in matrix:
            if row[0] > target:
                break
            else:
                rowToSearch += 1
        
        if rowToSearch == -1:
            return False
        else:
            first = 0
            last = len(matrix[0]) - 1
            middle = (first + last) // 2
            while first <= last:
                candidate = matrix[rowToSearch][middle]
                if candidate == target:
                    return True
                elif candidate < target:
                    first = middle + 1
                else:
                    last = middle - 1
                middle = (first + last) // 2
            
            return False
