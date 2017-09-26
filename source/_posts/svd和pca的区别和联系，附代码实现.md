---
title: svd和pca的区别和联系，附代码实现
date: 2017-06-28 17:40:45
tags: [svd, pca]
mathjax: true
---

> svd=singular value decomposition
> pca=principal component analysis

在做潜在语义分析(lsa)的时候，我用的svd，感觉svd和pca非常像，但是又有区别。所以查了一些资料，在这里翻译一下，并在最后，贴上python代码比较了这两种方法。

## PCA

假设`\( \mathbf X \)`是一个`\( n \times p \)`的矩阵，`n`是样本量, 而`p`是变量个数。那么，我们就可以计算得到协方差矩阵`\( \Singma \)`：

`
\[ \Sigma=X^TX/(n-1) \]
`

由于`\( \Sigma \)`是对称矩阵，那么它可以对角化:

`
\[ \Sigma = \mathbf V \mathbf L \mathbf V^\top \]
`

`\( \mathbf V \)`就是`\( \mathbf X \)`的特征向量构成的矩阵，而`\( \mathbf L \)`是一个对角矩阵，对角元素就是特征向量对应的特征值。

用`\( \mathbf Y \)`表示主成分矩阵，`\( y_i \)`表示第i个主成分向量。用`\( v_i \)`表示第i个特征向量。那么有关系式：

`
\[ y_i= \mathbf X v_i\]
`

即：

`
\[ Y= \mathbf X \mathbf V \]
`

## SVD

接下来我们看看SVD的性质。对`\( \mathbf X \)`进行SVD分解：

`
\[ \mathbf X = \mathbf U \mathbf S \mathbf V^\top \]
`

`\( \mathbf V \)`和上面提到的`\( \mathbf V \)`是一样的，但是在SVD中叫做singular vector(奇异向量)，而`\( \mathbf S \)`叫做奇异值构成的对角矩阵, 它与特征向量是不同的，但是他们之间是成比例的。如此，我们很容易得到：

`
\[ \mathbf X = \mathbf V \mathbf S \mathbf U^\top \mathbf U \mathbf S \mathbf V^\top /(n-1) = \mathbf V \frac{\mathbf S^2}{n-1}\mathbf V^\top \]
`

所以，特征值与奇异值之间的关系就是：

`
\[ \lambda_i = s_i^2/(n-1) \]
`

主成分也可以得到：

`
\[ \mathbf X \mathbf V = \mathbf U \mathbf S \mathbf V^\top \mathbf V = \mathbf U \mathbf S \]
`

下面我们通过python代码来探索svd和pca之间的关系

```python
import numpy as np
from numpy import linalg as la
np.random.seed(42)


def flip_signs(A, B):
    """
    utility function for resolving the sign ambiguity in SVD
    http://stats.stackexchange.com/q/34396/115202
    """
    signs = np.sign(A) * np.sign(B)
    return A, B * signs


# Let the data matrix X be of n x p size,
# where n is the number of samples and p is the number of variables
n, p = 5, 3
X = np.random.rand(n, p)
# Let us assume that it is centered
X -= np.mean(X, axis=0)

# the p x p covariance matrix
C = np.cov(X, rowvar=False)
print ("C = \n", C)
# C is a symmetric matrix and so it can be diagonalized:
l, principal_axes = la.eig(C)
# sort results wrt. eigenvalues
idx = l.argsort()[::-1]
l, principal_axes = l[idx], principal_axes[:, idx]
# the eigenvalues in decreasing order
print ("l = \n", l)
# a matrix of eigenvectors (each column is an eigenvector)
print ("V = \n", principal_axes)
# projections of X on the principal axes are called principal components
principal_components = X.dot(principal_axes)
print ("Y = \n", principal_components)

# we now perform singular value decomposition of X
# "economy size" (or "thin") SVD
U, s, Vt = la.svd(X, full_matrices=False)
V = Vt.T
S = np.diag(s)
print ("V2 = \n", V )
# 1) then columns of V are principal directions/axes.
assert np.allclose(*flip_signs(V, principal_axes))

# 2) columns of US are principal components
assert np.allclose(*flip_signs(U.dot(S), principal_components))

# 3) singular values are related to the eigenvalues of covariance matrix
assert np.allclose((s ** 2) / (n - 1), l)

# 8) dimensionality reduction
k = 2
PC_k = principal_components[:, 0:k]
US_k = U[:, 0:k].dot(S[0:k, 0:k])
assert np.allclose(*flip_signs(PC_k, US_k))

# 10) we used "economy size" (or "thin") SVD
assert U.shape == (n, p)
assert S.shape == (p, p)
assert V.shape == (p, p)
```