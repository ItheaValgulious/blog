---
title: Math Analysis Homework - Class 5
tags: [math-analysis,homework]
---

### T1

<div class='cbox'>

用柯西收敛准则证明数列收敛.

$$
\begin{array}{c}
a_n=\sum _{i = 2} ^{n}  \dfrac{\sin(ix)}{i(i+\sin(ix))} ,x\in R
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{c}
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
\end{array}
$$

</div>




### T2

<div class='cbox'>

$$
\begin{array}{c}
b_n=\sum _{i = 1} ^{n-1}  \vert a_{i+1}-a_i \vert \text{ is bounded} 
\Rightarrow a_n \text{ is convergent} 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{c}
\left. \begin{array}{ll}
b_n \text{ is increasing}  \\
b_n \text{ is bounded} 
\end{array} \right\}\Rightarrow \lim_{n \to \infty} b_n =B \\
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
\end{array}
$$

</div>



### T3

<div class='cbox'>

$$
\begin{array}{c}
\forall \epsilon , \exists N_1=N(\epsilon) \\ s.t.\\ 
i,j>N_1 \Rightarrow \vert x_i-x_j \vert < \epsilon \\
\Leftrightarrow  \\
x_n \text{ is convergent} 
\end{array}
$$

</div>

<div class='pbox'>

逆向三角不等式显然.考虑正向

$$
\begin{array}{c}
\epsilon_1:=1 \therefore i>N \Rightarrow x_i \in [x_N-\epsilon_1,x_N+\epsilon_1] \\
a_1:=x_N-\epsilon_1,b_1:=x_N+\epsilon_1 \\
\end{array}
$$

对$[a_i,b_i]$,考虑取 $\epsilon_i=\dfrac{\epsilon_{i-1}}{2}$,有$N_i=\max(N_{i-1},N(\epsilon_i)) \ s.t.\ \forall j>N_i,x_j\in [x_{N_i}-\epsilon_i,x_{N_i}+\epsilon_i]$.

于是令$a_i=\max(a_{i-1},x_{N_i}-\epsilon),b_i=\min(b_{i-1},x_{N_i}+\epsilon_i)$. 显然$\vert b_i-a_i \vert < \dfrac{1}{2^{i-1}}$,于是

$$
\begin{array}{c}
\left. \begin{array}{ll}
a_i\le a_{i+1} \\
b_i\ge b_{i+1} \\
\lim_{n \to \infty} b_n-a_n = 0
\end{array} \right\}
\\
\Rightarrow \exists!  \xi \in [a_n,b_n] \\ s.t.\\ 
\forall \epsilon,N=\min \{ i \vert b_i-a_i<\epsilon \} 
\Rightarrow 
n>N \Rightarrow \vert \xi-x_n\vert<\epsilon
\\
\text{Q.E.D}
\end{array}
$$

</div>




### T4

<div class='cbox'>

$$
\begin{array}{c}
a_0=3,a_n=a_{n-1}^2-2 \\
\Rightarrow \begin{cases}
\lim_{n \to \infty} a_n=+\infty \\
A_n:=\dfrac{a_n}{\prod_{i=0}^{n-1}a_i} \Rightarrow \lim_{n \to \infty} A_n = \sqrt{5}
\end{cases}
\end{array}
$$

</div>

<div class='pbox'>

(1)

$$
\begin{array}{c}
\left. \begin{array}{ll}
a_0=3,a_1=7,a_2=47 \\
n>2,a_{n-1}>2^{n} \Rightarrow a_n = a_{n-1}^2-2>2^{2n}-2>2^{n+1}
\end{array} \right\} \\
\stackrel{\text{induction}}{\Longrightarrow} a_n>2^{n+1} \\
\therefore
\lim_{n \to \infty} a_n\ge \lim_{n \to \infty} 2^{n+1} = \infty
\end{array}
$$

(2)

$$
\begin{array}{c}
a_n=a_{n-1}^2-2 \\
\Rightarrow (a_n-2)=(a_{n-1}-2)(a_{n-1}+2) \\
\Rightarrow \prod _{i = 1} ^{n}  (a_i+2 ) = \dfrac{a_{n+1}-2}{a_1-2} =\dfrac{a_{n+1}-2}{5}  \\
\Rightarrow  \\

A_n^2=\dfrac{a_{n}^2}{\prod _{i = 0} ^{n-1}  a_i^2}  \\
=\dfrac{a_{n+1}+2}{\prod _{i = 1} ^{n}  (a_i+2)}  \\
=5\dfrac{a_{n+1}+2}{a_{n+1}-2}  \\
\therefore \lim_{n \to \infty} A_n=\sqrt{5\dfrac{a_{n+1}+2}{a_{n+1}-2} }=\sqrt 5

\end{array}
$$




</div>

