---
title: Math Analysis Homework - Week 1
tags:
  - homework
  - math-analysis
date: 2025-09-15 19:05:08
---

# Math Analysis Homework - Week 1

## Class 1 Homework

### T1

<div class='cbox'>

$a_n\le b_n\le c_n, \lim_{n \to \infty} (c_n-a_n)=0  \Rightarrow a_n \text{收敛}$ 

</div>

<div class='pbox'>

Obviously wrong.

$$
\begin{array}{c}
a_n=b_n=c_n=n
\end{array}
$$

</div>


### T2

<div class='cbox'>

$$
\begin{array}{c}
a_n\le b_n\le c_n,b_n \text{收敛}  , \lim_{n \to \infty} (c_n-a_n)=0  \Rightarrow a_n \text{收敛} 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{c}
\forall \epsilon_1 > 0, \exists N_1 \ s.t.\ 
n>N_1  \Rightarrow c_n-a_n< \epsilon_1 \\
\therefore b_n-a_n\le c_n-a_n<\epsilon_1 \\
\text{又}\because \forall \epsilon_2 > 0\exists N_2 \ s.t.\ 
n>N_2  \Rightarrow b_n-B<\epsilon_2 \\
\therefore \vert a_n-B \vert \le \vert b_n-a_n \vert+\vert b_n-B \vert \le \epsilon+\epsilon_2 \\
\therefore \epsilon_1,\epsilon_2:=\frac{\epsilon}{2} 
\text{有} \\
\forall \epsilon,N:=\max(N_1,N_2), n>N  \Rightarrow  \vert a_n-B\vert < \epsilon \\
\text{Q.E.D}
\end{array}
$$

</div>

### T3

<div class='cbox'>

$$
\begin{array}{c}
\lim a_n = A, a_n\ne 0 \Rightarrow \lim \frac{a_{n+1}}{a_n} = 1 
\end{array}
$$

</div>

<div class='pbox'>

Wrong

$a_n=2^{-n}$

</div>

### T4

<div class='cbox'>

$$
\begin{array}{c}
\lim_{n \to \infty} a_nb_n = 0 \Rightarrow (\lim_{n \to \infty} a_n)(\lim_{n \to \infty} b_n) =0
\end{array}
$$

</div>

<div class='pbox'>

Wrong

$$
\begin{array}{c}
a_n=(n \bmod 2) \\
b_n= ((n+1) \bmod 2)
\end{array}
$$

</div>

### T5

<div class='cbox'>

$$
\begin{array}{c}
\lim_{n \to \infty} \dfrac{b_n}{a_n} =1, \lim_{n \to \infty} a_n=A  \Rightarrow \lim_{n \to \infty} b_n = A
\end{array}
$$

</div>

<div class='pbox'>

不妨设$A>0$,又因为取$\epsilon<A$可以让$n>N$时$a_n>0$,故不妨设$a_n>0$

又$,\epsilon_1<1,\epsilon_2<A$

$$
\begin{array}{c}
\forall \epsilon_1 \exists N_1 \ s.t.\ 
\vert \dfrac{a_n}{b_n} - 1 \vert < \epsilon_1 \\

\forall \epsilon_2 \exists N_2 \ s.t.\ 
\vert a_n - A \vert < \epsilon_2 
 \\

\therefore \dfrac{a_n}{b_n} \in (1-\epsilon_1,1+\epsilon_1) \\
a_n\in (A-\epsilon_2,A+\epsilon_2) \\
\therefore

b_n= \frac{a_n}{\frac{a_n}{b_n}} \in (\dfrac{A-\epsilon_2}{1+\epsilon_1},\dfrac{A+\epsilon_2}{1-\epsilon_1})\\
\therefore  b_n-A \in (\dfrac{-A\epsilon_1-\epsilon_2}{1+\epsilon_1},\dfrac{A\epsilon_1+\epsilon_2}{1-\epsilon_1} ), \\
\vert b_n-A \vert \le \dfrac{A\epsilon_1+\epsilon_2}{1-\epsilon_1}<\epsilon \\
\epsilon_1:= \dfrac{\epsilon}{100A} ,\epsilon_2:=\dfrac{\epsilon}{100} \\
\Rightarrow \vert b_n-A \vert \le \dfrac{A\epsilon_1+\epsilon_2}{1-\epsilon_1}=\dfrac{\dfrac{\epsilon}{50} }{1-\dfrac{\epsilon}{100A} }  \\

