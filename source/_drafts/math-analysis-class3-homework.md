---
title: Math Analysis Homework - Class 3
tags: [math-analysis,homework]
---

# Math Analysis Homework - Class 3

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

<div class='cbox'>

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

