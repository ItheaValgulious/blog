---
title: Math Analysis Homework - Week 2
tags:
  - math-analysis
  - homework
  - math
date: 2025-09-26 14:54:31
---



# Math Analysis Homework - Week 2

## Class 4

### T1

<div class="cbox">

设 $x_1 > 1, x_{n+1} = \frac{3x_n + 1}{x_n + 3}, n = 1, 2, \dots$

</div>

<div class='pbox'>

$$
\begin{gathered}
x_n>1 \Rightarrow  1<x_{n+1}=\dfrac{3x_n+1}{x_n+3}<3 \\
\text{Inductively},x_n\in (1,3)
x_{n+1}-x_n \\
=\dfrac{3x_n+1-x_n^2-3x_n}{x_n+3} \\
=\dfrac{1-x_n^2}{x_n+3}<0 \\
\therefore \{ x_n \} \text{is bounded and decreasing} \\\lim_{n \to \infty} x_n \text{exists}. \\


x_{n+1}=\dfrac{3x_n+1}{x_n+3} \\
\Rightarrow \lim_{n \to \infty} x_{n}=\dfrac{3(\lim_{n \to \infty} x_n)+1}{(\lim_{n \to \infty} x_n)+3}  \\
\Rightarrow \lim_{n \to \infty} x_n=1
\end{gathered}
$$

</div>



### T2

<div class="cbox">

设 $0 < a_1 < b_1$, 令 $a_{n+1} = \sqrt{a_n b_n}, b_{n+1} = \frac{a_n + b_n}{2}, n \in \mathbb{N}_+$. 证明: $\{a_n\}, \{b_n\}$ 收敛于同一极限.

</div>

<div class='pbox'>

$$
\begin{gathered}
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

\end{gathered}
$$

</div>

### T3

<div class='cbox'>

设数列 $\{x_n\}$ 满足 $0 < x_n < 1$ 与 $(1 - x_n)x_{n+1} > \frac{1}{4}, n = 1, 2, 3, \dots$, 求证: $\lim_{n \to \infty} x_n = \frac{1}{2}$.

</div>

<div class='pbox'>

$$
\begin{gathered}
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
\end{gathered}
$$

</div>


### T4

<div class="cbox">

设 $x_1 \in (0, 1), x_{n+1} = x_n(1 - x_n), n \in \mathbb{N}_+$, 证明: 数列 $\{nx_n\}$ 收敛, 并求其极限.

</div>

<div class='pbox'>


$$
\begin{gathered}
\lim_{n \to \infty} \dfrac{\dfrac{1}{x_n} }{n} \\
\stackrel{\text{ Stolz Theorem }}{\Longleftarrow}
\lim_{n \to \infty} \dfrac{1}{x_n} -\dfrac{1}{x_{n-1}}  \\
=\lim_{n \to \infty} \dfrac{1}{x_{n-1}(1-x_{n-1})} -\dfrac{1}{x_{n-1}} \\
=\lim_{n \to \infty} \dfrac{1}{1-x_{n-1}}   \\
=\dfrac{1}{1-\lim_{n \to \infty} x_{n-1}} 
\end{gathered} \\
$$

对于$x$,

$$
\begin{gathered}
\begin{cases}
x_1\le \dfrac{1}{1},x_2<\min(x_1,1-x_1)\le \dfrac{1}{2}   \\
x_n\le \dfrac{1}{n},n\ge 2 
\Rightarrow 
x_{n+1}<\dfrac{1}{n}(1-\dfrac{1}{n} )=\dfrac{n-1}{n^2} <\dfrac{1}{n+1}
\end{cases} \\
\Rightarrow x_n\le \dfrac{1}{n} \\
0<x_n\le  \dfrac{1}{n} \\
\stackrel{\text{Squeeze Theorem}}{\Longrightarrow}  \\
\lim_{n \to \infty} x_n=0 \\
\Rightarrow 
\lim_{n \to \infty} \dfrac{\dfrac{1}{x_n} }{n} =\dfrac{1}{1-\lim_{n \to \infty} x_{n}}=1 \\
\Rightarrow \lim_{n \to \infty} nx_n=1
\end{gathered}
$$

</div>



### T5

<div class="cbox">

求极限 $\lim_{n \to \infty} (n!e - [n!e])$.

</div>

<div class='pbox'>

