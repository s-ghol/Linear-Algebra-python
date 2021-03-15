## Matrices and Operations

### Matrices in Python (See read_matrix_input.py)
Matrices are represented as _lists_:
`matrix_A = [[1, 0], [0, 1]]`.
* If we want to look up a row one: `matrix_A[0] = [1,0]`.
* If we want to look up an element in the: `matrix_A[0,0] = 1 `


### Adding/ Subtracting two matrices (See operations_on_matrices.py)

To add or subtract two matrices together we must verify that the dimension of A is same as B. If this is true, then we simply add or subtract the corresponding elements:

<a href="https://www.codecogs.com/eqnedit.php?latex=A&space;=&space;\begin{bmatrix}&space;a&space;&b&space;\\&space;c&d&space;\end{bmatrix},&space;B&space;=&space;\begin{bmatrix}&space;e&space;&f&space;\\&space;g&h&space;\end{bmatrix}:&space;A&plus;B&space;=&space;\begin{bmatrix}&space;a&plus;e&space;&b&plus;f&space;\\&space;c&plus;g&space;&d&plus;h&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?A&space;=&space;\begin{bmatrix}&space;a&space;&b&space;\\&space;c&d&space;\end{bmatrix},&space;B&space;=&space;\begin{bmatrix}&space;e&space;&f&space;\\&space;g&h&space;\end{bmatrix}:&space;A&plus;B&space;=&space;\begin{bmatrix}&space;a&plus;e&space;&b&plus;f&space;\\&space;c&plus;g&space;&d&plus;h&space;\end{bmatrix}" title="A = \begin{bmatrix} a &b \\ c&d \end{bmatrix}, B = \begin{bmatrix} e &f \\ g&h \end{bmatrix}: A+B = \begin{bmatrix} a+e &b+f \\ c+g &d+h \end{bmatrix}" /></a>

### Scalar Multiplication

Let **A** be a matrix and **c** be a scalar where **(A)c = c(A)** (commutative), then **(A)c** is obtained by multiplying all entries in **A** by **c**

<a href="https://www.codecogs.com/eqnedit.php?latex=c\begin{bmatrix}&space;a_{11}&space;&a_{12}&space;\\&space;a_{21}&space;&a_{22}&space;\end{bmatrix}&space;=&space;\begin{bmatrix}&space;c(a_{11})&space;&c(a_{12})&space;\\&space;c(a_{21})&space;&c(a_{22})&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?c\begin{bmatrix}&space;a_{11}&space;&a_{12}&space;\\&space;a_{21}&space;&a_{22}&space;\end{bmatrix}&space;=&space;\begin{bmatrix}&space;c(a_{11})&space;&c(a_{12})&space;\\&space;c(a_{21})&space;&c(a_{22})&space;\end{bmatrix}" title="c\begin{bmatrix} a_{11} &a_{12} \\ a_{21} &a_{22} \end{bmatrix} = \begin{bmatrix} c(a_{11}) &c(a_{12}) \\ c(a_{21}) &c(a_{22}) \end{bmatrix}" /></a>


### Transpose

Transpose is an operator that performs the following: transpose of the _m x n_ matrix **A** is the _n x m_ matrix A^T

<a href="https://www.codecogs.com/eqnedit.php?latex=(A^{T})_{ij}&space;=&space;A_{ji}\\&space;\\&space;\begin{bmatrix}&space;1&2&3&space;\\&space;4&space;&5&6&space;\end{bmatrix}^{T}&space;=&space;\begin{bmatrix}&space;1&space;&4&space;\\&space;2&space;&5\\&space;3&6&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?(A^{T})_{ij}&space;=&space;A_{ji}\\&space;\\&space;\begin{bmatrix}&space;1&2&3&space;\\&space;4&space;&5&6&space;\end{bmatrix}^{T}&space;=&space;\begin{bmatrix}&space;1&space;&4&space;\\&space;2&space;&5\\&space;3&6&space;\end{bmatrix}" title="(A^{T})_{ij} = A_{ji}\\ \\ \begin{bmatrix} 1&2&3 \\ 4 &5&6 \end{bmatrix}^{T} = \begin{bmatrix} 1 &4 \\ 2 &5\\ 3&6 \end{bmatrix}" /></a>


