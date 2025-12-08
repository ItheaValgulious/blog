---
title: Real And Complex Analysis
tags:
  - math
  - note
  - real-analysis
  - complex-analysis
  - self-study
date: 2025-12-08 09:06:15
---


# Real And Complex Analysis

## Chapter 1 Abstract Integral

### Basic Definitions

需要注意的是$f^{-1}(A)=B$意思是$f(B)=A$,$\{ x \vert f(x)\in B \} =A$

<div class='dbox'>

$X$上的一个拓扑就是$X$的幂集族的子集($X$的子集族)$\tau$满足
- $\emptyset\in \tau,X\in \tau$
- $X$中元素的任意有限交和无限并仍属于$X$

定义了$\tau$的$X$是拓扑空间,$\tau$中元素为开集

</div>

<div class='dbox'>

$f:X\to Y$是连续函数当且仅当任意开集的原像是开集.

</div>

<div class='dbox'>

度量,度量空间

度量是一个二元函数$d(x,y)$满足
- $d(x,y)=d(y,x)$
- $d(x,y)+d(y,z)\ge d(x,z)$
- $d(x,y)=0 \Leftrightarrow x=y$
- $d(x,y)\in [0,+\infty)$

$B(x,r)=\{ y \vert d(x,y)<r\}$定义为开球.由开球做拓扑基生成的拓扑是度量空间.

</div>

<div class='cbox'>

在度量空间中,函数连续等价于对每一点$x_0$,任意$f(x_0)$的邻域$V$存在$x_0$的邻域$U$使得$f(U)\subseteq V$

</div>

<div class='pbox'>

左推右是容易的:$f^{-1}(V)$一定是包含$x_0$的开集.

右推左考虑对开像集$V$内的每个点$x$找到了一个开邻域$N_x\in V$,再找到$f(U_x)\subset N_x$,则把所有的$U_x$并起来就是$f^{-1}(V)$且是开集.

</div>


<div class='dbox'>

$\sigma \text{-algebra}$

$X$的子集族$m$满足

- $X\in m$
- $S\in m \Rightarrow S^C \in m$
- $m$中元素任意可数交(并)在$m$中

定义了$\sigma$-algebra的集合$X$为测度空间,$m$中的元素为可测集.

开集的原像是可测集的函数是可测函数.

</div>

sigma-algebra 实际上包含了所有对集合进行交并补差等运算的结果.

<div class='cbox'>

基本性质

1. 设 $Y$ 和 $Z$ 是拓扑空间，$g: Y \to Z$ 连续。
   - (a) 若 $X$ 是拓扑空间，$f: X \to Y$ 连续，则 $h = g \circ f: X \to Z$ 连续。
   - (b) 若 $X$ 是可测空间，$f: X \to Y$ 可测，则 $h = g \circ f: X \to Z$ 可测。

2. 设 $u$ 和 $v$ 是可测空间 $X$ 上的实可测函数，$\Phi$ 是平面到拓扑空间 $Y$ 的连续映射，定义 $h(x) = \Phi(u(x), v(x))$。则 $h: X \to Y$ 是可测的。
3. 设 $X$ 是可测空间。
    - (a) 若 $f = u + iv$，其中 $u, v$ 是实可测函数，则 $f$ 是复可测函数。
    - (b) 若 $f = u + iv$ 是复可测函数，则 $u, v$ 和 $|f|$ 都是实可测函数。
    - (c) 若 $f, g$ 是复可测函数，则 $f+g$ 和 $fg$ 也是。
    - (d) 若 $E$ 是可测集，则特征函数 $\chi_E$ 是可测函数。
    - (e) 若 $f$ 是复可测函数，则存在复可测函数 $\alpha$ 使得 $|\alpha|=1$ 且 $f = \alpha |f|$。
