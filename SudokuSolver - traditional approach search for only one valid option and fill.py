#Run time 803ms
#Tested at https://www.codewars.com/kata/5296bc77afba8baa690002d7/train/python

#---initialize puzzle---------------------------------------------------------------------------
original =  [[5, 3, 0, 0, 7, 0, 0, 0, 0],
             [6, 0, 0, 1, 9, 5, 0, 0, 0],
             [0, 9, 8, 0, 0, 0, 0, 6, 0],

             [8, 0, 0, 0, 6, 0, 0, 0, 3],
             [4, 0, 0, 8, 0, 3, 0, 0, 1],
             [7, 0, 0, 0, 2, 0, 0, 0, 6],

             [0, 6, 0, 0, 0, 0, 2, 8, 0],
             [0, 0, 0, 4, 1, 9, 0, 0, 5],
             [0, 0, 0, 0, 8, 0, 0, 7, 9]]

##supposedHardedstEverPuzzleEver = [
##    [8,0,0,0,0,0,0,0,0],
##    [0,0,3,6,0,0,0,0,0],
##    [0,7,0,0,9,0,2,0,0],
##    [0,5,0,0,0,7,0,0,0],
##    [0,0,0,0,4,5,7,0,0],
##    [0,0,0,1,0,0,0,3,0],
##    [0,0,1,0,0,0,0,6,8],
##    [0,0,8,5,0,0,0,1,0],
##    [0,9,0,0,0,0,4,0,0],
##]

A = original.copy()
print("original grid is:")
print("\n".join(str(A[i]) for i in range(9)))                

#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
#-----find possibilities (i.e. valid options) function------------------------------------------------------------
def findPossibilities(A, ci, cj):  #where ci is the specific cell's row (i) and the cell's column (j)
    poss=[1, 2, 3, 4, 5, 6, 7, 8, 9]

    #iterate down the column
    for i in range(9):  #this iterates from 0-8
        if A[i][cj] in poss:
            poss.remove(A[i][cj])

    #iterate across the row
    for j in range(9):
        if A[ci][j] in poss:
            poss.remove(A[ci][j])

    #iterate within the box
    if ci % 3 == 0: #is top row of a box
        box_i = [ci, ci + 1, ci + 2]
    if ci % 3 == 1: #is middle row of a box
        box_i = [ci-1, ci, ci + 1]
    if ci % 3 == 2: #is bottom of a box
        box_i = [ci-2, ci-1, ci]
    if cj % 3 == 0: #is left column of a box
        box_j = [cj, cj +1, cj + 2]
    if cj % 3 == 1: #is middle column of a box
        box_j = [cj-1, cj, cj +1]
    if cj % 3 == 2: #is right column of a box
        box_j = [cj-2, cj -1, cj]
    for i in box_i:
        for j in box_j:
            if A[i][j] in poss:
                poss.remove(A[i][j])

    #print(ci, cj, poss)            
    return poss

#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
#----given an intermediate (i.e. partially solved) grid, return a list of coordinates of the (remaining) empty cells-------
def findAllEmptyCells(A):
    emptyCellsAt = []    
    for i in range(9): 
        for j in range(9): #iterate across a row first, before you go to the row below
            if A[i][j] == 0:
                emptyCellsAt.append([i, j])
    return emptyCellsAt

#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
#-----given a partially solved grid, for all the empty cells, what are the valid options, ... --------------------
#----- ... and order these empty cells by those with fewest valid options to most valid options-------------------
#----- ... Return an ordered list of the empty cells' coordinates and their valid options.------------------------

def orderAllGridPossibilities(A):
    emptyCellsAt = findAllEmptyCells(A)
    allGridPossibilities = []
    for cell in emptyCellsAt:
        i, j = cell
        #print(i, j, findPossibilities(A, i, j))
        allGridPossibilities.append([i, j, findPossibilities(A, i, j)])
    allGridPossibilities.sort(key = lambda a: (len(a[2])))
    #print(allGridPossibilities)
    return allGridPossibilities


#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
#-------------main------------------------------------------------------------------------------------------------
#-------------traditional search and fill algorithm---------------------------------------------------------------

possibilitiesOfCellAt = []
while len(findAllEmptyCells(A)) > 0:
    potentialAssignments = orderAllGridPossibilities(A)

    for cell in potentialAssignments:
        if len(cell[2]) == 1:   # i.e. there's only 1 valid option for this empty cell
            i = cell[0]
            j = cell[1]
            A[i][j] = cell[2][0]     #so go ahead and insert this only-possible-valid-option for this empty cell (into the grid 'A')
    #print("\n".join(str(A[i])for i in range(9)))


"""return the solved puzzle as a 2d array of 9 x 9"""
print("final solution:")
print("\n".join(str(A[i])for i in range(9)))
