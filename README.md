

## Vectors 





## Matrices 

### Matrices in Python (See read_matrix_input.py)
**Definition:** Matrices are represented as _lists_:`A = ([1, 0], [0, 1])` or `A = [[1, 0], [0, 1]]`

* If we want to look up a row: `A[0] = [1,0]`
* If we want to look up an element: `A[0,0] = 1 `

In the matrix class; we represent matrices by lists contained inside a tuple.


### Adding/ Subtracting two matrices (See operations_on_matrices.py)

To add or subtract two matrices together we must verify that the dimension of A is same as B. If this is true, then we simply add or subtract the corresponding elements:

<img src="https://latex.codecogs.com/svg.image?A=\left[\begin{array}{ll}a&space;&&space;b&space;\\c&space;&&space;d\end{array}\right],&space;B=\left[\begin{array}{ll}e&space;&&space;f&space;\\g&space;&&space;h\end{array}\right]:&space;A&plus;B=\left[\begin{array}{ll}a&plus;e&space;&&space;b&plus;f&space;\\c&plus;g&space;&&space;d&plus;h\end{array}\right]" title="A=\left[\begin{array}{ll}a & b \\c & d\end{array}\right], B=\left[\begin{array}{ll}e & f \\g & h\end{array}\right]: A+B=\left[\begin{array}{ll}a+e & b+f \\c+g & d+h\end{array}\right]" />

### Scalar Multiplication

**Definition:** Let  _A_ be a matrix and _c_ be a scalar where  _(A)c = c(A)_ (commutative), then _(A)c_ is obtained by multiplying all entries in _A_ by _c_

<img src="https://latex.codecogs.com/svg.image?c\left[\begin{array}{ll}a_{11}&space;&&space;a_{12}&space;\\a_{21}&space;&&space;a_{22}\end{array}\right]=\left[\begin{array}{ll}c\left(a_{11}\right)&space;&&space;c\left(a_{12}\right)&space;\\c\left(a_{21}\right)&space;&&space;c\left(a_{22}\right)\end{array}\right]" title="c\left[\begin{array}{ll}a_{11} & a_{12} \\a_{21} & a_{22}\end{array}\right]=\left[\begin{array}{ll}c\left(a_{11}\right) & c\left(a_{12}\right) \\c\left(a_{21}\right) & c\left(a_{22}\right)\end{array}\right]" />


### Matrix Multiplication of A and B (See operations_on_matrices.py)

When performing matrix multiplication, the following condition must be met:
> The number of columns in the first matrix must be the same as the number of rows in the second matrix.

Consider the following matrices *A* and *B* and observe how we obtain the matrix *C* by performing a dot product on the ith row of *A* and the jth column of *B*:

<img src="https://latex.codecogs.com/svg.image?\begin{aligned}&{\left[\begin{array}{lll}a_{11}&space;&&space;a_{12}&space;&&space;a_{13}&space;\\a_{21}&space;&&space;a_{22}&space;&&space;a_{23}\end{array}\right]_{2&space;x&space;3}\left[\begin{array}{ll}b_{11}&space;&&space;b_{12}&space;\\b_{21}&space;&&space;b_{22}&space;\\b_{31}&space;&&space;b_{32}\end{array}\right]_{3&space;x&space;2}=\left[\begin{array}{ll}c_{11}&space;&&space;c_{12}&space;\\c_{21}&space;&&space;c_{22}\end{array}\right]_{2&space;x&space;2}}&space;\\&c_{11}=a_{11}&space;b_{11}&plus;a_{12}&space;b_{21}&plus;a_{13}&space;b_{31}&space;\\&c_{21}=a_{21}&space;b_{11}&plus;a_{22}&space;b_{21}&plus;a_{23}&space;b_{31}&space;\\&c_{12}=a_{11}&space;b_{12}&plus;a_{12}&space;b_{22}&plus;a_{13}&space;b_{32}&space;\\&c_{22}=a_{21}&space;b_{12}&plus;a_{22}&space;b_{22}&plus;a_{23}&space;b_{32}\end{aligned}" title="\begin{aligned}&{\left[\begin{array}{lll}a_{11} & a_{12} & a_{13} \\a_{21} & a_{22} & a_{23}\end{array}\right]_{2 x 3}\left[\begin{array}{ll}b_{11} & b_{12} \\b_{21} & b_{22} \\b_{31} & b_{32}\end{array}\right]_{3 x 2}=\left[\begin{array}{ll}c_{11} & c_{12} \\c_{21} & c_{22}\end{array}\right]_{2 x 2}} \\&c_{11}=a_{11} b_{11}+a_{12} b_{21}+a_{13} b_{31} \\&c_{21}=a_{21} b_{11}+a_{22} b_{21}+a_{23} b_{31} \\&c_{12}=a_{11} b_{12}+a_{12} b_{22}+a_{13} b_{32} \\&c_{22}=a_{21} b_{12}+a_{22} b_{22}+a_{23} b_{32}\end{aligned}" />

