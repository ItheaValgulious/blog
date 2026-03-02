---
title: A Fun Problem about Function Limits
tags: 
  - math
  - math-analysis
  - whims
date: 2025-11-10 14:28:49
---

# A Fun Problem about Function Limits

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f(x)\in C[0,+\infty) \\
\forall a>0,\lim_{n \to \infty} f(na)=0
\end{cases}
\Rightarrow \lim_{x \to +\infty} f(x)=0
\end{gathered}
$$

</div>

<div class='pbox'>

反证,考虑存在$\epsilon$和不合法的序列$x_n$, $\lim_{n \to \infty} x_n=+\infty$ ,$f(x_n)>\epsilon$.

那么容易证明存在序列$\delta_n,\forall x\in (x_i-\delta_i,x_i+\delta _i)$,有 $\vert f(x)-f(x_i) \vert \le \dfrac \epsilon2$,即$f(x)>\dfrac\epsilon2$

设$I_n=(x_n-\delta_n,x_n+\delta_n)$,我们希望存在一个$a$使得$na$在无限多个$I$中.

考虑假设我们让$a$在$[l,r]$中,那么$na\in I_k$就是$n\in (\dfrac{x_n-\delta_n}{a} ,\dfrac{x_n+\delta_n}{a} )$,那么合法的$n$对这个$k$也就是 $(\dfrac{x_n-\delta_n}{r} ,\dfrac{x_n+\delta_n}{l} )$.

这个区间的长度是 $\dfrac{x_n(r-l)}{lr} +\dfrac{2\delta_n(r-l)}{lr}$,第二项是正的而第一项随$x_n$增大趋向无穷,所以一定存在一个整数$n$,使得有对应的$a$.

确定$n$后$a$的范围是容易的,于是你就得到新的一个区间$[l',r']$,递归下去,就有了闭区间套,也就能证明存在一个$a$,使得$na$数列与无数个$I$有交,矛盾,得证.

</div>


