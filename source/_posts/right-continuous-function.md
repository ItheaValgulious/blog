---
title: Right Continuous Function
tags:
  - math
  - math-analysis
  - whims
date: 2025-11-03 07:58:58
---


# Can you find a function such that

### right continuous at every point but not left continuous on a **point**

$$
\begin{gathered}
f(x)=\lbrack x \rbrack 
\end{gathered}
$$

### right continuous at every point but not left continuous on a **dense point set**

考虑取一个包含全部有理数的序列$q_1,q_2\ldots$

$$
\begin{gathered}
f(x)=\sum _{i = 1} ^{+\infty} [q_i\le x]\dfrac{1}{2^i}  
\end{gathered}
$$

$2^{-i}$可以换成任意收敛级数.

这个在所有点右连续,在所有有理数点不左连续.

### right continuous at every point but not left continuous on a point on **every point**

$$
\begin{gathered}
\huge \text{Not Exists!} 
\end{gathered}
$$

我们称一个点$x$被$\epsilon$否决当且仅当$\forall \delta,\exists y\in [x-\delta,x],\vert f(y)-f(x)\vert>\epsilon$,即左不连续.

现在假设$f$所有点都右连续,那么任意$\epsilon$,对点$x_0$存在$x_0+\delta$满足$[x_0,x_0+\delta]$内任意两个点 $a,b$有  $\vert f(a)-f(b) \vert$ 小于$\epsilon$.然后我们令$x_{i+1}=x_i+\delta$,就可以得到一个数列,设它收敛到$X$,则$(x_0,X)$中的任何一点都不会被$\epsilon$否决.然后令新的$x_0=X$不断重复.你可以让$[x_0,X]$覆盖全部区间(而我们保证了$(x_0,X)$未被否决,所以可能被$\epsilon$否决的只有所有的区间端点)

因为你的区间有长度,包含互不相同的有理数,所以至多可数个.那么我们再用一个趋近于$0$的$\epsilon$数列,对每个$\epsilon$做上面那个操作,则一个左不连续点只能是某一次的区间端点(否则它始终不被否决,显然连续),于是只有可数乘可数个,还是可数个.