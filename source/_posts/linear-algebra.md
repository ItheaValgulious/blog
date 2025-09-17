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





## Done Right