4. 若 $\mathscr{F}$ 是 $X$ 的任意子集族，则存在包含 $\mathscr{F}$ 的最小 $\sigma$-代数 $\mathfrak{M}^*$。这称为由 $\mathscr{F}$ 生成的 $\sigma$-代数。


</div>

<div class='pbox'>

第一条由定义显然.

第二条考虑先建立$f(x)=(u(x),v(x))$是到平面的映射,则平面上长方形拓扑基$[a,b]\times [c,d]$的原像是$u^{-1}([a,b])\cap v^{-1}([c,d])$是开集,于是$h=\Phi(f)$可测

第三条应用第二条的结论:
- (a)是$\Phi(a,b)=a+bi$
- (b)是因为$\Re(z),\Im(z),\vert z\vert$是连续函数(欧氏空间?)
- (c)是$\Phi(a,b)=a+b,\Phi(a,b)=ab$
- (d)直接用定义
- (e)考虑$\dfrac{f}{\vert f\vert}=\alpha$,然后用1.和2.

第四条考虑取所有包含$\mathscr{F}$的sigma algebra的交集,只要说明这个交集是sigma-algebra.那你验证的时候发现那几条是显然的.

</div>

### Borel Sets

<div class='dbox'>

Borel 集 (Borel Sets)

设 $X$ 是拓扑空间。由 $X$ 中所有开集生成的最小 $\sigma$-代数 $\mathscr{B}$ 中的元素称为 $X$ 的 Borel 集。

Borel映射指的是Borel集的sigma-algebra下可测的映射.

</div>

<div class='cbox'>

*   闭集是 Borel 集。
*   $F_\sigma$ 集（闭集的可数并）和 $G_\delta$ 集（开集的可数交）是 Borel 集。
*   任何连续映射都是 Borel 可测的（Borel mapping）。


</div>

<div class='pbox'>

- 显然
- 显然
- 显然

</div>

<div class='cbox'>

设 $\mathfrak{M}$ 是 $X$ 上的 $\sigma$-代数，$Y$ 是拓扑空间，$f$ 映射 $X$ 到 $Y$。
- (a) 若 $\Omega = \{E \subset Y: f^{-1}(E) \in \mathfrak{M}\}$，则 $\Omega$ 是 $Y$ 上的 $\sigma$-代数。
- (b) 若 $f$ 可测且 $E$ 是 $Y$ 中的 Borel 集，则 $f^{-1}(E) \in \mathfrak{M}$。
- (c) 若 $Y = [-\infty, \infty]$ 且对每个实数 $\alpha$ 都有 $f^{-1}((\alpha, \infty]) \in \mathfrak{M}$，则 $f$ 可测。
- (d) 若 $f$ 可测，$Z$ 是拓扑空间，$g: Y \to Z$ 是 Borel 映射，且 $h = g \circ f$，则 $h$ 可测。


</div>

<div class='pbox'>

(a)在说$X$的sigma-algebra自然的引出了$Y$上的.由映射原像和像的关系验证定义是显然的.

(b)是考虑首先$E$是开集的时候定义显然,然后就得到$F_\sigma,G_\delta$,然后$F_{\sigma,\delta}$和$G_{\delta,\sigma}$这样扩展下去最后扩展到所有borel集.

**错,Borel集并不能被这样划分成可数层,一个反例是你这么划分之后每层取一个得到的集合**

考虑由(a),构造这样一个$\Omega$,则$\Omega$包含$E$中的所有开集(因为$f$可测).但因为Borel集的sigma algebra是最小的包含所有开集的sigma-algebra,所以$\Omega$包含所有Borel集,结束.

(c)是因为你可以由$(a,\infty]$通过可数交得到$[a,\infty]$然后$[-\infty,a)$,于是可以得到任何$(a,b)$,就说明所有开集都成立.

(d)显然

</div>

<div class='dbox'>

上极限与下极限

设 $\{a_n\}$ 是扩展实数序列。

