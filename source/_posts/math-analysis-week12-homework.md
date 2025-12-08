---
title: Math Analysis Homework - Week 12
tags:
  - math-analysis
  - math
  - homework
date: 2025-12-08 15:48:23
---


# Math Analysis Homework - Week 12

## Class 1

### T1

<div class="cbox">

$$ \int_{-1}^1 \frac{\arccos x}{\sqrt{1-x^2}}\mathrm{d}x $$

</div>

<div class='pbox'>

$$
\begin{gathered}
\text{let } x=\cos t \\
Ans=\int_{0}^{\pi} \dfrac{t}{\sin t} (-\sin t)dt \\
= \int_0^\pi tdt \\
=\dfrac{\pi^2}{2} 
\end{gathered}
$$

</div>



### T2

<div class="cbox">

$$ \int_0^{\frac{\pi}{2}} (\sqrt{\tan x} + \sqrt{\cot x})\mathrm{d}x $$

</div>

<div class='pbox'>

$$
\begin{gathered}
=2\int_0^{\frac\pi2} \sqrt {\tan x}dx \\
\xlongequal{ t=\sqrt{\tan x} } 4\int_0^{+\infty} \dfrac{t^2}{t^4+1}dt \\ 
=4\int_0^1 \dfrac{t^2+1}{t^4+1} dt \\
=4\int_0^1 \dfrac{1+\dfrac{1}{t^2} }{t^2+\dfrac{1}{t^2} } dt \\
\xlongequal{ s=t-\frac{1}{t}  }  4\int_{-\infty}^0 \dfrac{ds}{s^2+2} \\
\xlongequal{ s=\sqrt 2 \tan u } 4\int_{-\frac\pi2}^0 \dfrac{\sqrt 2 \sec^2 u}{2\sec^2 u} du \\
=\sqrt 2\pi
\end{gathered}
$$

</div>



### T3

<div class="cbox">

判断下列反常积分的敛散性：
$$ (1) \int_0^{\frac{\pi}{2}} \frac{1}{\sin^\alpha x \cos^\beta x}\mathrm{d}x \quad (\alpha > 0, \beta > 0) $$

</div>

<div class='pbox'>

$$
\begin{gathered}
x\to 0 \Rightarrow \dfrac{1}{\sin^\alpha x\cos^\beta x}\sim\dfrac{1}{x^\alpha} \\
x\to \frac\pi2 \Rightarrow t\to 0,\int_0^{\frac\pi2}\dfrac{1}{\sin^\alpha x\cos^\beta x} dx=\int_0^{\frac\pi2 }\dfrac{1}{\cos^\alpha t\sin^\beta t}dt \\
\Rightarrow \dfrac{1}{\sin^\beta x\cos^\alpha x} \sim \dfrac{1}{t^\beta}   \\
\Rightarrow \begin{cases}
\text{convergent} ,\alpha,\beta<1 \\
\text{not convergent} ,\max (\alpha,\beta) \ge 1
\end{cases}

\end{gathered}
$$

</div>

### T4

<div class="cbox">

$$ (5) \int_0^{+\infty} \frac{x|\ln x|^p}{x^2+1}\mathrm{d}x \quad (p \in \mathbb{R}) $$

</div>

<div class='pbox'>

$$
\begin{gathered}
=\int_0^{+\infty} \dfrac{\vert \ln x\vert^p}{x(1+x^2)} dx \\
\int_0^{1} \dfrac{\vert \ln x\vert^p}{x(1+x^2)} dx \\
+\int_1^{+\infty} \dfrac{\vert \ln x\vert^p}{x(1+x^2)} dx \\
=I_1+I_2 \\
\exists N,n>N \Rightarrow I_2=\int_1^{+\infty} \dfrac{\vert \ln p \vert ^p}{x(1+x^2)} dx<\int_1^{+\infty} \dfrac{1}{x^2} dx<\infty \\
\text{for } I_1,x\to 0,1+x^2 \to 1\\
\int_0^1 \dfrac{\vert \ln x \vert ^p}{x}dx \\
=\int_0^\infty t^pdt  \\
=\infty
\end{gathered}
$$

