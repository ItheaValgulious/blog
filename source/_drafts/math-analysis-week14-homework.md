---
title: Math Analysis Homework - Week 14
tags: [math,math-analysis,homework]
---

# Math Analysis Homework - Week 14

## Class 1

### T1

<div class="cbox">

2. 讨论下列无穷乘积的敛散性:
(2) $\prod_{n=1}^{\infty} \sqrt[n]{1 + \frac{1}{n}};$

</div>

<div class="pbox">

敛散性等价于

$$
\begin{gathered}
\sum_{n=1}^\infty \dfrac{\ln(1+\dfrac1n)}n \\
\because \lim_{n \to \infty}  \dfrac{\dfrac{\ln(1+\dfrac{1}{n} )}{n} }{\dfrac{1}{n^2} } =1,\sum _{n = 1} ^{\infty}  \dfrac{1}{n^2} <\infty \\
\xRightarrow{\text{ Comparison Test }}  \text{convergent} 
\end{gathered}
$$

</div>

### T2

<div class="cbox">

2. 讨论下列无穷乘积的敛散性:
(4) $\prod_{n=2}^{\infty} \left(\frac{n^2 - 1}{n^2 + 1}\right)^p \ (p \in \mathbb{R});$

</div>

<div class="pbox">

$$
\begin{gathered}
\ln(\prod_{n=2}^\infty (\dfrac{n^2-1}{n^2+1} )^p) \\
=p\sum _{n = 2} ^{\infty}  \ln(1+\dfrac{2}{n^2+1} ) \\
\because \lim_{n \to \infty}  \dfrac{\ln(1+\dfrac{2}{n^2+1} )}{\dfrac{1}{n^2} } =1,\sum _{n = 1} ^{\infty}  \dfrac{1}{n^2} <\infty \\
\xRightarrow{\text{ Comparison Test }} \text{convergent} 
\end{gathered}
$$

</div>

### T3

<div class="cbox">

3. 设数列 $\{a_n\}$, 其中
$$a_n = \begin{cases} -\frac{1}{\sqrt{k}}, & n = 2k - 1, \\ \frac{1}{\sqrt{k}} + \frac{1}{k} + \frac{1}{k\sqrt{k}}, & n = 2k. \end{cases}$$
证明: $\sum_{n=1}^{\infty} a_n$ 与 $\sum_{n=1}^{\infty} a_n^2$ 都发散, 但是 $\prod_{n=1}^{\infty} (1+a_n)$ 收敛.

</div>

<div class="pbox">

$$
\begin{gathered}
\sum _{n = 1} ^{\infty}  a_n^2 \\
=\sum _{n = 1} ^{\infty}  (\dfrac{1}{n} +(\dfrac{1}{\sqrt n} +\dfrac{1}{n} +\dfrac{1}{n^{\frac23}} ^2))
>\sum _{n = 1} ^{\infty}  \dfrac{1}{n}  \\
=\infty
\end{gathered}
$$

$$
\begin{gathered}
\sum _{n = 1} ^{\infty}  a_n=\sum _{n = 1} ^{\infty}  -\dfrac{1}{\sqrt{n}} +\dfrac{1}{\sqrt n} +\dfrac{1}{n} +\dfrac{1}{n\sqrt n}  \\
>\sum _{n = 1} ^{\infty}  \dfrac{1}{n} =\infty \\
\end{gathered}
$$

$$
\begin{gathered}
\ln(\prod _{n = 1} ^{\infty}  (1+a_n)) \\
\ln(\prod _{n = 1} ^{\infty}  (1-\dfrac{1}{\sqrt n} )(1+\dfrac{1}{\sqrt{n}} +\dfrac{1}{n} +\dfrac{1}{n\sqrt n} )) \\
=\ln(\prod _{n=1}^{\infty} (1-\dfrac{1}{n^2} )) \\
=\sum _{n = 1} ^{\infty} \ln(1-\dfrac{1}{n^2} ) \\
\sim -\sum _{n = 1} ^{\infty}  \dfrac{1}{n^2} >-\infty
\end{gathered}
$$

</div>