---
title: Math Analysis Homework - Sem 2 Week 2
tags: [math,math-analysis,homework]
---
# Math Analysis Homework - Sem 2 Week 2

## Class 1

### T1

<div class="cbox">

**2.** 设级数 $\sum_{n=1}^{\infty} a_n$ 收敛, 证明
$$\lim_{x \to 0^+} \sum_{n=1}^{\infty} \frac{a_n}{n^x} = \sum_{n=1}^{\infty} a_n.$$

</div>

<div class="pbox">

显然每一项$u_n=\dfrac{a_n}{n^x}$是连续的.

又因为$a_n$部分和收敛,$\dfrac1{n^x}$单调减且一直有界,由阿贝尔判别法知一致收敛.

于是极限函数也连续,即:

$$
\begin{gathered}
\lim_{x \to 0} (\sum_n u_n)(x)=(\sum_n u_n)(0)=\sum _{n = 1} ^{\infty}  a_n
\end{gathered}
$$

</div>

### T2

<div class="cbox">

**3.** 证明级数 $\sum_{n=1}^{\infty} (-1)^n x^n (1-x)$ 在 $[0, 1]$ 上绝对收敛, 一致收敛, 但不绝对一致收敛.

</div>

<div class="pbox">

$\forall x,\sum_{n=1}^\infty |(-1)^nx^n(1-x)|=\sum _{n = 1} ^{\infty} x^n(1-x)$在$(0,1)$由等比数列知收敛,在端点处验证易证收敛.

$(-1)^n$部分和有界,$x^n(1-x)$单调递减且趋近于$0$,由迪利克雷判别法知已知收敛.

$$
\begin{gathered}
\text{let } x_n=\dfrac n{n+1} \\
\Rightarrow 
|\sum_{i=n}^{2n} x^i(1-x)| \\
\ge \sum _{i = n} ^{2n}  x_{2n}^{2n}(1-x_{2n}) \\
=(n+1) (1-\dfrac1{2n+1})^{2n}\dfrac1{2n+1} \\
\to \dfrac{1}{2e} 
\end{gathered}
$$

由柯西判别法知不绝对收敛.

</div>

### T3

<div class="cbox">

**4.** 讨论下列级数的收敛性和一致收敛性、和函数的连续性:
(2) $f(x) = \sum_{n=1}^{\infty} \frac{x + n(-1)^n}{x^2 + n^2}, x \in (-\infty, +\infty).$

</div>

<div class="pbox">

$$
\begin{gathered}
u_n=\dfrac{x+n(-1)^n}{x^2+n^2}  \\
\text{when } n>2x ,|u_n|>\dfrac{n}{4n^2}=\dfrac1{4n} \\
\sum \dfrac1{4n}=\infty
\end{gathered}
$$

所以不绝对收敛.

$$
\begin{gathered}
u_{2n-1}+u_{2n} \\
=\dfrac{x-(2n-1)}{x^2+(2n-1)^2} +\dfrac{x+2n}{x^2+(2n)^2} \\
\le \dfrac{2x+1}{x^2+(2n-1)^2}=a_n   \\
u_{2n}+u_{2n+1} \\
=\dfrac{x+2n}{x^2+(2n)^2} +\dfrac{x-(2n+1)}{x^2+(2n+1)^2} \\
\ge \dfrac{2x-1}{x^2+(2n+1)^2}=b_n
\end{gathered}
$$

对任意$x$,$f(x)\in [b_n,a_n]$,而$a_n,b_n$收敛,且原级数通项一致收敛到$0$,所以$f$收敛.

再看$b_n$:

$$
\begin{gathered}
\sum _{i=n} ^{2n}  b_i \\
=\sum _{i=n} ^{2n}  \dfrac{2x-1}{x^2+(2i+1)^2} \\
\ge n \dfrac{2x-1}{x^2+(4n+1)^2} \\
=\dfrac{2x-1}{x} \dfrac{n}{x+\dfrac{(4n+1)^2}{x} } \\
\xlongequal{ x=4n+1 } \dfrac{2x-1}{x} \dfrac{n}{2(4n+1)}  \\
\to \dfrac{1}{4} \ne 0
\end{gathered}
$$

不一致收敛.

对任意闭区间$[-L,L]$,显然有$a_n\le \dfrac{2L+1}{(2n-1)^2}$,由优级数判别法知原级数内闭一致收敛,从而和函数连续.

</div>

### T4

<div class="cbox">

**5.** 问参数 $\alpha$ 取何值时, $f_n(x) = n^\alpha x e^{-nx} \quad (n=1, 2, \cdots)$
(1) 在 $[0, 1]$ 上收敛?
(2) 在 $[0, 1]$ 上一致收敛?
(3) $\lim_{n \to \infty} \int_0^1 f_n(x) dx$ 可在积分符号下取极限?

</div>

<div class="pbox">

(1):

任意$\alpha\in R$均收敛,$f_n\to 0$.

(2):

$$
\begin{gathered}
f_n'(x)= n^\alpha e^{-nx}(1-nx)\\
\sup_x |f_n(x)-0|=f_n(\dfrac1n)=e^{-1}n^{\alpha-1}
\end{gathered}
$$

所以$\alpha<1$时一致收敛.

(3):

$$
\begin{gathered}
\int_0^1 f_n(x)dx \\
=n^\alpha\dfrac1n(-x-\dfrac{1}n)e^{-nx}|_0^1 \\
=n^{\alpha-1} (\dfrac1n-\dfrac{n+1}ne^{-n}) \\
=n^{\alpha-2}(1-(n+1)e^{-n})
\end{gathered}
$$

所以$\alpha<2$时可取极限.


</div>