$b_k = \sup \{a_k, a_{k+1}, \dots\}$，$\beta = \inf \{b_1, b_2, \dots\}$。
$\beta$ 称为 $\{a_n\}$ 的上极限 (upper limit)，记为 $\limsup_{n \to \infty} a_n$。

类似地定义下极限 (lower limit)：$\liminf_{n \to \infty} a_n = -\limsup_{n \to \infty} (-a_n)$。

对于函数序列 $\{f_n\}$，$\sup f_n$ 和 $\limsup f_n$ 定义为逐点进行。
若 $\lim_{n \to \infty} f_n(x)$ 在每点存在，则称 $f$ 为序列 $\{f_n\}$ 的逐点极限。

</div>

<div class='cbox'>

若 $f_n: X \to [-\infty, \infty]$ 可测 ($n=1, 2, \dots$)，且 $g = \sup_{n \ge 1} f_n$，$h = \limsup_{n \to \infty} f_n$，则 $g$ 和 $h$ 也是可测的。

</div>

<div class='pbox'>

由上一条,只要证明对所有的$(a,+\infty]$满足原像可测.

对$g$,$g(x)>a \Leftrightarrow \exists k,f_k(x)>a$,于是$g^{-1}((a,+\infty])=\cup_i f_k^{-1}((a,+\infty])$可测.

而$h(x)=\inf_i \sup_{j>i} f_j(x)$,于是你用两次$g$的结论即可.

</div>


### Integral

<div class='dbox'>

简单函数

若复函数 $s$ 的值域仅包含有限个点，则称 $s$ 为简单函数 (simple function)。
形式为 $s = \sum_{i=1}^n \alpha_i \chi_{A_i}$。

</div>

<div class='cbox'>

$s$ 可测当且仅当每个 $A_i$ 可测。

</div>

<div class='pbox'>

显然

</div>

<div class='cbox'>

设 $f: X \to [0, \infty]$ 可测。存在可测简单函数序列 $s_n$ 使得：
- (a) $0 \le s_1 \le s_2 \le \dots \le f$。
- (b) 对每个 $x \in X$，$s_n(x) \to f(x)$ ($n \to \infty$)。

</div>

<div class='pbox'>

考虑把值域按照$2^{-i}$分成若干段$I_{i,k}=[k2^{-i},(k+1)2^{-i}),k\le 2^{2i}$.然后让 $f_n(x)=i \ s.t.\ f(x)\in I_{n,i}$,不存在就是$0$.

</div>

<div class='dbox'>

测度

- (a) 正测度 (positive measure) 是定义在 $\sigma$-代数 $\mathfrak{M}$ 上的函数 $\mu$，取值于 $[0, \infty]$，且具有可数可加性 (countably additive)：对于互不相交的可测集族 $\{A_i\}$，有 $\mu(\bigcup A_i) = \sum \mu(A_i)$。且假设至少有一个 $A$ 使 $\mu(A) < \infty$。
- (b) 测度空间 (measure space) 是一个赋有正测度的可测空间。
- (c) 复测度 (complex measure) 是定义在 $\sigma$-代数上的复值可数可加函数。

</div>

注意正测度不是复测度的子集,因为复测度值域通常不含$+\infty$

<div class='cbox'>

设 $\mu$ 是 $\sigma$-代数 $\mathfrak{M}$ 上的正测度。则：
- (a) $\mu(\emptyset) = 0$。
- (b) $\mu(A_1 \cup \dots \cup A_n) = \mu(A_1) + \dots + \mu(A_n)$ 若 $A_i$ 互不相交（有限可加性）。
- (c) $A \subset B \implies \mu(A) \le \mu(B)$（单调性）。
- (d) 若 $A_n \in \mathfrak{M}, A_n \subset A_{n+1}$ 且 $A = \bigcup A_n$，则 $\mu(A_n) \to \mu(A)$。
- (e) 若 $A_n \in \mathfrak{M}, A_n \supset A_{n+1}$ 且 $\mu(A_1)$ 有限，则 $\mu(A_n) \to \mu(\bigcap A_n)$。


