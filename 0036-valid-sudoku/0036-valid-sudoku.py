import collections

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                
                # Skip empty cells
                if val == '.':
                    continue
                    
                # Calculate sub-box coordinate identifier (0-2, 0-2)
                box_key = (i // 3, j // 3)
                
                # Check for duplicates in row, column, or sub-box
                if val in rows[i] or val in cols[j] or val in boxes[box_key]:
                    return False
                
                # Add value to the respective sets
                rows[i].add(val)
                cols[j].add(val)
                boxes[box_key].add(val)
                
        return True