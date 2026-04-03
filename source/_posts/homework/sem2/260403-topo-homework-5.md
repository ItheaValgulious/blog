---
title: Topo Homework - Week 5
tags:
  - topo
  - math
  - homework
date: 2026-04-03 16:47:45
---


# Topo Homework - Week 5

### T1

<div class="cbox">

**15.** (ERH) 证明 $C_1$ 空间 $X$ 是豪斯多夫空间当且仅当 $X$ 中任意序列至多有一个极限点.

</div>

<div class='pbox'>

$\Rightarrow$:因为$T_2$,故假设序列 $\{ x_n \}\to a,\{ x_n \} \to b,a\ne b$,则$\exists a\in U\subset X,\exists b\in V\subset X,U\cap V=\varnothing$,$U,V$是开集.但$\exists N,\forall n>N,x_i\in U\cap V=\varnothing$,$x_i\in \varnothing$,矛盾.故任意$x$至多有一个极限点.

$\Leftarrow$:由于$C_1$,故$\forall a\ne b,a,b\in X$,$\exists \{ U_n \}$是$a$的一组嵌套的($U_i\subset U_{i-1}$)邻域基,$\{ V_n \}$是$b$的嵌套的邻域基.现在证明$\exists a\in U,b\in V,U,V \text{ is open},U\cap V=\varnothing$,反证,假设任意两个分别包含$a,b$的开集都有交.

那么令$W_i=U_i\cap V_i\ne \varnothing$,构造点列 $\{ x_i \}$使得$x_i\in W_i$,由于$U_i\subset U_{i-1},V_i\subset V_{i-1}$,所以$W_i\subset W_{i-1}$,于是对$a$的任意开邻域$U$,存在$W_i$被其包含,从而能对任意$n>i,x_i\in U$;对$b$同理.故$x_n$有至少两个极限点,矛盾.

故任意$a,b$可以被两个不交开集分开,是$T_2$空间.

</div>

### T2

<div class="cbox">

**16.** (MH) 举例说明 $C_2$ 空间在连续映射下的像未必是 $C_2$ 空间.

</div>

<div class='pbox'>

考虑$R$上的标准拓扑到余有限拓扑的单位映射.

显然$R$是$C_2$空间,显然余有限拓扑中的开集都是标准拓扑上的开集,所以单位映射连续.

但是余有限拓扑不$C_2$:先假设它是$C_2$,存在一个可数基 $\{ B_i \}$,则设$C_i=X-B_i$是有限集,$S=\bigcup_i C_i$是可数集,那么必然有$S\ne R,\exists x\in X-S$.

但是考虑开集$X-\{x\}$,如果它是一些$B_i$的并,则$x$是一些$C_i$的交,但$x$不在任何$C_i$中,矛盾.

于是余有限拓扑确实不$C_2$,得证.

</div>

### T3

<div class="cbox">

**18.** (MR) 证明:
(1) 积空间 $X \times Y$ 第一 (二) 可数当且仅当 $X$ 与 $Y$ 都第一 (二) 可数;

</div>

<div class='pbox'>

(1):

第一可数:

若$X,Y$都$C_1$,对任意$(x,y)\in X\times Y,\exists x\in U_i\subset U_{i-1},\exists x\in V_i\subset V_{i-1}$为两组邻域基,则对任意$(x,y)$的邻域$W$,存在一个邻域基中元素$(x,y)\in A\times B\subset W$,存在$x\in U_i\subset A,y\in V_j\subset B$,于是得$(x,y)\in U_i\times V_j\subset A\times B\subset W$,于是$U_i\times V_j$是一组邻域基,而他是可数乘可数仍然可数个.

若$X\times Y$是$C_1$,则对$X$中任何 $x\in U,U \text{ is open}$,则任取$(x,y)$,存在$(x,y)$的邻域基 $W_i$,取 $V_i\times \{ y \}= W_i\cap (X\times \{ y \})$,那么存在$i$,$(x,y)\in W_i\subset U\times Y$,从而$V_i\subset U$,所有的$V_i$是邻域基.$X$是第一可数.对$Y$一样.

第二可数:

若$X,Y$都是第二可数有可数基$B_1,B_2$,那么 $X\times Y$的一组基 $\{ b_1\times b_2 |b_1\in B_1,b_2\in B_2\}$也是可数的,故$X\times Y$第二可数.

若$X\times Y$是第二可数的,那么取它的一组基$B$,取一个$y$,设$X$的基是 $B_x=\{ U |(U\times \{ y \} )=b\cap (X\times \{ y \} ),b\in B \}$,则任意$x\in W$,$\exists (x,y)\in V\subset W\times Y,V\in B$,则$U\times \{y\}=V\cap (X\times \{y\})$对应的$U$满足$x\in U\subset W$.从而$B_x$是拓扑基.

</div>

### T4

<div class="cbox">

**2.** (ER) 设 $X$ 为 $T_4$ 空间, $A$ 是 $X$ 的闭子集, $f : A \to \mathbb{R}^n$ 是连续映射, 证明 $f$ 可以连续扩张到 $X$ 上.

</div>

<div class='pbox'>

由tietze扩张定理,$\forall i,f^{(i)}:A\to R,f^{(i)}=P_i\circ f$可以连续扩张到$X$上成为$g^{(i)}:X\to R$,其中$P_i$是取第$i$个分量的投影映射.

那么因为每个分量都连续,设$g=(g(1),\ldots,g(n)):X\to R^n$,$R^n$ 有拓扑基 $B=\{ \times_{i=1}^n [a_i,b_i]|\forall \{ a_i \} ,\{ b_i \}  \}$
 