</div>

<div class='pbox'>

显然,显然(取后面的全是空),显然

对(d),考虑$A=\sum (A_{n+1}-A_n)$,于是$\mu(A)=\sum \mu(A_{n+1}-A_n)$,级数收敛显然部分和趋向$\mu(A)$.

对(e),考虑把$A_i$当全集然后对$A_k$的补集们用(d),要求$\mu(A_1)$是防止补集的测度出现$\infty-\infty$会爆炸(真的有反例,比如计数测度,$A_1=N$,然后 $A_n=A_{n-1}-\{ n-1 \}$)

</div>

<div class='dbox'>

我们把$R$扩充出$+\infty,-\infty$.

无穷有一些未定义行为.但定义$0\cdot \infty=0$

</div>

<div class='dbox'>

正函数的勒贝格积分

若 $s: X \to [0, \infty)$ 是可测简单函数，$s = \sum_{i=1}^n \alpha_i \chi_{A_i}$，定义 $\int_E s d\mu = \sum_{i=1}^n \alpha_i \mu(A_i \cap E)$。

若 $f: X \to [0, \infty]$ 可测，定义 $\int_E f d\mu = \sup \int_E s d\mu$，上确界取遍所有满足 $0 \le s \le f$ 的可测简单函数 $s$。

这称为 $f$ 关于测度 $\mu$ 在 $E$ 上的Lebesgue 积分。


</div>

<div class='cbox'>


积分的基本性质：
- (a) 若 $0 \le f \le g$，则 $\int_E f d\mu \le \int_E g d\mu$。
- (b) 若 $A \subset B$ 且 $f \ge 0$，则 $\int_A f d\mu \le \int_B f d\mu$。
- (c) 若 $f \ge 0$ 且 $c$ 为常数 ($0 \le c < \infty$)，则 $\int_E cf d\mu = c \int_E f d\mu$。
- (d) 若对所有 $x \in E$ 有 $f(x)=0$，则 $\int_E f d\mu = 0$。
- (e) 若 $\mu(E)=0$，则 $\int_E f d\mu = 0$。
- (f) 若 $f \ge 0$，则 $\int_E f d\mu = \int_X \chi_E f d\mu$。

</div>

<div class='pbox'>

对(a),$s\le f \Rightarrow s\le g$,显然.

对(b),对每个$s\le f$,都有$\int_A sd\mu\le \int_b sd\mu$,显然.

对(c),同样是对每个简单函数成立,然后再分析上确界性质成立.(e),(f)是一样

(d)是因为$0\le s\le f \Rightarrow s=0$.

</div>

<div class='cbox'>


设 $s, t$ 为非负可测简单函数。定义 $\phi(E) = \int_E s d\mu$。
则 $\phi$ 是 $\mathfrak{M}$ 上的测度。且 $\int_X (s+t) d\mu = \int_X s d\mu + \int_X t d\mu$。


</div>

<div class='pbox'>

先证是测度,就要证可数可加性,则

$$
\begin{gathered}
\sum_i \phi(E_i) \\
=\sum_i \int_{E_i}sd\mu \\
=\sum_i\sum_j \alpha_j \mu(E_i\cap A_j) \\
=\sum_j \alpha_j \sum_i\mu(E_i\cap A_j) \\
=\sum_j \alpha_j \mu(E \cap A_j) \\
=\phi(E)
\end{gathered}
$$

然后对$s+t$,考虑就是

$$
\begin{gathered}
\int_X (s+t)d\mu \\
=\sum_i \sum_j (\alpha_i+\beta_j)\mu(A_i\cap B_j) \\
=\sum_i \alpha_i \sum_j \mu(A_i\cap B_j) \\
+\sum_j \beta_j \sum_i \mu(A_i\cap B_j) \\
=\int_X sd\mu+\int_X td\mu
\end{gathered}
$$

