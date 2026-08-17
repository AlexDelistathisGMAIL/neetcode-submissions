class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Rows
        for row in board:
            counts = {}
            for element in row:
                if element != ".":
                    if counts.get(element, None) is None:
                        counts[element] = 1
                    else:
                        counts[element] += 1
            for key in counts:
                if counts[key] > 1:
                    return False
        
        # Columns
        for col in zip(*board):
            counts = {}
            for element in col:
                if element != ".":
                    if counts.get(element, None) is None:
                        counts[element] = 1
                    else:
                        counts[element] += 1
            for key in counts:
                if counts[key] > 1:
                    return False
        
        # Squares
        numRows = len(board)
        numCols = len(board[0])
        counts = {}
        for i in range(numRows):
            for j in range(numCols):
                element = board[i][j]
                if element != ".":
                    square = (i // 3) * 3 + (j // 3)
                    if counts.get((element, square), None) is None:
                        counts[(element, square)] = 1
                    else:
                        counts[(element, square)] += 1

        for key in counts:
                if counts[key] > 1:
                    return False

        return True
