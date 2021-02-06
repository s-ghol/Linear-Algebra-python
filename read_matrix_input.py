# -----------------------------------------------------------------------
# read_matrix_input.py
# -----------------------------------------------------------------------

# Accept inputs from console
# Populate the list with the inputs to form a matrix

def read_matrix_input():
    n = int(input("input number of rows "))  # number of rows
    m = int(input("input number of columns "))  # number of coloumns
    A = []
    for i in range(n):
        print("input row ", i+1)
        row = input().split()
        if len(row) == m:
            row_map = map(int, row)  # use map object with each string converted to an integer
            list_row = list(row_map)  # cast back to list
            A.append(list_row)
        else:
            print("length must be the column size of A")
            read_matrix_input()
    print(A)
    return A


read_matrix_input()
