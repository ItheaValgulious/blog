---
title: Linear Algebra
tags:
  - linear-algebra
  - note
date: 2025-09-15 07:55:19
---
# Linear algebra

## A fun question

<div class='cbox'>

In n-D space we can found at most $n+1$ vector $v_1\ldots v_{n+1}$ such that:  $\forall i\ne j,v_iv_j<0$

</div>

<div class='pbox'>

### An example in 3-D space(the one on the book)

The construction is Obviously($CH_4$)

Chosen a vector, the others must be in a semisphere. We say two semisphere is seperated by plane A.

And we notice that: if two vector's shadow on plane A construct a acute angle, their dot product must be positive, transformed it into a 2-D problems which is easy to solve.

### Generalize to n-D

We choose a vector $v_1$, and it can be written as $[1,0,\ldots 0]$(with some rotation)

so $\forall  v_i,i>1, v_iv_1<0 \Rightarrow v_{i,1} < 0 \Rightarrow v_{i,1}v_{j,1}>0 \Rightarrow v_iv_j-v_{i,1}v_{j,1} < 0$

then transformed it into the (n-1)-D situation.

The construction can be easily give during the induction

### Another Proof

given by Bing!

#### Lemma: Radon Partition

<div class='cbox'>

In n-D space, $n+2$ point could be divided to two convex hull with intersection.

</div>

<div class='pbox'>

$n+2$ vector must be dependent: $\exists c_i \ s.t.\ \sum _{i=1}^{n+2} c_i x_i = 0; \sum_i x_i = 0$(the second condition can be satisfied by add another all-1 dimension).

so divide the vector by sign of $c_i$ we got:$v=\sum_{i\in A} c_i x_i = \sum_{j\in B} c_jx_j$,so divide the eqution by $\sum_{i\in A} c_i$, you get one point($v$) in the intersection.

</div>

We noticed $0<v^2=(\sum_{i\in A} c_i x_i) \cdot (\sum_{j\in B} c_jx_j)<0$, contradiction!

</div>

## Operator's Left Inverse and Right Inverse

### Existance

<div class='cbox'>

对算子$T$来说,左逆存在等价于右逆存在.

</div>

<div class='pbox'>

#### Proof 1

注意到左逆存在等价于$T$是单射,右逆存在等价于$T$是满射.

又因为$T$单射等价于$T$满射等价于$T$双射,所以左逆存在等价于右逆存在且两个逆一定相同.

#### Proof 2

左逆推出$T$分解成初等行变换矩阵,然后一个一个取逆推右逆.

</div>


## Union of finite count of proper sub-space isn't V 

<div class='cbox'>

$$
\begin{array}{l}
F \text{ is inifinite Field} \\ 
\forall U_1\ldots U_k,U_i \text{ is subspace of } V(F) \\
V\ne \bigcup_{i=1}^k U_i
\end{array}
$$

</div>

<div class='pbox'>

考虑归纳,$k=1$成立,设$k-1$个不行,反证,那么可以取$v\notin \bigcup_{i=1}^{k-1} U_i$,必有$v\in U_k$.

再取$u\notin U_k$,令 $S=\{ u+iv \vert i \in R\}$,则对$j<k$,每个$U_j$至多包含一个$S$中的向量(否则$v\in U_j$),而$U_k$必然没有$S$中向量(否则$u\in U_k$),而$S$中有无限个向量,于是$S$不可能被他们包含,得证.

</div>

[think] 而这个定理甚至在有限域下有反例.