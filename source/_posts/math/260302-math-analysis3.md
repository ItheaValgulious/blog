---
title: Math Analysis3(Class Note)
tags:
  - math-analysis
  - note
  - math
date: 2026-03-02 14:20:41
---


# Math Analysis3(Class Note)

## 20260302

讲了一些函数项级数和一致收敛

<div class='cbox'>

证明$[0,a]$上$f_n(x)=(1+\dfrac{x}{n} )^n$一致收敛.

</div>

<div class='pbox'>

极限是$f(x)=e^x$

法1:Dini引理,单调性+连续秒了.

法2:

老师写的是你先求导,发现:

$$
\begin{gathered}
|f_n(x)-f(x)|=e^x(1-e^{-x}(1+\dfrac xn)^n)
\end{gathered}
$$

中后面那部分单调的.

法3:

直接求导,极值点有$0=((1+\dfrac xn)^n-e^x)'=(1+\dfrac1n)^{n-1}-e^x=0$,代入发现差是$\dfrac xn e^x$.然后结束.

</div>

讲了一下柯西准则的判别方法和距离的判别方法($\lim \sup_x |f_n-f|=0$)

<div class='cbox'>

如果$f_n$ 一致连续且逐点收敛,那么它一致收敛.

</div>

<div class='pbox'>

你可以选有限个点,使得其他所有点函数值与它们的最近距离不超过$\dfrac \epsilon2$,然后再取这有限个点收敛导$\dfrac \epsilon2$的最大的$N$即可.

</div>

## 20260304

一致收敛的迪利克雷判别法和阿贝尔判别法.

证明都是柯西判别法+阿贝尔引理.

注意这里不能把阿贝尔判别法转化成迪利克雷判别法了,因为$b_n(x)$关于$n$单调和$b_n$一致有界推不出一致收敛.

讲了优级数判别法.

<div class='cbox'>

$$
\begin{gathered}
\sum x^\alpha e^{-nx},\alpha >1 \text{ uniformly convergent on } [0,+\infty)
\end{gathered}
$$

</div>

<div class='pbox'>

对$x^\alpha e^{-nx}$求导,得到其最大值为$x=\dfrac \alpha n$时.于是因为

$$
\begin{gathered}
x^\alpha e^{-nx}\le (\dfrac{\alpha}n)^\alpha e^{-\alpha}
\end{gathered}
$$

而这个东西累加收敛.优级数判别法结束.

</div>

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
S(x)\in C[0,a],a>0 \\
S_0(x)=S(x),S_n(x)=\int_0^x S(t)dt \\
\end{cases} \\
\Rightarrow S_n\rightrightarrows 0
\end{gathered}
$$

</div>

<div class='pbox'>

$S(x)$连续所以有界,直接放缩到其界$M$,得到:

$$
\begin{gathered}
S_n(x)\le \dfrac{x^n}{n!}M\le \dfrac{a^n}{n!}M 
\end{gathered}
$$

所以加起来收敛到$e^aM$,优级数判别结束.

</div>

