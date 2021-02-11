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

<img src="https://render.githubusercontent.com/render/math?math=(A%5E%7BT%7D)_%7Bij%7D%20%3D%20A_%7Bji%7D%5C%5C%0A%5C%5C%0A%5Cbegin%7Bbmatrix%7D%0A1%262%263%20%5C%5C%20%0A4%20%265%266%20%0A%5Cend%7Bbmatrix%7D%5E%7BT%7D%20%3D%20%0A%5Cbegin%7Bbmatrix%7D%0A1%20%264%20%5C%5C%20%0A2%20%265%5C%5C%0A3%266%20%0A%5Cend%7Bbmatrix%7D">