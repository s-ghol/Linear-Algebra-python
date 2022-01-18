# author: @s.gholami
# -----------------------------------------------------------------------
# m_transpose.py
# -----------------------------------------------------------------------
import copy


def m_transpose(A: "mxn matrix") -> list:
    """
    Transposes matrx A (from a(ij) to a(ji))
    :param A: Matrix
    :type A: list
    :return: Transposed matrix
    :rtype: list
    """
    C = copy.deepcopy(A)
    row_A = len(A)
    col_A = len(A[0])
    # change a(ij) to a(ji) to perform the transpose
    for i in range(row_A):
        for j in range(col_A):
            C[j][i] = A[i][j]
    print(C)
    return C

    # # Faster method
    # return map(list, zip(*A))  # How: let A = [[1, 2], [3, 4]]; then (*A) passes in [1,2],[3,4]
    # #  instead of [[1, 2], [3, 4]]. Returns [(1,3),(2,4)]
    # Essentially zip(*M) returns the columns of a matrx


# main for function call.
if __name__ == "__main__":
    A = [[1, 2], [3, 4]]  # solution: [[1,3],[2,4]]
    m_transpose(A)
