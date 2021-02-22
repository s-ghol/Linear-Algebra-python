# author: @s.gholami
# -----------------------------------------------------------------------
# operations_on_matrices.py
# -----------------------------------------------------------------------

# Accept two parameters (matrices) A and B from user
# Perform operations, return result

import numpy
import copy


#
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
#             result.append(list(map(lambda x, y: x - y, i, j))) #check this line
#         print(result)
#         return result


# def m_multiply_by_c(A, scalar):
#     result = []
#     for i in A:
#         result.append(list(map(lambda x: scalar * x, i)))


def m_transpose(A):
    C = copy.deepcopy(A)
    row_A = len(A)
    col_A = len(A[0])
    # change a(ij) to a(ji) to perform the transpose
    for i in range(row_A):
        for j in range(col_A):
            C[j][i] = A[i][j]
    print(C)
    return C

#
# A = [[1, 2], [3, 4]]  # solution: [[1,3],[2,4]]
# m_transpose(A)
