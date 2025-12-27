---
title: Math Analysis Homework - Week 13
tags:
  - math-analysis
  - homework
  - math
date: 2025-12-17 08:25:48
---


# Math Analysis Homework - Week 13

## Class 1

### T1

<div class="cbox">

**1.** 判断下列级数的敛散性, 绝对收敛还是条件收敛?

(2) $\sum_{n=1}^{\infty}(-1)^{n-1} \frac{1}{n \ln n}$;

</div>

<div class="pbox">

$\dfrac{1}{n\ln n}$递减,莱布尼茨判别法知收敛

$$
\begin{gathered}
\int_1^\infty \dfrac{1}{x\ln x} dx=\int_1^\infty \dfrac{1}{x} dx =\infty
\end{gathered}
$$

条件收敛

</div>

### T2

<div class="cbox">

**1.** 判断下列级数的敛散性, 绝对收敛还是条件收敛?

(4) $\sum_{n=1}^{\infty} \sin(\pi \sqrt{n^2+1})$;

</div>

<div class="pbox">

$$
\begin{gathered}
\sqrt{n^2+1}-n=\dfrac{1}{\sqrt{n^2+1}+n} \text{ is decreasing}  \\
\Rightarrow \sin(\pi \sqrt{n^2+1})=\sin(\pi (\sqrt{n^2+1}-n))(-1)^n
\end{gathered}
$$

于是由莱布尼茨判别法收敛.

$$
\begin{gathered}
\sum_{n=1}^\infty {\left \vert \sin(\pi\sqrt{n^2+1}) \right \vert}  \\
=\sum_{n=1}^\infty \sin \dfrac{1}{\sqrt{ n^2+1 } +n}  \\
\sim \sum _{n=1} ^\infty \dfrac{1}{n+\sqrt{n^2}+1}  \\
\sim \sum \dfrac{1}{n}  
\end{gathered}
$$

发散.

于是条件收敛.


</div>

### T3

<div class="cbox">

**1.** 判断下列级数的敛散性, 绝对收敛还是条件收敛?

(6) $\sum_{n=1}^{\infty}(-1)^{n-1} \frac{1}{n^p \sqrt[n]{n}} \quad (p \in \mathbb{R})$;

</div>

<div class="pbox">

$p\le 0$:发散.

$p>0$:


$$
\begin{gathered}
\ln (x^{p+\frac1n})'=((p+\dfrac{1}{n} )\ln x)' \\
=\dfrac{np+1-\ln n}{n^2} 
\end{gathered}
$$

$n$足够大时$n^{p+\frac1n}$递增,整体递减,莱布尼茨判别法知收敛

对数判别法:

$$
\begin{gathered}
\dfrac{\ln n^p \sqrt[ n ]{ n } }{\ln n} =p+\dfrac{1}{n} \to p
\end{gathered}
$$

于是$p\in (0,1)$条件收敛,$p\in (1,\infty)$绝对收敛.

$p=1$时代入由比较法知条件收敛.

</div>

### T4

<div class="cbox">

**1.** 判断下列级数的敛散性, 绝对收敛还是条件收敛?

(8) $\sum_{n=1}^{\infty}(-1)^{n-1} \frac{\cos(nx)}{2^n}$;

</div>

<div class="pbox">

其绝对值小于$2^{-n}$,绝对收敛.

</div>

### T5

<div class="cbox">

**1.** 判断下列级数的敛散性, 绝对收敛还是条件收敛?

(10) $\sum_{n=1}^{\infty} \frac{\sin n}{n^{p+\frac{1}{n}}} \quad (p \in \mathbb{R})$;

</div>

<div class="pbox">

$p\le 0$发散.

由迪利克雷判别法,$p>0$时$\sin n$求和有界,$n$足够大时$n^{p+\frac1n}$递增,知收敛.

由比较法极限形式,$p\in (0,1]$条件收敛,$p\in (1,\infty)$绝对收敛

</div>

### T6

<div class="cbox">

**1.** 判断下列级数的敛散性, 绝对收敛还是条件收敛?

(12) $\sum_{n=1}^{\infty} \frac{\sin n}{n^p + \sin n} \quad (p \in \mathbb{R})$.

</div>

<div class="pbox">

$p\le 0$:显然发散.

$p>0$:

$$
\begin{gathered}
a_n=\dfrac{\sin n}{n^p+\sin n} \\
=\dfrac{\sin n}{n^p} \dfrac{1}{1+\dfrac{\sin n}{n^p} } \\
= \dfrac{\sin n}{n^p} (1-\dfrac{\sin n}{n^p}+o(\dfrac{\sin n}{n^p} )) \\
=\dfrac{\sin n}{n^p} -\dfrac{\sin^2 n}{n^{2p}} 
\end{gathered}
$$

