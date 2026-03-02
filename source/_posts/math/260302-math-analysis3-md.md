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



