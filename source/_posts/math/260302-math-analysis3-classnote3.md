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

讲了$f_n$连续且内闭一致收敛则 $\lim_{n \to \infty} f_n$连续

## 20260309

<div class='cbox'>

证明 $\sum _{n = 1} ^{\infty}  ne^{-nx}=S(x)\in C(0,+\infty)$

</div>

<div class='pbox'>

考虑对任意区间$[a,b]\subset (0,\infty)$,因为 $ne^{-nx}\le ne^{-na}$,而显然对任意$a$有$\sum ne^{-na}<\infty$,所以优级数判别法知内闭一致收敛,于是可以从$S_n$连续推$S$连续.

</div>

又讲了个 $\sum _{n = 2} ^{\infty}  (\dfrac{x}{\ln n} )^n\in C(-\infty,\infty)$的题,也是直接证内闭一致收敛,用优级数判别法,就做完了.

<div class='cbox'>

$$
\begin{gathered}
f(x)=\sum _{n = 0} ^{\infty}  \dfrac{x^n}{3^n} \cos (n\pi x^2) \\
\text{calculate } \lim_{x \to 1} f(x)
\end{gathered}
$$

</div>

<div class='pbox'>

显然是让你证一致收敛然后把$1$带进去.证一致收敛只要证$1$的小邻域,用优级数判别法放缩到等比数列就做完了.

</div>

<div class='cbox'>

讨论

$$
\begin{gathered}
S_n(x)=\sum _{n = 1} ^{\infty}  u_n=\sum _{n = 1} ^{\infty}  \dfrac{x^2}{(1+x^2)^n} 
\end{gathered}
$$

在$R$上一致收敛性.

</div>

<div class='pbox'>

考虑因为

$$
\begin{gathered}
S_n(x)=\begin{cases}
0,x=0 \\
1+x^2,x\ne 0
\end{cases}\notin C(R) \\
u_n\in C(R) \\
\Rightarrow \text{not uniformly continuous} 
\end{gathered}
$$

</div>


## 20260311

讲了一下一致收敛时可以交换极限和求导/积分的条件.

注意交换求导感觉不是很用记,和积分差不多,因为它的条件居然是关于导数一致收敛推原函数.

<div class='cbox'>

$x\in (-1,1)$时证明:

$$
\begin{gathered}
\sum _{n = 1} ^{\infty}  \dfrac{(-1)^{n-1}}{2n-1} x^{2n-1} = \arctan x
\end{gathered}
$$

</div>

<div class='pbox'>

$\arctan$是求导变成简单函数,所以只需证左边的导数一致收敛到右边,即证

$$
\begin{gathered}
\sum _{n = 1} ^{\infty}  (-1)^{n-1}x^{2n-2}\rightrightarrows \dfrac1{1+x^2}
\end{gathered}
$$

但这玩意不一致收敛,但你再想想发现刚才一致收敛的三个性质都只需要内闭,而内闭用优级数显然的.于是做完了.


</div>

<div class='cbox'>

$$
\begin{gathered}
f(x)=\sum _{n = 1} ^{\infty}  \dfrac{\cos(nx)}{n^2+1}  \\
\Rightarrow f\in C^1[0,\pi]
\end{gathered}
$$

</div>

<div class='pbox'>

这个题思路很显然就证$f(x)$和$f'(x)$一致连续.然后这些地方也很显然,但要注意的是

证明$f'$一致连续的时候,**$\sin nx$并非一致有界**,它会被放缩到

$$
\begin{gathered}
\dfrac{\cos(\dfrac x2)-\cos(\dfrac {(n+1)x}2)}{\sin \dfrac x2} \le \dfrac{1}{\sin \dfrac x2} 
\end{gathered}
$$

所以只能证出来内闭一致收敛,但是是够用的,就结束了.

</div>

## 20260313 习题课进化

开始不讲作业了.好像也只有这个题有点意思

<div class='cbox'>

$$
\begin{gathered}
f(x)=\sum _{n = 1} ^{\infty}  \dfrac{\{ nx \} }{n^2} \text{ is continuous for } x\notin Q, \text{ is discontinuous for } x\in Q
\end{gathered}
$$

</div>

<div class='pbox'>

对无理数$x$,则对每个项在$x$处都连续,又原级数显然一致收敛,所以连续.

对有理数$\dfrac pq$,把所有$q$的倍数的$n$的项拿出来组成新级数,则剩下的极限是连续函数,而拿出来的部分在此处不连续,所以结果也不连续.

然后直到此时我才想到对级数抽出任意一些项组成新级数这个操作的合法性:级数收敛,所以用结合律可以把每个要抽出的项和到上一个抽出的项之间的项都加起来,组成一个新的项,然后你抽出来的项和这个结合完了的级数做级数加法.

</div>