$$
\begin{gathered}
a_n=n!e-[n!e] \\
=\lim_{n \to \infty} \{ n!e \}  \\
=\lim_{n \to \infty} {\left\{ \sum _{i = 0} ^{\infty}  \dfrac{n!}{i!}  \right\}}  \\
=\lim_{n \to \infty} {\left\{ \sum _{i = n+1} ^{\infty} \dfrac{n!}{i!}   \right\}} \\
=\lim_{n \to \infty} {\left\{ \dfrac{1}{n+1} +\dfrac{1}{(n+1)(n+2)} +\dfrac{1}{(n+1)(n+2)(n+3)} +\ldots \right\}}  \\
<\lim_{n \to \infty} {\left\{ \sum _{i = 1} ^{\infty} (n+1)^{-i}  \right\}}  \\
=\lim_{n \to \infty} {\left\{ \dfrac{1}{n}  \right\}}  \\
=0
\end{gathered}
$$

</div>



### T6

<div class="cbox">

求极限 $\lim_{n \to \infty} a_n(\frac{1}{n + 1} + \frac{1}{n + 2} + \dots + \frac{1}{n + n})$.

</div>

<div class='pbox'>

$$
\begin{gathered}
x>\ln(x)+1 \\
\Rightarrow \dfrac{1}{x}\in(\ln(\dfrac{x}{x-1}),\ln(\dfrac{x+1}{x} ) )  \\
\Rightarrow a_n\in (\sum _{i = n+1} ^{2n} \ln(\dfrac{i}{i-1}),\sum _{i = n+1} ^{2n} \ln(\dfrac{i+1}{i} ) ) \\
=(\ln(\dfrac{2n}{n}),\ln(\dfrac{2n+1}{n+1} ) ) \\
\stackrel{\text{Squeeze Theorem}}{\Longrightarrow}
\lim_{n \to \infty} a_n=\ln(2)
\end{gathered}
$$

</div>



### T7

<div class="cbox">

设数列 $x_n = (1 + \frac{1}{2})(1 + \frac{1}{2^2})\dots(1 + \frac{1}{2^n})$, 证明 $\lim_{n \to \infty} x_n$ 存在.

</div>

<div class='pbox'>

$$
\begin{gathered}
x_n \text{ is obviously incresing}  \\
\ln(x_n)=\sum_{i=1}^n \ln(1+\dfrac{1}{2^i} ) \\
<\sum _{i = 1} ^{n} \dfrac{1}{2^i}  \\
<1 \\
\Rightarrow x_n<e
\Rightarrow \lim_{n \to \infty} x_n \text{exists}

\end{gathered}
$$

</div>



## Class 5

### T1

<div class='cbox'>

用柯西收敛准则证明数列收敛.

$$
\begin{gathered}
a_n=\sum _{i = 2} ^{n}  \dfrac{\sin(ix)}{i(i+\sin(ix))} ,x\in R
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\vert a_{n+m}-a_n \vert  \\
={\left \vert \sum _{i = n+1} ^{n+m}  \dfrac{\sin(ix)}{i(i+\sin(ix))} \right \vert}    \\
< \sum _{i = n+1} ^{n+m}  {\left \vert \dfrac{\sin(ix)}{i(i+\sin(ix))}  \right \vert}  \\
< \sum _{i = n+1} ^{n+m}  \dfrac{1}{i(i-1)}  \\
= \sum _{i = n+1} ^{n+m}  \dfrac{1}{i-1} -\dfrac{1}{i}  \\
=\dfrac{1}{n} -\dfrac{1}{n+m}  \\
<\dfrac{1}{n} \\

\Rightarrow \forall \epsilon,N:=\dfrac{1}{\epsilon} +100 \\
\Rightarrow \forall i,j>N,\vert a_i-a_j \vert < \epsilon
\\
\stackrel{\text{Cauchy Convergence Theorem}}{\Longrightarrow} \\
\\
\text{Q.E.D}
\end{gathered}
$$

</div>




### T2

<div class='cbox'>

$$
\begin{gathered}
b_n=\sum _{i = 1} ^{n-1}  \vert a_{i+1}-a_i \vert \text{ is bounded} 
\Rightarrow a_n \text{ is convergent} 
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\begin{cases}
b_n \text{ is increasing}  \\
b_n \text{ is bounded} 
\end{cases}\Rightarrow \lim_{n \to \infty} b_n =B \\
a_{n+m}-a_n=\sum _{i = n+1} ^{n+m}  a_{i}-a_{i-1} \\
\le \sum _{i = n+1} ^{n+m}  \vert a_i-a_{i-1} \vert  \\
=b_{n+m} - b_n
\\
\Rightarrow 
\forall \epsilon_1, \exists N \\ s.t.\\ 
n>N \Rightarrow \vert b_n-B \vert < \epsilon_1 \\
\Rightarrow b_{n+m}-b_n< \vert b_n-B \vert + \vert B-b_{n+m} \vert =2\epsilon_1 \\
\epsilon_1:=\dfrac{\epsilon}{2} \Rightarrow \forall x,y>N,\vert a_x-a_y \vert < \epsilon \\
\stackrel{\text{Cauchy Convergence Theorem}}{\Longrightarrow} \\
\\
\text{Q.E.D}
\end{gathered}
$$

