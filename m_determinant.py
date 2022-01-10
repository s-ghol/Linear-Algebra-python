# author: @s.gholami
# -----------------------------------------------------------------------
# m_determinant.py
# -----------------------------------------------------------------------

def m_determinant(A: " 2d matrix") -> int or float:
    """
    Finds the determinant of 2x2 matrix
    :param A: 2x2 matrix
    :type A: 2d list
    :return: constant;belongs ot the reals
    :rtype:  int or float; depends on the matrix
    """

    m_size = len(A)
    if m_size == 1:
        print(A[0], "is not a square matrix")
        return A[0]
    elif m_size == 2:
        determinant = A[0][0] * A[1][1] - A[0][1] * A[1][0]
        print("det(A) = {}".format(determinant))
        # print("det(A) = ", determinant)
        return determinant


