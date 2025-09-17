---
title: Math Analysis Homework - Class2
tags:
  - math-analysis
  - homework
date: 2025-09-17 16:10:45
---



### T1

<div class="cbox">

$\lim_{n\to\infty} \frac{(-2)^n + 3^n}{(-2)^{n+1} + 3^{n+1}}$

</div>

<div class='pbox'>

$$
\lim_{n \to \infty}  \frac{(-2)^n + 3^n}{(-2)^{n+1} + 3^{n+1}} \\
\lim_{n \to \infty}  =\frac{1}{3}  \frac{(\frac{-2}{3})^n +1}{(\frac{-2}{3})^{n+1} +1}  \\
\lim_{n \to \infty}  =\frac{1}{3} 
$$

</div>


### T2

<div class="cbox">

$\lim_{n\to\infty} \left[ \frac{1}{1 \cdot 2} + \frac{1}{2 \cdot 3} + \dots + \frac{1}{n(n+1)} \right]$

</div>

<div class='pbox'>

$$
=\lim_{n \to \infty}  \sum_{i=1}^n \frac{1}{i(i+1)} \\
=\lim_{n \to \infty}  \sum_{i=1}^n \frac{1}{i} -\frac{1}{i+1}  \\
=\lim_{n \to \infty}  1-\frac{1}{n+1}
=1
$$

</div>




### T3

<div class="cbox">

$\lim_{n\to\infty} \left[ \frac{1}{\sqrt{n^2+1}} + \frac{1}{\sqrt{n^2+2}} + \dots + \frac{1}{\sqrt{n^2+n}} \right]$

</div>

<div class='pbox'>

$$
\begin{array}{c}
\sum _{i = 1} ^{n}  \frac{1}{\sqrt{n^2+1}} \le \sum _{i = 1} ^{n}  \frac{1}{\sqrt{n^2+i}} \le \sum _{i = 1} ^{n}  \frac{1}{\sqrt{n^2+n}}  \\
\stackrel{\text{Squeeze Theorem}}{\Longrightarrow } \\

\lim_{n \to \infty} \sum _{i = 1} ^{n}  \frac{1}{\sqrt{n^2+1}} \le L=\lim_{n \to \infty} \sum _{i = 1} ^{n}  \frac{1}{\sqrt{n^2+i}} \le \lim_{n \to \infty} \sum _{i = 1} ^{n}  \frac{1}{\sqrt{n^2+n}}  \\
\Rightarrow 
\lim_{n \to \infty} \frac{n}{\sqrt{n^2+1}} \le L \le \lim_{n \to \infty} \frac{n}{\sqrt{n^2+n}}  \\
\Rightarrow 
\lim_{n \to \infty} \frac{1}{\sqrt{1+\frac{1}{n^2} }} \le L \le \lim_{n \to \infty} \frac{1}{\sqrt{1+\frac{1}{n} }}  \\
\Rightarrow L=1
\end{array}
$$

</div>



### T4

<div class="cbox">

$\lim_{n\to\infty} \sqrt[n]{n^2-n+2}$

</div>

<div class='pbox'>

Obviously: $n>2 \Rightarrow n^2-n+2>8>1$

$$
\begin{array}{c}
\vert (n^2-n+2)^{\frac{1}{n} }-1 \vert =(n^2-n+2)^{\frac{1}{n} }-1<\epsilon \\
\Leftarrow n^2-n+2<(1+\epsilon)^n \\
\Leftarrow F(x)=n^2-n+2<1+n\epsilon+\frac{(n^2-n)\epsilon^2}{2}+\frac{n(n-1)(n-2)}{6}\epsilon^3=G(x)   \\
\exists C_1(\epsilon),C_2(\epsilon) \\ s.t.\\ 
F(x)<C_1(\epsilon)n^2,G(x)>C_2(\epsilon)n^3 \\
\therefore N:=\frac{C_1(\epsilon)}{C_2(\epsilon)} +1 \Rightarrow (n>N \Rightarrow (n^2-n+2)^{\frac{1}{n} }-1<\epsilon) \\
\therefore \lim_{n\to\infty} \sqrt[n]{n^2-n+2}=1
\end{array}
$$

</div>



### T5

<div class="cbox">

$$
\lim_{n \to \infty} \sqrt[n]{\arctan(n)}
$$

</div>

<div class='pbox'>

$$
\begin{array}{c}
1<\arctan(n)<\frac{\pi}{2} \\
\Rightarrow 1<\sqrt[n]{\arctan(n)}<\sqrt[n]{\frac{\pi}{2} } \\

\left. \begin{array}{ll}
1<\sqrt[n]{\arctan(n)}<\sqrt[n]{\frac{\pi}{2} }  \\
\lim_{n \to \infty} 1=\lim_{n \to \infty} \sqrt[n]{\frac{\pi}{2} }
\end{array} \right\}
\stackrel{\text{Squeeze Theorem}}{\Longrightarrow }
\lim_{n \to \infty} \sqrt[n]{\arctan(n)}=1
\end{array}
$$

