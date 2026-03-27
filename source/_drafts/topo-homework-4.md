---
title: Topo Homework - Week 4
tags: [topo,math,homework]
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


</div>

### T4

<div class="cbox">

**22.** (E) 设 $f: X \to Y$ 是一个同胚. 证明对于每一个 $A \subset X$, 子映射 $f|_A: A \to f(A)$ 也是一个同胚.

</div>

<div class="pbox">


</div>

### T5

<div class="cbox">

**32.** (ERH) 设 $\mathbb{Z}$ 与 $\mathbb{Q}$ 带有从标准直线 $\mathbb{R}$ 诱导而来的子空间拓扑. 证明:
1. $\mathbb{Z}$ 与 $\mathbb{Q}$ 不同胚;
2. $\mathbb{Q}$ 不能嵌入 $\mathbb{Z}$.

</div>

<div class="pbox">


</div>

### T6

<div class="cbox">

**11.** (MR) 尝试给出 $T_1$ 条件下 $T_3$ 但非 $T_4$ 拓扑空间的例子.

</div>

<div class="pbox">


</div>

### T7

<div class="cbox">

**14.** (ER) 设 $\mathcal{B} = \{(a, b) \mid a, b \in \mathbb{R}, a < b\} \cup \{(c, d) \cap \mathbb{Q} \mid c, d \in \mathbb{R}, c < d\}$. 证明:
1. $\mathcal{B}$ 是 $\mathbb{R}$ 上一个拓扑 $\mathcal{T}$ 的基;
2. 拓扑空间 $(\mathbb{R}, \mathcal{T})$ 是豪斯多夫空间;
3. 拓扑空间 $(\mathbb{R}, \mathcal{T})$ 不是 $T_3$ 空间.

</div>

<div class="pbox">


</div>