因此发散

</div>



### T5

<div class="cbox">

$$ (7) \int_0^{+\infty} \frac{\sin x(1-\cos x)}{x^p}\mathrm{d}x \quad (p \in \mathbb{R}) $$

</div>

<div class='pbox'>

$$
\begin{gathered}
x\to 0 \Rightarrow \dfrac{\sin x(1-\cos x)}{x^p} \sim \dfrac12x^{3-p}, \\
\text{convergence } \Leftrightarrow p<4 \\
x\to \infty \Rightarrow \int_1^{+\infty}\dfrac{\sin x(1-\cos x)}{x^p} dx \\
=\int_1^{+\infty}{\left( \dfrac{\sin x}{x^p} -\dfrac{2^{p-1}\sin(2x)}{(2x)^p}  \right)}  dx \\
\begin{cases}
<\infty,p> 0 \\
=\infty,p\le 0
\end{cases}

\end{gathered}
$$

所以$p\in (0,4)$收敛,$p\in (-\infty,0]\cup [4,+\infty)$发散.

</div>



### T6

<div class="cbox">

3. 设 $f(x)$ 在每个有限区间 $[a, b]$ 上可积，且 $\lim_{x\to+\infty}f(x)=A, \lim_{x\to-\infty}f(x)=B$.
证明：对任意 $a > 0$, 反常积分 $\int_{-\infty}^{+\infty}(f(x+a)-f(x))\mathrm{d}x$ 收敛，并求出其值.

</div>

<div class='pbox'>

$$
\begin{gathered}
\int_L^R (f(x+a)-f(x))dx \\
=\int_{L+a}^{R+a} f(x)dx-\int_L^R f(x)dx \\
=\int_R^{R+a} f(x)dx-\int_L^{L+a} f(x)dx \\
\int_{-\infty}^\infty (f(x+a)-f(x))dx \\
=\lim_{R \to +\infty} \int_R^{R+a}f(x)dx \\
-\lim_{L\to -\infty} \int_L^{L+a}f(x)dx \\
=\lim_{R\to +\infty} af(\xi_1)-\lim_{L\to +\infty}af(\xi_2) \\
=a(A-B)
\end{gathered}
$$

</div>



### T7

<div class="cbox">

4. 设 $f(x)$ 在 $[a, +\infty)$ 上绝对可积，$g(x)$ 是以 $T$ 为周期的周期函数，并且 $g(x) \in R[0, T]$. 证明：
$$ \lim_{\lambda\to+\infty}\int_a^{+\infty}f(x)g(\lambda x)\mathrm{d}x = \frac{1}{T}\int_0^T g(x)\mathrm{d}x \int_a^{+\infty}f(x)\mathrm{d}x $$

</div>

<div class='pbox'>

$$
\begin{gathered}
\text{let }  n=\dfrac{(A-a)\lambda}{T}  \\

\lim_{\lambda \to +\infty} \int_a^{a+\frac {nT}\lambda} f(x)g(\lambda x)dx \\
=\lim_{\lambda \to +\infty} \sum_{i=0}^{n-1} \int_{a+i\frac T\lambda}^{a+(i+1)\frac T\lambda} (f(x)-f(a+\dfrac{iT}\lambda))g(\lambda x)dx+ \\
\lim_{\lambda \to +\infty} \sum_{i=0}^{n-1} \int_{a+i\frac T\lambda}^{a+(i+1)\frac T\lambda} f(a+\dfrac{iT}\lambda)g(\lambda x)dx \\
\end{gathered}
$$

$f$可积,所以