</div>



### T3

<div class='cbox'>

$$
\begin{gathered}
\forall \epsilon , \exists N_1=N(\epsilon) \\ s.t.\\ 
i,j>N_1 \Rightarrow \vert x_i-x_j \vert < \epsilon \\
\Leftrightarrow  \\
x_n \text{ is convergent} 
\end{gathered}
$$

</div>

<div class='pbox'>

逆向三角不等式显然.考虑正向

$$
\begin{gathered}
\epsilon_1:=1 \therefore i>N \Rightarrow x_i \in [x_N-\epsilon_1,x_N+\epsilon_1] \\
a_1:=x_N-\epsilon_1,b_1:=x_N+\epsilon_1 \\
\end{gathered}
$$

对 $[a_i,b_i]$ ,考虑取 $\epsilon_i=\dfrac{\epsilon_{i-1}}{2}$ ,有 

$$
N_i=\max(N_{i-1},N(\epsilon_i)) \ s.t.\ \forall j>N_i,x_j\in [x_{N_i}-\epsilon_i,x_{N_i}+\epsilon_i]
$$

于是令$a_i=\max(a_{i-1},x_{N_i}-\epsilon),b_i=\min(b_{i-1},x_{N_i}+\epsilon_i)$. 显然$\vert b_i-a_i \vert < \dfrac{1}{2^{i-1}}$,于是

$$
\begin{gathered}
\begin{cases}
a_i\le a_{i+1} \\
b_i\ge b_{i+1} \\
\lim_{n \to \infty} b_n-a_n = 0
\end{cases}
\\
\Rightarrow \exists!  \xi \in [a_n,b_n] \\ s.t.\\ 
\forall \epsilon,N=\min \{ i \vert b_i-a_i<\epsilon \} 
\Rightarrow 
n>N \Rightarrow \vert \xi-x_n\vert<\epsilon
\\
\text{Q.E.D}
\end{gathered}
$$

</div>




### T4

<div class='cbox'>

$$
\begin{gathered}
a_0=3,a_n=a_{n-1}^2-2 \\
\Rightarrow \begin{cases}
\lim_{n \to \infty} a_n=+\infty \\
A_n:=\dfrac{a_n}{\prod_{i=0}^{n-1}a_i} \Rightarrow \lim_{n \to \infty} A_n = \sqrt{5}
\end{cases}
\end{gathered}
$$

</div>

<div class='pbox'>

(1)

$$
\begin{gathered}
\begin{cases}
a_0=3,a_1=7,a_2=47 \\
n>2,a_{n-1}>2^{n} \Rightarrow a_n = a_{n-1}^2-2>2^{2n}-2>2^{n+1}
\end{cases} \\
\stackrel{\text{induction}}{\Longrightarrow} a_n>2^{n+1} \\
\therefore
\lim_{n \to \infty} a_n\ge \lim_{n \to \infty} 2^{n+1} = \infty
\end{gathered}
$$

(2)

$$
\begin{gathered}
a_n=a_{n-1}^2-2 \\
\Rightarrow (a_n-2)=(a_{n-1}-2)(a_{n-1}+2) \\
\Rightarrow \prod _{i = 1} ^{n}  (a_i+2 ) = \dfrac{a_{n+1}-2}{a_1-2} =\dfrac{a_{n+1}-2}{5}  \\
\Rightarrow  \\

A_n^2=\dfrac{a_{n}^2}{\prod _{i = 0} ^{n-1}  a_i^2}  \\
=\dfrac{a_{n+1}+2}{\prod _{i = 1} ^{n}  (a_i+2)}  \\
=5\dfrac{a_{n+1}+2}{a_{n+1}-2}  \\
\therefore \lim_{n \to \infty} A_n=\sqrt{5\dfrac{a_{n+1}+2}{a_{n+1}-2} }=\sqrt 5

\end{gathered}
$$

</div>

## Class 6

### T1

<div class='cbox'>

$$
\begin{gathered}
A,B \text{is upper bounder},S\subset\{ x+y\vert x\in A,y\in B \}   \\
\Rightarrow \sup S\le \sup A+\sup B
\end{gathered}
$$

</div>

<div class='pbox'>

显然$S$有界,则$\sup S$存在.

若$\sup S>\sup A+\sup B$,取$M=\sup A+\sup B$,

