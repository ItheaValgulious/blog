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
\lim_{x \to 0^+} f(x)=+\infty \\
\exists \{ a_n \},a_n\in (0,1),a_n<a_{n-1},\lim_{n \to \infty} a_n=0,\lim_{n \to \infty} f(a_n)=+\infty \\
\forall M>0,i,\exists k>i \ s.t.\ 
f(a_k)>f(a_i)+M \\
\Rightarrow \exists \xi \in (a_k,a_i),f'(\xi)=\dfrac{f(a_k)-f(a_i)}{a_k-a_i} <-M \\
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

Solution2:

假设$f(x)$不为$0$,那么存在一个点的邻域$(c,d)$,$f(c)=0$且$f(x)>0,\forall x\in (c,d)$.于是令 $g(x)=\ln \vert f(x) \vert$,得到$\vert g'(x)\vert\le 1$,这意味这$g$有界,但是$g(c^+)$是$-\infty$,矛盾.

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

## Class 2

### T1

<div class='cbox'>

$$
\begin{array}{l}
x\in [0,1],p\ge 2 \\
\Rightarrow 
(\dfrac{1+x}{2} )^p+(\dfrac{1-x}{2} )^p\le \dfrac{1}{2} (1+x^p)
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
f(x)=\dfrac{1}{2} (1+x^p)-(\dfrac{1+x}{2} )^p-(\dfrac{1-x}{2} )^p \\
f'(x)=\dfrac{p}{2}(x^{p-1} -(\dfrac{1+x}{2} )^{p-1}+ (\dfrac{1-x}{2} )^{p-1}) \\
p-1>1 \Rightarrow a^{p-1}+b^{p-1}<(a+b)^{p-1} \\
\therefore (\dfrac{1-x}{2})^{p-1}+x^{p-1}<(\dfrac{1+x}{2})^{p-1} \\
\Rightarrow f'(x)<0 \\
\Rightarrow f(x) \text{ is decreasing}  \\
f(x)>f(1)=0 \\
\\
\text{Q.E.D} 
\end{array}
$$

</div>



### T2

<div class='cbox'>

$$
\begin{array}{l}
x\in (0,\dfrac{\pi}{2} )\Rightarrow 2x<\sin x+\tan x
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
f(x)=\sin x+\tan x-2x \\
f'(x)=\cos x+\dfrac{1}{\cos^2 x}-2 \\
f''(x)=\sin x(\dfrac{2}{\cos^3 x} -1)>0 \\
\Rightarrow f'(x) \text{ is increasing}  \\
\Rightarrow f'(x)>f'(0)=0 \\
\Rightarrow f(x) \text{ is increasing}  \\
f(x)>f(0)=0 \\
\\
\text{Q.E.D}
\end{array}
$$

</div>



### T3

<div class='cbox'>

$$
\begin{array}{l}
\left. \begin{array}{ll}
\forall x\in[0,+\infty),\exists f'(x) \\
f(0)=0 \\
f'(x) \text{ is strictly increasing}
\end{array} \right\} \\
\Rightarrow \dfrac{f(x)}{x} \text{ is strictly increasing} 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
f(x)=f(x)-f(0)=(x-0)f'(\xi) \\
\xi\in(0,x) \Rightarrow f'(\xi)<f'(x) \\
\Rightarrow f(x)<xf'(x) \\
\Rightarrow (\dfrac{f(x)}{x} )'=\dfrac{xf'(x)-f(x)}{x^2} >0 \\
\\
\text{Q.E.D}
\end{array}
$$

</div>



### T4

<div class='cbox'>

calculate the extremum point for

