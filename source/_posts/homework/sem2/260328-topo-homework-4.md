---
title: Topo Homework - Week 4
tags:
  - topo
  - math
  - homework
date: 2026-03-28 15:18:34
---

# Topo Homework - Week 4

### T1

<div class="cbox">

**12.** (ERH) 证明下面的平面区域是同胚的:
1. 整个 $A=\mathbb{R}^2$ 平面;
2. 开象限 $B=\{(x, y) \mid x, y > 0\}$;
3. 开角 $C=\{(x, y) \mid x > y > 0\}$;
4. 平面去掉一条射线 $l$, 其中 $l = \{(x, y) \mid y = 0, x \geqslant 0\},D=A-l$.

</div>

<div class="pbox">

$f_1(x,y)=(e^x,e^y), f_1^{-1}(x,y)=(\ln x,\ln y)$,则 $f_1(A)=B,f_1^{-1}(B)=A,f_1,f_1^{-1} \text{ is continuous}$,故$A\cong B$.

$f_2(x,y)=(x+y,y),f_2^{-1}(x,y)=(x-y,y)$,则$f_2(B)=C,f_2^{-1}(C)=B$,且 $f_2,f_2^{-1} \text{ is continuous}$,故$B\cong C$.

$$
\begin{gathered}
\forall r>0,\theta\in (0,\frac\pi2) \\
\text{define } f_3 (r\sin \theta,r\cos \theta)=(r\sin 4\theta,r\cos 4\theta) \\
f_3^{-1}=(r\sin 4\theta,r\cos 4\theta)=(r\sin \theta,r\cos \theta) \\
\end{gathered}
$$

容易验证$f_3,f_3^{-1}$连续,且$f_3(C)=D,f_3^{-1}(D)=C$,故$C\cong D$.

($(x,y)\to (r,\theta)$连续,$(r\theta)\to (x,y),\theta\in (0,2\pi)$连续,故是三个连续函数的复合,都连续)

</div>

### T2

<div class="cbox">

**15.** (MRH) 设 $X = (0, 1) \cap \mathbb{Q}$ 和 $Y = ((0, 1) \cup (2, 3)) \cap \mathbb{Q}$ 都是标准直线 $\mathbb{R}$ 的子空间, 证明 $X$ 和 $Y$ 同胚.

</div>

<div class="pbox">

$(0,1)\cap Q=((0,\dfrac{\sqrt 2}{2} )\cap Q)\cup ((\dfrac{\sqrt 2}2,1)\cap Q)$,只需证明$\forall (a,b),(c,d)$有$(a,b)\cap Q\cong (c,d)\cap Q$,则由焊接引理可得到整体上的连续映射,从而$X\cong Y$.

考虑构造保序双射,则取 $\{ f_n \} _{n=1}^\infty$,要求每个$f$都是某个有限子集上的保序双射,则可以写$f_i\subset ((a,b)\cap Q\times (c,d)\cap Q)$且是有限集.

显然$A=(a,b)\cap Q,B=(c,d)\cap Q$可数,可以排成列 $\{ A_n \} ,\{ B_n \}$,考虑在第$2k-1$步将一个$A$中的元素加入定义域,在第$2k$步加入$B$中元素到值域.

那么现在取最小的$i$满足$x=A_i$不在$f_{i-1}$定义域中,则因为$f_{i-1}$是保序的,所以可以把所有定义域中的$A$中的元素分成$L,R$两个集合,满足$\forall l\in L,r\in R,l<x<r$,则有$\forall l'\in f(L),r'\in f(R),f(l')<f(r')$,于是可以从$(\max f(l'),\min f(r'))$中任取一个$B$中还没被定义的元素$y$,令$f_{i-1}=f_i\cup (x,y)$.对$2k$步加入$B$步中的同理.

则取$f=\bigcup_i f_i$为保序双射,从而显然连续且逆也连续,从而是同胚.

</div>

### T3

<div class="cbox">

**21.** (ERH) 设 $f: X \to Y$ 是一个同胚, $A \subset X$. 证明:
1. $A$ 在 $X$ 中是闭的当且仅当 $f(A)$ 在 $Y$ 中是闭的;
2. $f(\text{Cl}(A)) = \text{Cl}(f(A))$;
3. $f(\text{Int}(A)) = \text{Int}(f(A))$;
4. $f(\partial A) = \partial f(A)$;
5. $A$ 是点 $x \in X$ 的一个邻域当且仅当 $f(A)$ 是点 $f(x)$ 的一个邻域.

</div>

<div class="pbox">

1:$f$是同胚,故$f$连续,从而$f(A)$闭推$A$闭;$f^{-1}$连续,从而$A=f^{-1}(f(A))$闭推$f(A)$闭.

2:
$$
\begin{gathered}
\operatorname{Cl}A=\bigcap_{F \text{ is closed},F \supset A} F \\
\Rightarrow f(\operatorname{Cl}A)=f(\bigcap_{F \text{ is closed},F \supset A} F) \\
=\bigcap_{F \text{ is closed},F \supset A} f(F) \\
=\bigcap_{f(F) \text{ is closed},f(F) \supset f(A)} f(F) \\
=\operatorname{Cl}f(A)
\end{gathered}
$$

