---
title: Math Analysis Homework - Sem 2 Week 5
tags:
  - math-analysis
  - math
  - homework
date: 2026-04-02 17:48:22
---

# Math Analysis Homework - Sem 2 Week 5
### T1

<div class="cbox">

**2.** 设 $E \subset \mathbb{R}^2, P_0$ 为 $E$ 的聚点, 证明存在 $\mathbb{R}^2$ 中的点列 $\{P_n\} \subset E$ ($P_n \neq P_0, n \in \mathbb{N}$), 使得 $\lim_{n \to \infty} P_n = P_0$.

</div>

<div class='pbox'>

$P_0$是$E$的聚点,即对$P_0$的任意开球邻域$U=B(P_0,r)$,$E\cap U\ne \varnothing$.

则取$P_1\in B(P_0,1)\cap E$,取$P_n\in B(P_0,\dfrac12 \|P_{n-1},P_0\|)\cap E$,则 $\|P_{n-1}-P_0\|\to 0,P_{n-1}\to P_0$.

</div>

### T2

<div class="cbox">

**3.** 对于下列 $\mathbb{R}^2$ 中的点集 $E$, 求 $E$ 的内核 $E^o$, 边界集 $\partial E$, 导集 $E'$, 并判断哪些是开集、闭集、有界集、开区域和闭区域.
- (1) $E = \{(x, y) \mid 0 < x^2 + y^2 < 1\}$;
- (3) $E = \{(x, y) \mid x^2 + y^2 \leqslant 1\} \cup \{(x, y) \mid y = 0, 1 \leqslant x \leqslant 2\}$;
- (5) $E = \{(x, y) \mid (x^2 + y^2)(y^2 - x^2 + 1) \leqslant 0\}$;
- (7) $E = \left\{(x, y) \mid x = \frac{1}{n}, y = \frac{1}{m}; m, n \in \mathbb{N}\right\}$;

</div>

<div class='pbox'>

(1):

$$
\begin{gathered}
\operatorname{Int}E=E \\
\partial E=\{ (x,y)|x^2+y^2\in \{ 0,1 \} \} \\
E'=\{ (x,y)|x^2+y^2\in [0,1] \} 
\end{gathered}
$$

是开集,有界集,开区域,不是闭集,闭区域

(2):

$$
\begin{gathered}
\operatorname{Int}E=\{ (x,y)|x^2+y^2<1 \}  \\
\partial E=\{ (x,y)|x^2+y^2=1\lor (y=0\land x\in (1,2]) \}  \\
E'=E
\end{gathered}
$$

是闭集,有界集,不是闭集,不是开区域或闭区域(按照闭区域是开区域闭包的定义)

(3):

$$
\begin{gathered}
E=\{ (x,y)|y^2-x^2+1\le 0 \} \cup \{ (0,0) \}  \\
\operatorname{Int}E=\{ (x,y)|y^2-x^2+1<0 \}  \\
\partial E={ (x,y)|y^2-x^2+1=0 } \cup \{ (0,0) \} \\
E'=E
\end{gathered}
$$

是闭集,不是开集,有界集,闭区域或开区域

(4):

$$
\begin{gathered}
\operatorname{Int}E=\varnothing \\
\partial E=E \\
E'=\{ (0,0) \} 
\end{gathered}
$$

是闭集,不是开集,是有界集,不是开区域或闭区域

</div>

### T3

<div class="cbox">

**4.** 

(1) 设 $E_1, E_2$ 均为闭集, 证明 $E_1 \cup E_2$ 也是闭集. 若 $E_k (k \in \mathbb{N})$ 均为闭集, $\bigcup_{k=1}^\infty E_k$ 是否必为闭集?

(2) 设 $E_1, E_2$ 均为开集, 证明 $E_1 \cap E_2$ 也是开集. 若 $E_k (k \in \mathbb{N})$ 均为开集, $\bigcap_{k=1}^\infty E_k$ 是否必为开集?

</div>

<div class='pbox'>

(1):

$$
\begin{gathered}
\forall x\in (E_1\cup E_2)',\exists \{ x_n \} ,x_n\in E_1\cup E_2,\lim_{n \to \infty} x_n=x, \\
\text{we have } x_n\in E_1\lor x_n\in E_2,  \\
\text{let } y_0=0,y_n=\argmin_{k>y_{n-1}} \{ x_k\in E_1 \}  \\
\text{ so } x_{y_n}\in E_1,\lim_{n \to \infty} x_n=\lim_{n \to \infty} x_{y_n}\in E_1'\subset E_1\subset E_1\cup E_2 \\
\text{so } (E_1\cup E_2)'\subset (E_1\cup E_2),(E_1\cup E_2)\text{ is closed} 
\end{gathered}
$$

否,$\cup [\dfrac1n,1]=(0,1]$不是闭集.

(2):

$$
\begin{gathered}
x\in (E_1\cap E_2) \Rightarrow x\in E_1,x\in E_2 \\
\Rightarrow \exists x\in B(x,r_1)\subset E_1,x\in B(x,r_2)\subset E_2 \\
\Rightarrow x\in B(x,\min (r_1,r_2))\subset (E_1\cap E_2) \\
\Rightarrow E_1\cap E_2 \text{ is open} 
\end{gathered}
$$

</div>

### T4

<div class="cbox">

**5.** 设 $E \subset \mathbb{R}^2$, 证明 $E$ 的内核 $E^o$ 必为开集, $E$ 的导集 $E'$ 必为闭集.

</div>

<div class='pbox'>

(1):

$$
\begin{gathered}
\forall x\in \operatorname{Int}E \\
\exists r>0 \ s.t.\  x\in B(x,r)\subset E \\
\text{then } \forall y\in B(x,\dfrac r3),y\in B(y,\dfrac r3)\subset B(x,r)\subset \operatorname{Int}E \\
\text{so } x\in B(x,\dfrac r3)\subset E,\operatorname{Int}E \text{ is open} 
\end{gathered}
$$

(2):

$$
\begin{gathered}
\forall x\in E'',\exists \{ x_n \},x_n\in E' ,\lim_{n \to \infty} x_n=x \\
\exists \{ y_{n,m} \},y_{n,m}\in E ,\lim_{n \to \infty} y_{n,m}=x_m  \\
\text{construct } z_n=y_{k,n}, \text{where } \forall i>k-1,|y_{n,m}-x_m| <\dfrac1{2^n} \\
\text{then } z_n\in E,\lim_{n \to \infty} z_n=\lim_{n \to \infty} x_n=x\in E' \\
\Rightarrow E''\subset  E',E' \text{ is open} 
\end{gathered}
$$

</div>