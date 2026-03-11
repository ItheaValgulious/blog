---
title: Math Analysis Homework - Sem 2 Week 2
tags:
  - math
  - math-analysis
  - homework
date: 2026-03-09 20:12:07
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

又因为$a_n$部分和收敛,$\dfrac1{n^x}$单调减且一致有界,由阿贝尔判别法知一致收敛.

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

## Class 2  

### T1

<div class="cbox">

**6.** 证明 $f_n(x) = nx(1 - x)^n \ (n = 1, 2, \cdots)$ 在 $[0, 1]$ 上收敛而不一致收敛，但
$$\int_0^1 (\lim_{n\to\infty} f_n(x))dx = \lim_{n\to\infty} \int_0^1 f_n(x)dx.$$

</div>

<div class="pbox">

收敛:
- $x\in \{ 0,1 \} :f_n(x)=0\to 0$
- $\forall x\in (0,1),\exists (1-x)<A<1,f_n(x)=nxA^n\to 0$
所以$f_n\to 0$.

不一致收敛:取$x=\dfrac1n,f_n(x)=(1-\dfrac1n)^n\to \dfrac{1}{e}\ne 0$.

积分:$\int_0^1 f_n(x)dx=n\int_0^1 x^n(1-x)dx=\dfrac{n}{(n+1)(n+2)}\to 0=\int_0^1 0dx$.

</div>

### T2

<div class="cbox">

**8.** 设函数列 $\{f_n(x)\}$ 在 $\mathbb{R}$ 上一致连续且一致收敛于 $f(x)$。证明 $f(x)$ 在 $\mathbb{R}$ 上也一致连续。

</div>

<div class="pbox">

$$
\begin{gathered}
\begin{cases}
\forall \epsilon_1>0,\exists N \ s.t.\ 
\forall n>N,|f_n(x)-f(x)|<\epsilon_1 \\
\forall \epsilon_2>0,\exists \delta>0 \ s.t.\
\forall x,y\in \mathbb{R},|x-y|<\delta,|f_n(x)-f_n(y)|<\epsilon_2 \\
\text{let } \epsilon_1=\epsilon_2=\dfrac \epsilon 3 \\
\end{cases} \\
\Rightarrow \forall x,y\in \mathbb{R},|x-y|<\delta \\
|f(x)-f(y)|\le |f(x)-f_n(x)|+|f_n(x)-f_n(y)|+|f_n(y)-f(y)| \\
<\epsilon_1+\epsilon_2+\epsilon_1=\epsilon
\end{gathered}
$$

</div>

### T3

<div class="cbox">

**9.** 证明 $\sum_{n=1}^\infty (-1)^n \frac{1}{n^x}$ 在 $(0, +\infty)$ 上收敛而不一致收敛，但其和函数在 $(0, +\infty)$ 内连续，且有各阶连续导函数。

</div>

<div class="pbox">

收敛:$\forall x,\sum_{n=1}^\infty (-1)^n\dfrac1{n^x}$逐项递减且交错,由莱布尼茨判别法知收敛.

不一致收敛:$x=\frac1n$,$|(-1)^n \dfrac1{n^{\frac1n}}|\to 1\ne 0$

$\forall k\in Z,\forall [a,b]\subset (0,+\infty)$,$((-1)^n\dfrac1{n^x})^{(k)}=(-1)^{n+k}\dfrac1{n^x}\ln^k n$,$(-1)^{n+k}$部分和一致有界,$\dfrac{\ln^{n+k}}{n^x}$一致收敛到$0$,由迪利克雷判别法知在任意闭区间内一致收敛,从而任意阶导数内闭一致收敛.

于是和函数$f\in C^\infty(0,+\infty)$



</div>

### T4

<div class="cbox">

**11.** 设 $f(x) = \sum_{n=1}^\infty \sqrt{n}xe^{-nx^2}, x \in (0, +\infty)$。证明：

(1) $\sum_{n=1}^\infty \sqrt{n}xe^{-nx^2}$ 在 $(0, +\infty)$ 内收敛但不一致收敛；

(2) $f(x)$ 在 $(0, +\infty)$ 内连续；

