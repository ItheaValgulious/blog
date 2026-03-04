---
title: Math Analysis Homework - Sem 2 Week 1
tags:
  - math
  - homework
  - math-analysis
date: 2026-03-02 14:20:07
---


# Math Analysis Homework - Sem 2 Week 1

## Class 1


### T1

<div class="cbox">

**2.** 讨论下列函数序列在指定区间上的一致收敛性:

(2) $f_n(x) = \arctan nx$, (i) $x \in (0, 1)$, (ii) $x \in (1, +\infty)$;

</div>

<div class='pbox'>

$$
\begin{gathered}
\lim_{n \to \infty} f_n(x) = f(x) = \dfrac \pi 2 \\
\end{gathered}
$$

(i):

$$
\begin{gathered}
\text{let } x=\dfrac 1n \\
|f_n(x_n)-f(x_n)|=\arctan 1-\dfrac \pi 2=C>0
\end{gathered}
$$

不一致收敛

(ii):

$$
\begin{gathered}
|f_n(x)-f(x)|=|\arctan nx-\dfrac \pi 2|<|\arctan n-\dfrac \pi 2|\to 0
\end{gathered}
$$

一致收敛

</div>

### T2

<div class="cbox">

**2.** 讨论下列函数序列在指定区间上的一致收敛性:
(4) $f_n(x) = \frac{x^n}{1+x^n}$, (i) $x \in (0, 1)$, (ii) $x \in (1, +\infty)$;

</div>

<div class='pbox'>

(i):

$$
\begin{gathered}
x\in (0,1) \Rightarrow 
\lim_{n \to \infty} f_n(x)=f(x)=0 \\
\text{let } x_n=1-\dfrac 1n \\
\lim_{n \to \infty} |f_n(x_n)-f(x_n)|= \lim_{n \to \infty} \dfrac{(1-\dfrac 1n)^n}{1+(1-\dfrac 1n)^n}= \dfrac{1}{e+1}\ne 0 
\end{gathered}
$$

不一致收敛

(ii):

$$
\begin{gathered}
x\in (1,+\infty) \Rightarrow \lim_{n \to \infty} f_n(x)=f(x)=1 \\
\text{let } x_n=1+\dfrac 1n \\
\lim_{n \to \infty} |f_n(x_n)-f(x_n)|= \lim_{n \to \infty} 1-\dfrac{(1+\dfrac 1n)^n}{1+(1+\dfrac 1n)^n}= \dfrac{1}{e+1}\ne 0 
\end{gathered}
$$

不一致收敛

</div>

### T3

<div class="cbox">

**2.** 讨论下列函数序列在指定区间上的一致收敛性:
(6) $f_n(x) = n\left(\sqrt{x+\frac{1}{n}}-\sqrt{x}\right)$, $x \in (0, +\infty)$.

</div>

<div class='pbox'>

$$
\begin{gathered}
\lim_{n \to \infty} f_n(x)=\lim_{n \to \infty}  n(\sqrt{x+\frac1n}-\sqrt x)=\lim_{n \to \infty} \dfrac1{\sqrt{x+\frac1n}+\sqrt x}=\dfrac{1}{2\sqrt x}=f(x) \\
|f_n-f|=\dfrac1{2\sqrt x}-\dfrac1{\sqrt x+\sqrt{x+\frac1n}} \\
=\dfrac{\sqrt{x+\frac1n}-\sqrt x}{2\sqrt x(\sqrt x+\sqrt{x+\frac1n})}  \\
=\dfrac{1}{2n\sqrt x(\sqrt x+\sqrt{x+\frac1n})^2} \\
>\dfrac{1}{2n\sqrt x(x+1)} \\
\text{let } x_n=\dfrac1{n^2} \\
\Rightarrow |f_n-f|>\dfrac{1}{2(1+\dfrac1{n^2})}>\dfrac14
\end{gathered}
$$

不一致收敛

</div>

### T4

<div class="cbox">

**4.** 证明函数项级数 $\sum_{n=1}^\infty \frac{1}{n} \left[ e^x - \left( 1 + \frac{x}{n} \right)^n \right]$ 在 $(0, +\infty)$ 上不一致收敛.

</div>

<div class='pbox'>

