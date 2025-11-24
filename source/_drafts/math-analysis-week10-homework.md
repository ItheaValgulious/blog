---
title: Math Analysis Homework - Week 10
tags: [math,math-analysis,homework]
---

# Math Analysis Homework - Week 10

## Class 1

### T1

<div class='cbox'>

$$
\begin{gathered}
f(x)\in C^1[a,b] \\
\Rightarrow \max_{x\in [a,b]} \vert f(x) \vert \le \dfrac{1}{b-a} \int_a^b \vert f(x) \vert dx+\int_a^b \vert f'(x) \vert dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\text{let } \max_{x\in [a,b]}\vert f(x) \vert =\vert f(x_0) \vert  \\
\dfrac{1}{b-a} \int_a^b \vert f(x) \vert dx \\
\xlongequal{\text{ Fist Mean Value Theorem }} f(\xi),\xi \in [a,b] \\
\vert f(x_0) \vert = \vert f(\xi)+\int_{\xi}^{x_0} f'(x)dx \vert  \\
\le \vert f(\xi) \vert +\int_\xi^{x_0} \vert f'(x) \vert dx \\
\text{Q.E.D}
\end{gathered}
$$

</div>


### T2

<div class='cbox'>

$$
\begin{gathered}
f(x)\in C^1[0,1],f(0)=0 \\
\Rightarrow \int_0^1 \vert f(x) \vert ^2dx\le \int_0^1 \vert f'(x) \vert ^2 dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
f(x)=\int_0^x f'(t)dt \\
=\int_0^x f'(t)\cdot 1dt \\
\le (\int_0^x f'(t)^2 dt)^\frac12(\int_0^x dt)^\frac12 \\
\Rightarrow f(x)^2 \le x\int_0^x f'^2(t)dt \\
\le x\int_0^1 f'^2(t)dt \\
\Rightarrow \int_0^1 f(x)^2 dx\le \dfrac12 \int_0^1 f'^2(t)dt\le \int_0^1 f'^2(t)dt
\end{gathered}
$$

</div>



### T3

<div class='cbox'>

$$
\begin{gathered}
f(x)\in C[-1,1] \\
\Rightarrow \lim_{h \to 0^+} \int_{-1}^1 \dfrac{h}{h^2+x^2} f(x)dx=\pi f(0)
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\lim_{h \to 0^+} \int_{-1}^{-\delta} \dfrac{h}{h^2+x^2} +\int_{\delta}^1 \dfrac{h}{h^2+x^2} \\
\le  \lim_{h \to 0^+} \int_{-1}^{-\delta}\dfrac{h}{\delta^2}dx +\int_{\delta}^1 \dfrac{h}{\delta^2} dx \\
\le \lim_{h \to 0^+} \dfrac{2h}{\delta^2} \\
=0 \\
\forall \delta>0,
Ans=\lim_{h \to 0^+} \int_{-\delta}^\delta \dfrac{h}{h^2+x^2} f(x)dx \\
f(x)\in C[-1,1] \Rightarrow \forall p<1,\exists r \ s.t.\  \\
\text{WLOG,assume } f(x)>0 \\
\vert x \vert <r \Rightarrow f(x) \in (pf(0),\dfrac{1}{p}f(0)) \\
\text{let } \delta=r \Rightarrow  \\
I=f(0)(\lim_{h \to 0^+} \int_{-r}^r \dfrac{h}{h^2+x^2} dx) \\
Ans\in (pI,\dfrac{I}{p} ) \\
I=f(0)\lim_{h \to 0^+} 2\arctan \frac rh=\pi f(0) \\
Ans=\lim_{p \to 1} pI=\lim_{p \to 0} \dfrac{I}{p} =\pi f(0)
\end{gathered}
$$

</div>



### T4

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f(x)\in D^2[a,b] \\
f(\dfrac{a+b}{2} )=0
\end{cases} \\
\Rightarrow \vert \int_a^b f(x)dx \vert \le \dfrac{(b-a)^3}{24} \sup_{x\in[a,b]}\vert f''(x) \vert 

\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\text{let } m=\dfrac{a+b}{2}  \\ 
f(x)=(x-m )f'(m)+\dfrac{f''(\xi)}{2} (x-m)^2 \\
\le (x-m)f'(m)+\dfrac{\vert \sup f''(\xi)\vert}{2} (x-m)^2 \\
\Rightarrow \int_a^b f(x)=f'(m)\int_a^b (x-m)dx+\vert \sup f''(x)\vert \int_a^b \dfrac{(x-m)^2}{2}dx  \\
=\dfrac{(b-a)^3}{24} \sup \vert f''(x) \vert 
\end{gathered}
$$

</div>

### T5

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f(x) \in R[0,1] \\
\int_0^1 f(x)dx=1 \\
\int_0^1 xf(x)dx=0
\end{cases} \\
\Rightarrow \begin{cases}
\text{calculate } I(a)=\int_0^1 \vert ax-1 \vert dx,a\ge 0 \\
\sup_{x\in [0,1]} \vert f(x) \vert \ge \sqrt{2}+1
\end{cases}
\end{gathered}
$$

</div>

<div class='pbox'>

(1)

By geometry,$a<1$显然劣于$a=1$,考虑$a\ge 1$

$$
\begin{gathered}
I(a)=\dfrac{1}{2a} +\dfrac{(a-1)(1-\dfrac{1}{a} )}{2} \\
=\dfrac{a}{2} +\dfrac{1}{a} -1 \\
\ge \sqrt 2-1
\end{gathered}
$$

(2)


考虑反证,则 $\vert f(x) \vert <\sqrt 2+1$

$$
\begin{gathered}
-1=\int_0^1 f(x)(\sqrt 2x-1)dx \\
1=\vert \int_0^1 f(x)(\sqrt 2x-1)dx \vert  \\
<(\sqrt2+1)\int_0^1 \vert \sqrt2 x-1 \vert dx \\
=(\sqrt 2+1)(\sqrt 2-1) \\
=1
\end{gathered}
$$

矛盾,得证.


</div>



### T6

<div class='cbox'>

$$
\begin{gathered}
f(x)\in R[a,b] \\
\Rightarrow \forall \epsilon>0,\exists p(x),q(x) \text{ are step functions} ,f(x)\in [p(x),q(x)]\\ s.t.\\ 
\int_a^b (q(x)-p(x))dx<\epsilon
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
f(x)\in R[a,b] \\
\Rightarrow \forall \epsilon,\exists T \ s.t.\ 
\sum _{i = 1} ^{n} (M_i-m_i)\Delta x_i<\epsilon \\
\text{where } M_i=\sup_{x\in [t_{i-1},t_i]} f(x),m_i=\inf_{x\in [t_{i-1},t_i]} f(x) \\
\text{let } q(x)=\sum _{i = 1} ^{n}  M_i[x\in [t_{i-1},t_i]] \\
p(x)=\sum _{i = 1} ^{n}  m_1[x\in [t_{i-1},t_i]] \\
\text{where } [p]=1 \Leftrightarrow p \text{ is true}  \\
\int_a^b (q(x)-p(x))dx=\sum _{i = 1} ^{n} (M_i-m_i)\Delta x_i<\epsilon  
\end{gathered}
$$

</div>



### T7

<div class='cbox'>

$$
\begin{gathered}
f(x) \text{ is increasing at } [a,b] \\
\Rightarrow \int_a^b xf(x)dx \ge \dfrac{a+b}{2} \int_a^b f(x)dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\text{let } m=\dfrac{a+b}{2}  \\
\int_a^m (x-m )f(x) \\
=\int_m^b (m-x)f(a+b-x) \\
\int_a^b (x-m)f(x)=\int_a^m (x-m)f(x)+\int_m^b (x-m)f(x) \\
=\int_m^b (x-m)f(x)-\int_m^b (x-m)f(a+b-x) \\
=\int_m^b (x-m)(f(x)-f(a+b-x)) \\
\ge 0
\end{gathered}
$$

</div>
