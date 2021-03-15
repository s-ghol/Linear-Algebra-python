# author: @s.gholami
# -----------------------------------------------------------------------
# read_matrix_input.py
# -----------------------------------------------------------------------

# Accept inputs from console
# Populate the list with the inputs to form a matrix

def read_matrix_input():
    n = int(input("input number of rows "))
    m = int(input("input number of columns "))
    A = []
    for row_element in range(n):
        print("input row ", row_element+1)
        row = input().split()
        if len(row) == m:
            row_map = map(int, row)  # use map function convert string to integer
            list_row = list(row_map)
            A.append(list_row)
        else:
            print("length must be the column size of A")
            read_matrix_input()
    print(A)
    return A


read_matrix_input()