</div>



### T6

<div class="cbox">

$$
\lim_{n \to \infty} \sqrt[n]{2\sin^2(n)+\cos^2(n)}
$$

</div>

<div class='pbox'>

同上一题,里面有界,是$1$

</div>



### T7

<div class="cbox">

$\lim_{n\to\infty} \frac{[na_n]}{n}$, 这里 $\lim_{n\to\infty} a_n = a$.

</div>

<div class='pbox'>

$$
\left. \begin{array}{ll}
\frac{na_n-1}{n} <\frac{[na_n]}{n}<\frac{na_n+1}{n}  \\
\lim_{n \to \infty} \frac{na_n+1}{n}=\lim_{n \to \infty} a_n+\lim_{n \to \infty} \frac{1}{n}=a \\
\lim_{n \to \infty} \frac{na_n-1}{n}=\lim_{n \to \infty} a_n-\lim_{n \to \infty} \frac{1}{n}=a 
\end{array} \right\} \\
\stackrel{\text{Squeeze Theorem}}{\Longrightarrow }
\lim_{n\to\infty} \frac{[na_n]}{n}=a_n
$$

</div>



### T8

<div class="cbox">

证明 $a_n=\frac{2n+(-1)^n n}{3n+1}$ 发散

</div>

<div class='pbox'>

$$
\begin{array}{c}
\left. \begin{array}{ll}
\lim_{n \to \infty} a_{2n} = \lim_{n \to \infty} \frac{6n}{6n+1} =1 \\
\lim_{n \to \infty} a_{2n+1} = \lim_{n \to \infty} \frac{2n+1}{6n+4} =\frac{1}{3} \ne 1 
\end{array} \right\} \\
\Rightarrow \{ a_n \} \text{发散} 
\end{array}
$$

</div>



### T9

<div class="cbox">

$$
a_n\ne 0,\frac{a_{n+1}}{a_n} >0,\lim_{n \to \infty} \frac{a_{n+1}}{a_n} =0 \Rightarrow \exists N \ s.t.\ 
n>N \Rightarrow \{a_n\} \text{单调} 
$$

</div>

<div class='pbox'>

$$
\begin{array}{c}
\text{use } \epsilon_1=1,\exists N_1 \\ s.t.\\ 
\lim_{n \to \infty} \frac{a_{n+1}}{a_n} <1 \\
\text{exact }  a_{n+1}<a_n
\end{array}
$$

</div>



### T10

<div class="cbox">

设 $\lim_{n\to\infty} (x_n - x_{n-1}) = d$, 证明: $\lim_{n\to\infty} \frac{x_n}{n} = d$.

</div>

<div class='pbox'>

$$
\begin{array}{c}
\forall \epsilon_1, \exists N_1 \ s.t.\ 
n>N_1 \Rightarrow \vert x_n-x_{n-1}-d \vert <\epsilon_1 \\
\Leftrightarrow x_n-x_{n-1} \in [d-\epsilon_1,d+\epsilon_1] \\

\therefore x_n=x_{N_1}+\sum _{i = N_1+1} ^{n}  (x_i-x_{i-1}) \\
\in [x_{N_1}+(n-N_1)(d-\epsilon_1),x_{N_1}+(n-N_1)(d+\epsilon_1)] \\
\therefore \frac{x_n}{n} \in [\frac{x_{N_1}-N_1(d-\epsilon_1)}{n}+d-\epsilon_1,\frac{x_{N_1}-N_1(d+\epsilon_1)}{n}+d+\epsilon_1 ] \\
\forall \epsilon,\frac{x_n}{n} -d\in[\frac{x_{N_1}-N_1(d-\epsilon_1)}{n}-\epsilon_1,\frac{x_{N_1}-N_1(d+\epsilon_1)}{n}+\epsilon_1] \\


\epsilon_1:=\frac{\epsilon}{2} ,n:=\frac{2x_{N_1}-N_1(d-\epsilon_1)}{\epsilon}  \\
\Rightarrow \vert \frac{x_n}{n} -d \vert < \epsilon
\end{array}
$$

</div>



### T11

<div class="cbox">

设 $\lim_{n\to\infty} a_n = a (a>0, n \in \mathbb{N})$, 证明: $\lim_{n\to\infty} \sqrt[n]{a_1 a_2 \dots a_n} = a$, 并由此证明:
- 若 $\lim_{n\to\infty} \frac{a_{n+1}}{a_n} = a (a>0, n \in \mathbb{N})$,则 $\lim_{n\to\infty} \sqrt[n]{a_n} = a$; 
-  $\lim_{n \to \infty} \frac{\sqrt[n]{ n! } }{n} =\frac{1}{e}$ 

</div>

<div class='pbox'>

#### (1)

