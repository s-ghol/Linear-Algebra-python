# author: @s.gholami
# -----------------------------------------------------------------------
# m_multiplication.py
# -----------------------------------------------------------------------
import sys


def m_multiplication(A, B) -> list:
    """
    Performs multiplication on matrix A and B
    Requirement: col_A must equal row_B, which will yield a matrix c of size row_A X col_B
    :param A: Matrix A
    :type A: list
    :param B: Matrix B
    :type B: list
    :return C: Matrix; A*B = C
    :rtype: list
    """
    row_A = len(A)
    row_B = len(B)
    col_A = len(A[0])
    col_B = len(B[0])
    if col_A != row_B:
        print("Inner matrix size do not match")
        sys.exit(0)
    C = [[None] * col_B for _ in range(row_A)]  # (lxm)*(mxn) = (lxn)
    for i in range(row_A):
        for j in range(col_B):
            s = 0
            for k in range(row_B):
                s += A[i][k] * B[k][j]
            C[i][j] = s
    print(C)
    return C


# test
# main for function call.
if __name__ == "__main__":
    A = [[2, 1],
         [1, 1], ]
    B = [[0, 1],
         [1, 2]]
    m_multiplication(A, B)
