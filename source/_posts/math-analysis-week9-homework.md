---
title: Math Analysis Homework - Week 9
tags: [math-analysis,homework,math]
---

# Math Analysis Homework - Week 9

## Class 1

### T1

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f(x)\in C[a,b], \\
\forall g\in C[a,b],\int_a^b f(x)g(x)dx=0
\end{cases} \\
\Rightarrow f(x)=0
\end{gathered}
$$

</div>

<div class='pbox'>

反证,假设存在$f(x_0)\ne 0$,不妨设是$f(x_0)>0$,则存在$(x_0-\delta,x_0+\delta)$使得$\forall x\in (x_0-\delta,x_0+\delta),f(x)>\dfrac{f(x_0)}2$.

取

$$
\begin{gathered}
g(x)=\begin{cases}
1,\vert x-x_0 \vert <\dfrac{\delta}{2}  \\
\vert x-x_0-\dfrac{\delta}{2}  \vert,\vert x-x_0 \vert \in [\dfrac{\delta}{2},\delta) \\
0,\text{otherwise}
\end{cases} \\
\Rightarrow \int f(x)g(x)dx \ge \dfrac{f(x_0)}{2} \delta>0

\end{gathered}
$$

</div>



### T2

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
a,b>0,f(x)\in C[-a,b] \\
f(x)>0,\int_{-a}^bxf(x)dx=0
\end{cases} \\
\Rightarrow \int_{-a}^b x^2f(x)dx\le ab\int_{-a}^b f(x)dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}

\end{gathered}
$$

</div>



### T3

<div class='cbox'>

$$
\begin{gathered}
f(x)\in C[0,1],f(x)>0 \\
\Rightarrow \int_0^1 f(x)dx\int_0^1 \dfrac{1}{f(x)} dx\ge 1
\end{gathered}
$$

</div>

### T4

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f(x) \in C[0,\pi] \\
\int_0^\pi f(\theta)\cos \theta d\theta = \int_0^\pi f(\theta)\sin \theta d\theta =0 \\
\end{cases} \\
\Rightarrow \exists x_1,x_2\in (0,\pi),f(x_i)=0
\end{gathered}
$$

</div>

### T5

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f\in C[a,b],f(x)\ge 0 \\
M=\max f([a,b])
\end{cases}\\
\Rightarrow \lim_{n \to \infty} (\int_a^b f^n(x)dx)^\frac1n=M 
\end{gathered}
$$

</div>

### T6

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f \in C[a,b],f(x)\ge 0 \\
f(x) \text{ is strictly increasing}  \\
\forall p,\exists x_p\in [a,b] \\
f^p(x_p)=\dfrac{1}{b-a} \int_a^b f^p(t)dt
\end{cases} \\
\Rightarrow \lim_{p \to +\infty} x_p =b
\end{gathered}
$$

</div>

### T7

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f(x)\in C[0,1]\cap D(0,1) \\
f(1)=2\int_0^\frac12 xf(x)dx
\end{cases} \\
\Rightarrow \exists \xi\in (0,1) \\
f(\xi)+\xi f'(\xi)=0
\end{gathered}
$$

</div>

### T8

<div class='cbox'>

$$
\begin{gathered}
\lim_{n \to \infty} \int_0^{\frac\pi2}\sin^n xdx
\end{gathered}
$$

</div>

### T9

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f(x) \text{ is integrable on any limited range}  \\
\lim_{x \to +\infty} f(x)=l
\end{cases}
\\
\Rightarrow \lim_{x \to +\infty} \dfrac{1}{x} \int_0^x f(t)dt=l
\end{gathered}
$$

</div>

### T10

<div class='cbox'>

$$
\begin{gathered}
f(x) \text{ is integrable on } [A,B] \\
\Rightarrow \forall a<b \in (A,B) \\
\lim_{h \to 0} \int_a^b \vert f(x+h)-f(x) \vert dx=0
\end{gathered}
$$

</div>

### T11

<div class='cbox'>

$$
\begin{gathered}
\lim_{x \to +\infty} \dfrac{\int_0^x (\arctan t)^2dt}{\sqrt{1+x^2}} 
\end{gathered}
$$

</div>

### T12

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
b>0,f(x) \in C[0,b] \\
f(x) \text{ is strictly increasing}
\end{cases}  \\
\Rightarrow 2\int_0^b xf(x)dx\ge b\int_0^b f(x)dx 
\end{gathered}
$$

</div>

### T13

<div class='cbox'>

$$
\begin{gathered}
f(x)\in D[0,1],f(0)=0,f'(x)\in[0,1] \\
\Rightarrow \int_0^1 f^3(x)dx\le (\int_0^1 f(x)dx)^2
\end{gathered}
$$

</div>

### T14

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f(x) \in C[0,+\infty) \\
x>0 \Rightarrow \int_0^x f(t)dt=\dfrac{1}{2} xf(x)
\end{cases} \\
\Rightarrow f(x)=cx,x>0
\end{gathered}
$$

</div>

### T15

<div class='cbox'>

$$
\begin{gathered}
f(x) \in C[0,+\infty),f(x)>0 \\
\Rightarrow \phi(x)=\dfrac{\int_0^x tf(t)dt}{\int_0^x f(t)dt} \text{ is strictly increasing} 
\end{gathered}
$$

</div>

### T16

<div class='cbox'>

$$
\begin{gathered}
\int_0^1 (2x-1)e^{x^2-1}dx
\end{gathered}
$$

</div>



### T17

<div class='cbox'>

$$
\begin{gathered}
\lim_{n \to \infty} \sum _{k = 1} ^{n}  \sqrt{ \dfrac{(n+k)(n+k+1)}{n^4}  } 
\end{gathered}
$$

</div>

### T18

<div class='cbox'>

$$
\begin{gathered}
\forall x\in[-1,+\infty),f(x)=\int_{-1}^x \dfrac{e^{\frac1t}}{t^2(1+e^\frac1t)^2} dt \\
\Rightarrow  f(x)=?
\end{gathered}
$$

</div>

### T19

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f(x) \in D^2[0,1] \\
f(0)=f(1)=0 \\
x\in (0,1) \Rightarrow  f(x)\ne 0
\end{cases} \\
\Rightarrow \int_0^1 \vert \dfrac{f''(x)}{f(x)}  \vert dx\ge 4

\end{gathered}
$$

</div>