$$
\begin{array}{l}
f(x)=\arcsin \dfrac{2x}{1+x^2} 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
f'(x)=\dfrac{1}{\sqrt{1-(\dfrac{2x}{1+x^2} )^2}}\dfrac{2(1+x^2)-4x^2}{(1+x^2)^2}  \\
=\dfrac{2-2x^2}{\sqrt{x^4+2x^2+1-4x^2}(1+x^2)}  \\
=\dfrac{2(1-x^2)}{\vert 1-x^2 \vert (1+x^2)}   \\
x<-1 \Rightarrow f'(x)<0,f(x) \text{ is decreasing}  \\
x\in (-1,1) \Rightarrow f'(x)>0,f(x) \text{ is increasing}  \\
x>1 \Rightarrow f'(x)<0,f(x) \text{ is decreasing}  \\
\Rightarrow \text{minimum:} (-1,-\dfrac{\pi}{2} ),\text{maximum:} (1,\dfrac{\pi}{2} )
\end{array}
$$

</div>



### T5

<div class='cbox'>

calculate the extremum point for

$$
\begin{array}{l}
f(x)=(\sum _{i = 0} ^{n} \dfrac{x^i}{i!} )e^{-x},n\ge 1
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
f'(x)=e^{-x}(\sum _{i = 0} ^{n-1}  \dfrac{x^i}{i!} -\sum _{i = 1} ^{n}  \dfrac{x^i}{i!} ) \\
=-\dfrac{x^ne^{-x}}{n!}  \\
n \bmod 2=0:f'(x)\le 0(f'(x)=0 \Leftrightarrow x=0) \\
\Rightarrow f(x) \text{ has no extremum} \\
n \bmod 2=1:\operatorname{sign}f'(x)=-\operatorname{sign}x \\
\Rightarrow f(x) \text{ has maximum } (0,1)
\end{array}
$$

</div>



### T6

<div class='cbox'>

