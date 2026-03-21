---
title: Topo Homework - Week 3
tags:
  - topo
  - homework
  - math
date: 2026-03-21 13:22:42
---

# Topo Homework - Week 3

### T1

<div class="cbox">

T1. (ER) 确定下面每种情况中的 $\text{Int}(A), \text{Cl}(A)$ 和 $\partial A$:
- (1) 在下极限拓扑空间 $\mathbb{R}_l$ 中, $A = [0, 1]$;
- (2) $X = \{a, b, c\}, \mathcal{T} = \{X, \emptyset, \{a\}, \{a, b\}\}, A = \{a, c\}$;
- (3) 在欧氏直线 $\mathbb{R}$ 上, $A = (-1, 1) \cup \{2\}$;
- (4) 在下极限拓扑空间 $\mathbb{R}_l$ 中, $A = (-1, 1) \cup \{2\}$;
- (5) 在欧氏平面 $\mathbb{R}^2$ 上, $A = \{(\sin \theta, \cos \theta) \in \mathbb{R}^2 \mid 0 < \theta < \pi\}$.

</div>

<div class="pbox">

(1):  $\operatorname{Int}A=[0,1),\operatorname{Cl}A=[0,1],\partial A=\{ 1 \}$

(2):  $\operatorname{Int}A=\{ a \} ,\operatorname{Cl}A=X,\partial A=\{ b,c \}$

(3):  $\operatorname{Int}A=(-1,1),\operatorname{Cl}A=[-1,1]\cup \{ 2 \} ,\partial A=\{ -1,1,2 \}$ 

(4):  $\operatorname{Int}=(-1,1),\operatorname{Cl}A=[-1,1)\cup \{ 2 \} ,\partial A=\{ -1,2 \}$

(5):  $\operatorname{Int}A=\varnothing,\operatorname{Cl}A=A\cup \{ (0,1),(0,-1) \},\partial A=A\cup \{ (0,1),(0,-1) \}$


</div>

### T2

<div class="cbox">

T5. (MRH) 在 $\mathbb{R}$ 上采用标准拓扑. 是否存在集合 $A \subset \mathbb{R}$, 分别使得

(1) $A, \text{Cl}(A), \text{Int}(A)$ 和 $\text{Cl}(\text{Int}(A))$ 两两不同?

(2) $A, \text{Cl}(A), \text{Int}(A)$ 和 $\text{Int}(\text{Cl}(A))$ 两两不同?

(3) $A, \text{Cl}(A), \text{Int}(A), \text{Int}(\text{Cl}(A))$ 和 $\text{Cl}(\text{Int}(A))$ 两两不同?

</div>

<div class="pbox">

(1):取$A=Q\cup (0,1)$,则 $A=Q\cup (0,1),\operatorname{Cl}A=R,\operatorname{Int}A=(0,1),\operatorname{Cl}\operatorname{Int}A=[0,1]$

(2):取 $A=Q\cap (0,1)$,则 $\operatorname{Cl}A=[0,1],\operatorname{Int}A=\varnothing,\operatorname{Int}\operatorname{Cl}A=(0,1)$

(3):取$A=((Q\cup (0,1))\cap (-1,2)) \cup (Q\cap (3,4))$,则

$$
\begin{gathered}
\operatorname{Int}A=(0,1) \\
\operatorname{Cl}A=[-1,2]\cup [3,4] \\
\operatorname{Int}\operatorname{Cl}A=(-1,2)\cup (3,4) \\
\operatorname{Cl} \operatorname{Int}A=[0,1]
\end{gathered}
$$

</div>

### T3

<div class="cbox">

T12. (MR) 设 $A$ 和 $B$ 都是拓扑空间 $X$ 上的稠密子集, 且 $A$ 是开集. 证明 $A \cap B$ 也是稠密子集.

</div>

<div class="pbox">

$$
\begin{gathered}
A,B \text{ is dense}  \\
\Rightarrow \forall x\in U_x\subset X, \\
\exists a\in U_a\subset A\cap U_x, \\
\exists b\in U_a\cap B \\
b\in U_a\subset A \Rightarrow b\in A\cap B \\
b\in U_x \Rightarrow A\cap B \text{ is dense}
\end{gathered}
$$

</div>

### T4

<div class="cbox">

T20. (ERH) 设 $X$ 为一个拓扑空间, $A \subset X$. 证明:
- (1) $\partial A$ 是闭集;
- (2) $\partial A \cap \text{Int}(A) = \emptyset$;
- (3) $\partial A \cup \text{Int}(A) = \text{Cl}(A)$;
- (4) $\partial A \subset A$ 当且仅当 $A$ 是闭集;
- (5) $\partial A \cap A = \emptyset$ 当且仅当 $A$ 是开集;
- (6) $\partial A = \emptyset$ 当且仅当 $A$ 既是开集又是闭集.

</div>

<div class="pbox">

(1): 

$$
\begin{gathered}
\partial A=\operatorname{Cl}A\cap (X-\operatorname{Int}A) \\
\operatorname{Cl}A \text{ is close} \\
X-\operatorname{Int}A \text{ is close}  \\
\Rightarrow \partial A \text{ is close}
\end{gathered}
$$

(2):

$$
\begin{gathered}
\partial A=(\operatorname{Cl}A-\operatorname{Int}A)\cap \operatorname{Int}A=\varnothing
\end{gathered}
$$