\text{let } \epsilon<A  \Rightarrow 1-\dfrac{\epsilon}{100A} >\dfrac{1}{50}  \\

\therefore N=\max(N_1,N_2) \Rightarrow n>A \Rightarrow \vert b_n-A \vert < \epsilon \\

\text{Q.E.D}

\end{array}
$$


</div>

### T6

<div class='cbox'>

$$
\begin{array}{c}
\lim_{n \to \infty} \dfrac{3n^2+n}{2n^2-1} = \dfrac{3}{2} 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{c}
\dfrac{3n^2+n}{2n^2-1}-\dfrac{3}{2}>\dfrac{3n^2}{2n^2}-\dfrac{3}{2}=0  \\
\dfrac{3n^2+n}{2n^2-1}-\dfrac{3}{2}=\dfrac{3n^2+n-\frac{3}{2}(2n^2-1)}{2n^2-1} = \dfrac{n+\dfrac{3}{2} }{2n^2-1}\stackrel{n>1}{<} \dfrac{2n}{n^2} =\dfrac{2}{n} <\epsilon \\
\therefore
N:=\dfrac{2}{\epsilon} +114514 \\
\text{Q.E.D}
\end{array}
$$

</div>


### T7

<div class='cbox'>

$$
\begin{array}{c}
\lim_{n \to \infty} \sqrt{n^2+n}-n=\dfrac{1}{2}
\end{array}
$$

</div>



<div class='pbox'>

$$
\begin{array}{c}
\sqrt{n^2+n}-n=\dfrac{(\sqrt{n^2+n}-n)(\sqrt{n^2+n}+n)}{\sqrt{n^2+n}+n} \\
=\dfrac{n}{\sqrt{n^2+n}+n} \\
=\dfrac{1}{1+\sqrt{1+\frac{1}{n}}} \\
{\left \vert \dfrac{1}{1+\sqrt{1+\frac{1}{n}}}-\dfrac{1}{2}  \right \vert}  \\
= \dfrac{1}{2}-\dfrac{1}{1+\sqrt{1+\frac{1}{n}}} \\
=\dfrac{\sqrt{1+\frac{1}{n}}-1}{2(1+\sqrt{1+\frac{1}{n}})} \\
<\sqrt{1+\frac{1}{n}}-1 \\
\stackrel{\text{Bernoulli Inequality}}{<}1+\dfrac{1}{2n} -1 \\
=\dfrac{1}{2n} \\

\therefore N:=\frac{1}{2\epsilon}+100 \\

\text{Q.E.D}
\end{array}
$$

</div>

### T8

<div class='cbox'>

$$
\begin{array}{c}
\dfrac{n^2\arctan(n)}{1+n^2}=\dfrac{\pi}{2}
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{c}
\dfrac{n^2\arctan(n)}{1+n^2} \\
=\dfrac{n^2}{1+n^2}\arctan(n) \\
\end{array}
$$

<div class='cbox'>

$$
\begin{array}{c}
\lim_{n \to \infty} \dfrac{n^2}{1+n^2}=1
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{c}
\lim {\left \vert \dfrac{n^2}{1+n^2}-1 \right \vert} =\dfrac{1}{1+n^2}<\dfrac{1}{n} \\
N:=\dfrac{1}{\epsilon}+100 \\
\text{Q.E.D}
\end{array}
$$

</div>

<div class='cbox'>

$$
\begin{array}{c}
\lim_{n \to \infty} \arctan(n)=\dfrac{\pi}{2} 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{c}
N:=\tan(\dfrac{\pi}{2}-\dfrac{\epsilon}{2})
 \Rightarrow  \\
\forall \epsilon, \vert \arctan(n)-\dfrac{\pi}{2}\vert =\dfrac{\pi}{2}-\arctan(n)=\dfrac{\epsilon}{2}<\epsilon \\

\text{Q.E.D}
\end{array}
$$

</div>

<div class='cbox'>

$$
\begin{array}{c}
(\lim a_n)(\lim_{n \to \infty} b_n) = X,a_n>0,b_n>0  \Rightarrow  \lim_{n \to \infty} a_nb_n=X
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{c}
A:=\lim a_n,B:=\lim b_n \\
\forall \epsilon_1, \exists N_1 \ s.t.\ 
n>N_1  \Rightarrow  {\left \vert a_n-A \right \vert} < \epsilon \\