(3) $\sum_{n=1}^\infty \sqrt{n}xe^{-nx^2}$ 在 $(0, +\infty)$ 内可逐项求导，且有连续的导函数。

</div>

<div class="pbox">

$$
\begin{gathered}
a_n=\sqrt{n}xe^{-nx^2} \\
\end{gathered}
$$

收敛:$\lim_{n \to \infty} a_n^{\frac1n}=\lim_{n \to \infty} ^{-x^2}n^{\frac1{2n}}=e^{-x^2}<1$,由比较判别法知收敛.

不一致收敛:取$x=n^{-\frac12}$,则$a_n=\frac1e\ne 0$,由柯西条件知不一致收敛.

连续:$\forall [l,r]\subset (0,+\infty)$,$a_n'=2x\sqrt ne^{-nx^2}(1-nx)$,则当$\dfrac1n<l<r$时,$a_n(x)$在$[l,r]$递减,$a_n(x)\le a_n(l)=2l\sqrt{n}le^{-nl^2}$.由优级数判别法知一致收敛.所以$f$内闭一致收敛,且$f_n$连续,故$f$连续.

$a_n'=2x\sqrt ne^{-nx^2}(1-nx)$,$a_n''=2nx\sqrt{n}e^{-nx^2}(2nx^2-3)$,对任意$[l,r]\subset (0,+\infty)$,当$n>\dfrac{3}{2l^2}$时$a_n''>0,a_n'$单调增加,$a_n'(x)\le |a_n'(r)|=|2r\sqrt{n}re^{-nr^2}(1-nr)|$收敛,由优级数判别法知一致收敛,所以$f'$内闭一致收敛,且$f_n'$连续,故$f'$连续.

</div>

### T5

<div class="cbox">

**12.** 设 $f_n(x) \in C[a, b] (n \in \mathbb{N})$ 且 $\{f_n(x)\}$ 一致收敛于 $f(x), x \in [a, b]$, 又设 $f(x)$ 在 $[a, b]$ 上无零点。证明：

(1) 当 $n$ 充分大时，$f_n(x)$ 在 $[a, b]$ 上也无零点；

(2) $\{\frac{1}{f_n(x)}\}$ 在 $[a, b]$ 上一致收敛于 $\frac{1}{f(x)}$。

</div>

<div class="pbox">

(1): 

$$
\begin{gathered}
\begin{cases}
f_n(x)\in C[a,b] \\
f_n(x)\rightrightarrows f
\end{cases}
\\
\Rightarrow f\in C[a,b] \\
\Rightarrow |f|\in C[a,b] \\
\because \not \exists x,f(x)=0 \\
\therefore \exists x_0 \ s.t.\ 
|f(x)|\ge |f(x_0)|>0
\text{let } \epsilon=\dfrac{|f(x_0)|}2 \\
f_n(x)\rightrightarrows f \\
\Rightarrow \exists N \ s.t.\ 
\forall n>N,|f_n(x)-f(x)|<\epsilon \\
\Rightarrow |f_n(x)|\ge |f(x)|-\epsilon>0
\end{gathered}
$$

于是$f_n$无零点

(2):

$$
\begin{gathered}
f(x)\in C[a,b] \Rightarrow \exists M,m<|f(x)|<M \\
f_n(x)\rightrightarrows f \Rightarrow 
\forall \epsilon_1>0,\exists N \ s.t.\ 
\forall n>N,|f_n(x)-f(x)|<\epsilon_1 \\
\therefore \forall x,|\dfrac{1}{f_n(x)}-\dfrac{1}{f(x)}| \\
=\dfrac{|f_n(x)-f(x)|}{|f_n(x)||f(x)|} \\
<\dfrac{\epsilon_1}{m(m-\epsilon_1)} \\
\end{gathered}
$$

所以$\forall \epsilon$,取$\epsilon_1=10^{-5}m^2\epsilon$,则$\forall x,\dfrac{1}{f_n(x)}-\dfrac{1}{f(x)}| < \dfrac{\epsilon_1}{m(m-\epsilon_1)}<\epsilon$.

</div>

### T6

<div class="cbox">

