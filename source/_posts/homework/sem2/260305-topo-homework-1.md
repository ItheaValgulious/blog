---
title: Topo Homework - Week 1
tags:
  - topo
  - math
  - homework
date: 2026-03-05 23:13:45
---

# Topo Homework - Week 1

### T1

<div class="cbox">

**5. (ER)** 在三点集 $X = \{a,b,c\}$ 上, 平凡拓扑有两个开集, 离散拓扑有八个开集. 对于 $n = 3,4,5,6,7$ 中的每一个数, 找出 $X$ 上由 $n$ 个开集组成的拓扑, 或证明这样的拓扑不存在.

</div>

<div class="pbox">

- 3:$\{ \varnothing,X,\{ a \}\}$
- 4:$\{ \varnothing,X,\{ a \} ,\{ a,b \}\}$
- 5:$\{ \varnothing,X,\{ a \} ,\{ b \} ,\{ a,b \} \}$
- 6:$\{ \varnothing,X,\{ a \} ,\{ b \} ,\{ a,b \} ,\{ a,c \}  \}$

对于$n=7$,容易验证删掉任何一个开集都不构成拓扑.

</div>

### T2

<div class="cbox">

**6. (ER)** 在 $\mathbb{R}$ 上定义一个拓扑 $\mathcal{T}$ (通过列出其中的开集), 使得 $(0, 2), (1, 3) \in \mathcal{T}$, 并且 $\mathcal{T}$ 包含尽可能少的开集.

</div>

<div class="pbox">

$$
\begin{gathered}
\{ \varnothing,{\mathbb R},(0,2),(1,3),(1,2),(0,3) \} 
\end{gathered}
$$

</div>

### T3

<div class="cbox">

**9. (MR)** 确定下列哪些子集是直线 $\mathbb{R}$ 的下极限拓扑 $\mathbb{R}_l$ 的开集, 并证明之:

$$
\begin{gathered}
A = [1,2), \\ B = \{3\}, \\ C = [4,5], \\ D = (6,7), \\ E = (8,9].
\end{gathered}
$$

</div>

<div class="pbox">


$A$显然是.

设$U$是 ${\mathbb R}_l$的开集,则$U=\bigcup_i [a_i,b_i)$,设$B=\sup b_i$,则一定有$B\notin U,B=\sup U$.故排除$B,C,E$.

$D$是:$D=\bigcup_{n\in Z} [6+\dfrac1n,7)$

</div>

### T4

<div class="cbox">

**10. (ER)** 设 $X$ 是拓扑空间, $U \subset X$ 是开集, $F \subset X$ 是闭集. 证明 $U - F$ 是开集, $F - U$ 是闭集.

</div>

<div class="pbox">

$U-F=U\cap (X-F)$是两个开集的交,是开集.

$F-U=F\cap (X-U)$是两个闭集的交,是闭集.

</div>

### T5

<div class="cbox">

**14. (ER)** 设 $\mathbb{Q} = \{q \in \mathbb{R} \mid q \text{ 为有理数}\}$. 证明 $\{(a, b) \mid a, b \in \mathbb{Q}, a < b\}$ 是通常直线拓扑的一个基.

</div>

<div class="pbox">

显然 $\forall x,x\in (\lfloor x-1 \rfloor ,\lfloor x+1 \rfloor )$.

又有

$$
\begin{gathered}
\forall U \text{ is open },U\subset R,x\in U \\
\exists x\in(l,r)\subset U \\ 
\end{gathered}
$$

则令$a$为$(l,x)$中的某有理数,$b$为$(x,r)$中的某有理数,有$x\in (a,b)\subset (l,r)$

于是它与开区间基生成相同的拓扑.

</div>

### T6

<div class="cbox">

