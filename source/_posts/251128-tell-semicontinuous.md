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


<div class='cbox'>

于是对任意函数$f$,取上极限后$g(x_0)=\limsup_{x\to x_0} f(x)$的函数$g$一定上半连续.

</div>

<div class='pbox'>

这是为什么呢.你注意上极限其实也是

$$
\begin{gathered}
g(x_0)=\inf_{\delta} \sup_{\vert x-x_0 \vert <\delta} f(x)
\end{gathered}
$$

于是$g(x_0)=A$意味着 $\forall \epsilon,\exists \delta, \sup_{\vert x-x_0 \vert <\delta} f(x)<A+\epsilon$,也就是$x$的一个邻域内,所有值都小于$A+\epsilon$,则这也蕴含了这个邻域内所有的$g$都不大于$A+\epsilon$,于是半连续得证.

</div>

<div class='cbox'>

开集/闭集的特征函数分别是下半/上半连续

</div>

<div class='pbox'>

由定义

</div>

<div class='cbox'>

上半连续/下半连续分别对下确界/上确界封闭

</div>

<div class='pbox'>

考虑只证下半连续的上确界.

那么$\sup_n f_n>a$的集合其实就是每个$f>a$的集合的并,开集的并还是开集,结束

</div>

<div class='cbox'>

下半连续的可数正系数和还是下半连续,上半连续的有限和还是上半连续

</div>

注意这里是不一样的,一个反例是我们取一些闭集,它们的并集是一个开集,比如$[\dfrac1{n+1},\dfrac1n]$,它们的并集是$(0,1]$,所以这些集合的特征函数加起来在$0$那里就不是上半连续的.

<div class='pbox'>

首先有限和都是显然的啊.

然后对下半连续,注意到可数正系数和其实是我们定义$S$是部分和,然后取上确界,即证.

而对上半连续你只能取下确界不能取上确界就寄了.

</div>



