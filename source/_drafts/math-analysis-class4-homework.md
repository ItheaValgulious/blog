---
title: Math Analysis Homework - Class 4
tags: [math-analysis,homework]
---


# Math Analysis Homework - Class 4


### T1

<div class="cbox">

设 $x_1 > 1, x_{n+1} = \frac{3x_n + 1}{x_n + 3}, n = 1, 2, \dots$

</div>

<div class='pbox'>

$$
\begin{array}{c}
x_n>1 \Rightarrow  1<x_{n+1}=\dfrac{3x_n+1}{x_n+3}<3 \\
\text{Inductively},x_n\in (1,3)
x_{n+1}-x_n \\
=\dfrac{3x_n+1-x_n^2-3x_n}{x_n+3} \\
=\dfrac{1-x_n^2}{x_n+3}<0 \\
\therefore \{ x_n \} \text{is bounded and decreasing} \\\lim_{n \to \infty} x_n \text{exists}. \\


x_{n+1}=\dfrac{3x_n+1}{x_n+3} \\
\Rightarrow \lim_{n \to \infty} x_{n}=\dfrac{3(\lim_{n \to \infty} x_n)+1}{(\lim_{n \to \infty} x_n)+3}  \\
\Rightarrow \lim_{n \to \infty} x_n=1
\end{array}
$$

</div>



### T2

<div class="cbox">

设 $0 < a_1 < b_1$, 令 $a_{n+1} = \sqrt{a_n b_n}, b_{n+1} = \frac{a_n + b_n}{2}, n \in \mathbb{N}_+$. 证明: $\{a_n\}, \{b_n\}$ 收敛于同一极限.

</div>

<div class='pbox'>

$$
\begin{array}{c}
\forall n,a_n<b_n \\
\Rightarrow \begin{cases}
b_n>a_{n+1}=\sqrt{a_n b_n}>a_n \\
a_n<b_{n+1}=\frac{a_n+b_n}{2}<b_n
\end{cases}
\\
\Rightarrow 
\begin{cases}
a_n<b_n<b_{n-1}<\ldots<b_1, \\
b_n>a_n>a_{n-1}>\ldots>a_1
\end{cases} \\
\Rightarrow 
\{ a_n \} ,\{ b_n \} \text{ is bounded and monotonic} \\
\Rightarrow A=\lim_{n \to \infty} a_n,B=\lim_{n \to \infty} b_n \text{ exists}   \\
\Rightarrow 
\begin{cases}
\lim_{n \to \infty} b_{n+1} = \lim_{n \to \infty} \frac{a_n + b_n}{2} \\
\lim_{n \to \infty} a_{n+1} = \sqrt{a_n b_n}
\end{cases} \\

\Rightarrow 
\begin{cases}
B=\dfrac{A+B}{2}  \\
A=\sqrt{ A B } \\ 
\end{cases}
\Rightarrow A=B

\end{array}
$$

</div>

### T3

<div class='cbox'>

设数列 $\{x_n\}$ 满足 $0 < x_n < 1$ 与 $(1 - x_n)x_{n+1} > \frac{1}{4}, n = 1, 2, 3, \dots$, 求证: $\lim_{n \to \infty} x_n = \frac{1}{2}$.

</div>

<div class='pbox'>

$$
\begin{array}{c}
\dfrac{1}{4(1-x_n)}<x_{n+1}<1  \\
\Rightarrow x_n<\dfrac{3}{4}  \\
\dfrac{1}{4(1-x_{n-1})}<x_n<\dfrac{3}{4}  \\
\Rightarrow x_{n-1}<\dfrac{2}{3} \\
\text{同理} 
\Rightarrow x_{n-2}<\dfrac{1}{2}  \\
\therefore \forall n,x_n<\dfrac{1}{2} \\
\text{又} x_{n+1}=\dfrac{1}{4(1-x_n)} > x_n \\
\Leftrightarrow (2x_n-1)^2>0
\Rightarrow \text{True}  \\
X=\lim_{n \to \infty} x_n \text{ exists}  \\
x_{n+1}>\dfrac{1}{4(1-x_n)}  \\
\Rightarrow X\ge \dfrac{1}{4(1-X)}  \\
\Rightarrow X=\dfrac{1}{2} 
\end{array}
$$

</div>


### T4

<div class="cbox">

设 $x_1 \in (0, 1), x_{n+1} = x_n(1 - x_n), n \in \mathbb{N}_+$, 证明: 数列 $\{nx_n\}$ 收敛, 并求其极限.

