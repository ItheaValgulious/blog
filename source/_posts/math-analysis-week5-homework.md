---
title: Math Analysis Homework - Week 5
tags:
  - math-analysis
  - math
  - homework
date: 2025-10-20 21:21:51
---


# Math Analysis Homework - Week 5

## Class 1

### T1

<div class='cbox'>

$$
\begin{array}{l}
\sum _{i = 0} ^{n}  \dfrac{a_i}{n+1-i}=0 \\
\Rightarrow \exists x_0\in(0,1),\sum _{i = 0} ^{n}  a_ix_0^{n-i}=0 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\text{let } f(x)=\sum _{i = 0} ^{n}  a_ix^{n-i} \\
\text{let } F(x)=\sum _{i = 0} ^{n}  \dfrac{a_ix^{n-i+1}}{n-i+1}  \\
F(0)=0,F(1)=\sum _{i = 0} ^{n}  \dfrac{a_i}{n+1-i} =0 \\
\stackrel{\text{ Rolle's Theorem }}{\Longrightarrow} \exists \xi \in (0,1),f(\xi)=F'(\xi)=0 \\
\Rightarrow x_0=\xi
\end{array}
$$

</div>



### T2

<div class='cbox'>

$$
\begin{array}{l}
\left. \begin{array}{ll}
f(x)\in C[a,b] \\
\forall x\in (a,b),\exists f'(x) \\
f(a)=f(b)=0
\end{array} \right\} \\
\Rightarrow \begin{cases}
a>0 \Rightarrow \exists \xi\in(a,b),f'(\xi)=\dfrac{f(\xi)}{\xi}  \\
\forall \lambda,\exists \xi,f'(\xi)=\lambda f(\xi)
\end{cases}
\end{array}
$$

</div>

<div class='pbox'>

(1)

$$
\begin{array}{l}
\text{let } F(x)=\dfrac{f(x)}{x}  \\
F(a)=F(b)=0 \\
\stackrel{\text{ Rolle's Theorem }}{\Longrightarrow}\exists \xi\in (a,b),F'(\xi)=0 \\
\Rightarrow F'(\xi)=\dfrac{f'(\xi)\xi-f(\xi)}{\xi^2} =0 \\
\Rightarrow f'(\xi)=\dfrac{f(\xi)}{\xi} 
\end{array}
$$

(2)

$$
\begin{array}{l}
\text{let } F(x)=e^{-\lambda x}f(x) \\
F(a)=F(b)=0
\Rightarrow
\exists \xi \in (a,b),F'(\xi)=0 \\
\Rightarrow x=\xi,
F'(x)=e^{-\lambda x}(f'(x)-\lambda f(x))=0 \\
\Rightarrow f'(x)=\lambda f(x)
\end{array}
$$

</div>



### T3

<div class='cbox'>

$$
\begin{array}{l}
\left. \begin{array}{ll}
\forall x\in [0,1],\exists f'''(x) \\
f(0)=f(1)=0 \\
F(x)=x^2f(x)
\end{array} \right\}\Rightarrow \exists \xi\in (0,1),F'''(\xi)=0
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
F'(x)=2xf(x)+x^2f'(x) \\
F''(x)=2f(x)+4xf'(x)+x^2f''(x) \\
F(0)=0,F(1)=0 \\
\stackrel{\text{ Rolle's Theorem }}{\Longrightarrow}\exists x_1\in (0,1),F'(x_1)=0 \\
F'(0)=0,F'(x_1)=0 \\
\stackrel{\text{ Rolle's Theorem }}{\Longrightarrow}\exists x_2\in (0,x_1),F''(x_2)=0 \\
F''(0)=0,F''(x_2)=0 \\
\stackrel{\text{ Rolle's Theorem }}{\Longrightarrow}\exists \xi \in (0,x_2) \subset (0,1),F'''(\xi)=0
\end{array}
$$

</div>



### T4

<div class='cbox'>

$$
\begin{array}{l}
\left. \begin{array}{ll}
\forall x\in (0,a),\exists f'(x) \\
f(0^+)=+\infty
\end{array} \right\} \\
\Rightarrow f'(x) \text{ has no lower bound on the right-hand neibourhood of } 0 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\lim_{x \to 0^+} f(x)=\infty \\
\exists \{ a_n \},a_n\in (0,1),a_n<a_{n-1},\lim_{n \to \infty} a_n=0,\lim_{n \to \infty} f(a_n)=+\infty \\
\forall M<0,i,\exists k>i \ s.t.\ 
f(a_k)<f(a_i)+M \\
\Rightarrow \exists \xi \in (a_k,a_i),f'(\xi)=\dfrac{f(a_k)-f(a_i)}{a_k-a_i} <M \\
\\
\text{Q.E.D} 
\end{array}
$$

</div>



### T5

<div class='cbox'>

$$
\begin{array}{l}
\left. \begin{array}{ll}
f \in C[a,b] \\
\forall x\in(a,b),\exists f'(x) \\
f \text{ is not constant or linear function}  \\
\end{array} \right\}  \\
\Rightarrow \exists \xi \in (a,b),\vert f'(\xi) \vert >{\left \vert \dfrac{f(b)-f(a)}{b-a}  \right \vert} 
\end{array}
$$

</div>

<div class='pbox'>

不妨设$f(b)>f(a)$

$$
\begin{array}{l} \\
\text{let } k=\dfrac{f(b)-f(a)}{b-a}=
\exist x_0,f(x_0)\ne (x_0-a)k+f(a) \\
\dfrac{f(b)-f(a)}{b-a}=\dfrac{f(b)-f(x_0)+f(x_0)-f(a)}{b-x_0+x_0-a}  \text{ is bewteen } \\
\dfrac{f(x_0)-f(a)}{x_0-a} ,\dfrac{f(b)-f(x_0)}{b-x_0}   \\

f(x)\stackrel{\text{ Lagrange Mean Value Theorem }}{\Longrightarrow} \\
\exists x_1,f'(x_1)=\dfrac{f(x_0)-a}{x_0-a}  \\
\exists x_2,f'(x_2)=\dfrac{f(b)-f(x_0)}{b-x_0}  \\
\end{array}
$$

则  $\vert k \vert$在$f'(x_1),f'(x_2)$之间,取绝对值大的一个即可.

</div>



### T6

<div class='cbox'>

$$
\begin{array}{l}
\left. \begin{array}{ll}
\forall x\in [a,+\infty),\exists f'(x) \\
f(a)=0 \\
x \ge a \Rightarrow  \vert f'(x) \vert \le \vert f(x) \vert 
\end{array} \right\} \\
\Rightarrow \forall x\in [a,+\infty),f(x)=0
\end{array}
$$

</div>

<div class='pbox'>

不妨设$a=0$

$$
\begin{array}{l}
\text{let } F(x)=e^{-2x}f^2(x)\ge 0 \\
F'(x)=2e^{-2x}f(x)(f'(x)-f(x))\le 0 \\
\forall x>a=0,F(x)\le F(a) \\
\because F(x)\ge 0 \\
\Rightarrow F(x)=0,f(x)=0
\end{array}
$$

</div>



### T7

<div class='cbox'>

$$
\begin{array}{l}
\left. \begin{array}{ll}
f\in C[a,b] \\
\forall x\in(a,b),\exists f''(x) \\
f(a)=f(b)=0 \\
f'_+(a)>0
\end{array} \right\} \\
\Rightarrow \exists \xi \in (a,b),f''(\xi)<0
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
f(a)=f(b)=0 \\
\stackrel{\text{ Rolle's Theorem }}{\Longrightarrow}\exists x_1\in(a,b),f'(x_1)=0 \\
\exists f''(x) \Rightarrow f'(x) \in C(a,b) \\
f'_+(a)>0 \Rightarrow \exists x_2 \in (a,a+\delta),f'(x_2)>0 \\
\exists \xi \in (x_2,x_1) \subset (a,b),f''(\xi)=\dfrac{f'(x_1)-f'(x_2)}{x_1-x_2} <0
\end{array}
$$

</div>



### T8

<div class='cbox'>

$$
\begin{array}{l}
\forall x \in (0,+\infty),\exists f'(x) \\
\lim_{x \to +\infty} f'(x)=+\infty
\end{array} \\
\Rightarrow f(x) \text{ is not uniformly continuous in } (0,+\infty)
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\lim_{x \to +\infty} f'(x)=+\infty \\
\epsilon=1 \\
\forall \delta \\
\text{let } M=\dfrac{2}{\delta}  \Rightarrow \exists X,x>X \Rightarrow f'(x)>M \\
\forall x>M,\vert f(x+\delta)-f(x) \vert = \vert \delta f'(\xi) \vert >2>\epsilon \\
\\
\text{Q.E.D}
\end{array}
$$

</div>



### T9

<div class='cbox'>

$$
\begin{array}{l}
\left. \begin{array}{ll}
\lim_{x \to x_0^+} f(x)=f(x_0) \\
\forall x \in (x_0,x_0+\delta_0),\exists f'(x) \\
\exists f'(x_0^+)
\end{array} \right\} \\
\Rightarrow f'_+(x_0)=f'(x_0^+)
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\stackrel{\text{ Lagrange Mean Value Theorem }}{\Longrightarrow} \\
\dfrac{f(x_0+h)-f(x_0)}{h}=f'(\xi),\xi \in (x_0,x_0+h) \\ \\
f'_+(x_0)=
\lim_{h \to 0^+} \dfrac{f(x_0+h)-f(x_0)}{h}=\lim_{\xi \to x_0^+} f'(\xi) =f'(x_0^+)\\
\end{array}
$$

</div>

