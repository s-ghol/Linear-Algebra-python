# author: @s.gholami
# -----------------------------------------------------------------------
# read_matrix_input.py
# -----------------------------------------------------------------------

# Accept inputs from console
# Populate the list with the inputs to form a matrix

def equations_to_matrix() -> list:
    """

    :return: augmented matrix formed from user input (user inputs = linear equations)
    :rtype: list
    """
    n = int(input("input number of rows "))
    m = int(input("input number of columns "))
    A = []
    for row_space in range(n):
        print("input row ", row_space + 1)
        row = input().split()
        if len(row) == m:
            row_map = list(map(int, row))  # use map function convert string to integer
            A.append(row_map)
        else:
            print("length must be the column size of A")
            equations_to_matrix()
    print(A)
    return A


# main for function call.
if __name__ == "__main__":  # __name__ = m_determinant
    equations_to_matrix()
else:
    print("read_matrix_input.py is being imported into another module ")