</div>

$$
\begin{array}{c}
\lim_{n \to \infty} \dfrac{\dfrac{1}{x_n} }{n} \\
\stackrel{\text{ Stolz Theorem }}{\Longleftarrow}
\lim_{n \to \infty} \dfrac{1}{x_n} -\dfrac{1}{x_{n-1}}  \\
=\lim_{n \to \infty} \dfrac{1}{x_{n-1}(1-x_{n-1})} -\dfrac{1}{x_{n-1}} \\
=\lim_{n \to \infty} \dfrac{1}{1-x_{n-1}}   \\
=\dfrac{1}{1-\lim_{n \to \infty} x_{n-1}} 
\end{array} \\
$$

对于$x$,

$$
\begin{array}{c}
\left. \begin{array}{ll}
x_1\le \dfrac{1}{1},x_2<\min(x_1,1-x_1)\le \dfrac{1}{2}   \\
x_n\le \dfrac{1}{n},n\ge 2 
\Rightarrow 
x_{n+1}<\dfrac{1}{n}(1-\dfrac{1}{n} )=\dfrac{n-1}{n^2} <\dfrac{1}{n+1}
\end{array} \right\} \\
\Rightarrow x_n\le \dfrac{1}{n} \\
0<x_n\le  \dfrac{1}{n} \\
\stackrel{\text{Squeeze Theorem}}{\Longrightarrow}  \\
\lim_{n \to \infty} x_n=0 \\
\Rightarrow 
\lim_{n \to \infty} \dfrac{\dfrac{1}{x_n} }{n} =\dfrac{1}{1-\lim_{n \to \infty} x_{n}}=1 \\
\Rightarrow \lim_{n \to \infty} nx_n=1
\end{array}
$$

### T5

<div class="cbox">

求极限 $\lim_{n \to \infty} (n!e - [n!e])$.

</div>

<div class='pbox'>

$$
\begin{array}{c}
a_n=n!e-[n!e] \\
=\lim_{n \to \infty} \{ n!e \}  \\
=\lim_{n \to \infty} {\left\{ \sum _{i = 0} ^{\infty}  \dfrac{n!}{i!}  \right\}}  \\
=\lim_{n \to \infty} {\left\{ \sum _{i = n+1} ^{\infty} \dfrac{n!}{i!}   \right\}} \\
=\lim_{n \to \infty} {\left\{ \dfrac{1}{n+1} +\dfrac{1}{(n+1)(n+2)} +\dfrac{1}{(n+1)(n+2)(n+3)} +\ldots \right\}}  \\
<\lim_{n \to \infty} {\left\{ \sum _{i = 1} ^{\infty} (n+1)^{-i}  \right\}}  \\
=\lim_{n \to \infty} {\left\{ \dfrac{1}{n}  \right\}}  \\
=0
\end{array}
$$

</div>



### T6

<div class="cbox">

求极限 $\lim_{n \to \infty} a_n(\frac{1}{n + 1} + \frac{1}{n + 2} + \dots + \frac{1}{n + n})$.

</div>

<div class='pbox'>

$$
\begin{array}{c}
x>\ln(x)+1 \\
\Rightarrow \dfrac{1}{x}\in(\ln(\dfrac{x}{x-1}),\ln(\dfrac{x+1}{x} ) )  \\
\Rightarrow a_n\in (\sum _{i = n+1} ^{2n} \ln(\dfrac{i}{i-1}),\sum _{i = n+1} ^{2n} \ln(\dfrac{i+1}{i} ) ) \\
=(\ln(\dfrac{2n}{n}),\ln(\dfrac{2n+1}{n+1} ) ) \\
\stackrel{\text{Squeeze Theorem}}{\Longrightarrow}
\lim_{n \to \infty} a_n=\ln(2)
\end{array}
$$

</div>



### T7

<div class="cbox">

设数列 $x_n = (1 + \frac{1}{2})(1 + \frac{1}{2^2})\dots(1 + \frac{1}{2^n})$, 证明 $\lim_{n \to \infty} x_n$ 存在.

</div>

$$
\begin{array}{c}
x_n \text{ is obviously incresing}  \\
\ln(x_n)=\sum_{i=1}^n \ln(1+\dfrac{1}{2^i} ) \\
<\sum _{i = 1} ^{n} \dfrac{1}{2^i}  \\
<1 \\
\Rightarrow x_n<e
\Rightarrow \lim_{n \to \infty} x_n \text{exists}

\end{array}
$$