from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        for i in range(9):
            checkedNumsHorizontal = [0] * 9
            checkedNumsVertical = [0] * 9
            
            for j in range(9):
                if board[i][j] != ".":
                    if checkedNumsHorizontal[int(board[i][j]) - 1] == 0:
                        checkedNumsHorizontal[int(board[i][j]) - 1] = 1
                    else:
                        return False
                    
                if board[j][i] != ".":
                    if checkedNumsVertical[int(board[j][i]) - 1] == 0:
                        checkedNumsVertical[int(board[j][i]) - 1] = 1
                    else:
                        return False
                
        for i in range(3):
            for j in range(3):
                checkedNumsSubBox = [0] * 9
                for k in range(3):
                    for l in range(3):
                        if (board[i*3 + k][j*3 + l]) != ".":
                            if checkedNumsSubBox[int(board[i*3 + k][j*3 + l]) - 1] == 0:
                                checkedNumsSubBox[int(board[i*3 + k][j*3 + l]) - 1] = 1
                            else:
                                return False

        return True