(3):

$$
\begin{gathered}
\partial A\cup \operatorname{Int}A=(\operatorname{Cl}A-\operatorname{Int}A)\cup \operatorname{Int}A=\operatorname{Cl}A
\end{gathered}
$$

(4):

$$
\begin{gathered}
\operatorname{Int}A\subset A \\
\Rightarrow 
\operatorname{Cl}A-\operatorname{Int}A\subset A \Leftrightarrow \operatorname{Cl}A\subset A \Leftrightarrow A \text{ is close} 
\end{gathered}
$$

(5):

$$
\begin{gathered}
\partial A\cap A=\operatorname{Cl}A\cap (X-\operatorname{Int}A)\cap A \\
=A-A\cap \operatorname{Int}A \\
\Rightarrow \partial A\cap A=\varnothing \Leftrightarrow A\cap \operatorname{Int}A=A \Leftrightarrow A \text{ is open} 
\end{gathered}
$$

(6):

By (4),(5):

$$
\begin{gathered}
A \text{ is open and close}  \\
\Leftrightarrow \partial A\subset A \land \partial A\cap A=\varnothing \\
\Leftrightarrow \partial A = \varnothing
\end{gathered}
$$

</div>

### T5

<div class="cbox">

T2. (ER) 设 $f: X \to Y$. 证明下列陈述等价:
- (4) 对 $X$ 的任意子集 $A \subset X$, $f(\text{Cl}(A)) \subset \text{Cl}(f(A))$;
- (5) 对 $Y$ 的任意子集 $B \subset Y$, $\text{Cl}(f^{-1}(B)) \subset f^{-1}(\text{Cl}(B))$.

</div>

<div class="pbox">

$$
\begin{gathered}
(4) \Rightarrow (5): \\
\text{let } A=f^{-1}(B) \\
\Rightarrow f(\operatorname{Cl} f^{-1} (B))\subset \operatorname{Cl}f(f^{-1}(B))\subset \operatorname{Cl}B \\
\Rightarrow \operatorname{Cl}f^{-1}(B) \subset f^{-1}(f(\operatorname{Cl}f^{-1} (B)))\subset f^{-1}(\operatorname{Cl}B) \\
(5) \Rightarrow (4): \\
\text{let } B=f(A) \\
\Rightarrow \operatorname{Cl}A\subset \operatorname{Cl}f^{-1}(f(A))\subset f^{-1}(\operatorname{Cl}f(A)) \\
\Rightarrow f(\operatorname{Cl}A)\subset f(f^{-1}(\operatorname{Cl}f(A)))\subset \operatorname{Cl}f(A)
\end{gathered}
$$

</div>

### T6

<div class='cbox'>

$$
\begin{gathered}
X,Y \text{are topo spaces} ,A\subset X,B\subset Y \\
\Rightarrow \operatorname{Int}(A\times B)=\operatorname{Int}A\times \operatorname{Int}B
\end{gathered}
$$

</div>

<div class='pbox'>

设$X,Y$的拓扑基分别是$C,D$,则让

$$
\begin{gathered}
\operatorname{Int}A=\bigcup_{i\in S} C_i,\operatorname{Int} B=\bigcup_{i\in T} D_i
\end{gathered}
$$

左边由定义是被$A\times B$包含的开集的并,等价于被$A\times B$包含的拓扑基的并,而某个拓扑基有: 

$$
\begin{gathered}
C_i\times D_j\subset A\times B  \\
\Leftrightarrow C_i\subset A\land D_j\subset D  \\
\Leftrightarrow C_i\subset \operatorname{Int}A\land D_j\subset \operatorname{Int}B
\end{gathered}
$$

所以$A\times B$内的拓扑基恰好是所有$C_i\times D_j$.

而右侧是

$$
\begin{gathered}
\operatorname{Int}A\times \operatorname{Int}B \\
=\bigcup_{i\in S} C_i \times \bigcup_{i\in T} D_i \\
=\bigcup_{i\in S,j\in T} C_i\times D_j
\end{gathered}
$$

所以两侧相等.

</div>

### T7

<div class='cbox'>

$$
\begin{gathered}
\overline{A\cap B}\subset \overline{ A } \cap \overline{ B }  \\
\overline{ A\cup B } =\overline{ A } \cup \overline{ B } 
\end{gathered}
$$

</div>

<div class='pbox'>

(1):

$$
\begin{gathered}
\overline{ A\cap B } \subset \overline{ A } ,\overline{ A\cap B } \subset \overline{ B } \Rightarrow \overline{ A\cap B } \subset \overline{ A } \cap \overline{ B } 
\end{gathered}
$$

(2):

$$
\begin{gathered}
\overline{ A } \subset \overline{ A\cap B } ,\overline{ B } \subset \overline{ A\cap B }  \\
\Rightarrow \overline{ A } \cup \overline{ B } \subset \overline{ A\cup B } 
\end{gathered}
$$

对另一侧, $\forall x\in \overline{ A\cup B }$,假设$X$不在$A$和$B$的闭包中,那么$\exists x\in U_1,x\in U_2,U_1,U_2 \text{ is open},U_1\cap A=U_2\cap B=\varnothing$,则$(U_1\cap U_2)\cap (A\cup B)=\varnothing$,推出 $x\notin \overline{ A\cup B }$,矛盾,得证.

</div>
