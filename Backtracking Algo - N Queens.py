N = 7 #size of board

board =                [[0, 0, 0, 0, 0, 0, 0], 
			[0, 0, 0, 0, 0, 0, 0], 
			[0, 0, 0, 0, 0, 0, 0], 
			[0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0]]

ld = [0] * 30 #leftDiagonal = each element of this represents a left diagonal and stores a 0,...
              #...(technically we don't need 30 elements, we need exactly 2N-1 elements)...
              #...until a queen has been placed in that diagonal, at which point the diagonal...
              #...takes a value of 1.
              # = row - column + N-1
              #Add N-1 so that the indexing starts at zero.

rd = [0] * 30 #rightDiagonal = row+column

cl = [0] * 30 #column. This array records whether the column (at the corresponding index)...
              #...has had a queen placed on it


#this part works as follows: we're going to iterate through the columns. For a particular column,...
#we're going to iterate through the rows. We try  

def main(board, col):
    if col >=N:
        return True
    for i in range(N):  #where i represents the row, i.e. we're iterating through the rows
        if( ld[i - col + N-1] != 1 #no other queens in the same leftDiagonal
            and rd[i + col]   != 1 #no other queens in the same rightDiagonal
            and cl[i]         != 1 #no other queens in the same column #todo-why use cl[i]? 
            ):

            ld[i - col + N-1] = 1 #update the ld flag
            rd[i + col]       = 1 #update the rd flag
            cl[i]             = 1 #update the cl flag
            board[i][col]     = 1 #update the board


            if (main(board, col+1)):  #loop again and place next queen in next col
                return True
                         
            # else backtrack 
            ld[i - col + N-1] = 0 #update the ld flag
            rd[i + col]       = 0 #update the rd flag
            cl[i]             = 0 #update the cl flag
            board[i][col]     = 0 #update the board

    #print("There's no solution for col", col)
    return False

main(board, 0)
print('\n'.join(str(board[i]) for i in range(N)))

