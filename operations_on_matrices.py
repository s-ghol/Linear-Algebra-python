# author: @s.gholami
# -----------------------------------------------------------------------
# operations_on_matrices.py
# -----------------------------------------------------------------------

# Accept two parameters (matrices) A and B from user
# Perform operations, return result
import sys

import numpy
import copy


# -----------------------------------------------------------------------
# def m_add(A, B):
#     result = []
#     # check dimension of A and B
#     # row_A = len(A)
#     # row_B = len(B)
#     # col_A = len(A[0])
#     # col_B = len(B[0])
#     dim_A = numpy.shape(A)
#     dim_B = numpy.shape(B)
#     if dim_A == dim_B:
#         # add
#         for(i, j) in zip(A,B):
#             result.append(list(map(lambda x, y: x + y, i, j)))
#         print(result)
#         return result
#
#
# A=[[1,1],[1,1]]
# B=[[2,2],[2,2]]
# m_add(A, B)

# -----------------------------------------------------------------------

# def m_subtract(A, B):
#     result = []
#     # check dimension of A and B
#     # row_A = len(A)
#     # row_B = len(B)
#     # col_A = len(A[0])
#     # col_B = len(B[0])
#     dim_A = numpy.shape(A)
#     dim_B = numpy.shape(B)
#     if dim_A == dim_B:
#         # add
#         for(i, j) in zip(A,B):
#             result.append(list(map(lambda x, y: x - y, i, j)))
#         print(result)
#         return result

# -----------------------------------------------------------------------

# Scalar multiplication
# def m_multiply_by_c(A, scalar):
#     result = []
#     for i in A:
#         result.append(list(map(lambda x: scalar * x, i)))

# -----------------------------------------------------------------------

# Transpose A
# def m_transpose(A):
#     C = copy.deepcopy(A)
#     row_A = len(A)
#     col_A = len(A[0])
#     # change a(ij) to a(ji) to perform the transpose
#     for i in range(row_A):
#         for j in range(col_A):
#             C[j][i] = A[i][j]
#     print(C)
#     return C


# A = [[1, 2], [3, 4]]  # solution: [[1,3],[2,4]]
# m_transpose(A)

# -----------------------------------------------------------------------
#
# # Matrix Multiplication of A and B
# def m_multiplication(A, B):
#     """
#     Requirement: col_A must equal row_B, which will yield a matrix c of size row_A X col_B
#     :param A: Matrix elements of A
#     :type A: list
#     :param B: Matrix elements of B
#     :type B: list
#     :return C: multiplication result in a list C
#     :rtype: list
#     """
#     row_A = len(A)
#     row_B = len(B)
#     col_A = len(A[0])
#     col_B = len(B[0])
#     if col_A != row_B:
#         print("Inner matrix size do not match")
#         sys.exit(0)
#     C = [[None]*col_B for _ in range(row_A)] # (nxm)X(pxq) = (nxq) iff m = p
#     for i in range(row_A):
#         for j in range(col_B):
#             s = 0
#             for k in range(row_B):
#                 s += A[i][k] * B[k][j]
#             C[i][j] = s
#     print(C)
#     return C
#
# #test
# E = [[2, 1],
#      [1, 1],]
# F = [[0, 1],
#      [1, 2],
#      [1, 2]]
# m_multiplication(E, F)
# -----------------------------------------------------------------------

def m_determinant(A):
    m_size = len(A)
    if m_size == 1:
        print(A[0],"is not a square matrix")
        return A[0]
    elif m_size == 2:
        determinant = A[0][0]* A[1][1] - A[0][1]* A[1][0]
        print("det(A) = ", determinant)
        return determinant
    else:
        pass

E = [[2, 1],
     [2,3]]
m_determinant(E)