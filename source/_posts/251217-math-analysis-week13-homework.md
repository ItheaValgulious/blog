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

于是$p\in (-\infty,\dfrac12)$发散,$(\dfrac12,1]$条件收敛,$(1,+\infty)$绝对收敛.

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