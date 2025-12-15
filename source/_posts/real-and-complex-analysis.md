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
- $\varnothing\in \tau,X\in \tau$
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
- (a) $\mu(\varnothing) = 0$。
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

## Chapter 2 Borel Measure

<div class='dbox'>

复向量空间

略

</div>

然后他说,$f(x)\to \int_X f(x)d\mu$是线性泛函,$f(x) \to \int_X g(x)f(x)d\mu$当$g$有界时是线性泛函.

### 拓扑学基础

<div class='dbox'>

设 $X$ 是一个拓扑空间。
- (a) 集合 $E \subset X$ 称为**闭集**，如果其补集 $E^c$ 是开集。
- (b) 集合 $E \subset X$ 的**闭包** $\bar{E}$ 是包含 $E$ 的 $X$ 中最小的**闭集**。
- (c) 集合 $K \subset X$ 称为**紧集**，如果 $K$ 的每一个开覆盖都包含一个有限子覆盖。特别地，如果 $X$ 本身是紧的，则称 $X$ 为紧空间。
- (d) 点 $p \in X$ 的**邻域**是包含 $p$ 的 $X$ 的任意开子集。
- (e) $X$ 称为 **Hausdorff 空间**，如果满足：若 $p \in X, q \in X$ 且 $p \neq q$，则存在 $p$ 的邻域 $U$ 和 $q$ 的邻域 $V$ 使得 $U \cap V = \varnothing$。
- (f) $X$ 称为**局部紧**的，如果 $X$ 的每一点都有一个闭包为紧集的邻域。


</div>

<div class='cbox'>

设 $K$ 是拓扑空间 $X$ 中的紧集，$F$ 是闭集。如果 $F \subset K$，则 $F$ 是紧集。

</div>

<div class='pbox'>

考虑任意包含$F$的无限开覆盖,加入$F^C$后一定覆盖$K$,而它有有限子覆盖.此时如果$F^C$在里面你把它去掉,得到的就是$F$的有限覆盖.

</div>

<div class='cbox'>


**Corollary**
如果 $A \subset B$ 且 $B$ 具有紧闭包，则 $A$ 也具有紧闭包。


</div>

<div class='pbox'>

显然

</div>




<div class='cbox'>

设 $X$ 是 Hausdorff 空间，$K \subset X$，$K$ 是紧集，且 $p \in K^c$。

则存在开集 $U$ 和 $W$ 使得 $p \in U$，$K \subset W$，且 $U \cap W = \varnothing$。

</div>

这个是想说你不仅可以分开两个点,也可以分开一个点和一个集合.

<div class='pbox'>

考虑对$K$内的每个点$k_i$取一个邻域$S_i$,与$p$的一个邻域$T_i$不交($S_i\cap T_i=\varnothing$),则$S_n$构成$K$的开覆盖,于是取它的有限覆盖是覆盖$K$的,则把它们并起来作为$W$,把对应的$T_i$的交作为$U$即可.

</div>

<div class='cbox'>

**Corollary**

(a) Hausdorff 空间的紧子集是闭集。

(b) 如果 $F$ 是 Hausdorff 空间中的闭集，$K$ 是紧集，则 $F \cap K$ 是紧集。

</div>

<div class='pbox'>

(a)考虑因为外面每个点都能找到一个邻域和这个子集无交,没有边界点是开集,所以子集是闭集.

(b)考虑一个无限覆盖,然后补上对称差,然后得到有限覆盖,然后去掉对称差.

</div>

<div class='cbox'>


如果 $\{K_\alpha\}$ 是 Hausdorff 空间中紧子集的集合，且 $\bigcap_\alpha K_\alpha = \varnothing$，则 $\{K_\alpha\}$ 的某个有限子集也有空交集。

</div>

<div class='pbox'>

第一反应是考虑$K_\alpha^C$构成对全集的覆盖,但没有说整个空间是紧的.

所以你任取一个紧集$K_0$,那么这些补集构成对它的覆盖,那么取有限覆盖,这有限个元素再交上$K_0$本身一定是空.

</div>

<div class='cbox'>

设 $U$ 是局部紧 Hausdorff 空间 $X$ 中的开集，$K \subset U$，且 $K$ 是紧集。则存在一个闭包为紧集的开集 $V$，使得
$$ K \subset V \subset \bar{V} \subset U. $$

