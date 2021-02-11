## Matrices and Operations

### Matrices in Python (See read_matrix_input.py)
Matrices are represented as _lists_:
`matrix_A = [[1, 0], [0, 1]]`. And so matrix_A[0,0] will yield 1


### Adding/ Subtracting tow matrices (See operations_on_matrices.py)

To add or subtract two matrices together we must verify that the dimension of A is same as B. If this is true, then we simply add or subtract the corresponding elements:

<img src="https://render.githubusercontent.com/render/math?math=A%20%3D%5Cbegin%7Bbmatrix%7D%0Aa%20%26%20b%20%5C%5C%20%0Ac%20%26%20d%0A%5Cend%7Bbmatrix%7D%0A%2B%0A%5Cbegin%7Bbmatrix%7D%0Ae%20%26f%20%5C%5C%20%0Ag%20%26h%0A%5Cend%7Bbmatrix%7D%0A%3D%0A%5Cbegin%7Bbmatrix%7D%0Aa%2Be%20%26b%2Bf%20%5C%5C%20%0Ac%2Bg%20%26d%2Bh%20%0A%5Cend%7Bbmatrix%7D">

### Scalar Multiplication

Let **A** be a matrix and **c** be a scalar where **Ac = cA** (commutative), then **Ac** is obtained by multiplying all entries in **A** by **c**

<img src="https://render.githubusercontent.com/render/math?math=c%5Cbegin%7Bbmatrix%7D%0A%20a_%7B11%7D%26%20a_%7B12%7D%20%5C%5C%20%0A%20a_%7B21%7D%20%26%20a_%7B22%7D%20%0A%5Cend%7Bbmatrix%7D%20%3D%20%5Cbegin%7Bbmatrix%7D%0A%20c(a_%7B11%7D)%26%20c(a_%7B12%7D)%20%20%5C%5C%20%0Ac(a_%7B21%7D)%20%26%20c(a_%7B22%7D)%0A%5Cend%7Bbmatrix%7D">


### Transpose 

Transpose is an operator that performs the following: transpose of the _m x n_ matrix **A** is the _n x m_ matrix A^T

<a href="https://www.codecogs.com/eqnedit.php?latex=(A^{T})_{ij}&space;=&space;A_{ji}\\&space;\\&space;\begin{bmatrix}&space;1&2&3&space;\\&space;4&space;&5&6&space;\end{bmatrix}^{T}&space;=&space;\begin{bmatrix}&space;1&space;&4&space;\\&space;2&space;&5\\&space;3&6&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?(A^{T})_{ij}&space;=&space;A_{ji}\\&space;\\&space;\begin{bmatrix}&space;1&2&3&space;\\&space;4&space;&5&6&space;\end{bmatrix}^{T}&space;=&space;\begin{bmatrix}&space;1&space;&4&space;\\&space;2&space;&5\\&space;3&6&space;\end{bmatrix}" title="(A^{T})_{ij} = A_{ji}\\ \\ \begin{bmatrix} 1&2&3 \\ 4 &5&6 \end{bmatrix}^{T} = \begin{bmatrix} 1 &4 \\ 2 &5\\ 3&6 \end{bmatrix}" /></a>