$$
\begin{gathered}
\lim_{\lambda \to +\infty} \sum_{i=0}^{n-1} \int_{a+i\frac T\lambda}^{a+(i+1)\frac T\lambda} (f(x)-f(a+\dfrac{iT}\lambda))g(\lambda x)dx \\
\le \lim_{\lambda \to +\infty}  M\sum_{i=0}^{n-1} \sup_{x,y} \vert f(x)-f(y) \vert \dfrac{T}{\lambda}  \\
=0
\end{gathered}
$$

而第二项有

$$
\begin{gathered}
\lim_{\lambda \to +\infty} \sum_{i=0}^{n-1} \int_{a+i\frac T\lambda}^{a+(i+1)\frac T\lambda} f(a+\dfrac{iT}\lambda)g(\lambda x)dx  \\
=\lim_{\lambda \to +\infty} \sum_{i=0}^{n-1}f(a+\dfrac{iT}\lambda) \int_{a+i\frac T\lambda}^{a+(i+1)\frac T\lambda} g(\lambda x)dx \\
=\lim_{\lambda \to +\infty} \sum_{i=0}^{n-1}f(a+\dfrac{iT}\lambda) \int_0^Tg(x)dx \dfrac{1}{\lambda}  \\
=(\dfrac{1}{T} \int_0^T g(x)dx)\lim_{\lambda \to +\infty}\sum_{i=0}^{n-1}f(a+\dfrac{iT}\lambda)\dfrac{T}{\lambda}  \\
=\frac{1}{T}\int_0^T g(x)\mathrm{d}x \int_a^{A}f(x)\mathrm{d}x
\end{gathered}
$$

然后我们现在算的

$$
\begin{gathered}
\int_a^{a+\frac{nT}\lambda} f(x)g(\lambda x)dx
\end{gathered}
$$

和

$$
\begin{gathered}
\int_a^{A} f(x)g(\lambda x)dx
\end{gathered}
$$

差的长度不超过$\lambda$,而$f,g$都有界,所以当$\lambda\to 0$时两式相等.最后让$A\to \infty$即可.

</div>



### T8

<div class="cbox">

5. 设 $g(x)$ 是以 $T$ 为周期的周期函数，并且 $g(x) \in R[0, T]$. 证明：
$$ \lim_{\lambda\to+\infty} \lambda \int_\lambda^{+\infty} \frac{g(x)}{x^2}\mathrm{d}x = \frac{1}{T}\int_0^T g(x)\mathrm{d}x $$

</div>

<div class='pbox'>

$$
\begin{gathered}
\xlongequal{ t=\frac{x}{\lambda}  } \int_1^{+\infty}\dfrac{g(\lambda t)}{t^2} dt \\
\xlongequal{ f(x)=\frac{1}{x^2} } {\left( \dfrac{1}{T} \int_0^T g(x)dx  \right)} {\left( \int_1^{+\infty} \dfrac{1}{x^2} dx\right)}  \\
=\dfrac{1}{T} \int_0^T g(x)dx
\end{gathered}
$$



</div>



### T9

<div class="cbox">

6. 设 $F(x) = \int_0^x \left(\frac{1}{t} - \left[\frac{1}{t}\right]\right)\mathrm{d}t$, 试证：$F'_+(0) = \frac{1}{2}$.

</div>

<div class='pbox'>

$$
\begin{gathered}
F'_+(0) \\
=\lim_{x \to 0^+} \dfrac{\int_0^x \{ \dfrac{1}{t}  \} dt}{x}  \\
=\lim_{x \to 0^+} \dfrac{\int^{\infty}_{\frac1x}  \dfrac{\{ t \} }{t^2} dt}{x}  \\
\xlongequal{ \lambda=\frac{1}{x}  } \lim_{\lambda \to +\infty} \lambda\int_\lambda^{+\infty} \dfrac{g(t)}{t^2}dt,g(t)=\{ t \}  
\end{gathered}
$$

由上一题,答案即 $\int_0^1 \{ t \} dt=\dfrac{1}{2}$

</div>