### Transpose

Transpose is an operator that performs the following: transpose of the _m x n_ matrix *A* is the _n x m_ matrix <img src="https://latex.codecogs.com/svg.image?A^{T}" title="A^{T}" /> 

<img src="https://latex.codecogs.com/svg.image?\begin{gathered}\left(A^{T}\right)_{i&space;j}=A_{j&space;i}&space;\\{\left[\begin{array}{lll}1&space;&&space;2&space;&&space;3&space;\\4&space;&&space;5&space;&&space;6\end{array}\right]^{T}=\left[\begin{array}{ll}1&space;&&space;4&space;\\2&space;&&space;5&space;\\3&space;&&space;6\end{array}\right]}\end{gathered}" title="\begin{gathered}\left(A^{T}\right)_{i j}=A_{j i} \\{\left[\begin{array}{lll}1 & 2 & 3 \\4 & 5 & 6\end{array}\right]^{T}=\left[\begin{array}{ll}1 & 4 \\2 & 5 \\3 & 6\end{array}\right]}\end{gathered}" />

### Trace

**Definition:** For a square matrix <img src="https://latex.codecogs.com/svg.image?A&space;\in&space;M_{n,n}" title="A \in M_{n,n}" />, we define the **trace** of _A (tr(A)_) to the sums of the diagonal entries of _A_. i.e

<img src="https://latex.codecogs.com/svg.image?If\&space;A&space;=&space;[ij]\&space;then\&space;tr(A)=a_{1,1}&plus;a_{2,2}&plus;...&plus;a_{n,n}" title="If\ A = [ij]\ then\ tr(A)=a_{1,1}+a_{2,2}+...+a_{n,n}" />

### Reduced Row Echelon Form



### Elementary Matrices
**Definition:** An _elementary matrix_ is a matrix obtained by applying exactly one _elementary row operation_ to the identity matrix. 

### Equivalent Matrix 
**Definition:** A matrix _B_ is said to be equivalent to another matrix _A_ if _B_ can be obtained by applying a ***finite*** number of elementary row operations to _A_.

<img src="https://latex.codecogs.com/svg.image?That\&space;is:\&space;A&space;\stackrel{o&space;p_{1}}{\longrightarrow}&space;A_{1}&space;\stackrel{o&space;p_{2}}{\longrightarrow}&space;A_{2}&space;\stackrel{o&space;p_{3}}{\longrightarrow}&space;\cdots&space;\stackrel{o&space;p_{k}}{\longrightarrow}&space;B&space;." title="That\ is:\ A \stackrel{o p_{1}}{\longrightarrow} A_{1} \stackrel{o p_{2}}{\longrightarrow} A_{2} \stackrel{o p_{3}}{\longrightarrow} \cdots \stackrel{o p_{k}}{\longrightarrow} B ." />

### Determinant of a Matrix

**Definition:** *Let* <img src="https://latex.codecogs.com/svg.image?A&space;=&space;[aij]" title="A = [aij]" /> *be a square* n × n *matrix. Set* <img src="https://latex.codecogs.com/svg.image?Aij&space;" title="Aij " />*by the matrix obtained by removing the* i*th row and* j*th column from* A*. The* **determinant** *of* A*, written* <img src="https://latex.codecogs.com/svg.image?det(A)" title="det(A)" />

<img src="https://latex.codecogs.com/svg.image?|A|=\sum_{j=1}^{n}(-1)^{1&plus;j}&space;a_{1&space;j}\left|A_{1&space;j}\right|" title="|A|=\sum_{j=1}^{n}(-1)^{1+j} a_{1 j}\left|A_{1 j}\right|" />

In general the determinat is a function which takes and input (square matrix) and produces an output (scalar value).

* If A is a nonhomogeneous matrix with a non-zero determinant, then A has unique solution
* If A has a non-zero determinant then A has an inverse; with linear independent columns

##### 2D Determinant 

A 2 by 2 determinant is defined to be

<img src="https://latex.codecogs.com/svg.image?\operatorname{det}\left[\begin{array}{ll}a&space;&&space;b&space;\\c&space;&&space;d\end{array}\right]=a&space;d-b&space;c" title="\operatorname{det}\left[\begin{array}{ll}a & b \\c & d\end{array}\right]=a d-b c" />

##### 3D Determinant 



### Orthogonal Matrices and Rotation 

**Definition:** A matrix <img src="https://latex.codecogs.com/svg.image?A&space;\in&space;M_{n,n}" title="A \in M_{n,n}" /> is **orthogonal** if <img src="https://latex.codecogs.com/svg.image?A^{T}A&space;=&space;I\&space;where\&space;I\&space;is\&space;the\&space;identity\&space;matrix" title="A^{T}A = I\ where\ I\ is\ the\ identity\ matrix" />