则$\forall x\in A,y\in B,x\le \sup A,y\le \sup B \Rightarrow x+y \le M$

于是$M$是比$\sup S$小的上界,矛盾.

故$\sup S\le \sup A+\sup B$

eg. 当$A,B,S$均为有限集恰好为 $\{ x+y\vert x\in A,y\in B \} $ 时显然严格不等号不成立.

</div>

### T2

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
A,B \text{ aren't empty},\alpha\ge 0, \\
C=A+\alpha B =\{ x\vert x=a+\alpha b,a\in A,b\in B \}  
\end{cases} \\
\Rightarrow \sup(A+\alpha B)=M=\sup A+\alpha \sup B

\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\forall c\in C=a+\alpha b, \\
a\le \sup A,b\le \sup B \Rightarrow a+\alpha b\le \sup A+\alpha \sup B=M \\
\forall M'<M,\epsilon=M-M' \\
\text{let }X=\sup A-\dfrac{\epsilon}{3} ,Y=\sup B+\dfrac{\epsilon}{3\alpha} \\
\text{According to the definition of supremum, } \exists a>X\in A,y>Y\in B \\
\Rightarrow  \exists c=a+b\in C,c>X+Y>M'
\Rightarrow \sup C=\sup A+\alpha \sup B
\end{gathered}
$$

</div>



### T3

<div class='cbox'>

$$
\begin{gathered}
A\subset B \\
\Rightarrow \sup A\le \sup B,\inf A \ge \inf B
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\text{if }\sup A>\sup B \\
\text{let }M=\sup B
\stackrel{\text{Def of supremum}}{\Longrightarrow} \exists a\in A,a>M=\sup B \\
\begin{cases}
a\in A \stackrel{A\subset B}{\Longrightarrow} a\in B \\
a>\sup B
\end{cases}
\Rightarrow \text{False}  \\
\therefore \sup A\le \sup B
\end{gathered}
$$

取 $C=-A,D=-B,C\subset D,\sup C\le \sup D \Rightarrow \inf A\ge \inf B$,

</div>

### T4

<div class='cbox'>

$$
\begin{gathered}
\forall x\in A,y\in B,x\le y \\
\Rightarrow \sup A\le \inf B
\end{gathered}
$$

</div>

<div class='pbox'>

假设$\sup A>\inf B$,$M\in (\sup A,\inf B)$,由$\sup A$定义$\exists a\in A,a>M$,由$\inf B$定义$\exists b\in B,b<M$,故$a>M>b$,与$\forall x\in A,y\in B,x\le y$矛盾.

故$\sup A\le \inf B$

</div>

## Class 7

### T1

<div class='cbox'>

$$
\begin{gathered}
\lim_{x \to x_0} \sqrt{ x } =\sqrt x_0
\end{gathered}
$$

</div>

<div class='pbox'>

if $x_0\ne 0$
$$
\begin{gathered}
\vert \sqrt x-\sqrt {x_0} \vert  \\
={\left \vert \dfrac{x-x_0}{\sqrt x+\sqrt {x_0}} \right \vert}   \\
\le \dfrac{\delta}{\sqrt{x_0} }  \\
\therefore \delta:=\dfrac{\sqrt{x_0}\epsilon}{2} \Rightarrow  \\
\forall \epsilon,x\in N(x_0,\delta),\vert \sqrt x-\sqrt {x_0} \vert <\epsilon
\end{gathered}
$$

if $x_0=0,\sqrt x_0=0$

$$
\begin{gathered}
\delta:=\dfrac{\epsilon^2}{4} \Rightarrow \forall \epsilon,x\in N(x_0,\delta), \\
\vert \sqrt x-\sqrt {x_0} \vert =\dfrac{\epsilon}{4} <\epsilon
\end{gathered}
$$

$$
\begin{gathered}

\text{Q.E.D}
\end{gathered}
$$

</div>





### T2

<div class='cbox'>

$$
\begin{gathered}
\lim_{x \to +\infty} (\sqrt{ x+1 } -\sqrt{ x-1 } ) =0
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\sqrt{ x+1 } -\sqrt{ x-1 }   \\
=\dfrac{2}{\sqrt{x+1}+\sqrt{x-1}}  \\
<\dfrac{1}{\sqrt{x}} \\

\therefore \forall \epsilon \in (0,1),
\delta:=\dfrac{4}{\epsilon^2}, \\
x>\delta \Rightarrow \sqrt{x+1}-\sqrt{ x-1 } <\dfrac{1}{\sqrt{ x } } =\dfrac{\epsilon}{2} < \epsilon
\\
\text{Q.E.D}
\end{gathered}
$$

</div>


