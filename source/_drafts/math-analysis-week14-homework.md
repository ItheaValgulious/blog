---
title: Math Analysis Homework - Week 14
tags: [math,math-analysis,homework]
---

# Math Analysis Homework - Week 14

## Class 1

### T1

<div class="cbox">

2. 讨论下列无穷乘积的敛散性:
(2) $\prod_{n=1}^{\infty} \sqrt[n]{1 + \frac{1}{n}};$

</div>

<div class="pbox">

敛散性等价于

$$
\begin{gathered}
\sum_{n=1}^\infty \dfrac{\ln(1+\dfrac1n)}n \\
\because \lim_{n \to \infty}  \dfrac{\dfrac{\ln(1+\dfrac{1}{n} )}{n} }{\dfrac{1}{n^2} } =1,\sum _{n = 1} ^{\infty}  \dfrac{1}{n^2} <\infty \\
\xRightarrow{\text{ Comparison Test }}  \text{convergent} 
\end{gathered}
$$

</div>

### T2

<div class="cbox">

2. 讨论下列无穷乘积的敛散性:
(4) $\prod_{n=2}^{\infty} \left(\frac{n^2 - 1}{n^2 + 1}\right)^p \ (p \in \mathbb{R});$

</div>

<div class="pbox">

$$
\begin{gathered}
\ln(\prod_{n=2}^\infty (\dfrac{n^2-1}{n^2+1} )^p) \\
=p\sum _{n = 2} ^{\infty}  \ln(1+\dfrac{2}{n^2+1} ) \\
\because \lim_{n \to \infty}  \dfrac{\ln(1+\dfrac{2}{n^2+1} )}{\dfrac{1}{n^2} } =1,\sum _{n = 1} ^{\infty}  \dfrac{1}{n^2} <\infty \\
\xRightarrow{\text{ Comparison Test }} \text{convergent} 
\end{gathered}
$$

</div>

### T3

<div class="cbox">

3. 设数列 $\{a_n\}$, 其中
$$a_n = \begin{cases} -\frac{1}{\sqrt{k}}, & n = 2k - 1, \\ \frac{1}{\sqrt{k}} + \frac{1}{k} + \frac{1}{k\sqrt{k}}, & n = 2k. \end{cases}$$
证明: $\sum_{n=1}^{\infty} a_n$ 与 $\sum_{n=1}^{\infty} a_n^2$ 都发散, 但是 $\prod_{n=1}^{\infty} (1+a_n)$ 收敛.

</div>

<div class="pbox">

$$
\begin{gathered}
\sum _{n = 1} ^{\infty}  a_n^2 \\
=\sum _{n = 1} ^{\infty}  (\dfrac{1}{n} +(\dfrac{1}{\sqrt n} +\dfrac{1}{n} +\dfrac{1}{n^{\frac23}} ^2))
>\sum _{n = 1} ^{\infty}  \dfrac{1}{n}  \\
=\infty
\end{gathered}
$$

$$
\begin{gathered}
\sum _{n = 1} ^{\infty}  a_n=\sum _{n = 1} ^{\infty}  -\dfrac{1}{\sqrt{n}} +\dfrac{1}{\sqrt n} +\dfrac{1}{n} +\dfrac{1}{n\sqrt n}  \\
>\sum _{n = 1} ^{\infty}  \dfrac{1}{n} =\infty \\
\end{gathered}
$$

$$
\begin{gathered}
\ln(\prod _{n = 1} ^{\infty}  (1+a_n)) \\
\ln(\prod _{n = 1} ^{\infty}  (1-\dfrac{1}{\sqrt n} )(1+\dfrac{1}{\sqrt{n}} +\dfrac{1}{n} +\dfrac{1}{n\sqrt n} )) \\
=\ln(\prod _{n=1}^{\infty} (1-\dfrac{1}{n^2} )) \\
=\sum _{n = 1} ^{\infty} \ln(1-\dfrac{1}{n^2} ) \\
\sim -\sum _{n = 1} ^{\infty}  \dfrac{1}{n^2} >-\infty
\end{gathered}
$$

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