$$
\begin{array}{l}
xf''(x)+3x(f'(x))^2=1-e^{-x} \\
\Rightarrow \begin{cases}
x=c(c\ne 0) \text{ is an extremum } \Rightarrow f(c)\text{ is a minimum}  \\
x=c(c=0) \text{ is an extremum } \Rightarrow f(c) \text{ is a minimum} 
\end{cases}

\end{array}
$$

</div>

<div class='pbox'>

(1)

$$
\begin{array}{l}
x=c \text{ is an extremum}  \\
\Rightarrow f'(c)=0 \\
cf''(c)+3c(f'(c))^2=1-e^{-c} \\
\Rightarrow \operatorname{sign} f''(c)=\operatorname{sign} \dfrac{1-e^{-c}}{c} =1 \\
\Rightarrow \lim_{x \to c} \dfrac{f'(x)-f'(c)}{x-c}=\dfrac{f'(x)}{x-c} >0 \\
\Rightarrow \operatorname{sign}  f'(x)=\operatorname{sign} (x-c) \\
\Rightarrow f(x) \text{ is a minimum} 
\end{array}
$$

(2)

$$
\begin{array}{l}
f'(0)=0 \\
\lim_{x \to 0} (f''(x)+3f'^2(x))=\lim_{x \to 0} \dfrac{1-e^{-x}}{x} =1 \\
\Rightarrow f''(0)=1 \\
\stackrel{\text{ same as (1)'s proof }}{\Longrightarrow} f(x) \text{ is a minimum} 
\end{array}
$$

</div>



### T7

<div class='cbox'>

$$
\begin{array}{l}
p>1,x\in [0,1] \Rightarrow  \\
\dfrac{1}{2^{p-1}} \le x^p+(1-x)^p\le 1
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
x\le 1 \Rightarrow x^p\le x \Rightarrow x^p+(1-x)^p\le x+1-x=1 \\
f(x)=x^p+(1-x)^p \\
f'(x)=px^{p-1}-p(1-x)^{p-1}=p(x^{p-1}-(1-x)^{p-1}) \\
x>\dfrac{1}{2} \Rightarrow x>1-x \Rightarrow f'(x)>0 \\
x<\dfrac{1}{2} \Rightarrow f'(x)<0 \\
\Rightarrow (\dfrac{1}{2},f(\dfrac{1}{2})) \text{ is a minimum} ,f(x)\ge f(\dfrac{1}{2})=2^{-(p-1)}
\end{array}
$$

</div>



### T8

<div class='cbox'>

$$
\begin{array}{l}
\left. \begin{array}{ll}
f,g:R\to R \\
f''(x)+f'(x)g(x)-f(x)=0 \\
f(a)=f(b)=0(a<b)
\end{array} \right\} \\
\Rightarrow \forall x\in [a,b],f(x)=0
\end{array}
$$

</div>

<div class='pbox'>

此证明已弃用.但应该是正确的.

$$
\begin{array}{l}
f''(x)+f'(x)g(x)-f(x)=0 \\
\Leftrightarrow \forall x,f'(x)\ne 0 \lor f''(x)=f(x) \\
\forall x_0\in (a,b),f'(x_0)=0 \\
\text{Assume } f(x_0)\ne 0 \\
\text{Without loss of generality,assume } f(x_0)>0 \\
\Rightarrow f''(x_0)=f(x_0)>0 \\
\Rightarrow \exists \delta,\exists x_0'\in (x_0,\delta),f'(x_0')>0 \\
\exists \xi,f'(\xi)=\dfrac{f(x_0)-f(b)}{x_0-b} <0 \\
\stackrel{\text{ Darbox Theorem }}{\Longrightarrow}\exists x_1\in (x_0,\xi),f'(x_1)=0 \\
\text{Repeat this you get } \{ x_n \} ,x_i\in (x_{i-1},\xi),f'(x_i)=0 \\
\lim_{n \to \infty} x_n=\xi,\lim_{n \to \infty} f'(x_n)=0\ne f'(\xi) \\
\text{Ridiculous!} \\
\Rightarrow f'(x)=0 \Rightarrow f(x)=f''(x)=0 \\
\text{Assume } f(x_0)\ne 0,a_0=a,b_0=b \\
\exists x_1\in (a_i,x_0),x_2\in (x_0,b_i), \\
f'(x_1)=\dfrac{f(x_0)}{x_0-a_i} \ne 0 \\
f'(x_2)=\dfrac{f(x_0)}{x_0-b_i} \ne 0 \\
f'(x_1)f'(x_2)<0 \Rightarrow \exists x_3,f'(x_3)=0 \\
\Rightarrow f'(x_3)=f(x_3)=0 \\
f'(x_1)\ne 0 \Rightarrow \exists x_1'\in N(x_1),f(x_1')\ne 0 \\
\text{same for } \exists x_2'\in N(x_2),f(x_2')\ne 0 \\
\Rightarrow \exists f(a_i)=f(x_3)=0,x_1'\in(a_i,x_3),f(x_1')\ne 0 \\
\exists f(x_3)=f(b_i)=0,x_2'\in (x_3,b_i),f(x_2')\ne 0 \\
\text{let } [a_{i+1},b_{i+1}]=\text{the shorter one in } [a_i,x_3],[x_3,b_i] \\
\Rightarrow \begin{cases}
b_{i+1}-a_{i+1}\le \dfrac{1}{2} (b_i-a_i) \\
[a_i,b_i]\supset [a_{i+1},b_{i+1}] \\
\exists c_i\in [a_i,b_i],f(c_i)\ne 0
\end{cases}
 \\
\stackrel{\text{ Nested Intervals Principle }}{\Longrightarrow} \\
\exists \xi \in [a_i,b_i] \\
\lim_{n \to \infty} a_n=\xi \\
\lim_{n \to \infty} c_n=\xi \\
\lim_{n \to \infty} f(a_n)=\lim_{n \to \infty} f(c_n) \\
\text{Ridiculous!} \\
\Rightarrow \forall x\in (a,b),f(x)=0 
\\
\text{Q.E.D}
\end{array}
$$

上面那个太麻烦了

考虑区间中的最大值$f(x_0)$,注意到$f'(x_0)=0,f(x_0)\ge 0,f''(x_0)\le 0$矛盾.于是$f(x_0)=0$

最小值同理.

</div>