**15. (DRH)** 设 $A \subset \mathbb{R}$. 若 $A$ 含有每一个形如 $\{a, a+b, \cdots, a+(n-1)b\}$ 的子集, 其中 $b \neq 0$, 则称 $A$ 包含一个长度为 $n$ 的算术级数. 考虑正整数集 $\mathbb{N}_+$ 的一个子集 $F$ 的如下性质: $\exists n \in \mathbb{N}_+$, 使得 $F$ 不包含长度为 $n$ 的算术级数. 证明: 存在 $\mathbb{N}_+$ 上的一个拓扑, 使得有上面性质的 $\mathbb{N}_+$ 的子集和 $\mathbb{N}_+$ 本身能构成这个拓扑的一个闭子集族.

**注** 在求解上面问题的过程中, 可能需要用到组合数学的**范德瓦尔登 (van der Waerden) 定理**: $\forall n \in \mathbb{N}_+$, 存在 $N \in \mathbb{N}_+$, 使得对于 $\{1,2,\cdots,N\}$ 的每一个子集 $A$, $A$ 与 $\{1,2,\cdots,N\} \setminus A$ 这两个集合中至少有一个含有长度为 $n$ 的算术级数.

</div>

<div class="pbox">

考虑直接定义满足性质的集合的补集是开集,或者说直接定义满足性质的集合是闭集.则只需要验证闭集的三条公里:

显然空集和全集成立.

对无限交,若$F_1$存在$n$使得$F_1$不含长度为$n$的算数级数,则任意$\bigcap F_i\subset F_1$也不含长度为$n$的算术级数,仍未闭集.

对有限并,考虑反证,如果$F_1\cup F_2$含有任意长度的算术级数,则任意选定$n$,一定存在$N$满足题述定理.而$F_1\cup F_2$中可以找到$\{c_n=a+bn\}$长度不小于$N$,那么设$c_n$中$F_i$元素的下标的集合是$S_i$,则$S_1,\{1\ldots N\}-S_1$中至少有一个有长$n$的算术级数,也就是说$S_1,S_2$中至少有一个包含长$n$的算数级数,设为$\{p_n\}$,则$c_{p_n}$一定是$F_1$或$F_2$中的算数级数,与$F_1,F_2$是闭集矛盾.故$F_1\cup F_2$不含任意长的算数级数.

于是得证.

</div>

### T7

<div class="cbox">

证明$f$是单射时等号成立:

**(1)** $f(\bigcap_{\lambda} A_{\lambda}) \subset \bigcap_{\lambda} f(A_{\lambda})$
If $f$ is injective, then "$=$" holds.

**(2)** $f(f^{-1}(B)) \subset B$
If $f$ is surjective, then "$=$" holds.

**(3)** $f^{-1}(f(A)) \supset A$
If $f$ is injective, then "$=$" holds.

</div>

<div class="pbox">

(1):

$$
\begin{gathered}
\forall x\in f(\bigcap_\lambda A_\lambda),\forall A_\lambda,\exists a\in A_\lambda \ s.t.\ 
f(a)=x,x\in f(A_\lambda) \\
\Rightarrow f(\bigcap_\lambda A_\lambda)\subset \bigcap_\lambda f(A_\lambda) \\
\text{if } f \text{ is injective:} \\
\forall x\in \bigcap_\lambda f(A_\lambda) \\
\exists! a \ s.t.\ 
f(a)=x \\
\Rightarrow\forall \lambda, a\in A_\lambda \\
\Rightarrow x\in f(\bigcap_\lambda A_\lambda) \\
\end{gathered}
$$
相互包含所以取等.

(2):

$$
\begin{gathered}
\forall b \in f(f^{-1}(B)), \\
\exists x\in f^{-1}(B) \ s.t.\ f(x)=b \\
\therefore b \in B \\
\text{if } f \text{ is surjective:} \\
\forall b\in B \\
\exists x\in f^{-1}(b)\subset f^{-1}(B),f(x)=b \\
\Rightarrow b\in f(f^{-1}(B))
\end{gathered}
$$

相互包含所以取等.

(3):

$$
\begin{gathered}
\forall a\in A ,a\in f^{-1}(f(a)) \\
\text{if } f \text{ is injective:} \\
\forall a \in f^{-1}(f(A)) \\
\exists b\in A,f(b)=f(a) \\
\xRightarrow{\text{ f is injection }} b=a,a\in A
\end{gathered}
$$

相互包含所以取等
</div>