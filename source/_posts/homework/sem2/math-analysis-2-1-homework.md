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
\\
\text{Q.E.D}
\end{gathered}
$$

</div>