### Matrix Multiplication of A and B (See operations_on_matrices.py)

When performing matrix multiplication, the following condition must be met:
> The number of columns in the first matrix must be the same as the number of rows in the second matrix.

Consider the following matrices **A** and **B** and observe how we obtain the matrix **C** by performing a dot product on the ith row of **A** and the jth column of **B**:


<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{bmatrix}&space;a_{11}&space;&&space;a_{12}&space;&a_{13}&space;\\&space;a_{21}&space;&&space;a_{22}&space;&&space;a_{23}&space;\end{bmatrix}_{2x3}&space;\begin{bmatrix}&space;b_{11}&space;&b_{12}&space;\\&space;b_{21}&b_{22}&space;\\&space;b_{31}&space;&b_{32}&space;\end{bmatrix}_{3x2}&space;=&space;\begin{bmatrix}&space;c_{11}&space;&c_{12}&space;\\&space;c_{21}&space;&c_{22}&space;\end{bmatrix}_{2x2}&space;\\&space;\\&space;\indent&space;c_{11}&space;=&space;a_{11}b_{11}&plus;a_{12}b_{21}&plus;a_{13}b_{31}\\&space;\indent&space;c_{21}&space;=&space;a_{21}b_{11}&plus;a_{22}b_{21}&plus;a_{23}b_{31}\\&space;\indent&space;c_{12}&space;=&space;a_{11}b_{12}&plus;a_{12}b_{22}&plus;a_{13}b_{32}\\&space;\indent&space;c_{22}&space;=&space;a_{21}b_{12}&plus;a_{22}b_{22}&plus;a_{23}b_{32}\\" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;a_{11}&space;&&space;a_{12}&space;&a_{13}&space;\\&space;a_{21}&space;&&space;a_{22}&space;&&space;a_{23}&space;\end{bmatrix}_{2x3}&space;\begin{bmatrix}&space;b_{11}&space;&b_{12}&space;\\&space;b_{21}&b_{22}&space;\\&space;b_{31}&space;&b_{32}&space;\end{bmatrix}_{3x2}&space;=&space;\begin{bmatrix}&space;c_{11}&space;&c_{12}&space;\\&space;c_{21}&space;&c_{22}&space;\end{bmatrix}_{2x2}&space;\\&space;\\&space;\indent&space;c_{11}&space;=&space;a_{11}b_{11}&plus;a_{12}b_{21}&plus;a_{13}b_{31}\\&space;\indent&space;c_{21}&space;=&space;a_{21}b_{11}&plus;a_{22}b_{21}&plus;a_{23}b_{31}\\&space;\indent&space;c_{12}&space;=&space;a_{11}b_{12}&plus;a_{12}b_{22}&plus;a_{13}b_{32}\\&space;\indent&space;c_{22}&space;=&space;a_{21}b_{12}&plus;a_{22}b_{22}&plus;a_{23}b_{32}\\" title="\begin{bmatrix} a_{11} & a_{12} &a_{13} \\ a_{21} & a_{22} & a_{23} \end{bmatrix}_{2x3} \begin{bmatrix} b_{11} &b_{12} \\ b_{21}&b_{22} \\ b_{31} &b_{32} \end{bmatrix}_{3x2} = \begin{bmatrix} c_{11} &c_{12} \\ c_{21} &c_{22} \end{bmatrix}_{2x2} \\ \\ \indent c_{11} = a_{11}b_{11}+a_{12}b_{21}+a_{13}b_{31}\\ \indent c_{21} = a_{21}b_{11}+a_{22}b_{21}+a_{23}b_{31}\\ \indent c_{12} = a_{11}b_{12}+a_{12}b_{22}+a_{13}b_{32}\\ \indent c_{22} = a_{21}b_{12}+a_{22}b_{22}+a_{23}b_{32}\\" /></a>
