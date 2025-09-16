---
title: Math Analysis
tags:
  - math-analysis
  - note
date: 2025-09-15 07:55:19
---

# Math analysis

## Class 1 Some Inequality and Def of limit

### Triangle Inequality

<div class='cbox'>

$$
a,b\in R  \Rightarrow {\left \vert {\left \vert a \right \vert} -{\left \vert b \right \vert}   \right \vert}  \le  {\left \vert a+b \right \vert} \leq {\left \vert a \right \vert} + {\left \vert b \right \vert}
$$

</div>

<div class='pbox'>

$$
\begin{array}{c}
    -{\left \vert a \right \vert} {\left \vert b \right \vert} \le ab\le {\left \vert a \right \vert} {\left \vert b \right \vert}
 \Rightarrow  \\
{\left \vert a \right \vert} ^2-2 {\left \vert a \right \vert} {\left \vert b \right \vert}  + {\left \vert a+b \right \vert} ^2
\le a^2+2ab+b^2 
\le {\left \vert a \right \vert} ^2+2 {\left \vert a \right \vert} {\left \vert b \right \vert}  + {\left \vert a+b \right \vert} ^2 \Rightarrow  \\
({\left \vert a \right \vert} -{\left \vert b \right \vert} )^2\le (a+b)^2\le ({\left \vert a \right \vert} +{\left \vert b \right \vert} )^2
\end{array}
$$


</div>

向量的模长也满足 也可以用这个做法.

### Cauchy-Schwarz Inequality

<div class='cbox'>

$$
\begin{array}{c}
0<x_i \in R  \Rightarrow 
\dfrac{\sum_i x_i}{n} \ge \sqrt[n]{\prod_i x_i} \ge \dfrac{n}{\sum_i \dfrac{1}{x_i} }  
\end{array}
$$


</div>

<div class='pbox'>

显然 取$x_i=\dfrac{1}{x_i}$能用左边不等式推右边 只证左边

归纳,$2$的幂次显然吧

对非$2$的幂次$n$,用$X=\sqrt[n]{\prod_i x_i}$补完,直接套

</div>

### Array's Limit

<div class='cbox'>

$$
\begin{array}{c}
lim_{n\to \infty} a_n = A  \Leftrightarrow  \\
\forall \epsilon >0 \exists N \ s.t.\ 
n\ge N  \Rightarrow \left \vert a_n-A \right \vert < \epsilon
\end{array}
$$

</div>

注意
- $N=N(\epsilon)$
- $N$ 不唯一
- $\epsilon$ 可限制在任意$(0,a),a>0$

#### Eg 1

<div class='cbox'>

$\lim_n n^{\frac{1}{n} }=1$


</div>

<div class='pbox'>

$$
\begin{array}{c}
\vert n^{\frac{1}{n} }-1 \vert  \\
= \vert (\sqrt n \sqrt n)^{\frac{1}{n} } -1 \vert \\
={\left \vert (\prod_i 1 \cdot \sqrt n\sqrt n)^{\frac{1}{n} } -1 \right \vert}  \\
\le {\left \vert \dfrac{n-2+2\sqrt n}{n}  -1 \right \vert}  \\
\le \dfrac{2}{\sqrt n} 
\end{array}
$$

Or try this:

$$
\begin{array}{c}
{\left \vert n^{\frac{1}{n} }-1 \right \vert} =n^{\frac{1}{n} }-1<\epsilon \\
\Leftarrow  n^{\frac{1}{n}}<(\epsilon+1) \\
\Leftarrow  n<(1+\epsilon)^n \\
\Leftarrow n<1+\epsilon n+\frac{\epsilon^2n(n-1)}{2} 
\end{array}
$$

Solve the equation, it's a parabola with upward opening so the solution exists.

</div>

[think] At this stage, we cannot say $\lim g(f(n))=g(\lim f(n))$ which depends on continuity of function. But you sometimes can rewrite the proof with inequality.

## Class 2

### About $Q$

<div class='cbox'>

$$
\begin{array}{c}
\sqrt n \in Z \cup Q^C
\end{array}
$$

</div>

<div class='pbox'>

$p^2=q^2n$ Integer factorization

More natural than textbook but it doesn't depend on Integer factorization.

</div>

<div class='cbox'>

$\dfrac{p}{q}$ is finite decimal or repeating decimal

</div>

<div class='pbox'>

Simulate how the division is done and consider the remainder will be repeated.

</div>

### About Cardinality

<div class='cbox'>

#### Find a bijection of $[0,1]$ and $(0,1)$

</div>

<div class='pbox'>


$$
\begin{array}{c}
f(x):(0,1) \to [0,1]=\begin{cases}
0,x=\dfrac{1}{2} \\
1,x=\dfrac{1}{3} \\
\dfrac{1}{n-2} , x=\dfrac{1}{n} \\
x, \text{otherwise}
\end{cases}

\end{array}
$$

</div>

Wow!