**13.** 设 $f_n(x)$ 在 $[a, b]$ 上满足条件：存在 $K > 0$ 使得
$$|f_n(x) - f_n(y)| \le K|x - y|, x, y \in [a, b], n = 1, 2, \cdots,$$
且 $\{f_n(x)\}$ 在 $[a, b]$ 上点态收敛于 $f(x)$。求证：$\{f_n(x)\}$ 在 $[a, b]$ 上一致收敛于 $f(x)$。

</div>

<div class="pbox">

这不是好几天课上的原题吗?甚至不用Lipschitz条件,一致连续就够了的.

如果一致连续,对任意$\epsilon$,对每个点$x$取一个小邻域使得其中函数值差小于$\dfrac \epsilon2$,又因为点态收敛可以取$N$使得$n>N$时$|f_n(x)-f(x)|<\dfrac\epsilon2$.然后用这些小邻域有限覆盖,在最终的有限个小邻域中取$N$的最大值即为$N$,一致收敛.

</div>

### T7

<div class="cbox">

**14.** 设 $f(x) = \sum_{n=1}^\infty \frac{x^n \cos\frac{n\pi}{x}}{(1+2x)^n}$，求 $\lim_{x\to 1} f(x)$ 及 $\lim_{x\to +\infty} f(x)$。

</div>

<div class="pbox">

不妨设$x\in [\frac12,\infty)$

(1):

先证一致收敛:

$$
\begin{gathered}
\dfrac{x^n\cos\frac{n\pi}{x}}{(1+2x)^n} \le \dfrac{x^n}{(1+2x)^n} \le \left(\dfrac{x}{1+2x}\right)^n \le 2^{-n}
\end{gathered}
$$

优级数判别法知一致收敛.又因为$f_n$连续所以$f$连续,所以:

$$
\begin{gathered}
\lim_{x \to 1} f(x) = \sum_{n=1}^\infty \dfrac{1}{(-3)^n} \\
=-\dfrac{1}{4} 
\end{gathered}
$$

(2):

考虑 $\lim_{x \to 0}  f(\dfrac1x)$:

$$
\begin{gathered}
f(\frac1x)=\sum_{n=1}^\infty \dfrac{\cos n\pi x}{(x+2)^n} \\
\end{gathered}
$$

显然在$(0,\infty)$上仍然能用优级数判别法证一致收敛

于是$f(\frac1x)|_{x=0}=\sum_{n=1}^\infty \dfrac{1}{(0+2)^n}=1$

</div>

### T8

<div class="cbox">

**16.** 设函数 $f(x)$ 在 $\mathbb{R}$ 上具有任意阶导数，且不恒为 $0$，又
$$|f^{(n)}(x) - f^{(n-1)}(x)| \le \frac{1}{n^2}, (n \in \mathbb{N}, x \in \mathbb{R}).$$
证明：$\{f^{(n)}(x)\}$ 在 $\mathbb{R}$ 上一致收敛于 $F(x) = ce^x, (x \in \mathbb{R})$，其中 $c$ 为常数。

</div>

<div class="pbox">

由柯西,$\forall n>m$,

$$
\begin{gathered}
|f^{(n)}-f^{(m)}|\le \sum_{i=m+1}^n |f^{(i)}-f^{(i-1)}| \\
\le \sum_{i=m+1}^n \dfrac{1}{i^2} \\
\le \dfrac1{n-1}
\end{gathered}
$$

所以一致收敛.

$$
\begin{gathered}
|f^{(n)}-f^{(n+1)}|\le \epsilon_n=\dfrac{1}{n^2} \\
|(e^{-x}f^{(n)})'|\le \epsilon_n e^{-x} \\
|e^{-x}f^{(n)}(x)-e^{-x}f^{(n)}(y)|\le \epsilon_n |e^{-x}-e^{-y}|
\end{gathered}
$$

设$G(x)=\lim_{n\to +\infty} f^{(n)}(x)$

固定$x,y$,取$n\to +\infty$,得到$|e^{-x}G(x)-e^{-x}G(y)|=0$.于是$e^{-x}f^{(n)}$逐点收敛到常数,$f^{(n)}$收敛到$ce^x$,且一致收敛.

</div>