</div>

<div class='pbox'>

对$K$内每个点$k_i$先取一个闭包是紧的邻域$S_i$,那么这个邻域内一定有一个在$U$内的更小邻域且闭包是紧的(紧集内的闭集是紧的).这些邻域中有一个$K$的有限覆盖为 $\{ V_n \}$.令$G=\bigcup V_i$

如果$U$是全集问题就解决了,但问题是$\overline G\subset U$不满足.

此时考虑$U^C$,对$U^C$中的任何一个点$u_i$可以找一个邻域$U_i$和包含$K$的开集$W_i$不交,$U_i\cap W_i=\varnothing \Rightarrow u_i\notin \overline {W_i}$(这是因为$u_i$如果在边界上那么它的邻域$U_i$需要与$W_i$相交).

**此时考虑 $\{ \overline{G}\cap \overline{W_i}\cap U^C \}$ 这组集合**,紧集交闭集是紧的于是它们是紧的,且它们交集为空,于是其中有限个交集为空,也就意味着$\overline{G}\cap \bigcap \overline{W_i}$与$U^C$交为空,于是取$V=G\cap \bigcap W_i$即可.

</div>

[think] 你先想到$G$是容易的,然后你考虑$U^C$得到$W$也是可以想到的,然后你会想把$W$交起来交$G$当构造,但直接交就不是开集了.你考虑你其实就是希望$((\bigcap \overline {W_i})\cap \overline G)\cap U^C=\varnothing$,所以取有限的就够用.

要会用这个 紧集族的有限交 性质

<div class='dbox'>

设 $f$ 是拓扑空间上的实（或广义实）函数。

如果对于每个实数 $\alpha$，集合 $\{x: f(x) > \alpha\}$ 是开集，则称 $f$ 是**下半连续**的。

如果对于每个实数 $\alpha$，集合 $\{x: f(x) < \alpha\}$ 是开集，则称 $f$ 是**上半连续**的。

</div>

<div class='dbox'>

拓扑空间 $X$ 上的复函数 $f$ 的**支集 (support)** 是集合 $\{x: f(x) \neq 0\}$ 的闭包。

$X$ 上所有**支集为紧集**的**连续**复函数的集合记为 $C_c(X)$。

</div>


<div class='cbox'>

设 $X$ 和 $Y$ 是拓扑空间，且 $f: X \to Y$ 是连续的。如果 $K$ 是 $X$ 的紧子集，则 $f(K)$ 是紧集。

</div>

连续函数把紧集映成紧集

<div class='pbox'>

考虑一个$f(K)$的开覆盖,其中每个开集的原像都是开集,且都要包含$f(K)$的原像$f^{-1}(f(K))\supset K$,于是它们的原像覆盖$K$,那么取$K$的有限覆盖再映射回来就有限覆盖$f(K)$.

</div>

<div class='cbox'>

**Corollary**

任意 $f \in C_c(X)$ 的值域是复平面的紧子集。

</div>

<div class='pbox'>

紧子集并了一个单点$0$当然还是紧的.

</div>


<div class='dbox'>

记号 $K \prec f$ 表示 $K$ 是 $X$ 的紧子集，$f \in C_c(X)$，对所有 $x \in X$ 有 $0 \le f(x) \le 1$，且对所有 $x \in K$ 有 $f(x)=1$。

记号 $f \prec V$ 表示 $V$ 是开集，$f \in C_c(X)$，$0 \le f \le 1$，且 $f$ 的支集包含于 $V$。

记号 $K \prec f \prec V$ 表示同时满足上述两个条件。

</div>

<div class='cbox'>

Urysohn's Lemma

设 $X$ 是局部紧 Hausdorff 空间，$V$ 是 $X$ 中的开集，$K \subset V$，且 $K$ 是紧集。则存在 $f \in C_c(X)$ 使得
$$ K \prec f \prec V. $$

</div>

<div class='pbox'>

所以你要怎么构造一个连续函数呢?这个定理说你把集合和有理数对应:

现在你有$K\subset V$,我们知道可以找到$K\subset V_1\subset \overline{V_1}\subset V$.然后你又可以分成$K\subset V_1$和$\overline{V_1}\subset V$细分,可以得到一个无限延伸的二叉树.

