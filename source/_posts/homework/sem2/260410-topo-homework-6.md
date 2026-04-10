---
title: Topo Homework - Week 5
tags:
  - math
  - topo
  - homework
date: 2026-04-10 23:05:47
---

# Topo Homework - Week 5

### T1

<div class="cbox">

**7. (ERH)** 设 $A$ 为度量空间 $(X, d)$ 的紧致子集.
- (1) $A$ 的直径定义为 $D(A) = \sup\{d(x, y) \mid x, y \in A\}$, 证明存在 $x, y \in A$, 使得 $D(A) = d(x, y)$;
- (2) 设 $x \in X, x \notin A$, 证明存在 $y \in A$, 使得 $d(x, A) = d(x, y)$;
- (3) 设 $B$ 是 $X$ 的闭集, $B \cap A = \emptyset$. 证明 $d(A, B) > 0$.

</div>

<div class="pbox">

(1):

设$f_A(x)=\sup_y\{d(x,y)|y\in A\}$.因为$A$是紧集,$d(x,y)$固定$x$后是关于$y$的连续函数把紧集映成$R$上紧集,故此时$f_A(x)=\max_y\{d(x,y)|y\in A\}$.

又容易看出$f_A(x)$连续(存在$x$的邻域$B(x,\delta)$,$\forall y,x'\in U$,$d(x',y)<d(x,y)+d(x,x')<d(x,y)+\delta$,从而$f(B(x,\delta))\subset B(f(x),\epsilon)$).于是$f_A(A)$紧,存在$x,D(A)=f_A(x)$,故都取的到.

(2):

设$g_A(x)=\inf_y\{d(x,y)|y\in A\}$,把上一问第一段的内容里$\sup$换成$\inf$即证.

(3):

$$
\begin{gathered}
d(A,B)=\inf_A g_B(x)
\end{gathered}
$$

因为$A\cap B=\varnothing$,故$\forall x\in A,x\in X-B,\exists x\in B(x,\epsilon)\subset X-B$,故$g_B(x)>0$.又因为连续,所以外部这个$\inf$必然在某个$y\in A$处取到,即$\exists y,d(A,B)=f(y)>0$.

</div>

### T2

<div class="cbox">

**8. (ERH)** 给出 $\mathbb{R}^2$ 的一个没有勒贝格数的开覆盖的例子.

</div>

<div class="pbox">

$R$都有,何必$R^2$.

设调和级数列$H_n=\sum_{i=1}^n \dfrac1i$.取开覆盖

$$
\begin{gathered}
O=\{ (-(H_{n+1}+\dfrac1n),-(H_n-\dfrac1n))\cup ((H_n-\dfrac1n),(H_{n+1}+\dfrac1n)) |n\in N^*\} \cup \{(-1,1)\}
\end{gathered}
$$

显然$x\to \infty$时其所在区间长度趋近于$0$,没有勒贝格数.

</div>

### T3

<div class="cbox">

**10. (MRH)** 给出下列空间的一点紧致化的同胚空间的几何描述:
- (1) $(0, 1) \cup (2, 3)$;
- (2) 平环 $\{(x, y) \in \mathbb{R}^2 \mid 1 < x^2 + y^2 < 2\}$;
- (3) 不含顶点的正方形块 $\{(x, y) \in \mathbb{R}^2 \mid x, y \in [-1, 1], |xy| < 1\}$;
- (4) 带状区域 $\{(x, y) \in \mathbb{R}^2 \mid x \in [0, 1]\}$.

</div>

<div class="pbox">

(1):

两个分别一点紧化都是$S^1$,然后粘起来是$S^1\wedge S^1$.

(2):

香蕉,再把两边的端点重合.

(3):

把这四个顶点粘合成一个

(4):

$S^1\times [-1,1]/\{\{0\}\times [-1,1]\}$

</div>

### T4

<div class="cbox">

**1. (ER)** 尝试找出 $X = \{a, b, c, d\}$ 的两个拓扑, 其中一个连通, 另一个不连通.

</div>

<div class="pbox">

平凡拓扑连通.离散拓扑不连通.

$$
\begin{gathered}
\{ \{ a,b \} ,\{ c,d \} ,\varnothing,X \} \text{ is disconnected}  \\
\{ \{ a,b,c,d \} ,\{ a,b,c \} ,\{ a,b \} ,\{ a \} ,\varnothing,X \} \text{ is connected} 
\end{gathered}
$$

</div>

### T5

<div class="cbox">

**2. (ERH)** 设 $\{C_n \mid n \in \mathbb{N}\}$ 为拓扑空间 $X$ 的一族连通子集, 满足对每个 $j \ge 1$, $C_j \cap C_{j+1} \neq \emptyset$. 证明 $\bigcup_{n \in \mathbb{N}} C_n$ 也是 $X$ 的连通子集.

</div>

<div class="pbox">

假设$U=\bigcup_n C_n$不连通,则存在开集$A,B$满足$A\cap B\cap U=\varnothing,U\subset A\cup B,(A\cap U)\ne \varnothing,(B\cap U)\ne \varnothing$.

那么对每个$C_n$都有$C_n\subset A\lor C_n\subset B$.不妨设$C_1\subset A$,则若$C_i\subset A$,则若$C_{i+1}\subset B$则$C_{i+1}\cap C_i=\varnothing$矛盾,于是$C_{i+1}\subset A$,于是$\forall n,C_n\subset A$,与$B\cap U\ne \varnothing$矛盾.

于是连通.

</div>

### T6

<div class="cbox">

**3. (ERH)** 证明:
- (1) $\mathbb{R}^2$ 中所有至少有一个坐标是有理数的点构成的集合 $A$ 连通;
- (2) $\mathbb{R}^2$ 中所有第二个坐标为有理数的点构成的集合 $B$ 不连通.

</div>

<div class="pbox">

(1):

对任意两个满足这个条件的点$(x,y),(a,b)$.

若是相同的维度上是有理数,不妨设是第一维,则$f(t)=(x,ty+(1-t)b)$是一条道路.

若不同维度上是有理数,不妨设$x\in Q,b\in Q$,则两个点都用上面的方法与$(x,b)$连通.所以他道路连通,所以它连通.

(2):

$R\times (-\infty,\sqrt 2)\cap Q$和$R\times (\sqrt 2,\infty)\cap Q$是满足不连通判定条件的两个集合.

</div>

### T7

<div class="cbox">

**5. (E)** 在 $\mathbb{R}$ 上, $\mathcal{B} = \{(-a, a) \mid a \in \mathbb{R}, a \ge 0\}$ 是一个拓扑基, 证明它所生成的拓扑空间是连通的.

</div>

<div class="pbox">

只需证不存在一个非空真子开集既开又闭.

但你开集一定包含$0$,闭集一定不包含$0$,所以一定不存在.于是连通.

</div>

### T8

<div class="cbox">

**9. (MR)** 设 $A$ 和 $B$ 是 $X$ 的两个连通的子集, $A \cap \text{Cl}(B) \neq \emptyset$, 证明 $A \cup B$ 也是连通的.

</div>

<div class="pbox">

反证,假设可以被$U\cap V=\varnothing$两个闭集分开.则因为$A,B$连通,不妨设$A\subset U,B\subset V$.

那么 $B\subset V \Rightarrow \operatorname{Cl}B\subset V \Rightarrow U\cap V=\varnothing$,矛盾.得证.

</div>

### T9

<div class="cbox">

**10. (MRH)** 设 $A$ 和 $B$ 都是 $X$ 的开子集 (或者闭子集), 它们的并集和交集都是连通的, 证明 $A$ 和 $B$ 也都是连通的.

</div>

<div class="pbox">

假设$A$不连通,$A=U\cup V,U\cap V=\varnothing,U,V$是开集.

则$A\cap B=(U\cap B)\cup (V\cap B)$连通,于是必有$U\cap B=\varnothing$或$V\cap B=\varnothing$,不妨设$U\cap B=\varnothing$.

则$A\cup B=U\cup (V\cup B)$,$U$和$V\cup B$是一个满足不连通判定条件的分割.与$A\cup B$连通矛盾.得证.

</div>