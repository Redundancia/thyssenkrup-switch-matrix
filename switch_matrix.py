import random
from datetime import datetime
from time import sleep
import copy
def switch_matrix(matrix):
    print_starting_time()
    steps_taken = []
    matrix_len = len(matrix)
    while True:
        # switch everything to one except the last 3 rows, we achieve this by pressing the place one row below our target, so we can just iterate over them in order

        #idea for better: trim both edges, like make the first row and first column only 1, is that easy? if yes, then this scales infinately easily, every round would make
        # the matrix one less(like 6x6->5x5->4x4->3x3) then random solve a 3x3 is minimal computing time, much better than an infitely scaling 3xX
        for row_number,row in enumerate(matrix[0:matrix_len-2]):
            for column_number,column in enumerate(matrix):
                if matrix[row_number][column_number] == 0:
                    
                    #switch we press
                    matrix[row_number+1][column_number] = 1

                    #above switch
                    if row_number >= 0:
                        matrix[row_number][column_number] = 1 if matrix[row_number][column_number] == 0 else 0

                    #below switch
                    if row_number+2 < matrix_len:
                        matrix[row_number+2][column_number] = 1 if matrix[row_number+2][column_number] == 0 else 0

                    # switch to the right
                    if column_number+1 < matrix_len:
                        matrix[row_number+1][column_number+1] = 1 if matrix[row_number+1][column_number+1] == 0 else 0

                    #switch to the left
                    if column_number-1 >=0:
                        matrix[row_number+1][column_number-1] = 1 if matrix[row_number+1][column_number-1] == 0 else 0

                    steps_taken.append([row_number+1,column_number])
        #now all the switches are 1 except the ones in the last 3 row
        return solve_3xX_matrix(matrix,steps_taken)




def print_starting_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

def matrix_clear(matrix,matrix_len):
    for row in matrix:
        if sum(row) != matrix_len:
            return False
    return True


def print_matrix(matrix):
    for row in matrix:
        print(''.join(str(row)))
    print("\n")

def solve_3xX_matrix(matrix, steps_taken):
    print("Start 3xX solve")
    matrix_len_row = len(matrix)
    matrix_len_col = len(matrix[0])
    #well this is just randomly solving a 3xX matrix, with 3x6 it's small enough to work fast, scales, but not well? already 90+% of the steps are here
    while True:
        row_number = random.randrange(matrix_len_row-1, matrix_len_row)
        column_number = random.randrange(matrix_len_col)
        steps_taken.append([row_number, column_number])
        matrix[row_number][column_number] = 1
        #above switch
        if row_number-1 >= 0:
            matrix[row_number-1][column_number] = 1 if matrix[row_number-1][column_number] == 0 else 0

        #below switch
        if row_number+1 < matrix_len_row:
            matrix[row_number+1][column_number] = 1 if matrix[row_number+1][column_number] == 0 else 0

        # switch to the right
        if column_number+1 < matrix_len_col:
            matrix[row_number][column_number+1] = 1 if matrix[row_number][column_number+1] == 0 else 0

        #switch to the left
        if column_number-1 >=0:
            matrix[row_number][column_number-1] = 1 if matrix[row_number][column_number-1] == 0 else 0
        if matrix_clear(matrix,matrix_len_col):
            print(f"Congrats, you solved it! Size: {matrix_len_col} X {matrix_len_col}")
            print(f"Total steps: {str(len(steps_taken))}")
            #print("Steps taken: " + str([row for row in steps_taken]))
            print_matrix(matrix)
            print()
            return

#5x5 matrix
switch_matrix([[random.randrange(2), random.randrange(2), random.randrange(2),random.randrange(2), random.randrange(2)],
                    [random.randrange(2), random.randrange(2), random.randrange(2),random.randrange(2), random.randrange(2)],
                    [random.randrange(2), random.randrange(2), random.randrange(2),random.randrange(2), random.randrange(2)],
                    [random.randrange(2), random.randrange(2), random.randrange(2),random.randrange(2), random.randrange(2)],
                    [random.randrange(2), random.randrange(2), random.randrange(2),random.randrange(2), random.randrange(2)]])


#6x6 matrix
for i in range(100):
    print(f"Iteration: {str(i)}")
    switch_matrix([[random.randrange(2), random.randrange(2), random.randrange(2),random.randrange(2), random.randrange(2), random.randrange(2)],
                          [random.randrange(2), random.randrange(2), random.randrange(2),random.randrange(2), random.randrange(2), random.randrange(2)],
                          [random.randrange(2), random.randrange(2), random.randrange(2),random.randrange(2), random.randrange(2), random.randrange(2)],
                          [random.randrange(2), random.randrange(2), random.randrange(2),random.randrange(2), random.randrange(2), random.randrange(2)],
                          [random.randrange(2), random.randrange(2), random.randrange(2),random.randrange(2), random.randrange(2), random.randrange(2)],
                          [random.randrange(2), random.randrange(2), random.randrange(2),random.randrange(2), random.randrange(2), random.randrange(2)]])
print("Done!")