$$
\begin{gathered}
\text{let } a_n=\dfrac{1}{n} (e^x-\left(1+\dfrac{x}{n}\right)^n) \\
\sum_{i=n}^{2n} a_i \\
=\sum_{i=n}^{2n} \dfrac{1}{i} (e^x-\left(1+\dfrac{x}{i}\right)^i) \\
>\sum_{i=n}^{2n} \dfrac{1}{2n} (e^x-(1+\dfrac{x}{2n})^{2n}) \\
=\dfrac12(e^x-(1+\dfrac{x}{2n})^{2n}) \\
=g_n(x) \\
\text{let } x_n=2n \\
\lim_{n \to \infty} g_n(x_n)=\lim_{n \to \infty} \dfrac12 (e^{2n}-2^{2n})\ne 0
\end{gathered}
$$

不一致收敛.

</div>

### T5

<div class="cbox">

**6.** 设 $f(x)$ 在 $(a, b)$ 内有连续的导数 $f'(x)$, 且 $f_n(x) = n\left[ f\left(x+\frac{1}{n}\right) - f(x) \right]$.
求证: 在闭区间 $\alpha \le x \le \beta$ ($a < \alpha < \beta < b$) 上 $\{f_n(x)\}$ 一致收敛于 $f'(x)$.

</div>

<div class='pbox'>

$$
\begin{gathered}
f(x)\in C^1[a,b] \\
\xRightarrow{\text{ Lagrange Mean Value Theorem }}  \\
f_n(x)=f'(\xi_x),\xi_x\in [x,x+\frac1n] \\
\because f'(x)\in C[a,b] \\
f' \text{ is uniformly continuous on } [a,b] \\
\forall \epsilon>0,\exists \delta, \\ s.t.\\ 
\forall |x_1-x_2|<\delta,|f'(x_1)-f'(x_2)|<\epsilon \\
\text{let } n>\dfrac1\epsilon \\
\Rightarrow \forall x,|f_n(x)-f(x)|=|f'(\xi_x)-f'(x)|<\epsilon \\
\text{Q.E.D}
\end{gathered}
$$

</div>

### T6

<div class="cbox">

**9.** 设 $\varphi(x)$ 为 $[0, 1]$ 上的连续函数. 对任意的 $n \in \mathbb{N}$, 令
$$f_n(x) = \int_0^x \varphi(t^n)\mathrm{d}t, \quad x \in [0, 1].$$
证明: $\{f_n(x)\}$ 在 $[0, 1]$ 上一致收敛于 $x\varphi(0)$.

</div>

<div class='pbox'>

$$
\begin{gathered}
\text{if } x<1: \\
\lim_{n \to \infty} \int_0^x \varphi(t^n)dt=\lim_{n \to \infty}  x\varphi(\xi(n)^n),\xi(n) \in [0,x] \\
\because 0<\xi^n(n)<x^n \\
\therefore \lim_{n \to \infty} \xi^n(n)=0 \\
\lim_{n \to \infty} x\varphi(\xi^n(n))=x\varphi(0)
\end{gathered}
$$

$$
\begin{gathered}
\text{if } x=1: \\
\lim_{n \to \infty} \int_0^1 \varphi(t^n)dt \\
=\lim_{n \to \infty} \int_0^{1-\frac1{\ln n}} \varphi(t^n)dt + \int_{1-\frac1{\ln n}}^1 \varphi(t^n)dt \\
=\lim_{n \to \infty} (1-\dfrac{1}{\ln n})\varphi(\xi^n)+\lim_{n \to \infty} \dfrac{1}{\ln n} \varphi(\xi_2^n) \\
=A+B \\
\because \varphi\in C[0,1] \\
\therefore \exists M,|\varphi|<M \\
\therefore B\le \lim_{n \to \infty} \dfrac{1}{\ln n}M=0 \Rightarrow B=0 \\
\lim_{n \to \infty} (1-\dfrac1{\ln n})\varphi(\xi^n(n)) \\
=\lim_{n \to \infty} (1-\dfrac1{\ln n}) \cdot \lim_{n \to \infty}  \varphi(\xi^n(n)) \\
=\varphi(0) \\
\end{gathered}
$$

然后用课上的结论,$f_n$导数有界,所以收敛变成一致收敛,做完了.

</div>

## Class 2

### T1

<div class="cbox">