</div>

<div class='cbox'>

Lebesgue 单调收敛定理 (Lebesgue's Monotone Convergence Theorem)

设 $\{f_n\}$ 是 $X$ 上的可测函数序列，满足：
- (a) $0 \le f_1(x) \le f_2(x) \le \dots \le \infty$ 对每点 $x$ 成立，
- (b) $f_n(x) \to f(x)$ ($n \to \infty$) 对每点 $x$ 成立。

则 $f$ 可测，且 $\int_X f_n d\mu \to \int_X f d\mu$ ($n \to \infty$)。


</div>

<div class='pbox'>

由前面结论,那么$f=\limsup_n f_n$可测.

设 $\alpha=\lim_{n \to \infty} \int_X f_nd\mu$,显然$\alpha\le f_Xfd\mu$.只要证另一边.

取$s<f$,$E_n=\{ x\vert f_n(x)\ge cs(x) \},c\in (0,1)$,则

$$
\begin{gathered}
\int_X f_nd\mu\ge \int_{E_n} f_nd\mu\ge c\int_{E_n} sd\mu
\end{gathered}
$$

那么对$n$取极限,$E_n$会变成$X$

$$
\begin{gathered}
\alpha \ge c\int_{X} sd\mu
\end{gathered}
$$

再对$c$取极限就是

$$
\begin{gathered}
\alpha \ge \int_X sd\mu
\end{gathered}
$$

再对$s$取上确界就能得到右边是$\int_X fd\mu$.

</div>

[think] 这个证明是怎么回事呢?因为积分是简单函数积分的上确界所以你只要说明对简单函数.但$f_n$可能始终不大于某个简单函数(否则你直接取那个$f_n$,它的积分比简单函数大),所以你只能先证明$cs$最后再取极限干回来.AI说这是常见套路.

[think] 这个定理在$E_n$缩小积分值时用到了非负性.

<div class='cbox'>

若 $f_n: X \to [0, \infty]$ 可测，且 $f(x) = \sum_{n=1}^\infty f_n(x)$，则 $\int_X f d\mu = \sum_{n=1}^\infty \int_X f_n d\mu$。


</div>

<div class='pbox'>

对部分和数列$F_n$用上面的单调定理.因为有限求和和积分总是可交换的.

</div>

<div class='cbox'>

Fatou 引理 (Fatou's Lemma)

若 $f_n: X \to [0, \infty]$ 可测，则 $\int_X (\liminf_{n \to \infty} f_n) d\mu \le \liminf_{n \to \infty} \int_X f_n d\mu$。

</div>

<div class='pbox'>

$$
\begin{gathered}
g_k(x)=\inf_{n\ge k} f_n(x)
\end{gathered}
$$

则$g_k$是单调递增的,于是对它用单调收敛定理就有

$$
\begin{gathered}
\lim_{k \to +\infty} \int_X g_k(x)d\mu=\int_X \lim_{k\to +\infty} g_k(x)d\mu=\int_X \liminf f_n(x)d\mu
\end{gathered}
$$

又因为

$$
\begin{gathered}
\forall n\ge k \\
g_k\le f_n \\
\Rightarrow \int_X g_k(x)d\mu\le \int_X f_n(x)d\mu \\
\Rightarrow \int_X g_k(x)d\mu\le \inf_{n\ge k} f_n(x)d\mu
\end{gathered}
$$

带入上式左边即证.

</div>

[think] 其中使用单调收敛那一步依赖非负.

<div class='cbox'>

设 $f: X \to [0, \infty]$ 可测，定义 $\phi(E) = \int_E f d\mu$。则 $\phi$ 是 $\mathfrak{M}$ 上的测度，且对于任意值域在 $[0, \infty]$ 的可测函数 $g$，有 $\int_X g d\phi = \int_X gf d\mu$。
*(注：有时记作 $d\phi = f d\mu$)*。

</div>

<div class='pbox'>

先证$\phi$是测度.只要证

$$
\begin{gathered}
\sum\phi(E_n) \\
=\sum_n \sup_{s<f} \int_{E_n} sd\mu \\
\ge \sup \sum_n \int_{E_n} sd\mu \\
=\phi(E)
\end{gathered}
$$

那么要证反过来的,

$$
\begin{gathered}
\sum \phi(E_n) \\
=\sum_n \sup_{s<f} \int_{E_n} sd\mu \\
\ge \sum_n \int_{E_n} sd\mu,(s>cf,c<1) \\
\ge c\phi(E)
\end{gathered}
$$

然后取极限让$c=1$,于是$\phi$是测度.

则

$$
\begin{gathered}
\int_X gd\phi \\
=\sup_{s<g} \sum_i \alpha_i \int_{A_i} fd\mu \\
=\sup_{s<g} \sum_i \int_{A_i} sfd\mu \\
=\sup_{s<g} \int_X sfd\mu
\end{gathered}
$$

然后显然这个不大于$\int_X gfd\mu$.

又因为一定存在$s>cg(c<1)$,就能取$c$极限的证明不小于,于是得证.

</div>

### Complex Integral

<div class='dbox'>

$L^1(\mu)$

$L^1(\mu)$ 是所有满足 $\int_X |f| d\mu < \infty$ 的复可测函数 $f$ 的集合。成员称为 Lebesgue 可积函数 或 可和函数。
</div>

<div class='dbox'>

复函数的积分

若 $f = u + iv \in L^1(\mu)$，定义 $\int_E f d\mu = \int_E u^+ d\mu - \int_E u^- d\mu + i \int_E v^+ d\mu - i \int_E v^- d\mu$。

</div>

<div class='cbox'>

设 $f, g \in L^1(\mu)$，$\alpha, \beta$ 为复数。则 $\alpha f + \beta g \in L^1(\mu)$，且 $\int_X (\alpha f + \beta g) d\mu = \alpha \int_X f d\mu + \beta \int_X g d\mu$。

</div>

<div class='pbox'>

首先对于正函数:

基本性质里已经证了乘法,只要证加法.

那么$\int_X ad\mu+\int_X bd\mu=\sup \int_X s_1d\mu+\sup \int_X s_2d\mu\ge \sup \int_X (s_1+s_2)d\mu=\int_X (a+b)d\mu$.

另一边还是取$c$取极限的套路显然.

然后对复函数积分,先拆开然后用四遍正函数的显然是对的.

</div>

<div class='cbox'>

若 $f \in L^1(\mu)$，则 $|\int_X f d\mu| \le \int_X |f| d\mu$。

</div>

<div class='pbox'>

存在$\vert \alpha\vert=1,\alpha \int_X fd\mu\in R$

则

$$
\begin{gathered}
\vert \int_X fd\mu \vert  \\
=\int_X \alpha fd\mu \\
=\int_X \Re(\alpha f)d\mu \\
\le \int_X \vert f \vert d\mu
\end{gathered}
$$

取实部是因为和是实数,虚部加起来一定是$0$.

</div>

<div class='cbox'>

Lebesgue 控制收敛定理 (Lebesgue's Dominated Convergence Theorem)

设 $\{f_n\}$ 是复可测函数序列，使得 $f(x) = \lim_{n \to \infty} f_n(x)$ 对每点 $x$ 存在。

若存在 $g \in L^1(\mu)$ 使得对所有 $n$ 和 $x$ 都有 $|f_n(x)| \le g(x)$，

则 $f \in L^1(\mu)$，
$\lim_{n \to \infty} \int_X |f_n - f| d\mu = 0$，
且 $\lim_{n \to \infty} \int_X f_n d\mu = \int_X f d\mu$。

</div>

<div class='pbox'>

首先我们可以看出有了模长积分为$0$那个就能推出后面那个极限和积分可交换. 

然后你要注意到固定$x$后$\vert f(x)\vert=\lim_{n\to \infty} \vert f_n(x)\vert \le g(x)$,于是$\vert f_n-f\vert \le 2g$.

$$
\begin{gathered}
\int_X 2gd\mu \stackrel{\text{Fatou's lemma}}{\le} \liminf_n \int_X (2g-\vert f_n-f \vert )d\mu\\
=\int_X 2gd\mu+\liminf -\int_X \vert f_n-f \vert d\mu \\
\Rightarrow \limsup \int_X \vert f_n-f \vert d\mu \le 0
\end{gathered}
$$

</div>

[think] 就是你其实想直接用Fatou的结论反一下说明$\limsup \int_X \vert f_n-f\vert\le \int_X \limsup \vert f_n-f\vert$的,但fatou不是对称的因为它是对非负函数(所以有个底限制了函数值),所以要对称过来需要$g$.

### Almost Everywhere

<div class='dbox'>

几乎处处

若性质 $P$ 在 $E$ 中除去一个测度为 0 的集合 $N$ 外处处成立，则称 $P$ 在 $E$ 上几乎处处 (almost everywhere, a.e.) 成立。
若 $\mu(\{x: f(x) \neq g(x)\}) = 0$，写作 $f \sim g$。若 $f \sim g$，则对任意 $E$，$\int_E f d\mu = \int_E g d\mu$。

</div>

<div class='cbox'>

完备化

设 $(X, \mathfrak{M}, \mu)$ 是测度空间。令 $\mathfrak{M}^*$ 为所有满足存在 $A, B \in \mathfrak{M}$ 使得 $A \subset E \subset B$ 且 $\mu(B-A)=0$ 的集合 $E$ 的族。定义 $\mu(E) = \mu(A)$。

则 $\mathfrak{M}^*$ 是 $\sigma$-代数，$\mu$ 是 $\mathfrak{M}^*$ 上的测度。

这个扩展测度称为完备的 (complete)，$\mathfrak{M}^*$ 称为 $\mathfrak{M}$ 的 $\mu$-完备化。


</div>

<div class='pbox'>

要证明新的测度和sigma algebra.

显然$\mu(B-A)+\mu(A)=\mu(B)$所以$\mu(A)=\mu(B)$.

那么对先添加的集合,发现$E^C$一定也同时存在.若$A_i\subset E_i\subset B_i$,则$\bigcap A_i\subset \bigcap E_i\subset \bigcap B_i$,所以也都存在,是sigma-algebra.

而测度方面,新的集合都可以加上一个$\mu(B-E)=0$变成$\mu(B)$所以是对的.

</div>

<div class='bbox'>

关于扩展可测函数的定义：如果 $f$ 定义在 $E \in \mathfrak{M}$ 上且 $\mu(E^c)=0$，且对任意开集 $V$，$f^{-1}(V) \cap E$ 可测，则可以称 $f$ 在 $X$ 上可测（通过在 $E^c$ 上令 $f=0$）。

</div>

<div class='cbox'>

设 $\{f_n\}$ 是几乎处处定义的复可测函数序列，且 $\sum_{n=1}^\infty \int_X |f_n| d\mu < \infty$。
则级数 $f(x) = \sum_{n=1}^\infty f_n(x)$ 对几乎所有 $x$ 收敛，$f \in L^1(\mu)$，且 $\int_X f d\mu = \sum_{n=1}^\infty \int_X f_n d\mu$。

</div>

<div class='pbox'>

先设$S_i$是$f_i$的定义域,$S=\bigcap S_i$,$\mu(S^C)=0$

设$g(x)=\sum_{i=1}^\infty \vert f_i(x)\vert$,则单调收敛定理说

$$
\begin{gathered}
\int_X g(x)=\lim_{n \to \infty} \int_X \sum_{i=1}^n \vert f_n(x) \vert  \\
=\lim_{n\to \infty} \sum_{i=1}^n \int_X \vert f_n(x) \vert  \\
<\infty
\end{gathered}
$$

$g(x)$几乎处处收敛可以推出$f(x)$几乎处处收敛.$g$可积也可以推出$f$可积.

然后考虑用$g$控制收敛,

$$
\begin{gathered}
f\le \vert f \vert \le g
\end{gathered}
$$

于是可交换.

</div>

<div class='cbox'>

- (a) 设 $f: X \to [0, \infty]$ 可测，$E \in \mathfrak{M}$，且 $\int_E f d\mu = 0$。则在 $E$ 上几乎处处 $f=0$。
- (b) 设 $f \in L^1(\mu)$ 且对所有 $E \in \mathfrak{M}$ 有 $\int_E f d\mu = 0$。则在 $X$ 上几乎处处 $f=0$。
- (c) 设 $f \in L^1(\mu)$ 且 $|\int_X f d\mu| = \int_X |f| d\mu$。则存在常数 $\alpha$ 使得几乎处处 $\alpha f = |f|$。

</div>

<div class='pbox'>

(a)

取$s\ge cf,c\in (0,1)$,$c\int_E fd\mu\le \int_E sd\mu=\sum_i \alpha_i \mu(A_i)$.

则$\alpha_i\ne 0 \Rightarrow \mu(A_i)=0$,于是$s$几乎处处为$0$.然后$s$为$0$的地方$f$一定为$0$.

(b)

把大于$0$的原像和小于$0$的分别用(a)

(c)

$$
\begin{gathered}
\alpha \int_X fd\mu=\vert \int_X fd\mu \vert \\
\Rightarrow \int_X \alpha fd\mu=\int_X \Re(\alpha f)d\mu=\int_X \vert f \vert d\mu \\
\Rightarrow \int_X (\vert f \vert -\Re(\alpha f))d\mu=0
\end{gathered}
$$

对最后一行用(a).


</div>

<div class='cbox'>

设 $\mu(X) < \infty, f \in L^1(\mu)$, $S$ 是复平面上的闭集。若对于每个满足 $\mu(E)>0$ 的 $E \in \mathfrak{M}$，平均值 $A_E(f) = \frac{1}{\mu(E)} \int_E f d\mu$ 都在 $S$ 中，则几乎对所有 $x \in X$，有 $f(x) \in S$。

</div>

<div class='pbox'>

$S$是闭集所以$S^C$是开集,所以对$S^C$的每个点存在一个小圆盘$D(x,r)\subset S^C$,$S^C$可以表示为可数个小圆盘的并集,只要说明对每个小圆盘原像测度是$0$.

而对一个小圆盘$D(x,r)$,设$f^{-1}(D(x,r))=E$,则

$$
\begin{gathered}
\vert A_E(f)-x \vert  \\
={\left \vert \dfrac{1}{\mu(E)} \int_E (f-x)d\mu \right \vert}  \\
\le \dfrac{1}{\mu(E)} \int_E \vert f-x \vert d\mu \\
\le r
\end{gathered}
$$

但着代表了$A_E(f)$在圆盘内部,与题目条件矛盾.

</div>

<div class='cbox'>

设 $\{E_k\}$ 是可测集序列，使得 $\sum_{k=1}^\infty \mu(E_k) < \infty$。则几乎所有 $x \in X$ 只属于有限个 $E_k$。

</div>

<div class='pbox'>

要利用我们的新工具.

$$
\begin{gathered}
\sum_{k=1}^\infty \mu(E_k)=\int_X \sum_{k=1}^\infty \chi_{E_k}d\mu=\int_X gd\mu<\infty
\end{gathered}
$$

从而$\mu(g^{-1}(\infty))=0$,而$g^{-1}(\infty)$恰好就是属于无穷个$E$的$x$的集合.

</div>

