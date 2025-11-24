---
title: Cayley Hamilton
tags: [linear-algebra,math,whims]
---

# Cayley Hamilton

好了大家都知道内容说的是矩阵$A$特征多项式$p(\lambda)=\vert \lambda I-A\vert$有$p(A)=0$

## 如果$F=R,C$

或者说,如果$F$满足$F$的多项式方程的根也属于$F$,即我们可以搞特征值那一套.

证明方法会很多.

比如舒尔定理+因式分解,则$p(A)=\prod_i (A-\lambda_i)$,你可以排列这些因式使得$A=B_1B_2\ldots B_n$且${B_k}_{,k,k}=0$,于是乘起来显然对任意向量是$0$.

比如直接考虑广义本征空间$G(A,\lambda)$上$(T-\lambda I)_{G(A,\lambda)}$是幂零的.

## 如果任意域

然后大家都知道你不能直接声称$p(A)=\det (AI-A)$带进去做,**因为$\lambda I$是数乘但带入$A$就成了矩阵乘法.**

为了让它们一样,容易想到我们把原来的数$a$变成$aI$,因为这样符合数乘规则和数之间的运算.

于是新的$AI-A$实际上是矩阵

$$
\begin{gathered}
B_{i,j}=\begin{cases}
A-a_{i,j}I,i=j \\
-a_{i,j}I,i\ne j
\end{cases}
\end{gathered}
$$

**这里$AI$是数字$A$数乘矩阵$I$,而$-A$是一个矩阵,其中数字是$a_{i,j}I$**.

而原来我们说$AI-A=0$,那新的矩阵显然不是一个$0$矩阵,但是难以注意到,取原来空间的一组基$e_1\ldots e_n$,考虑

$$
\begin{gathered}
\text{let } E=\begin{bmatrix}
    e_1 \\
    e_2 \\
    \ldots \\
    e_n
\end{bmatrix} \\
B E=\begin{bmatrix}
    x_1 \\
    x_2 \\
    \ldots \\
    x_n
\end{bmatrix}
\end{gathered}
$$

(如果觉得在把$n\times n$矩阵当数的情况下引入$n\times 1$的向量是坏文明,可以把向量变成$n\times n$的对角矩阵,容易验证性质不变).

则

$$
\begin{gathered}
x_k=\sum _{i = 1} ^{n}  B_{k,i}e_i \\
=Ae_k-\sum _{i = 1} ^{n}  a_{k,i}e_i \\
=0
\end{gathered}
$$

那么考虑在新的域下定义的伴随矩阵仍然是能用的(只用到行列式,即只需要加和乘),乘上伴随矩阵就得到

$$
\begin{gathered}
\vert B\vert E=\vert B \vert IE= B^*BE=0
\end{gathered}
$$

而$\det B$是什么呢,你发现大矩阵求行列式的结构$\det (AI-A)$和求小矩阵的结构$\det xI-A$是完全一样的,只要把$AI$替换成$x$,就会得到$\det B=p(A)$,而这是个$n\times n$的矩阵,且乘一组基是$0$,所以$p(A)=0$

这样你就通过在$n\times n$矩阵的环上定义的矩阵和行列式,以及它们和原本矩阵的结构的相似性证明了这个问题.

这个证法其实和走抽象代数,走张量积的做法本质相同(甚至你把矩阵塞到矩阵里就是张量积的坐标形式).