---
title: Tell Semicontinuous
tags:
  - math
  - whims
date: 2025-11-28 12:06:39
---


我们生活在虚拟世界的证据:你看到了一个概念,然后他就会天天冒出来,而以前它并不会天天冒出来.

## Def

上半连续说的是向上增长的时候是连续的,函数值不能突然上升但可以突然下降.

于是一个定义是$x_0$处上半连续定义为$\forall \epsilon>0$,存在$x_0$的邻域$U$使得$\forall x\in U,f(x)<f(x_0)+\epsilon$.

而同样我们可以理解$(-\infty,a)$的原像是开集,$[a,+\infty)$的原像是闭集.意思是你在一个小于$a$的地方,你往旁边走一点点还是小于$a$的(开),你在一个大于等于$a$的地方走一点点却可能是小于$a$的(闭).

第三个定义说的是

$$
\begin{gathered}
\limsup_{x\to x_0} f(x)\le f(x_0)
\end{gathered}
$$

这里的上极限是不包含$x_0$的.如果包含自身的话$\limsup_{x\to x_0}f(x)=f(x_0)$,这个和第一个是容易转化的:你上极限比$f(x_0)$大就是任意小邻域都有比$x_0$大的点.

## Conclusion

于是对任意函数$f$,取上极限后$g(x_0)=\limsup_{x\to x_0} f(x)$的函数$g$一定上半连续.

这是为什么呢.你注意上极限其实也是

$$
\begin{gathered}
g(x_0)=\inf_{\delta} \sup_{\vert x-x_0 \vert <\delta} f(x)
\end{gathered}
$$

于是$g(x_0)=A$意味着 $\forall \epsilon,\exists \delta, \sup_{\vert x-x_0 \vert <\delta} f(x)<A+\epsilon$,也就是$x$的一个邻域内,所有值都小于$A+\epsilon$,则这也蕴含了这个邻域内所有的$g$都不大于$A+\epsilon$,于是半连续得证.

