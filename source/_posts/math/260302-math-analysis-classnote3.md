---
title: Math Analysis (Class Note 3)
tags:
  - math-analysis
  - note
  - math
date: 2026-03-02 14:20:41
---


# Math Analysis (Class Note 3)

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

<div class='cbox'>

$E$为可数集,$|f_n(x)|\le \phi(x),\forall x\in E$,则存在 $\{ n_k \}$, $f_{n_k}$在$E$上收敛.

</div>

<div class='pbox'>

我们直到单调有界有收敛子列,所以对于$E$有限的情况,你可以从满足在前$k$个元素上收敛的子列中选出满足在前$k+1$个元素上收敛的子列,依此类推,最后选出的子列在$E$上收敛.

那么现在有理,考虑设$f_{i,j}$表示在前$i$个元素收敛上的子列的第$j$项.考虑如果取$f_{i,i}$是不是就对完了.对任意点,只要说明$f_{i,i}$从某项起是任意$f_n$的子列.那么这个只要你保证$f_{i,j}$在$f_{i-1}$中在$f_{i-1,j}$后面就可以了吧

</div>

<div class='cbox'>

$f_n$单调,$|f_n(x)|\le \phi(x),\forall x$,则存在 $\{ n_k \}$, $f_{n_k}$收敛.

</div>

<div class='pbox'>

考虑用刚才的结论:先随便拿一个可数稠密集$E$,得到一个子列仍命名为$f_i$和其在这个$E$上的极限$f$.

然后我们尝试扩展这个函数到整个空间,比如我们定义$g(x)=\sup_{y<x,y\in E} f(y)$.

容易验证这个函数也是单增的.所以它最多有可数个间断点,考虑:

如果$g$在$x$处连续,则$f_i(x)\to g(x)$.那么我们任取它邻域内两个点,则它每一项都会夹在这两边两个点的值中间,所以它的极限点集合的极差小于任意值,只能是$0$.

那么对于$g$的不连续点,因为个数可数,我们直接再把它们也扔到$E$里,因为你$f_i$是收敛的所以你得到的一定是相同的函数,于是得证.

</div>

## 20260315

<div class='cbox'>

设 $f(x)=\sum _{n = 0} ^\infty  a_nx^n$

若$f(x)$在$x_0$处收敛,则任意$|x|<|x_0|$也收敛,且绝对收敛,一致收敛.

若$f(x)$在$x_0$处发散,则任意$|x|>|x_0|$也发散

</div>

<div class='pbox'>

(1):

若$f(x_0)$收敛,则显然有$a_nx^n\to 0$,对$|x|<|x_0|$有:

$$
\begin{gathered}
f(x)=\sum _{n = 0} ^{\infty}  a_nx^n \\
= \sum _{n = 0} ^{\infty} a_nx_0^n \dfrac{x^n}{x_0^n}    \\
\le \sum _{n = 0} ^{\infty}  |a_nx_0^n| |\dfrac{x^n}{x_0^n} |
\end{gathered}
$$

而第一项$a_nx_0^n$因为收敛所以有界,所以整体用优级数判别法知收敛,顺便就推出一致收敛和绝对收敛.

(2):

直接反证+用(1)即可.

</div>



由这个结论你可以得到收敛半径的存在性,于是有:

<div class='cbox'>

收敛半径$r$满足:

$$
\begin{gathered}
\dfrac{1}{r} =\limsup_{n\to \infty} \sqrt[ n ]{ a_n } 
\end{gathered}
$$

然后一个常用形式是若

$$
\begin{gathered}
\exists \lim_{n \to \infty} \dfrac{a_n}{a_{n-1}}  \\
\Rightarrow \dfrac{1}{r} = \dfrac{a_n}{a_{n-1}}  
\end{gathered}
$$

</div>

<div class='pbox'>

只需要证第一个形式,第二个形式可以直接推到第一个形式.

其实就是你用根式法去证逐点的收敛就好了:

$$
\begin{gathered}
|x|<\dfrac{1}{\limsup_{n\to \infty} \sqrt[ n ]{ a_n }}   \\
\Rightarrow \limsup_{n \to \infty} \sqrt[ n ]{ a_nx^n } =x\limsup_{n \to \infty} \sqrt[n]{a_n}<1
\end{gathered}
$$