分别看:第一项是$p\le 1$条件收敛$p>1$绝对收敛,第二项$p>\dfrac12$收敛$p<\dfrac12$发散.

于是$p\in (-\infty,\dfrac12]$发散,$(\dfrac12,1]$条件收敛,$(1,+\infty)$绝对收敛.

</div>

### T7

<div class="cbox">

**2.** 设级数 $\sum_{n=2}^{\infty} (a_n - a_{n-1})$ 绝对收敛, 且级数 $\sum_{n=1}^{\infty} b_n$ 收敛. 证明: 级数 $\sum_{n=1}^{\infty} a_n b_n$ 收敛.

</div>

<div class="pbox">

$$
\begin{gathered}
\sum _{i = 1} ^{n}   a_ib_i \\
=\sum_{i=1}^n a_i(B_i-B_{i-1}) \\
=\sum_i^{n-1} B_i(a_i-a_{i+1})+a_nB_n \\
\end{gathered}
$$

对第二项,$B_n,a_n$分别收敛($a_n$收敛用柯西),故收敛.

对第一项:

$$
\begin{gathered}
\sum _{i = 1} ^{n-1}  \vert B_i \vert \vert a_i-a_{i-1} \vert  \\
\le M\sum _{i = 1} ^{n-1} \vert a_i-a_{i-1} \vert  
\end{gathered}
$$

绝对收敛,所以第一项收敛.

于是原式收敛.

</div>

### T8

<div class="cbox">

**3.** 设级数 $\sum_{n=2}^{\infty} (a_n - a_{n-1})$ 绝对收敛, 且 $\lim_{n\to\infty} a_n = 0$, 级数 $\sum_{n=1}^{\infty} b_n$ 的部分和有界. 证明: 级数 $\sum_{n=1}^{\infty} a_n b_n$ 收敛.

</div>

<div class="pbox">

和上个题一摸一样啊,先到

$$
\begin{gathered}
\sum _{i = 1} ^{n}  a_ib_i=\sum_i^{n-1} B_i(a_i-a_{i+1})+a_nB_n \\
\end{gathered}
$$

然后第一项和上面一样处理是收敛,第二项因为$a_n$极限是$0$,$B_n$有界所以收敛到$0$.于是原式收敛.

</div>

## Class 2

### T1

<div class="cbox">

**1.** 求下列数列的上、下极限:
(1) $\frac{n+1}{n}(1 + (-1)^{n+1})$;

</div>

<div class="pbox">

偶数列到$0$,奇数列到$2$,且覆盖了所有元素.

$$
\begin{gathered}
\limsup a_n=2,\liminf a_n=0
\end{gathered}
$$

</div>

### T2

<div class="cbox">

**1.** 求下列数列的上、下极限:
(2) $\sin \frac{n\pi}{2} + n \cos \frac{n\pi}{2}$.

</div>

<div class="pbox">

取$n=4k$得到$\limsup a_n=+\infty$.

取$n=-4k$得$\liminf a_n=-\infty$.

</div>

### T3

<div class="cbox">

**3.** 设 $x_n > 0, y_n > 0$, 证明: $\displaystyle \liminf_{n\to\infty} x_n \cdot \liminf_{n\to\infty} y_n \leqslant \liminf_{n\to\infty} x_ny_n \leqslant \limsup_{n\to\infty} x_n \cdot \liminf_{n\to\infty} y_n$.

</div>

<div class="pbox">

$a_n=\inf_{k>n} x_k,b_n=\inf_{k>n} y_k$.

则$\liminf x_n \liminf y_n=\lim a_n \lim b_n=\lim a_nb_n$.

而$c_n=\inf_{k>n} x_ky_k\ge a_nb_n$:假设$c_n<a_nb_n$,取$\epsilon<\dfrac{a_nb_n-c_n}2$,则能取到$x_ky_k<c_n+\epsilon$,但显然$a_n\le x_k,b_n\le y_k$,于是$c_n+\epsilon>a_nb_n,c_n<a_nb_n$,与$\epsilon<a_nb_n-c_n$矛盾.

于是 $c_n=\inf_{k>n} x_ky_k,\lim_{n \to \infty} c_n<\lim_{n \to \infty} a_nb_n$,左边得证.

