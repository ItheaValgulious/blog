---
title: I am a pig
tags:
  - math-analysis
  - whims
date: 2026-01-06 09:29:26
---


# I am a pig

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
\sum _{n = 1} ^{\infty}   a_n=A<\infty \\
r_n=\sum _{i = n} ^{\infty} a_n \\
a_n>0
\end{cases} \\
\Rightarrow \begin{cases}
\sum _{n = 1} ^{\infty}  \dfrac{a_n}{r_n}=\infty \\
\sum _{n = 1} ^{\infty}  \dfrac{a_n}{\sqrt{r_n}}<\infty  
\end{cases}
\end{gathered}
$$

</div>

<div class='pbox'>

Sol1:

设$f(n)=r_n,f'(n)=r_{n+1}-r_{n}=-a_n$.

对第一问:

$$
\begin{gathered}
\sum_{n=1}^\infty \dfrac{-f'(n)}{f(n)} \sim \int_{x=1}^\infty \dfrac{-f'(x)}{f(x)} dx=-\ln f(x) |_{x=1}^\infty=\infty
\end{gathered}
$$

对第二问:

$$
\begin{gathered}
\sum _{n = 1} ^{\infty}  \dfrac{-f'(n)}{\sqrt{f(n)}}\sim \int_{x=1}^\infty \dfrac{-f'(x)}{\sqrt{f(x)}}  dx=-2\sqrt{f(x)}|_{x=1}^\infty<\infty
\end{gathered}
$$

只要这样的$f$存在你就赢了,而你发现比如你指定每个整数点$n$处2阶导为$0$,一阶导为$-a_n$,函数值为$r_n$,就可以分别构造每段的函数然后拼起来.存在性是显然的.或者说指定所有整数点处任意有限阶导数都是能这么做的.所以当判断收敛性的时候对任意数列你都可以大胆比拟$f(n)=a_n,f'(n)=a_{n+1}-a_n,f''(n)=f'(n+1)-f'(n)$这样的函数.

但有一个问题,积分判别法要求$f$的单调性,所以你还要保证你的$f$递减,你注意到整数点确实是单调的,那么单调性要求满足起来是容易的.

(实际上,因为你完全不要求高阶导数,完全可以直接用若干段折线).

Sol2:

但其实即使不构造$f$,你只要构造那个积分的结果的数列.

对第一问,你原来要积分$\int \dfrac{f'}{f}=\ln f$,所以令$x_n=\ln(r_{n+1})-\ln(r_{n})$.

如果直接从积分出发,则$x_n=\dfrac{a_n}{\xi},\xi\in(r_{n+1},r_n)$.不好用.因为你不能保证$n\to \infty$的时候$\dfrac{r_n}{r_{n-1}}\to 1$.但是你注意到想收敛一定有$\dfrac{a_n}{r_n}\sim 0$,于是$\dfrac{r_n}{r_{n-1}}\to 1$,就弄完了.

对于第二问也一样,构造$x_n=2\sqrt{r_{n-1}}-2\sqrt{r_n}$,则$x_n=(r_{n-1}-r_n)\dfrac1{\sqrt{\xi}}=\dfrac{a_n}{\sqrt\xi}$.这时同样没有$\sqrt{\dfrac{r_n}{r_{n-1}}}=1$.但这里你要个不等号就行了,就弄完了.

</div>

这两个做法看起来相似,但图像上考虑的话,第二个是在连续函数上放缩x轴,第一个没有.第二个里的$\xi$放缩被藏在第一个的积分上和/下和里了.

然后这个题一开始花了大量时间去考虑另一个思路,之前一个作业让你根据一个收敛数列$a_n$构造另一个收敛数列$b_n$使得$\lim \dfrac{a_n}{b_n}=\infty$,当时想的做法是考虑两个收敛的函数$f,g$,那么$f\circ g^{-1}(r_n)-f\circ g^{-1}(r_{n-1})$一定收敛,是考虑几何上把数列做了个重映射,然后这个题一开始也在想直接找一个重映射解决这个题.所以I am a pig.