$$
\begin{array}{c}
{\left \vert \sqrt[n]{ \prod_i a_i } -a \right \vert} <\epsilon \\
\Leftrightarrow a-\epsilon<\sqrt[n]{ \prod_i a_i }<a+\epsilon \\
\Leftrightarrow (a-\epsilon)^n<\prod_i a_i<(a+\epsilon)^n \\
\forall \epsilon_1,\exists N_1 \ s.t.\ 
n>N_1 \Rightarrow a_n\in [a-\epsilon_1,a+\epsilon_1] \\
\prod_i a_i=(\prod_{i=1}^{N_1} a_i) (\prod_{i=N_1+1}^{n}a_i)\in [A(a-\epsilon_1)^{n-N_1},A(a+\epsilon_1)^{n-N_1}] \\
\text{let} \epsilon_1:=\frac{\epsilon}{2} ,\text{Consider } A(a-\epsilon_1)^{n-N_1}>(a-\epsilon)^n: \\
\Leftrightarrow \frac{A}{(a-\epsilon_1)^{N_1}} >(\frac{a-\epsilon}{a-\epsilon_1} )^n \\
\text{Since }\frac{a-\epsilon}{a-\epsilon_1}<1,\exists N_2 \ s.t.\ 
n>N_2 \Rightarrow \text{不等式成立} \\
\text{右侧同理有} N_3 \\
\therefore N=N_1+N_2+N_3 \\ s.t.\\ 
n>N  \\ 
\Rightarrow  (a-\epsilon)^n<A(a-\epsilon_1)^{n-N_1}<\prod_i a_i<A(a+\epsilon_1)^{n-N_1}<(a+\epsilon)^n\\
\Rightarrow {\left \vert \sqrt[n]{ \prod_i a_i } -a \right \vert} <\epsilon 
\end{array}
$$

#### (2)

令$b_n=\frac{a_{n+1}}{a_n}$,则问题转化为(1).

#### (3)

$$

\begin{array}{c}
e=\lim_{n \to \infty} (1+\frac{1}{n})^n  \\
\Rightarrow \frac{1}{e} =\lim_{n \to \infty} (\frac{n}{n+1} )^n \\
a_n:=(\frac{n}{n+1})^n 
\text{检验符合引理}
\\
\text{Q.E.D}
\end{array}
$$

</div>



### T12

<div class="cbox">

设 $\lim_{n\to\infty} x_n = +\infty$, 证明: $\lim_{n\to\infty} \frac{x_1+x_2+\dots+x_n}{n} = +\infty$.

</div>

<div class='pbox'>

$$
\begin{array}{c}
\forall X,X_1:=X+1  \\
\lim_{n \to \infty} x_n=\infty \Rightarrow \exists N_1 \ s.t.\ 
n>N_1 \Rightarrow x_n>X_1=X+1 \\
\text{for }n>N_1,\frac{\sum _{i = 1} ^{n}  x_i}{n} =\frac{\sum _{i = 1} ^{N_1}  x_i+\sum _{i = N_1+1} ^{n}  X+1}{n} \\
>(1-\frac{N_1}{n})(X+1)  \\
n:=N_1(X+1)+100 \\
\Rightarrow \frac{\sum _{i = 1} ^{n}  x_i}{n} >X
\end{array}
$$

</div>



### T13

<div class="cbox">

$$
a_n>0,\lim_{n \to \infty} \frac{a_n}{a_{n+1}+a_{n+2}}=0 \Rightarrow a_n \text{is unbounded}  
$$

</div>

<div class='pbox'>

反证,设$\exists M$ 令$0<a_n<M$.

$$

\begin{array}{c}
\epsilon=\frac{1}{5} ,\frac{a_n}{a_{n+1}+a_{n+2}} <\frac{1}{5} \Rightarrow a_{n+1}+a_{n+2}>5a_n \\
\therefore \max(\{ a_{n+1},a_{n+2} \} )>2a_n \\
\therefore b_1=N+1,b_i=a_{b_{i-1}+1},a_{b_{i-1}+2} \text{中较大的一个的下标} 
\Rightarrow a_{b_i}>2^ia_{b_1}
\end{array}
$$

故$a$有发散子列,$a$发散.

</div>



### T14

<div class="cbox">

设数列$\{x_n\}$单调增加, $\lim_{n\to\infty} \frac{x_1+x_2+\dots+x_n}{n} = a$, 证明: $\lim_{n\to\infty} x_n = a$.

</div>

<div class='pbox'>

若存在$x_i>a$,则$n>i$时$x_n>a$,$\lim_{n \to \infty} x_i>a$. 由课上Eg知 $\frac{\sum _{i = 1} ^{n}  x_i}{n}=\lim_{n \to \infty} x_i>a$,故$x_i<a$.

于是
$$
\left. \begin{array}{ll}
\frac{\sum _{i = 1} ^{n}  x_i}{n} <x_n<a \\
\lim_{n \to \infty} a =a \\
\lim_{n \to \infty} \frac{\sum _{i = 1} ^{n}  x_i}{n}=a
\end{array} \right\}
\Rightarrow 
\lim_{n \to \infty} x_n=a
$$


</div>

