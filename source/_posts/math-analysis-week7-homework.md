---
title: Math Analysis Homework - Clas 7
tags: [math-analysis,math,homework]
---

# Math Analysis Homework - Clas 7

## Class 1

### T1

<div class='cbox'>

$$
\begin{array}{l}
f(x)=\dfrac{1+x+x^2}{1-x+x^2} 
\end{array}
$$

的四阶配亚诺余项麦克劳林级数是?

</div>

<div class='pbox'>

$$
\begin{array}{l}
f(x)=1+\dfrac{2x}{x^2-x+1} \\
\end{array}
$$

考虑

$$
\begin{array}{l}
\dfrac{1}{1-(x-x^2)} \\
=1+(x-x^2)+(x-x^2)^2+(x-x^2)^3+o((x-x^2)^3) \\
=1+x-x^2+x^2-2x^3+x^3+o(x^3) \\
=1+x-x^3+o(x^3) \\
f(x)=1+2x+2 x^2-2x^4+o(x^4)
\end{array}
$$

</div>



### T2

<div class='cbox'>

Solve $a,b$ such that

$$
\begin{array}{l}
\lim_{x \to 0} \dfrac{(a+b\cos x)\sin x-x}{x^5}=C\ne 0
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
(a+b\cos x)\sin x-x \\
=(a+b-\dfrac{bx^2}{2}+\dfrac{bx^4}{24}+o(x^5))(x-\dfrac{x^3}{6} +\dfrac{x^5}{120} )-x
\end{array}
$$

要求其$0$到$4$阶项系数为零,$5$阶非零,即

$$
\begin{array}{l}
\begin{cases}
a+b=1 \\
-\dfrac{a+b}{6} -\dfrac{b}{2} =0 \\
\dfrac{b}{24} +\dfrac{a+b}{120}+\dfrac{b}{12}  \ne 0
\end{cases}
\end{array}
$$

得

$$
\begin{array}{l}
\begin{cases}
a=\dfrac{4}{3}  \\
b=-\dfrac{1}{3} 
\end{cases}
\end{array}
$$

</div>

啥叫x的五阶无穷小啊... 如果理解成$o(x^5)$也没解啊.


### T3

<div class='cbox'>

$$
\begin{array}{l}
\lim_{x \to +\infty} (\sqrt[ 6 ]{ x^6+x^5 } -\sqrt[ 6 ]{ x^6-x^5 } )
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\text{let } t=\dfrac{1}{x}  \\
Ans=\lim_{t \to 0} \dfrac{\sqrt[6]{1+t}-\sqrt[ 6 ]{ 1-t } }{t}  \\
=\lim_{t \to 0} \dfrac{(1+t)^{-\frac56}}{6}+\dfrac{(1-t)^{-\frac56}}{6} \\
= \dfrac{1}{3} 
\end{array}
$$

</div>



### T4

<div class='cbox'>

$$
\begin{array}{l}
\alpha>-1 \\
\lim_{n \to \infty} \prod _{i = 1} ^{n} (1+\dfrac{i}{n^{\alpha+2}} )^{n^\alpha} 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
=\exp \lim_{n \to \infty} n^\alpha \sum _{i = 1} ^{n}  \ln(1+\dfrac{i}{n^{\alpha+2}} ) \\
=\exp \lim_{n \to \infty} n^\alpha \sum _{i = 1} ^{n}  \dfrac{i}{n^{\alpha+2}}  \\
=\exp \lim_{n \to \infty} n^\alpha \dfrac{1}{2n^\alpha} \\
=\sqrt e
\end{array}
$$

</div>