右边,设$d_n=\sup_{k>n} x_k$.则$\forall \epsilon,\exists k,b_n>y_k-\epsilon$同时$c_n<x_ky_k$,$d_n>x_k$,则$c_n<x_ky_k<d_n(b_n+\epsilon)$对任意$\epsilon$,于是$c_n\le d_nb_n$,于是右边得证.

</div>

## Class 3
### T1

<div class="cbox">

**5.** 设 $x_1 > 0, x_{n+1} = 1 + \frac{1}{x_n} (n=1, 2, \cdots)$, 证明:

(1) $1 \leqslant \liminf_{n\to\infty} x_n \leqslant \limsup_{n\to\infty} x_n \leqslant 2$;

(2) $\lim_{n\to\infty} x_n$ 存在, 并求其极限值.

</div>

<div class="pbox">

$$
\begin{gathered}
\text{let } S=\limsup_{n \to \infty} x_n,I=\liminf_{n \to \infty} x_n \\
\begin{cases}
S=1+\dfrac{1}{I} \\
I=1+\dfrac{1}{S}  \\
S\ge I>0
\end{cases}
\Rightarrow 
S=I=\dfrac{1+\sqrt 5}{2} \in [1,2]
\end{gathered}
$$

得证.

</div>

### T2

<div class="cbox">

**6.** 设 $a_n > 0$, 证明: $\limsup_{n\to\infty} n \left(\frac{1+a_{n+1}}{a_n} - 1\right) \geqslant 1$.

</div>

<div class="pbox">

反证,假设 $\limsup_{n \to \infty} n(\dfrac{1+a_{n+1}}{a_n} -1)<1$,则存在$N$使得$n>N$时:

$$
\begin{gathered}
n(\dfrac{1+a_{n+1}}{a_n} -1)<1 \\
\Rightarrow \dfrac{a_{n+1}}{n+1} <\dfrac{a_n}{n} -\dfrac{1}{n+1}  \\
\Rightarrow \dfrac{a_{n}}{n}<\dfrac{a_{N+1}}{N+1}-\sum _{i = N+2} ^{n}  \dfrac{1}{i}    \\
\end{gathered}
$$

调和级数发散,所以存在$n$使得右边为负,左边$\dfrac{a_n}n<0$,与$a_n>0$矛盾
</div>

### T3

<div class="cbox">

**7.** 设数列 $\{x_n\}$ 满足: $x_n + x_m - 1 \leqslant x_{n+m} \leqslant x_n + x_m + 1$, 证明: $\{\frac{x_n}{n}\}$ 收敛.

</div>

<div class="pbox">

取$n=pk+r$:

$$
\begin{gathered}
x_n=x_{pk+r}\in [kx_p+x_r-k,kx_p+x_r+k] \\
\dfrac{x_n}{n} \in [\dfrac{k(x_p-1)}{pk+r}+\dfrac{x_r}{pk+r}  ,\dfrac{k(x_p+1)}{pk+r}+\dfrac{x_r}{pk+r} ]  \\
\limsup_{n \to \infty} \dfrac{x_n}{n} \in [\dfrac{x_p-1}{p} ,\dfrac{x_p+1}{p}] \\
\limsup_{n \to \infty} \dfrac{x_n}{n} \in [\liminf_{p \to \infty} \dfrac{x_p}{p} ,\liminf_{np \to \infty} \dfrac{x_p}{p} ]
\end{gathered}
$$

即上下极限相等,收敛.

</div>

### T4

<div class="cbox">

**8.** 设正数列 $\{a_n\}$. 证明: $\limsup_{n\to\infty} \sqrt[n]{a_n} \leqslant 1$ 的充分必要条件是: 对任意的 $l > 1$, 成立 $\lim_{n\to\infty} \frac{a_n}{l^n} = 0$.

</div>

<div class="pbox">

首先前推后:反证,假设 $\exists l>1,\lim_{n \to \infty} \dfrac{a_n}{l^n} =a\ne 0$.则 $\exists N,\forall n>N,a_n>\epsilon l^n,\limsup_{n \to \infty} \sqrt[ n ]{ a_n } \ge l>1$.

后推前,反证,假设 $\limsup_{n \to \infty} \sqrt[ n ]{ a_n }=A >1$,则存在子列$a_{p_n}$使得 $\sqrt[n]{a_{p_n}}>B,B\in (1,A)$,于是

$$
\begin{gathered}
\text{let } l=B,\limsup_{n \to \infty} \dfrac{a_n}{l^n} \ge \limsup_{n \to \infty} \dfrac{a_{p_n}}{l^n} >\limsup_{n \to \infty} \dfrac{B^n}{l^n} =1
\end{gathered}
$$

矛盾,得证.

</div>