大于方向一样.

</div>

<div class='cbox'>

收敛域内一定内闭一致收敛.

</div>

<div class='pbox'>

在开区间内内闭一致收敛是显然的.

如果端点是收敛的情况,只考虑右侧.此时还是写成 $\sum _{n = 1} ^{\infty}  a_nr^n(\dfrac{x}{r})^n$,然后$a_nr^n$一致收敛,$(\dfrac xr)^n$单调递减一致有界,由Abel判别法知一致收敛

</div>

<div class='cbox'>

幂级数求导/积分 收敛半径不变

</div>

<div class='pbox'>

$\lim_{n \to \infty} \sqrt[ n ]{ n }$ =1,所以求导积分完的式子用$\limsup$看一眼就知道了.

</div>

端点处呢?

<div class='cbox'>

若级数在端点处收敛则积分完了也收敛.

</div>

<div class='pbox'>

可以先用abel说明一致收敛然后逐项积分

可以直接用abel判别法拆成$\sum_{n=0}^\infty a_nx^n \dfrac{x}{n+1}$然后右边有界左边收敛做.

</div>

## 20260323

<div class='cbox'>

$$
\begin{gathered}
f(x)=1+\sum _{n = 1} ^{\infty} \dfrac{(2n-1)!!}{(2n)!!} x^n   
\end{gathered}
$$

</div>

<div class='pbox'>

你要先判断一下收敛性,比值法容易得到半径是$1$,然后端点处你可以:神秘不等式放缩或直接套斯特林公式得到应该是左边收敛右边发散.

注意力比较好的做法是观察$f'$,发现它和$\dfrac12 f$比较像,然后用$f'-\dfrac12f$建微分方程.

注意力不那么好的做法是直接考虑$f(x^2)$,那么你求个导给底下消掉一项,然后平移一下用积分给顶上消掉一项,也建立微分方程.

注意力非常好的注意到

$$
\begin{gathered}
f(x)=\sum _{n = 0} ^{\infty}  \binom{2n}n (\dfrac{x}{4} )^n
\end{gathered}
$$

于是

$$
\begin{gathered}
\dfrac1x \int f(4x)
\end{gathered}
$$

