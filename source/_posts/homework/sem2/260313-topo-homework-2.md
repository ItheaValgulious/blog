---
title: Topo Homework - Week 2
tags:
  - topo
  - math
  - homework
date: 2026-03-13 10:03:34
---


# Topo Homework - Week 2

### T1

<div class="cbox">

**1.** (ER) 尝试给出 $X = \{a, b, c, d\}$ 的两个非豪斯多夫的拓扑、一个豪斯多夫的拓扑, 并证明它们对应的拓扑空间不同胚.

</div>

<div class="pbox">

Not T2:
- $\{\varnothing,X, \{ a \} ,\{ a,b \} ,\{ a,b,c \}  \}$
- $\{\varnothing,X, \{ a,b,c,d \} \}$

T2:

- 离散拓扑

T2是拓扑性质:若存在连续双射$f:X\to Y$是同胚,则$X$中的开集/闭集与$Y$中的一一对应,所以$T_i$均为拓扑性质.因此T2的一定与其他的不同胚.

对非T2的两个,开集数量不同,肯定没法双射.不同胚.

</div>

### T2

<div class="cbox">

**2.** (ER) 证明豪斯多夫空间的乘积是豪斯多夫空间.

</div>

<div class="pbox">

若$(X,_X),Y$为T2可分空间,则考虑$\forall (x_1,y_1),(x_2,y_2)\in X\times Y$,则因为$X$是T2可分的,所以 $\exists x_1\in U_1,x_2\in U_2,U_1,U_2 \text{ is open},U_1\cap U_2=\varnothing$.同理存在$y_1\in V_1,y_2\in V_2,V_1,V_2 \text{ is open},V_1\cap V_2=\varnothing$.于是$(x_1,y_1)\in (U_1\times V_1),(x_2,y_2)\in (U_2\times V_2)$满足条件,乘积空间T2可分.

</div>

### T3

<div class="cbox">

**2.** (ER) 设 $A$ 是 $X$ 中闭集, $B$ 是 $Y$ 中闭集. 证明 $A \times B$ 是 $X \times Y$ 中闭集.

</div>

<div class="pbox">

$A=X-C,B=Y-D$,则$C\times D\cup C\times Y\cup X\times D$是开集,于是$A\times B=X\times Y-(C\times D\cup C\times Y\cup X\times D)$是闭集.

</div>

### T4

<div class="cbox">

**11.** (E) 证明在 $\mathbb{Z}$ 的数字线拓扑空间中, $\{n\}$ 是闭集当且仅当 $n$ 是偶数.

</div>

<div class="pbox">

若$n=2k$是偶数,则$Z-\{n\}=\bigcup_{i\ne k} \{2i-1,2i,2i+1\}$为开集,所以$\{n\}$是闭集.

若$n=2k+1$不为奇数,假设$\{n\}$是闭集,则$A=Z-\{n\}$是开集,所以存在$i$使得$n+1\in \{2i-1,2i,2i+1\}\subset A$或$n+1\in {2i+1}\subset A$.因为$n+1$是偶数所以第二种不可能只能是第一种,则$i=k+1$,则其包含$n$,矛盾,所以$\{n\}$不是闭集.

</div>

### T5

<div class="cbox">

**8.** (E) 证明在 $\mathbb{R}$ 的下极限拓扑空间中, $[a, b)$ 是闭集.

</div>

<div class="pbox">

$R-[a,b)=(-\infty,a)\cup [b,\infty)=\bigcup_i [a-i,a)\cup \bigcup_i [b,b+i)$为开集,故$[a,b)$是闭集.

</div>