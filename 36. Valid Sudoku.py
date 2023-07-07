class Solution:
    def isValidSudoku(self, board: str) -> bool:
        Sudo_board = board
        RowSIze = 9
        ColumnSize = 9

        def StrToInt(array):
            for row in range(RowSIze):
                for column in range(ColumnSize):
                    if array[column][row] == ".":
                        array[column][row] = 0
                    else:
                        array[column][row] = int(array[column][row])
        
        def showArray(array):
            for row in range(RowSIze):
                for column in range(ColumnSize):
                    
                    print(array[row][column], end=" ")

                print("\n")
        
        def Check_Row(array,column,Check_num):
            for row in range(RowSIze):
                if array[row][column] == Check_num:
                    return True
            return False
        
        def Check_Column(array,row,Check_num):
            for column in range(ColumnSize):
                if array[row][column] == Check_num:
                    return True
            return False
                
        def Check_box(array,row,column,Check_num):
            local_row = row - (row % 3)
            local_column = column - (column % 3)

            for i in range(local_row, local_row + 3):
                for j in range(local_column, local_column + 3):
                    if array[i][j] == Check_num:
                        return True
            return False

        
        def Ulimate_check(array,row,column,Check_num):
            if Check_Row(array,column,Check_num) & Check_Column(array,row,Check_num) & Check_box(array,row,column,Check_num):
                return True
            else:
                return False

        def solve(array):
            for row in range(RowSIze):
                for column in range(ColumnSize):
                    if array[row][column] == 0:
                        for Try in range(1,10):
                            if Ulimate_check(array,row,column,Try) == False:
                                array[row][column] = Try

                                if solve(array):
                                    return True
                                else:
                                    array[row][column] = 0
                                    #print(row,column)
                                    return False

                            
        StrToInt(Sudo_board)
        #showArray(Sudo_board)
        if solve(Sudo_board):
            showArray(Sudo_board)
            return True
        else:
            showArray(Sudo_board)
            return False

        





sol = Solution.isValidSudoku(0,[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])
print(sol)