\forall \epsilon_2, \exists N_2 \ s.t.\ 
n>N_2  \Rightarrow  {\left \vert b_n-B \right \vert} < \epsilon \\

\therefore n>\max(N_1,N_2)  \Rightarrow \\
  a_n \in (A-\epsilon_1,A+\epsilon_1),b_n\in (B-\epsilon_2,B+\epsilon_2) \\
\Rightarrow  \\
a_nb_n \in ((A-\epsilon_1)(B-\epsilon_2),(A+\epsilon_1)(B+\epsilon_2)) \\
\vert a_nb_n-AB\vert < A\epsilon_2+B\epsilon_1+\epsilon_1\epsilon_2\\
\forall \epsilon, \epsilon_2:=\dfrac{\epsilon}{4A},\epsilon_1:=\dfrac{\epsilon}{4B} \\
\therefore \vert a_nb_n-AB\vert=\dfrac{\epsilon}{2}+\dfrac{\epsilon^2}{16AB}\stackrel{\epsilon<AB}{<}\epsilon \\

\text{Q.E.D}
\end{array}
$$

</div>

$$
\begin{array}{c}
\lim_{n \to \infty} \dfrac{n^2\arctan(n)}{1+n^2}=\lim_{n \to \infty} \dfrac{n^2}{1+n^2} \lim_{n \to \infty} \arctan(n)=1\times \dfrac{\pi}{2} = \dfrac{\pi}{2} \\

\text{Q.E.D}
\end{array}
$$



</div>

## Class 2

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

##### Solution 1

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
\therefore N:=N_1+N_2+N_3 \\ s.t.\\ 
n>N  \\ 
\Rightarrow  (a-\epsilon)^n<A(a-\epsilon_1)^{n-N_1}<\prod_i a_i<A(a+\epsilon_1)^{n-N_1}<(a+\epsilon)^n\\
\Rightarrow {\left \vert \sqrt[n]{ \prod_i a_i } -a \right \vert} <\epsilon 
\\
\text{Q.E.D}
\end{array}
$$

##### Solution 2

唐. 可以用调和均值/算数均值夹两边.

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

若存在$x_N>a$,则$n>N$时$x_n>a$,$\lim_{n \to \infty} x_N>a$,则$\exists A\in (x_N,A)$. 并有$\forall i\ge N, x_i>A>a$,则

$$
\begin{array}{c}
\lim_{n \to \infty} \frac{\sum _{i = 1} ^{n}  x_i}{n} \\
>\lim_{n \to \infty} \frac{\sum _{i = 1} ^{N}  a_i}{n}+\frac{n-N}{n}(a+(A-a))
=A>a
\end{array}
$$

矛盾,故$\forall i,x_i<a$

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

## Class 3

### T1

<div class='cbox'>

$\lim_{n \to \infty} \frac{1 + \frac{1}{\sqrt{2}} + \cdots + \frac{1}{\sqrt{n}}}{\ln \sqrt{n}}$


</div>


<div class='pbox'>

$$
\begin{array}{c}
\lim_{n \to \infty} \frac{1 + \frac{1}{\sqrt{2}} + \cdots + \frac{1}{\sqrt{n}}}{\ln \sqrt{n}} \\
\stackrel{\text{Stolz Theorem}}{\Leftarrow  }\lim_{n \to \infty} \dfrac{\dfrac{2}{\sqrt n} }{\ln\dfrac{n}{n-1} }  \\
\stackrel{x>1 \Rightarrow \ln(x)>2\frac{x-1}{x+1} }{>}\lim_{n \to \infty} \dfrac{\dfrac{2}{\sqrt{ n } } }{\dfrac{2}{2n-1}  }\\
=+\infty

\end{array}
$$

</div>



### T2

<div class='cbox'>

$\lim_{n \to \infty} \frac{1 + \sqrt{2} + \sqrt[3]{3} + \cdots + \sqrt[n]{n}}{n}$

</div>

<div class='pbox'>

$$
\begin{array}{c}
\lim_{n \to \infty} \frac{1 + \sqrt{2} + \sqrt[3]{3} + \cdots + \sqrt[n]{n}}{n} \\
\stackrel{\text{Stolz Theorem}}{\Leftarrow }\lim_{n \to \infty} \dfrac{\sqrt[n]{n}}{1}  \\
=1
\end{array}
$$