3:
$$
\begin{gathered}
f(\operatorname{Int}A)=f(X-\operatorname{Cl}(X-A)) \\
=f(X)-f(\operatorname{Cl}(X-A)) \\
=f(X)-(\operatorname{Cl}(f(X)-f(A))) \\
=Y-\operatorname{Cl}(Y-A) \\
=\operatorname{Int}A
\end{gathered}
$$

4:
$$
\begin{gathered}
f(\partial A)=f(\operatorname{Cl}A-\operatorname{Int}A) \\
=f(\operatorname{Cl}A)-f(\operatorname{Int}A) \\
=\operatorname{Cl}f(A)-\operatorname{Int}f(A) \\
=\partial f(A)
\end{gathered}
$$

5:
$$
\begin{gathered}
A \text{ is a neighborhood of }x  \\
\Leftrightarrow \exists x\in U\subset A,U \text{ is open}  \\
\Leftrightarrow \exists f(x) \in f(U)\subset f(A),f(U) \text{ is open}  \\
\Leftrightarrow f(A) \text{ is a neighborhood of } f(x)
\end{gathered}
$$

</div>

### T4

<div class="cbox">

**22.** (E) 设 $f: X \to Y$ 是一个同胚. 证明对于每一个 $A \subset X$, 子映射 $f|_A: A \to f(A)$ 也是一个同胚.

</div>

<div class="pbox">

若$f$连续,则$f|_A^{-1}(V)=f^{-1}(V)\cap A$是$A$中开集,于是$f|_A$连续,而$f|_A^{-1}=f^{-1}|_{f(A)}$连续.同时$f$是双射显然有$f|_A$是单射,而$f|_A:A\to f(A)$也是满射,故是双射,且其和逆都连续,是同胚.

</div>

### T5

<div class="cbox">

**32.** (ERH) 设 $\mathbb{Z}$ 与 $\mathbb{Q}$ 带有从标准直线 $\mathbb{R}$ 诱导而来的子空间拓扑. 证明:
1. $\mathbb{Z}$ 与 $\mathbb{Q}$ 不同胚;
2. $\mathbb{Q}$ 不能嵌入 $\mathbb{Z}$.

</div>

<div class="pbox">

${\mathbb Z}$的上的拓扑是离散拓扑,${\mathbb Q}$上的拓扑是开集为所有$(a,b)\cap Q$.

假设$f:Q\to A$是连续双射,其中$A$是$Z$的子空间,那么$\forall S\subset Q$,$f(S) \text{ is open} \Rightarrow S \text{ is open}$,但$Q$中单点集是闭集,矛盾,所以不存在$Q\to A$的连续双射.所以不同胚也不能嵌入.



</div>

### T6

<div class="cbox">

**12.** (ER) 证明$T_4$空间的闭子空间仍然是$T_4$空间.

</div>

<div class="pbox">

设$X$是$T_4$空间,$F\subset X$是$X$的闭子空间.

对$F$中的任意两个闭集$A_F,B_F$,因为$F$是闭集所以$A,B$在$X$中的$A_X,B_X$也是闭集,所以存在$U_X\cap V_X=\varnothing,A_x\subset U_X,B_X\subset V_X$,于是$U_F=U_X\cap F,V_F=V_X\cap F$是$X$中的开集,故存在$A_F\subset U_F,B_F\subset V_F,U_F\cap V_F=\varnothing$,故$F$是$T_4$空间.

</div>

### T7

<div class="cbox">

**14.** (ER) 设 $\mathcal{B} = \{(a, b) \mid a, b \in \mathbb{R}, a < b\} \cup \{(c, d) \cap \mathbb{Q} \mid c, d \in \mathbb{R}, c < d\}$. 证明:
1. $\mathcal{B}$ 是 $\mathbb{R}$ 上一个拓扑 $\mathcal{T}$ 的基;
2. 拓扑空间 $(\mathbb{R}, \mathcal{T})$ 是豪斯多夫空间;
3. 拓扑空间 $(\mathbb{R}, \mathcal{T})$ 不是 $T_3$ 空间.

</div>

<div class="pbox">

1:显然$(n,n+1)$覆盖了$R$,对任意两个$\mathcal B$中的元素:
若都是开区间,则显然交也属于$\mathcal B$;若一个是开区间一个是开区间内的有理数则其交等于两个都是开区间的有理数也在$\mathcal B$中.

2:对任意两个点$x<y$,取$(x-1,\dfrac{x+y}2),(\dfrac{x+y}2,y+1)$即满足条件.

3:取闭集$F=((-1,1)\cap Q)^C\cap [0,1]$是$[0,1]$中的无理数,取点$\dfrac12$,则若存在一个开集$V$包含$F$和一个开集$U$包含$\dfrac12$,则$\exists \delta>0$使得$U\supset (\dfrac12-\delta,\dfrac12+\delta)\cap Q$,那么在$(\dfrac12-\delta,\dfrac12+\delta)$中任取一无理数,其无法被任何开集包含而与$U$不交.

</div>