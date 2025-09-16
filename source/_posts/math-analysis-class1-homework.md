---
title: Math Analysis Class-1 Homework
tags:
  - homework math-analysis
date: 2025-09-15 19:05:08
---


# Class 1 Homework

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
\lim_n a_nb_n = 0 \Rightarrow (\lim_n a_n)(\lim_n b_n) =0
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
\lim_n \dfrac{b_n}{a_n} =1, \lim_n a_n=A  \Rightarrow \lim_n b_n = A
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
\lim_n \dfrac{3n^2+n}{2n^2-1} = \dfrac{3}{2} 
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
\lim_n \sqrt{n^2+n}-n=\dfrac{1}{2}
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
\lim_n \dfrac{n^2}{1+n^2}=1
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
\lim_n \arctan(n)=\dfrac{\pi}{2} 
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
(\lim a_n)(\lim_n b_n) = X,a_n>0,b_n>0  \Rightarrow  \lim_n a_nb_n=X
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
\lim_n \dfrac{n^2\arctan(n)}{1+n^2}=\lim_n \dfrac{n^2}{1+n^2} \lim_n \arctan(n)=1\times \dfrac{\pi}{2} = \dfrac{\pi}{2} \\

\text{Q.E.D}
\end{array}
$$



</div>