</div>

### T3

<div class='cbox'>

$\lim_{n \to \infty} \frac{a_1 + 2a_2 + \cdots + na_n}{\sum_{i=1}^n i}$ (已知 $\lim_{n \to \infty} a_n = a$)

</div>

<div class='pbox'>

$$
\begin{array}{c}
\lim_{n \to \infty} \frac{a_1 + 2a_2 + \cdots + na_n}{\sum_{i=1}^n i} \\
\stackrel{\text{Stolz Theorem}}{\Leftarrow }
\lim_{n \to \infty} \dfrac{na_n}{n} \\
=a
\end{array}
$$

</div>


### T4

<div class='cbox'>

计算极限 $\lim_{n \to \infty} (n!)^{\frac{1}{n^2} }$.

</div>

<div class='pbox'>

$$
\begin{array}{c}
\left. \begin{array}{ll}
1<(n!)^{\frac{1}{n^2} }<(n^n)^{\frac{1}{n^2} }=n^{\frac{1}{n} } \\
\lim_{n \to \infty} 1=\lim_{n \to \infty} n^{\frac{1}{n} }=1
\end{array} \right\} \\
\stackrel{\text{Squeeze Theorem}}{\Longrightarrow } \lim_{n \to \infty} (n!)^{\frac{1}{n^2} }=1
\end{array}
$$

</div>

### T5

<div class='cbox'>

设 $x_n = \frac{1}{n^2} \sum_{k=0}^n \ln \binom{n}{k}$, $n=1,2,\cdots$, 求极限 $\lim_{n \to \infty} x_n$.

</div>

<div class='pbox'>

$$
\begin{array}{c}
\frac{1}{n^2} \sum_{k=0}^n \ln \binom{n}{k} \\
\stackrel{\text{Stolz Theorem}}{\Leftarrow }
\dfrac{\sum _{i = 0} ^{n} \ln\binom{n}{i}-\sum _{i = 0} ^{n-1}  \ln \binom{n-1}{i}}{2n-1}  \\
=\dfrac{\sum _{i = 0} ^{n-1} \ln(\dfrac{n}{n-i} )}{2n-1}  \\
=\dfrac{\ln(\dfrac{n^n}{n!} )}{2n-1}  \\
= \dfrac{n\ln(\dfrac{n}{\sqrt[n]{ n! } } )}{2n-1} \\
\text{According to homework class-2:} \\
\lim_{n \to \infty} \dfrac{\sqrt[n]{ n! } }{n} =\dfrac{1}{e} \\
\Rightarrow \lim_{n \to \infty}  \dfrac{n\ln(\dfrac{n}{\sqrt[n]{ n! } } )}{2n-1}  \\
=\lim_{n \to \infty} \dfrac{n}{2n-1} \lim_{n \to \infty} \ln(\dfrac{n}{\sqrt[n]{ n! } } ) \\
=\dfrac{1}{2} 

\end{array}
$$

</div>

还是用了连续性/kk

### T6

<div class='cbox'>

设 $\lim_{n \to \infty} n(A_n - A_{n-1}) = 0$, 试证: 当极限 $\lim_{n \to \infty} \frac{A_1 + A_2 + \cdots + A_n}{n}$ 存在时, $\lim_{n \to \infty} A_n = \lim_{n \to \infty} \frac{A_1 + A_2 + \cdots + A_n}{n}$.

</div>

<div class='pbox'>

$$
\begin{array}{c}
x_n:=\sum _{i = n} ^{n} \Delta A_i i \\
=\sum _{i = 1} ^{n}  i(A_i-A_{i-1}) \\
=nA_n-\sum_{i=1}^{n-1} A_i \\
\lim_{n \to \infty} \dfrac{x_n}{n} \\
\stackrel{\text{Stolz Theorem}}{\Leftarrow  } \dfrac{x_n-x_{n-1}}{n-(n-1)} =n\Delta A_n
=0 \\
\therefore \lim_{n \to \infty} A_n- \lim_{n \to \infty}  \dfrac{\sum _{i = 1} ^{n-1}  A_i}{n-1} = \lim_{n \to \infty} \dfrac{x_n}{n} =0 \\
\lim_{n \to \infty} A_n=a
\end{array}
$$

</div>