**Example:**

The 2D rotation matrix is given by:

<img src="https://latex.codecogs.com/svg.image?R=\left[\begin{array}{cc}\cos&space;\theta&space;&&space;-\sin&space;\theta&space;\\\sin&space;\theta&space;&&space;\cos&space;\theta\end{array}\right]" title="R=\left[\begin{array}{cc}\cos \theta & -\sin \theta \\\sin \theta & \cos \theta\end{array}\right]" />

A 30 degree rotation **R** becomes:

<img src="https://latex.codecogs.com/svg.image?R=\left[\begin{array}{rr}\sqrt{3}&space;/&space;2&space;&&space;-1&space;/&space;2&space;\\1&space;/&space;2&space;&&space;\sqrt{3}&space;/&space;2\end{array}\right]" title="R=\left[\begin{array}{rr}\sqrt{3} / 2 & -1 / 2 \\1 / 2 & \sqrt{3} / 2\end{array}\right]" />

We can verify that R is indeed orthogonal by evaluating <img src="https://latex.codecogs.com/svg.image?A^{T}A" title="A^{T}A" />

<img src="https://latex.codecogs.com/svg.image?\left[\begin{array}{rr}\sqrt{3}&space;/&space;2&space;&&space;-1&space;/&space;2&space;\\1&space;/&space;2&space;&&space;\sqrt{3}&space;/&space;2\end{array}\right]^{T}\left[\begin{array}{rr}\sqrt{3}&space;/&space;2&space;&&space;-1&space;/&space;2&space;\\1&space;/&space;2&space;&&space;\sqrt{3}&space;/&space;2\end{array}\right]" title="\left[\begin{array}{rr}\sqrt{3} / 2 & -1 / 2 \\1 / 2 & \sqrt{3} / 2\end{array}\right]^{T}\left[\begin{array}{rr}\sqrt{3} / 2 & -1 / 2 \\1 / 2 & \sqrt{3} / 2\end{array}\right]" /> <img src="https://latex.codecogs.com/svg.image?=" title="=" /> <img src="https://latex.codecogs.com/svg.image?\left[\begin{array}{rr}\sqrt{3}&space;/&space;2&space;&&space;1&space;/&space;2&space;\\-1&space;/&space;2&space;&&space;\sqrt{3}&space;/&space;2\end{array}\right]\left[\begin{array}{rr}\sqrt{3}&space;/&space;2&space;&&space;-1&space;/&space;2&space;\\1&space;/&space;2&space;&&space;\sqrt{3}&space;/&space;2\end{array}\right]=\left[\begin{array}{ll}1&space;&&space;0&space;\\0&space;&&space;1\end{array}\right]" title="\left[\begin{array}{rr}\sqrt{3} / 2 & 1 / 2 \\-1 / 2 & \sqrt{3} / 2\end{array}\right]\left[\begin{array}{rr}\sqrt{3} / 2 & -1 / 2 \\1 / 2 & \sqrt{3} / 2\end{array}\right]=\left[\begin{array}{ll}1 & 0 \\0 & 1\end{array}\right]" />

If A is orthogonal then the following is also true:

<img src="https://latex.codecogs.com/svg.image?A^{\mathrm{T}}=A^{-1}" title="A^{\mathrm{T}}=A^{-1}" />




### Matrix plus Graph Theory (See graphs.py)

Graph is a pair _G = (V, E)_, _V_ is a set of **vertices**, and _E_ is the set of **edges**. Two vertices u,v are adjacent iff an edge e = uv.
**Adjacency Matrix M:** is a relation over the set of vertices of the graph G. M is a nxn matrix where n = cardinality (number of elements of a set) of V:

<img src="https://latex.codecogs.com/svg.image?M(i,&space;j)=&space;\begin{cases}1,&space;&&space;\text&space;{&space;if&space;edge&space;}&space;i&space;j&space;\in&space;E&space;\\&space;0,&space;&&space;\text&space;{&space;if&space;edge&space;}&space;i&space;j&space;\notin&space;E\end{cases}" title="M(i, j)= \begin{cases}1, & \text { if edge } i j \in E \\ 0, & \text { if edge } i j \notin E\end{cases}" />

Consider the following example:

<img src="https://latex.codecogs.com/svg.image?V=\{a,&space;b,&space;c\},&space;E=\{a&space;b,&space;a&space;c,&space;b&space;c,&space;b&space;a,&space;c&space;b\}\left\{\left[\begin{array}{lll}0&space;&&space;1&space;&&space;1&space;\\1&space;&&space;0&space;&&space;0&space;\\0&space;&&space;1&space;&&space;0\end{array}\right]\right." title="V=\{a, b, c\}, E=\{a b, a c, b c, b a, c b\}\left\{\left[\begin{array}{lll}0 & 1 & 1 \\1 & 0 & 0 \\0 & 1 & 0\end{array}\right]\right." />