是卡特兰数,直接套结论(

</div>

## 20260325

<div class='cbox'>

求$(1+x)^\alpha$的泰勒级数何时收敛到自身

</div>

<div class='pbox'>

考虑只需证泰勒公式的余项趋近于$0$,一个方法是用柯西余项:

$$
\begin{gathered}
R_n(x)=\dfrac{f^{(n+1)(\xi)}}{n!} (x-\xi)^n (x-a) \\
=\alpha\binom{\alpha-1}{n} (1+\xi)^{\alpha-n-1}(x-\xi)^n x
\end{gathered}
$$

就,这个时候$\xi$范围跟着变是讨厌的,不如$\theta\in (0,1)$:

$$
\begin{gathered}
\alpha\binom{\alpha-1}{n} (1+\theta x)^{\alpha-n-1}(1-\theta)^nx^{n+1} \\
=\alpha\binom{\alpha-1}{n}x^n (\dfrac{1-\theta}{1+\theta x} )^n (1+\theta x)^{\alpha -1} x
\end{gathered}
$$

其中 $(\dfrac{1-\theta}{1+\theta x} )^n$有界,$(1+\theta x)^{\alpha-1}$也有界,其中$\binom{\alpha-1}n x^n$由比值法知$x\in (-1,1)$时到$0$,于是就完事了.

---

另一个做法是,注意到只证明$(-1,1)$收敛是容易的,也就是上个做法中趋近到$0$的那部分,于是直接逐项求导凑一凑你会得到:

$$
\begin{gathered}
(1+x)S'(x)=\alpha S(x)
\end{gathered}
$$

直接解出来即可.

---

再考虑端点处,$\alpha\le -1$时$|\binom \alpha n|=|\binom{n-\alpha+1} {-\alpha+1}|$极限不为$0$,肯定发散.

若$\alpha>-1$,则$\dfrac{\binom \alpha n}{\binom \alpha {n-1}}=\dfrac{\alpha+1}n-1$,则$x=1$处$n$充分大时为递减的交错级数,收敛.

$x=-1$时,相邻两项比变成$1-\dfrac{\alpha+1}n$,拉贝判别法得 $\lim_{n \to \infty} (n-1)(1-\dfrac{a_n}{a_{n-1}})=\alpha+1$,于是$\alpha>0$收敛,$\alpha<0$发散.

</div>

## 20260327

<div class='cbox'>

Tauber's Theorem

若级数 $f(x)=\sum _{i = 1} ^{n}  a_nx^n$收敛半径为$1$,且 $\lim_{n \to \infty} na_n=0$,且 $\lim_{x \to 1^-} f(x)=S$存在,则 $\sum _{n = 1} ^{\infty}  a_n=S$

</div>

<div class='pbox'>

考虑

$$
\begin{gathered}
\lim_{x\to 1^-} |f(x)-\sum _{i = 1} ^{\infty}  a_i |\\
\le \lim_{x\to 1^-}  [|\sum _{i = 1} ^{n}  a_n(x^n-1)| \\
+|\sum _{i = n} ^{\infty}  a_nx^n|] \\
=\lim_{x\to 1^-} A_n(x)+\lim_{x \to 1^-} B_n(x)
\end{gathered}
$$

我们要证的是

取$x=1-\dfrac1n$(这么取写起来比较奇怪,实际上我们是取$n=\dfrac1{1-x}$,因为$x$这边是外层极限,$n$是你自己取的一个划分点可以随便变),则:

$$
\begin{gathered}
\lim_{n \to \infty}  A_n(1-\dfrac1n) \\
\le\lim_{n \to \infty}  \sum _{i = 1} ^{n}  |a_i(x-1)|i \\
=\lim_{n \to \infty} \dfrac1n \sum _{i = 1} ^{n}  ia_i \\
=\lim_{n \to \infty} na_n \\
=0
\end{gathered}
$$

这部分用Stolz是经典的.

对$B_n$用神秘放缩

$$
\begin{gathered}
B_n(1-\dfrac1n) \\
=|\sum _{i = n} ^{\infty}  (ia_i)\dfrac 1i(1-\dfrac1n)^i |\\
\le \dfrac{\delta_n} n \sum _{i = n}^\infty (1-\dfrac{1}{n} )^i \\
\le \dfrac{\delta_n}{n} n \\
=\delta_n
\end{gathered}
$$

其中$\delta_n$表示$ia_i$对$i>n$的绝对值最大值,显然趋近于$0$,就做完了.

</div>

[think] AI发话了:

他说你考虑:

$$
\begin{gathered}
S_n=\sum _{i = 1} ^{\infty} a_i[i\le n] \\
f(e^{-\frac1N})=\sum _{i = 1} ^{\infty} a_ie^{-\frac iN}  
\end{gathered}
$$

他俩共同点是给前面一个很接近$1$的系数,给后面一个接近$0$的系数去做一个前缀和.

然后好像还是很魔怔.不懂.

## 20260330

Wallis公式:

<div class='cbox'>

$$
\begin{gathered}
\lim_{n \to \infty} \dfrac{1}{2n+1} (\dfrac{(2n)!!}{(2n-1)!!} )^2=\dfrac\pi 2
\end{gathered}
$$

</div>

<div class='pbox'>

通过经典的$I_n=\int_0^{\frac\pi2}\sin^n xdx$分部积分,我们知道:

$$
\begin{gathered}
I_n=\begin{cases}
\dfrac{(n-1)!!}{(n)!!},n=2k-1 \\
\dfrac{(n-1)!!}{(n)!!}\dfrac\pi 2,n=2k
\end{cases}
\end{gathered}
$$

从而考虑$n=2k-1,2k,2k+1$,显然$I_n$是递减的:

$$
\begin{gathered}
\dfrac{(2k-2)!!}{(2k-1)!!} >\dfrac{(2k-1)!!}{(2k)!!} \dfrac\pi2 >\dfrac{(2k)!!}{(2k+1)!!}  \\
\Rightarrow \begin{cases}
\dfrac{1}{2n+1} (\dfrac{(2n)!!}{(2n-1)!!})^2=\dfrac{((2k)!!)^2}{(2k+1)!!(2k-1)!!}<\dfrac\pi2 \\
\dfrac{2k+1}{2k} \dfrac{1}{2k+1} \dfrac{((2k)!!)^2}{((2k-1)!!)^2} =\dfrac{(2k-2)!!(2k)!!}{(2k-1)!!} > \dfrac\pi 2
\end{cases}
\end{gathered}
$$

从而夹逼知极限为$\dfrac\pi2$.

</div>



斯特林公式

感觉书上的做法好魔怔,它会有一步直接的用到

$$
\begin{gathered}
\dfrac{1}{x} \ln(\dfrac{1+x}{1-x} )
\end{gathered}
$$

且这个形式还是通过换元$x=\dfrac1{2n+1}$得到的,十分非人,而我们发现其实可以人类一些:

<div class='cbox'>

$$
\begin{gathered}
n!=\sqrt{ 2\pi n } (\dfrac{n}{e} )^n e^{\frac {\theta_n}{12n}},\theta_n\in (0,1)
\end{gathered}
$$

</div>

<div class='pbox'>

上来先取$\ln$做差,得到:

$$
\begin{gathered}
a_n=\sum _{i = 1} ^{n}  \ln i-(n+\dfrac12)\ln n-n
\end{gathered}
$$

只需证 $a_n=C\dfrac{\theta_n}{12n}$,然后套Wallis公式待定系数确定$C$.

那么仍然做差,然后直接展成级数:

$$
\begin{gathered}
a_n-a_{n-1}=(n-\dfrac12)\ln(1-\dfrac1n)+1 \\
=(n-\dfrac{1}{2} )\sum _{i = 1} ^{\infty}  \dfrac{1}{i n^i}  \\
=-\sum _{i = 2} ^{\infty}  \dfrac{1}{n^i} \dfrac{i-1}{2i(i+1)}  \\
<0
\end{gathered}
$$

所以$a_n$单调递减,还需说明有界才能确定它有极限,发现:

$$
\begin{gathered}
\dfrac{\dfrac{i-1}{2i(i+1)}}{\dfrac{i}{2(i+1)(i+2)}}  \\
=\dfrac{(i-1)(i+2)}{i^2} \\
=1+\dfrac{i-2}{i^2} \ge 1 
\end{gathered}
$$

所以系数是递减的,从而可以放缩:

$$
\begin{gathered}
a_n-a_{n-1} \\
=-\sum _{i = 2} ^{\infty}  \dfrac{1}{n^i} \dfrac{i-1}{2i(i+1)}  \\ \\
\ge -\sum _{i = 2} ^{\infty}  \dfrac{1}{12} \dfrac{1}{n^i}  \\
=-\dfrac{1}{12} \dfrac{1}{n(n-1)}  \\
\end{gathered}
$$

从而得到

$$
\begin{gathered}
a_n=\sum _{i = 2} ^{n}  a_i-a_{i-1} \\
\ge a_1-\dfrac{1}{12} +\dfrac{1}{12n}  
\end{gathered}
$$

同时$a_n<a_1$,,于是$a_n\in [a_1-\dfrac1{12}+\dfrac1{12n},a_1]$,给出了误差项.

最后用极限形式去待定系数一下常数就好了,那部分比较显然不写了.

</div>

## 20260410

<div class='cbox'>

$$
\begin{gathered}
S=\sum _{m = 1} ^{\infty} \sum _{n = 1} ^{\infty}  \dfrac{m^2n}{3^m(n3^m+m3^n)}   
\end{gathered}
$$

</div>


<div class='pbox'>

有定理说只要这玩意按某种顺序求和绝对收敛就都绝对收敛.容易发现按对角线求和绝对收敛.

$$
\begin{gathered}
S=\sum _{m = 1} ^{\infty}  \sum _{n = 1} ^{\infty}  \dfrac{1}{a_m(a_m+a_n)}  \\
\Rightarrow 2S=\sum _{m = 1} ^{\infty}  \sum _{n = 1} ^{\infty}  \dfrac{1}{a_m(a_m+a_n)} +\dfrac{1}{a_n(a_m+a_n)}  \\
=\sum _{m = 1} ^{\infty}  \sum _{n = 1} ^{\infty}  \dfrac{1}{a_na_m}  \\
=(\sum _{i = 1} ^{\infty}  a_i )^2=\dfrac{9}{16}
\Rightarrow S=\dfrac{9}{32}  
\end{gathered}
$$

其中$a_i=\dfrac{i}{3^i}$.

</div>

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
a_n,b_n\ge 0 \\
\sum _{n = 1} ^{\infty}  a_n=+\infty \\
\lim_{n \to \infty} \dfrac{b_n}{a_n} =\infty \\
\sum _{n = 1} ^{\infty}  a_nx^n \text{ has convergent radius } 1
\end{cases}
\Rightarrow \lim_{x \to 1^-} \dfrac{\sum _{n = 1} ^{\infty} b_nx^n}{\sum _{n = 1} ^{\infty}   a_nx^n} =A
\end{gathered}
$$

</div>

<div class='pbox'>

如果不是那个级数的话这是显然的:显然前面有限项比后面微不足道.但现在因为有幂级数他收敛了导致后面的反而成小的了.

但你再想想发现$x\to 1$的时候还是后面的占主导.你要说明这一点.于是你取$N$,原式变为:

$$
\begin{gathered}
Ans=\lim_{x \to 1^-} \dfrac{\sum _{n = N+1} ^{\infty} b_nx^n +\sum _{n = 1} ^{N}  b_nx^n }{\sum _{n = N+1} ^{\infty} a_nx^n +\sum _{n = 1} ^{N}  a_nx^n} =\dfrac{S_1(N)+L_1(N)}{S_2(N)+L_2(N)} 
\end{gathered}
$$

前面这部分直接等于 $L_1(N)=\sum _{n = 1} ^{N} a_n,L_2(N)=\sum _{n = 1} ^{N}  b_n$.

然后再让$x\to 1^-$,$S_i$趋近于无穷.所以存在$\delta$使得$x>1-\delta$时$\dfrac{L_i}{S_i}<\epsilon$.

于是

$$
\begin{gathered}
Ans\in (\dfrac{S_1}{S_2}\dfrac{1}{1+\epsilon} ,\dfrac{S_1}{S_2} (1+\epsilon)) 
\end{gathered}
$$

又因为容易取$N$使得$n>N$时$\dfrac {b_n}{a_n}\in (A-\epsilon,A+\epsilon)$,于是$\dfrac{S_1}{S_2}\in (A-\epsilon,A+\epsilon)$.

然后让$\epsilon\to 0$即可.


</div>



<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f(x)\in C^\infty[0,R] \\
\forall x\in [0,R],\forall n,f^{(n)}(x)\ge 0
\end{cases} \\
\Rightarrow f\text{ 's taylor series at } x=0 \text{ is convergent to } f
\end{gathered}
$$

</div>

<div class='pbox'>

首先你感觉拉格朗日余项在这里比较废物,你应该使用积分余项:

$$
\begin{gathered}
R_n(x)=\dfrac{1}{n!} \int_0^x f^{(n+1)}(t)(x-t)^ndt
\end{gathered}
$$

然后你要需要不管通过什么方法拿到一个上界.你发现因为泰勒展开级数每项都是正的,所以余项一定有$R_n(x)\in (0,f(x))$.

所以

$$
\begin{gathered}
R_n(x)=\dfrac{1}{n!} \int_0^x f^{(n+1)}(t)(x-t)^ndt \\
=\dfrac{1}{n!} \int_0^x f^{(n+1)}(t)(R-t)^n \dfrac{(x-t)^n}{(R-t)^n}  dt \\
\le \dfrac{x^n}{R^n} \dfrac{1}{n!} \int_0^x f^{(n+1)}(t)(R-t)^n  dt \\
=(\dfrac{x}{R} )^n R_n(R) \\
\le (\dfrac{x}{R})^n f(R)
\end{gathered}
$$

于是就收敛到$0$了.

</div>

感觉这个放缩还是太难想到了啊!我炸了.