$\forall x\in B,g^{-1}(x)=\bigcap_{i=1}^n (g^{(i)})^{-1}([a_i,b_i])$,是有限个开集的交还是开集.故它把所有拓扑基中的元素拉回到开集,故它把所有开集拉回到开集,$g$是$f$的连续扩张.


</div>

### T5

<div class="cbox">

**7.** (ER) 设 $X$ 为仅含有有限个点的拓扑空间, 证明 $X$ 可度量化的充要条件是 $X$ 为离散空间. 试举出一个有可数无限个点的可度量化空间, 但该空间非离散的例子.

</div>

<div class='pbox'>

(1):假设其可度量化,因为 $d(a,b)=0 \Leftrightarrow a=b$,则$\forall b\ne a,d(a,b)>0$,设$d_a=\dfrac12 \min_{b\ne a} \{d(a,b)\}$,则取开球$B(a,d_a)=a$,故单点集是开集,是离散拓扑.而离散拓扑都可以用离散度量$d(x,y)=1-[x=y]$度量化.

(2):$Z$上赋予所有等差数列为开集的拓扑.

</div>

### T6

<div class="cbox">

**1.** (ER) 确定下面的每一个子空间 (有标准子空间拓扑) 是否是紧的. 不紧的给出一个没有有限子覆盖的开覆盖.
- (1) $\mathbb{N}_+$;
- (2) $\mathbb{R}$;
- (3) $\mathbb{Q}$;
- (4) $(0,1]$;
- (5) $\left\{ \frac{1}{n} \mid n \in \mathbb{N}_+ \right\}$;
- (6) $\left\{ \frac{1}{n} \mid n \in \mathbb{N}_+ \right\} \cup \{0\}$.

</div>

<div class='pbox'>

(1):不紧,所有单点集是一个满足条件的开覆盖.

(2):不紧,$\{(x-1,x+1)\}_{x\in R}$是满足条件的开覆盖.

(3):不紧,$\{(x-1,x+1)\cap Q\}_{x\in Q}$是满足条件的开覆盖.

(4):不紧,$\{ (\dfrac1n,2) \}_{n\in N_+}$是满足条件的开覆盖

(5):不紧,所有单点集

(6):紧

</div>

### T7

<div class="cbox">

**2.** (ER) 设 $X = \{a, b, c, d, \dots\}$ 是由可列个点组成的集合. 尝试给出 $X$ 的两个拓扑, 其中一个空间是紧致的, 另一个不是紧致的.

</div>

<div class='pbox'>

平凡拓扑是紧致的,离散拓扑不是紧致的()

余有限拓扑是紧致的,排成一列后数字线/标准拓扑不是.

</div>

### T8

<div class="cbox">

**8.** (ER) 设 $X$ 为拓扑空间.

(1) 用定义证明 $X$ 的两个紧子集的并是紧子集;

(2) 可数个紧子集的并一定是紧子集吗?

</div>

<div class='pbox'>

(1):

对两个紧子集的并$A\cup B$的一组开覆盖 $U_\lambda,\lambda \in S$,它也是$A,B$各自的开覆盖,故其有两个有限的子集$T_1\subset S,T_2\subset S$分别是$A,B$各自的有限子覆盖,则$T_1\cup T_2$是$A\cup B$的有限子覆盖.

(2):

不一定,如$R$上标准拓扑,$[n,n+1]$是紧集,$\cup_{n\in Z} [n,n+1]=R$不紧.

</div>

### T9

<div class="cbox">

**15.** (MRH) 设 $\mathcal{T}_1$ 和 $\mathcal{T}_2$ 是 $X$ 上的两个拓扑, 且 $\mathcal{T}_2 \subset \mathcal{T}_1$. 证明:
- (1) 如果 $(X, \mathcal{T}_1)$ 是紧致的, $(X, \mathcal{T}_2)$ 是豪斯多夫的, 则 $\mathcal{T}_1 = \mathcal{T}_2$;
- (2) 如果 $(X, \mathcal{T}_2)$ 是豪斯多夫的, 且 $\mathcal{T}_2 \subsetneq \mathcal{T}_1$, 则 $(X, \mathcal{T}_1)$ 不是紧致的;
- (3) 如果 $(X, \mathcal{T}_1)$ 是紧致的, 且 $\mathcal{T}_2 \subsetneq \mathcal{T}_1$, 则 $(X, \mathcal{T}_2)$ 不是豪斯多夫的.

</div>

<div class='pbox'>

考虑单位映射$i:A=(X,\mathcal{T}_1)\to (X,\mathcal{T}_2)=B,j=i^{-1}$.

$\mathcal{T}_2\subset \mathcal{T}_2 \Rightarrow i \text{ is continuous}$.

(1):因为$A$紧致$B$是Hausdorff,故$i$把闭集(紧集)映到紧集(闭集),于是$j$连续,$i,j$是同胚,$A=B$.

(2):这不就是把(1)重新说了一遍?

(3):这不也是把(1)重说了一遍?

</div>

### T10

<div class='cbox'>

$C_1$空间的乘积或子空间也是$C_1$的.

</div>

<div class='pbox'>

乘积空集前面证过了.

对子空间$A\subset X$,考虑$x$在$X$中的一组可数邻域基$U_i$,则显然有$\forall x\in U\subset A$是$x$在$A$中的开邻域,存在$U=U'\cap A$,而$\exists U_i\subset U'$,故存在$U_i\cap A\subset U'\cap A=U$,故$U_i\cap A$是子空间的邻域基,可数.

</div>



