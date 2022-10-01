# SPDX-FileCopyrightText: 2022-present gv-sh <gv-sh@outlook.com>
#
# SPDX-License-Identifier: MIT

zx      = lambda x              : 0
zxy     = lambda x,y            : 0
ox      = lambda x              : 1
oxy     = lambda x,y            : 1

mat     = lambda m, n, f=zxy    : [[f(i,j) for i in range(n)] for j in range(m)]
row     = lambda n, f=zx        : [[f(i) for i in range(n)]]
col     = lambda m, f=zx        : [[f(i)] for i in range(m)]
sqr     = lambda n, f=zxy       : mat(n, n, f)
vec     = lambda n, f=zx        : [f(i) for i in range(n)]
I       = lambda n, f=zx        : sqr(n, lambda i,j: 1 if i==j else 0)

add     = lambda A, B           : [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
sub     = lambda A, B           : [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
mul     = lambda A, k           : [[k * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]
dot     = lambda A, B           : [[sum([A[i][k] * B[k][j] for k in range(len(A[0]))]) for j in range(len(B[0]))] for i in range(len(A))]

T       = lambda A              : [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
is_eq   = lambda A, B           : all([all([A[i][j] == B[i][j] for j in range(len(A[0]))]) for i in range(len(A))])

# row ops
rswp    = lambda A, i, j        : [A[j] if k == i else A[i] if k == j else A[k] for k in range(len(A))]
rmul    = lambda A, i           : [mul([A[i]], k)[0] if k == i else A[k] for k in range(len(A))]
radd    = lambda A, i, j        : [add([A[i]], mul([A[j]], k))[0] if k == i else A[k] for k in range(len(A))]
rdel    = lambda A, i           : [A[k] for k in range(len(A)) if k != i]

# col ops
cswp    = lambda A, i, j        : T(rswp(T(A), i, j))
cmul    = lambda A, i           : T(rmul(T(A), i))
cadd    = lambda A, i, j        : T(radd(T(A), i, j))
cdel    = lambda A, i           : T(rdel(T(A), i))