那么我们可以把它对应有理数的二进制小数表示吧,我们给第$i$层的集合对$(K,V)$赋值,如果它是左儿子赋值$2^{-i}$,是右儿子赋值$0$,对一个点$p$把所有满足$p\in V-K$的$(K,V)$对的权值加起来作为函数值.(自然还要单独赋值$K$和$V^C$上的值)

因为每层至多有一个对的权值被加了,所以一定收敛.

那么显然对每个实数对应了一个开集原像,所以是连续函数.

紧集寄掉了,我们现在构造的东西支集是$\overline V$不保证是紧的.

但是没有关系,把我们上面的构造改成从$(K,V')$作为根建二叉树即可,其中$K\subset V'\subset \overline{V'}\subset V$即可.

</div>

<div class='cbox'>

设 $V_1, \dots, V_n$ 是局部紧 Hausdorff 空间 $X$ 的开子集，$K$ 是紧集，且
$$ K \subset V_1 \cup \dots \cup V_n. $$
则存在函数 $h_i \prec V_i$ ($i=1, \dots, n$) 使得
$$ h_1(x) + \dots + h_n(x) = 1 \quad (x \in K). $$
集合 $\{h_1, \dots, h_n\}$ 称为 $K$ 上从属于覆盖 $\{V_1, \dots, V_n\}$ 的单位分解。


</div>

<div class='pbox'>

对$K$内每个点$p$存在$p\in N_p\subset \overline{N_p}\subset V_{i_p}$,然后它们之中有一个$K$的有限覆盖,我们令$H_k=\bigcup_{i_p=k} \overline{N_p}$.

这样我们找到一些紧集被$V$包含且覆盖$K$.

则可以找到$H_i\prec g_i\prec V_i$,然后令

$$
\begin{gathered}
h_i=g_i\prod_{j=1}^{i-1} (1-g_j)
\end{gathered}
$$

</div>

<div class='cbox'>

The Riesz Representation Theorem

设 $X$ 是局部紧 Hausdorff 空间，$\Lambda$ 是 $C_c(X)$ 上的正线性泛函。则在 $X$ 中存在一个包含所有 Borel 集的 $\sigma$-代数 $\mathfrak{M}$，并且在 $\mathfrak{M}$ 上存在唯一的正测度 $\mu$，它在下述意义下表示 $\Lambda$：
- (a) 对每一个 $f \in C_c(X)$，$\Lambda f = \int_X f d\mu$，
- (b) 对每一个紧集 $K \subset X$，$\mu(K) < \infty$。
- (c) 对每一个 $E \in \mathfrak{M}$，$\mu(E) = \inf\{\mu(V): E \subset V, V \text{ is open}\}$.(外正则)
- (d) 对每一个开集 $E$ 以及每一个满足 $\mu(E) < \infty$ 的 $E \in \mathfrak{M}$，关系 $\mu(E) = \sup\{\mu(K): K \subset E, K \text{ is compact}\}$
成立。(内正则)
- (e) 如果 $E \in \mathfrak{M}$，$A \subset E$，且 $\mu(E)=0$，则 $A \in \mathfrak{M}$。

</div>

<div class='pbox'>

首先,如果$\Lambda$可以对不连续函数那就直接用$\mu(S)=\Lambda \chi_S$就行了,所以你考虑逼近.同时因为$M$必须包含所有开集,定义$\mu(V)=\inf_{V\prec f} \Lambda f$或$\mu(V)=\sup_{f\prec V}$.

但这两种里只有第二种是可以的,注意$f\prec V$是一定可行的而$\prec f$的定义其实是对紧集定义的,这个开集外面可能没有紧集.

此时可以定义其他所有集合(后面会筛选出合适的$M$,剩余集合的值不要了)的值是$\mu(E)=\inf_{V\subset E} \mu(V)$.

然后为了构造Borel代数$M$,我们取所有满足内外正则性的有限集合,即满足$\mu(E)=\sup_{K\subset E} \mu(K)$且$\mu(E)<\infty$的构成$M_f$,所有满足,对任意$M_f$中的集合$A$,有$A\cap E\in M_f$中的集合$E$组成最终所求的代数$M$.

[think] 这个构造还是很难想到.不过$M_f$到$M$的一个理解方式是要求无限集合的每个局部有想要的性质.

现在要证明性质了:

<div class='cbox'>

$\mu(E)\le \sum_i \mu(E_i),\bigcup E_i=E,E_i\cap E_j=\emptyset$

</div>

<div class='pbox'>

先证明$\mu(V_1\cup V_2)\le \mu(V_1)+\mu(V_2)$,对任意$g\prec V_1\cup V_2$,存在$f_1\prec V_1,f_2\prec V_2$,且对 $\operatorname{supp} g$有$f_1+f_2=1$.那么$g=gf_1+gf_2$,于是$\Lambda g=\Lambda (gf_1+gf_2)\le \Lambda f_1+\Lambda f_2=\mu(V_1)+\mu(V_2)$对任意$g$成立,取上确界后成立.

考虑一组$V_i\supset E_i,V\supset E,f\prec V$,那么$f$的支集一定可以被有限集$C$中的$V_i,i\in C$覆盖,于是

$$
\begin{gathered}
\Lambda f\le \mu(\bigcup_{i\in C} V_i)\le \sum_{i\in C}\mu(V_i)\le \sum_{i=1}^\infty\mu(E_i)+\epsilon \\
\Rightarrow \mu(E)\le \sum_{i=1}^\infty \mu(E_i)+\epsilon \\
\Rightarrow \mu(E)\le \sum_{i=1}^\infty \mu(E_i)
\end{gathered}
$$

</div>

<div class='cbox'>

紧集$K\in M_f$,且$\mu(K)=\sup_{K\prec f} \Lambda f$

</div>

<div class='pbox'>

测度有界是因为$\Lambda$的值域是不包含无穷的.所以对一个紧集只要找到开集$V\supset K$且$\overline V$是紧的,则由刚才的Urysohn,$\exists f\prec V$,又一定$\exists \overline{V}\prec g$,则显然

$$
\begin{gathered}
f\le g \\
\Rightarrow \Lambda f\le \Lambda g \\
\Rightarrow \sup \Lambda f\le \inf \Lambda g \\
\Rightarrow \mu(K)\le \mu(V)\le \inf\Lambda g<\infty
\end{gathered}
$$

然后是考虑一个开集,$V\supset K$满足$\mu(V)\le \mu(K)+\epsilon$(根据$K$的测度的定义),那么我们一定可以找到$K\prec f\prec V$,于是$\mu(K)\le \Lambda f\le \mu(V)<\mu(K)+\epsilon$,对$\epsilon$取极限得证.

</div>

<div class='cbox'>

测度有限的开集都在$M_f$中(满足内正则)

</div>

<div class='pbox'>

考虑取一个$f\prec V,\Lambda f>\mu(V)-\epsilon$

</div>





</div>



**2.15 Definition**
定义在局部紧 Hausdorff 空间 $X$ 的所有 Borel 集构成的 $\sigma$-代数上的测度 $\mu$ 称为 $X$ 上的 **Borel 测度**。如果 $\mu$ 是正测度，Borel 集 $E \subset X$ 称为**外正则**的，如果它具有定理 2.14 中的性质 (c)；称为**内正则**的，如果它具有定理 2.14 中的性质 (d)。如果 $X$ 中的所有 Borel 集既是外正则又是内正则的，则称 $\mu$ 是**正则**的。

**2.16 Definition**
拓扑空间中的集合 $E$ 称为 **$\sigma$-紧**的，如果 $E$ 是可数个紧集的并。
测度空间中的集合 $E$（带有测度 $\mu$）称为具有 **$\sigma$-有限测度**，如果 $E$ 是可数个满足 $\mu(E_i) < \infty$ 的集合 $E_i$ 的并。

**2.17 Theorem**
设 $X$ 是局部紧、$\sigma$-紧的 Hausdorff 空间。如果 $\mathfrak{M}$ 和 $\mu$ 如定理 2.14 中所述，则 $\mathfrak{M}$ 和 $\mu$ 具有以下性质：
(a) 如果 $E \in \mathfrak{M}$ 且 $\epsilon > 0$，则存在闭集 $F$ 和开集 $V$ 使得 $F \subset E \subset V$ 且 $\mu(V-F) < \epsilon$。
(b) $\mu$ 是 $X$ 上的正则 Borel 测度。
(c) 如果 $E \in \mathfrak{M}$，则存在集合 $A$ 和 $B$ 使得 $A$ 是 $F_\sigma$ 集，$B$ 是 $G_\delta$ 集，$A \subset E \subset B$，且 $\mu(B-A)=0$。

**2.18 Theorem**
设 $X$ 是局部紧 Hausdorff 空间，且其中每个开集都是 $\sigma$-紧的。设 $\lambda$ 是 $X$ 上的任意正 Borel 测度，且对每个紧集 $K$ 都有 $\lambda(K) < \infty$。则 $\lambda$ 是正则的。

**2.19 Euclidean Spaces**
欧几里得 $k$ 维空间 $R^k$ 是所有坐标 $\xi_i$ 为实数的点 $x=(\xi_1, \dots, \xi_k)$ 的集合。
定义 $x+y$ 和 $\alpha x$。定义内积 $x \cdot y = \sum \xi_i \eta_i$ 和范数 $|x|=(x \cdot x)^{1/2}$。度量定义为 $\rho(x,y)=|x-y|$。
$R^k$ 中的开集是可数个不相交盒子的并。

**2.20 Theorem**
在 $R^k$ 的某个 $\sigma$-代数 $\mathfrak{M}$ 上存在唯一的正完备测度 $m$，具有以下性质：
(a) 对每个 $k$-维胞腔 (box/cell) $W$，$m(W) = \text{vol}(W)$。
(b) $\mathfrak{M}$ 包含 $R^k$ 中的所有 Borel 集；更确切地说，$E \in \mathfrak{M}$ 当且仅当存在 $A, B \subset R^k$ 使得 $A \subset E \subset B$，$A$ 是 $F_\sigma$，$B$ 是 $G_\delta$，且 $m(B-A)=0$。此外，$m$ 是正则的。
(c) $m$ 是平移不变的，即对每个 $E \in \mathfrak{M}$ 和每个 $x \in R^k$，有 $m(E+x) = m(E)$。
(d) 如果 $\mu$ 是 $R^k$ 上任意正的平移不变 Borel 测度，且对每个紧集 $K$ 都有 $\mu(K) < \infty$，则存在常数 $c$ 使得对所有 Borel 集 $E \subset R^k$ 有 $\mu(E) = c m(E)$。
(e) 对每一个 $R^k$ 到 $R^k$ 的线性变换 $T$，对应一个实数 $\Delta(T)$，使得对每个 $E \in \mathfrak{M}$，有 $m(T(E)) = \Delta(T)m(E)$。

**2.21 Remarks**
如果 $m$ 是 $R^k$ 上的 Lebesgue 测度，习惯上将 $L^1(m)$ 写为 $L^1(R^k)$。
如果 $k=1$，习惯上将 $\int f dm$ 写为 $\int_a^b f(x) dx$。
并非每个 Lebesgue 可测集都是 Borel 集。并非 $R^k$ 的每个子集都是 Lebesgue 可测的。

**2.22 Theorem**
如果 $A \subset R^1$ 且 $A$ 的每个子集都是 Lebesgue 可测的，则 $m(A)=0$。

**Corollary**
每一个正测度集合都有不可测子集。

**2.23 Determinants**
定理 2.20(e) 中的比例因子 $\Delta(T)$ 可以通过行列式进行代数解释：
$\Delta(T) = |\det T|$。

**2.24 Lusin's Theorem**
设 $f$ 是 $X$ 上的复可测函数，$\mu(A) < \infty$，若 $x \notin A$ 则 $f(x)=0$，且 $\epsilon > 0$。则存在 $g \in C_c(X)$ 使得
$$ \mu(\{x: f(x) \neq g(x)\}) < \epsilon. $$
此外，我们可以安排使得 $\sup_{x \in X} |g(x)| \le \sup_{x \in X} |f(x)|$。

**Corollary**
假设 Lusin 定理的条件满足且 $|f| \le 1$。则存在序列 $\{g_n\}$ 使得 $g_n \in C_c(X)$，$|g_n| \le 1$，且
$$ f(x) = \lim_{n \to \infty} g_n(x) \quad \text{a.e.} $$

**2.25 The Vitali-Caratheodory Theorem**
设 $f \in L^1(\mu)$，$f$ 是实值函数，且 $\epsilon > 0$。则在 $X$ 上存在函数 $u$ 和 $v$ 使得 $u \le f \le v$，$u$ 是上半连续且上有界的，$v$ 是下半连续且下有界的，并且
$$ \int_X (v-u) d\mu < \epsilon. $$