**10.** 判别下列级数的一致收敛性:
(3) $\sum_{n=1}^{\infty} \frac{nx}{(1+x)(1+2x)\cdots(1+nx)}$, 其中 (i) $0 < x \leqslant l$, (ii) $0 < l \leqslant x < +\infty$.

</div>

<div class='pbox'>

$$
\begin{gathered}
u_n(x)=\dfrac{nx}{\prod_{i=1}^n (1+ix)}
\end{gathered}
$$

(i):

令$x_{n}=\dfrac4{n^2}$,则:

$$
\begin{gathered}
\prod_{i=1}^{n} (1+ix_n)\le (1+\dfrac4{n})^n\le e^4 \\
\Rightarrow u_{n}(x_n)\ge \dfrac4{e^4n}
\end{gathered}
$$

因为$\dfrac{u_n}{u_{n-1}}=\dfrac n{(n-1)(1+nx)}$,得到$x<\dfrac1{n(n-1)}$时$u_n(x)$增加,反之减小.

于是可得$u_n(x_n)<u_{n-1}(x_n)<\ldots<u_{\lfloor n/2\rfloor}(x_{n})$.

于是$\sum_{i=1}^n u_i(x)>\sum_{i=\lfloor n/2\rfloor}^n u_i(x)\ge \dfrac2{e^4}$.

于是由柯西条件,不一致收敛.

(ii):

$$
\begin{gathered}
\text{when } x\ge l: \\
u_n(x)=\dfrac{nx}{1+nx} \cdot \dfrac1{\prod_{i=1}^n (1+ix)}
\end{gathered}
$$

其中第一项一致有界$1$,第二项显然有优级数$(1+l)^{-n}$一致收敛,由阿贝尔判别法知一致收敛.


</div>

### T2

<div class="cbox">

**11.** 设 $\{a_n\}$ 为单调递减正数列, 且 $\sum_{n=1}^{\infty} a_n \sin nx$ 在 $[0, \pi]$ 上一致收敛. 证明: $\lim_{n\to\infty} na_n = 0$.

</div>

<div class='pbox'>

因为一致收敛,由柯西条件,可知

$$
\begin{gathered}
\forall n,\{x_n\},|\sum_{i=n}^{2n} a_i\sin(ix_i)|\to 0 \\
\text{let } x_n=\dfrac1{2n},n>1000 \\
\Rightarrow \sin(nx_n) \text{ is increasing with } n,\sin(nx_n)>0 \\
|\sum_{i=n}^{2n} a_i\sin(ix_i)| \\
=\sum_{i=n}^{2n} a_i\sin(ix_i) \\
\ge \sum_{i=n}^{2n} a_{2n}\sin(\dfrac12) \\
=2na_{2n} \dfrac{\sin\frac12}{2}\to 0
\end{gathered}
$$

偶数项收敛到$0$,奇数项小于其前一项也收敛到$0$,得证.

</div>

### T3

<div class="cbox">

**13.** 判断下列函数项级数的一致收敛性:
(2) $\sum_{n=2}^{\infty} \frac{(-1)^n}{n+\sin x}$, $-\infty < x < +\infty$;

</div>

<div class='pbox'>

$(-1)^n$部分和有界,$\dfrac1{n+\sin x}$单调递减且一致收敛到$0$,由迪利克雷判别法知一致收敛.

</div>

### T4

<div class="cbox">

**13.** 判断下列函数项级数的一致收敛性:
(5) $\sum_{n=1}^{\infty} \frac{(-1)^{[\sqrt{n}]}}{\sqrt{n(n+x)}}$, $0 < x < +\infty$;

</div>

<div class='pbox'>

$$
\begin{gathered}
=\sum_{k=1}^\infty (-1)^k\sum_{n=k^2}^{(k+1)^2-1} \dfrac{1}{\sqrt{n(n+x)}} \\
\end{gathered}
$$

经过巨量的计算我们发现后面那一坨是单调的.但我觉得我们还是写个正常的东西吧.

直接弄成

$$
\begin{gathered}
\sum _{n = 1} ^{\infty}  \dfrac{(-1)^{[\sqrt{n}]}}n\dfrac1{\sqrt{1(1+\dfrac xn)}}
\end{gathered}
$$

第二项单调且有界,只需证第一项部分和收敛.

考虑

