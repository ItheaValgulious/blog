---
title: Divergence Theorem in Physics
tags:
  - physics
  - math
  - whims
date: 2026-03-27 09:29:38
---

# Divergence Theorem in Physics

很早就知道数学中这个散度定理和物理电磁/引力的高斯公式应该是一回事的,所以考虑一下是怎么回事.

## 高斯公式的引力形式

<div class='cbox'>

高斯公式的引力形式:

$$
\begin{gathered}
\iint_{\delta V} gdS=-4\pi GM
\end{gathered}
$$

</div>

<div class='pbox'>

回忆高斯定理:对闭区域$V$上的可微多元向量值函数$f:R^3\to R^3$,有:

$$
\begin{gathered}
\iint_{\delta V} f dS = \iiint_V \nabla \cdot f dV
\end{gathered}
$$

那么我们让$Mf$是引力场的函数(因为后面有密度所以把$M$提出来)则左边形式已经对了,关键是算右边.

一个任意形状的引力场我们不知道怎么写,所以先考虑一个质点的引力场.此时有 $Mf(\vec r)=\dfrac{GM}{|r|^3}\vec r$.

直接硬做:$f_x(r)=\dfrac{M}{s^{\frac32}} x$,其中$s=\sum_x x^2$,则

$$
\begin{gathered}
\dfrac {df_x}{dx}=GM(s^{-\frac32}-3s^{-\frac52}x^2)=GMs^{-\frac52}(s-3x^2) \\
\Rightarrow \nabla\cdot f=\sum_x \dfrac{df_x}{dx} =GMs^{-\frac52}(3s-3\sum_x x^2)=0
\end{gathered}
$$

于是你得到除了原点外的散度都为$0$.原点是一个奇点,我还不会狄拉克函数,所以先不管那里.

一个点的现在你明白了,现在考虑一个体积的引力场.

<div class='bbox'>

然后这里我脑抽了在于没想明白为什么我可以直接把点的向量场积分起来得到整个物体的向量场:你物体的向量场中每个微元并非一个点而是一个小体积元.

然后你发现确实是脑子抽了:我们可以这么做是因为向量场关于点是连续的,所以可积性保证了当$dV\to 0$时这个区域内任意两个点在某点$x$处的引力场向量的差也趋近于$0$,所以可以说明黎曼和变成积分的时候你的误差也变成$0$.

</div>

所以你确实可以把每个点的向量场积起来得到物体的引力场.所以左侧右侧同时积分:

$$
\begin{gathered}
\iint_{S=\delta V}gdS \\
=\iint_{\vec r\in S=\delta V}(\iiint_{\vec x\in A} f_{\vec x} (\vec r)\rho(\vec x)dA)\cdot dS \\
=\iiint_{\vec x\in A}\rho(\vec x)(\iint_{\vec r\in S=\delta V}f_{\vec x} (\vec r)\cdot dS)dA  
\end{gathered}
$$

<div class='bbox'>

我为什么可以随便交换积分号?$f_x$明明是不连续的(有奇点$x$)?

这时候AI给了两种解释:

1. Fubini-Tonelli Theorem说明,由于第二行那个式子的绝对值积分有界,就能保证你随便交换.
2. 弱奇点原理:$f_x$在$x$发散的速度是$\Theta(\dfrac1{x^2})$,而你密度有界的情况下,密度对体积的积分的速度恰好是$x^2$,所以他俩乘起来就没有奇点了.你发现发散速度阶数小于维数的都是合法的.

</div>

我们先假装这个交换是比较自然的,那么考虑内层积分就是球一个质点的引力场的引力通量了,那么可以用高斯定理:

$$
\begin{gathered}
=\iiint_{\vec x\in A}\rho(\vec x)(\iiint_{\vec r\in V-B(\vec x,\delta)} \nabla\cdot f_{\vec x}(\vec r)dV-\iint_{S=\delta B(\vec x,\delta)}f_{\vec x}\cdot dS)dA \\
=\iiint_{\vec x\in A}\rho(\vec x)(-4\pi G)dA \\
=-4\pi MG
\end{gathered}
$$

这里因为有个奇点,所以你不对整个区域使用高斯定理,而是把原点$\vec x$周围的一个小球体挖掉,减掉内部边界的引力通量就是外边界的.则那个三重体积分我们知道里面的散度都是$0$所以积分完了也是$0$;而另一部分内部小圆的积分,因为对称性所以有引力场垂直于球面,容易知道通量是$4\pi \delta^2 \dfrac{G}{\delta^2}=4\pi G$(注意内部的面符号是反的).

</div>

## Ex:球壳引力公式

<div class='cbox'>

只要证明两条:
- 均匀球壳对外部引力等效于质量集中在质心
- 均匀球壳对内部引力为$0$

</div>

对于点在球内可以直接把球拆成小球和外壳.

<div class='pbox'>

那么第一条,设外部距离球心为$r$的一个点,则取半径为$r$的球面,根据对称性引力通量是$4\pi r^2 g$.而根据高斯定理你知道它是$4\pi MG$,于是得到$g=\dfrac{MG}{r^2}$,就证完了.

对第二条,设内部距离球心为$r$的一个点,仍然取这个球面,考虑其引力通量,你惊喜的发现引力通量只能是$0$,就做完了.

</div>

## 狄拉克函数

一个更简单的处理那个东西.导致你可以把单点质量的散度直接写成这个$C\delta^3$的形式

但是想严格话不能只说一点处的值是$\infty$,其他地方是$0$,而是把它看成测度和分布.感觉需要一点实分析水平,以后再说.