$$
\begin{gathered}
\sum _{k=1}^\infty (-1)^k \sum _{n = k^2} ^{k^2+2k}\dfrac{1}{n}  \\
\dfrac1n\in [\ln(n+1)-\ln(n),\ln(n)-\ln(n-1)] \\
\sum _{n = k^2} ^{k^2+2k}\dfrac{1}{n}\in [\ln((k+1)^2)-\ln(k^2),\ln(k^2+2k)-\ln(k^2-1)] \\
\end{gathered}
$$

因为

$$
\begin{gathered}
\ln(k^2+2k)-\ln(k^2-1)\le \ln(k^2)-\ln((k-1)^2) \\
\Leftrightarrow (k^2+2k)(k-1)^2\le k^2(k^2-1)
\end{gathered}
$$

比较系数得成立,于是单调.

于是由阿贝尔判别法知一致收敛.


</div>

### T5

<div class="cbox">

**14.** 在区间 $[0, 1]$ 上, 定义
$u_n(x) = \begin{cases} \dfrac1n, & x = \frac{1}{n}, \\ 0, & x \neq \frac{1}{n}. \end{cases}$

证明:
- $\sum_{n=1}^\infty u_n(\dfrac1n)$发散.
- $\sum_{n=1}^\infty u_n(x)$在$[0,1]$一致收敛,且没有优级数.

</div>

<div class='pbox'>

$$
\begin{gathered}
\sum _{n = 1} ^{+\infty} u_n(\dfrac1n)=\sum_{n=1}^\infty \dfrac1n=+\infty \\
|\sum_{n=N}^\infty u_n(x)|= \begin{cases}
\dfrac1k,\exists k\ge N,x=\dfrac1k \\
0,\text{otherwise}
\end{cases} \\
\le \dfrac1N\to 0
\end{gathered}
$$

一致收敛.

设$a_n$为$u_n(x)$的优级数,则$a_n\ge u_n(\dfrac1n)=\dfrac1n$,则$a_n$发散,故不存在优级数.

</div>

### T6

<div class="cbox">

**15.** 设级数 $\sum_{n=1}^{\infty} a_n$ 收敛, 证明: 函数项级数 $\sum_{n=1}^{\infty} a_n e^{-nx}$ 在 $[0, +\infty)$ 内一致收敛.

</div>

<div class='pbox'>

$\sum_{n=1}^\infty a_n$(常函数)一致收敛,$e^{-nx}$单调下降且一致有界$1$,由阿贝尔判别法知一致收敛.

</div>

### T7

<div class="cbox">

**16.** 设级数 $\sum_{n=1}^{\infty} \frac{1}{|a_n|}$ 收敛. 证明: 函数项级数 $\sum_{n=1}^{\infty} \frac{1}{x-a_n}$ 在不包含点 $a_n (n=1, 2, \cdots)$ 的任何有界闭集上绝对一致收敛.

</div>

<div class='pbox'>

显然$a_n\to \infty$.因为有界,设有界闭集$D$满足$M=\sup D$,则$\exists N,n>N\Rightarrow |a_n|>2M$.

于是

$$
\begin{gathered}
\forall n\ge N,|a_n-x|\ge \dfrac{a_n}2 \\
\sum _{n = N} ^{\infty}  |\dfrac{1}{x-a_n}|\le \dfrac1{2|a_n|}
\end{gathered}
$$

则$\sum_n \dfrac1{2|a_n|}$为优级数,由优级数判别法知一致收敛.

</div>

### T8

<div class="cbox">

**17.** 讨论下列函数项级数的一致收敛性:
(1) $\sum_{n=2}^{\infty} \ln \left( 1 + \frac{x}{n\ln^2 n} \right)$, $x \in [a, b]$, $a > 0$;

</div>

<div class='pbox'>

$$
\begin{gathered}
|\ln(1+\dfrac{x}{n\ln^2 n})|\le \ln(1+\dfrac{b}{n\ln^2 n} )\le \dfrac{b}{n\ln^2 n}=c_n \\
\sum_{n=2}^\infty c_n,\int_2^\infty \dfrac1{x\ln^2 x}dx=\int_{\ln 2}^\infty \dfrac1{x^2}dx<\infty \text{同敛散}  
\end{gathered}
$$

所以$c_n$收敛,由优级数判别法知一致收敛

</div>