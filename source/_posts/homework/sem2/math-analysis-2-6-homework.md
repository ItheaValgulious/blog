---
title: Math Analysis Homework - Sem 2 Week 6
tags:
  - math
  - math-analysis
  - homework
date: 2026-04-16 10:52:13
---


# Math Analysis Homework - Sem 2 Week 6

### T1

<div class="cbox">

**2.** (2) $\lim_{(x,y)\to(0,0)} \frac{x^2+y^2}{\sqrt{x^2+y^2+1}-1}$

</div>

<div class='pbox'>

存在

令$t=x^2+y^2$,显然$(x,y)\to (0,0)$时$t\to 0$,则原式极限为:

$$
\lim_{t \to 0} \dfrac{t}{\sqrt{t+1}-1}=2 
$$


</div>

### T2

<div class="cbox">

**2.** (4) $\lim_{(x,y)\to(0,0)} xy \frac{x^2-y^2}{x^2+y^2}$

</div>

<div class='pbox'>

$$
\begin{gathered}
0\le \lim_{(x,y) \to (0,0)} |xy \frac{x^2-y^2}{x^2+y^2}| \\
\le \lim_{(x,y) \to (0,0)} |xy| |\dfrac{x^2-y^2}{x^2+y^2} | \\
\le \lim_{(x,y) \to (0,0)} |xy| \\
=0
\end{gathered}
$$

由夹逼定理,原式极限为$0$.

</div>

### T3

<div class="cbox">

**2.** (6) $\lim_{\substack{x \to \infty \\ y \to \infty}} \frac{x+y}{x^2-xy+y^2}$

</div>

<div class='pbox'>

$$
\begin{gathered}
\lim_{\substack{x \to \infty \\ y \to \infty}} \frac{x+y}{x^2-xy+y^2} \\
\le \lim_{\substack{x \to \infty \\ y \to \infty}} \dfrac{|x+y|}{|xy|}  \\
=\lim_{\substack{x \to \infty \\ y \to \infty}} |\dfrac{1}{x}| +|\dfrac{1}{y}|  \\
=0
\end{gathered}
$$

</div>

### T4

<div class="cbox">

判断$(0,0)$处极限存在性:

**3.** (1) $f(x,y) = \frac{3x-2y}{2x-3y} \quad \left(y \neq \frac{2x}{3}\right)$

</div>

<div class='pbox'>

$$
\begin{gathered}
f(x,y)=\dfrac 23+\dfrac{5}{3} \dfrac{x}{2x-3y} \\
\text{let } y=kx \\
\Rightarrow \lim_{(x,y) \to (0,0)} f(x,y) \\
=\dfrac{2}{3} +\lim_{(x,y) \to (0,0)} \dfrac{5}{3} \dfrac{x}{(2-3k)x}  \\
=\dfrac{2}{3} +\dfrac{5}{3} \dfrac{1}{2-3k} 
\end{gathered}
$$

与$k$相关,不存在.

</div>

### T5

<div class="cbox">

判断$(0,0)$处极限存在性:

**3.** (3) $f(x,y) = \frac{x^2y}{x^4+y^2}$

</div>

<div class='pbox'>

$y=x^2$时,极限为

$$
\begin{gathered}
\lim_{x \to 0} \dfrac{x^4}{2x^4} =\dfrac{1}{2} 
\end{gathered}
$$

$y=x$时,极限为

$$
\begin{gathered}
\lim_{x \to 0} \dfrac{x^3}{x^4+x^2} =0\ne \dfrac{1}{2} 
\end{gathered}
$$

不存在.

</div>

### T6

<div class="cbox">

计算函数的两个累次极限

**4.** (1) $f(x,y) = \frac{x^2-y^2+x^3+y^3}{x^2+y^2} \quad (x \to 0, y \to 0)$

</div>

<div class='pbox'>

$$
\begin{gathered}
\lim_{x \to 0} \lim_{y \to 0} f(x,y) \\
=\lim_{x \to 0} \dfrac{x^2+x^3}{x^2}  \\
=1 \\
\lim_{y\to 0} \lim_{x \to 0} f(x,y) \\
=\lim_{y \to 0} \dfrac{-y^2+y^3}{y^2}  \\
=-1
\end{gathered}
$$

</div>

### T7

<div class="cbox">

计算函数的两个累次极限

**4.** (3) $f(x,y) = \frac{x^y}{1+x^y} \quad (x \to +\infty, y \to 0^+)$

</div>

<div class='pbox'>

$$
\begin{gathered}
\lim_{x \to +\infty} \lim_{y \to 0^+} f(x,y) \\
=\lim_{x \to +\infty} \dfrac{1}{2}  \\
=\dfrac{1}{2}  \\
\lim_{y \to 0^+} \lim_{x \to +\infty} f(x,y) \\
=\lim_{y \to 0^+} 1 \\
=1
\end{gathered}
$$

</div>

### T8

<div class="cbox">

**5.** 设二元函数 $f(x,y)$ 在 $D: [a,b] \times [c,d]$ 上定义. 若 $\forall P' \in D, \lim_{\substack{P \to P' \\ P \in D}} f(P)$ 都存在. 证明 $f$ 是 $D$ 上的有界函数.

</div>

<div class='pbox'>

反证,假设$f$无界,则存在点列$p_n$满足$f(p_n)>n$.

由于$D$是有界闭区域,有列紧性,知存在$k_n$使得 $p_{k_n}$收敛,设极限为$p_0$.

则

$$
\begin{gathered}
\lim_{n \to \infty} f(x_{k_n}) \\
=\lim_{p \to p_0} f(p) = A\text{ exists} 
\end{gathered}
$$

但 $\lim_{n \to \infty}  f(p_{k_n})=\lim_{n \to \infty} f(p_n)=+\infty$,矛盾.故$f$有界.

</div>

### T9

<div class="cbox">

讨论下列函数的连续性.

**1.** (1) $f(x,y) = \frac{1}{\sqrt{x^2+y^2}}$

</div>

<div class='pbox'>

$$
\begin{gathered}
\forall (x_0,y_0)\ne (0,0) \\
\lim_{(x,y) \to (x_0,y_0)} f(x,y)=\dfrac{1}{\sqrt{ x_0^2+y_0^2 } } =f(x_0,y_0)  \\
\Rightarrow f(x,y)\in C(R^2-\{ 0 \})
\end{gathered}
$$

</div>

### T10

<div class="cbox">

讨论下列函数的连续性.

**1.** (3) $f(x,y) = [x+y]$

</div>

<div class='pbox'>

$$
\begin{gathered}
\forall (x_0,y_0) \ s.t.\ 
x_0+y_0\notin Z \\
\forall \epsilon>0 \\
\text{let } m=\min(x_0+y_0-[x_0+y_0],[x_0+y_0+1]-x_0-y_0) \\
\forall (x,y)\in B((x_0,y_0),\dfrac m2) \\
x+y\in ([x_0+y_0],[x_0+y_0+1]) \\
\Rightarrow f(x,y)=[x_0+y_0] \\
\text{else if } x_0+y_0\in Z \\
\lim_{(x,y) \to (x_0,y_0),y=y_0+x_0-x} f(x,y)=f(x_0+y_0) \\
\lim_{(x,y) \to (x_0,y_0),y=y_0+x-x_0} f(x,y)=[2x-x_0+y_0]=[x_0+y_0]+1\ne f(x_0,y_0) \\
\end{gathered}
$$

$f(x,y)$在$x+y\notin Z$时连续,$x+y\in Z$时不连续.

</div>

### T11

<div class="cbox">

讨论下列函数的连续性.

**1.** (5) $f(x,y) = \begin{cases} \frac{\sin xy}{y}, & y \neq 0, \\ 0, & y = 0 \end{cases}$

</div>

<div class='pbox'>

$$
\begin{gathered}
\forall (x_0,y_0),y_0\ne 0: \\
\lim_{(x,y) \to (x_0,y_0)}f(x,y)= f(x_0,y_0) \\
\text{else if } y_0=0: \\
\lim_{(x,y) \to (x_0,0)} f(x,y)=\dfrac{\sin (xy)}{y} =x \\
\end{gathered}
$$

故$f(x,y)$在$R^2-\{(x,y)|x\ne 0,y=0\}$连续,在$\{(x,y)|x\ne 0,y= 0\}$不连续

</div>

### T12

<div class="cbox">

**3.** 设常数 $p > 0$, 又
$$f(x,y) = \begin{cases} \frac{x}{(x^2+y^2)^p}, & x^2+y^2 \neq 0, \\ 0, & x^2+y^2 = 0 \end{cases}$$
讨论 $f(x,y)$ 在 $(0,0)$ 处的连续性.

</div>

<div class='pbox'>

从$x=0$这条直线趋近得极限为$0$.

$p> \dfrac12$时,从$x=y$逼近得极限为

$$
\begin{gathered}
\lim_{x \to 0} \dfrac{x}{2^p x^{2p}} =\dfrac1{2^p}x^{1-2p}=\infty
\end{gathered}
$$

极限甚至不存在.

$p=\dfrac12$时,从$x=y$逼近得极限为$\dfrac1{2^p}\ne 0$,极限也不存在.

$y<\dfrac12$时:

$$
\begin{gathered}
\lim_{(x,y) \to (0,0)} |f(x,y)|= \\
\lim_{r\to 0} |\dfrac{r\cos(\theta(r))}{r^{2p}}| = \\
\lim_{r\to 0} |\cos(\theta(r))r^{1-2p}| \le \\
\lim_{r\to 0}  |r^{1-2p}|=0

\end{gathered}
$$

故$p<\dfrac12$时连续,$p\ge \dfrac12$时不连续.

</div>

### T13

<div class="cbox">

**4.** (2) $\lim_{(x,y)\to(0,a)} \frac{\sin xy}{x} \quad (a \neq 0)$

</div>

<div class='pbox'>

$$
\begin{gathered}
\lim_{x \to 0} \dfrac{\sin x}{x} =1 \\
\Rightarrow \forall \epsilon>0,\exists \delta \in (0,\min(1,\epsilon)) \ s.t.\ 
x<\delta \Rightarrow \sin x\in (1-\epsilon x,1+\epsilon x) \\
\Rightarrow \forall x<\delta,|y-a|<\delta ,\sin(xy)\in ((1-\epsilon)xy,(1+\epsilon)xy) \\
\Rightarrow \dfrac{\sin xy}{x} \in ((1-\epsilon)(a-\delta),(1+\epsilon)(a+\delta))
\end{gathered}
$$

由夹逼原理,$(x,y)\to (0,a)$时$\epsilon,\delta\to 0$,$\lim_{(x,y)\to (0,a)} \dfrac{\sin xy}x=a$.

</div>

### T14

<div class="cbox">

**4.** (4) $\lim_{\substack{x \to +\infty \\ y \to a}} \left( \frac{x+y}{x} \right)^{\frac{x+y}{y}} \quad (a \neq 0)$

</div>

<div class='pbox'>

取$\ln$,只需求

$$
\begin{gathered}
\lim_{\substack{x \to +\infty \\ y \to a}} L(x,y)=\lim_{\substack{x \to +\infty \\ y \to a}}\dfrac{x+y}{y} \ln \dfrac{x+y}{x}  \\
\text{when } x>\dfrac1\delta_0,|y-a|<\delta_0 \\
\dfrac{x+y}{x} =1+\dfrac yx\in (1,1+\delta_0 (a+\delta_0)) \\
\dfrac{x+y}{y} >1+\dfrac{1}{\delta_0(a+\delta_0)}  \\
\text{Since } \lim_{x \to 1} \dfrac{\ln x}{x-1}=1, \\
\forall \epsilon>0,\exists \delta>0, \ s.t.\ 
\forall x<\delta,\ln x\in ((1-\epsilon)(x-1),(1+\epsilon)(x-1)) \\
\text{let } \delta_0<\min(\dfrac{\delta}{2a},\epsilon) ,\delta_0(a+\delta_0)<\delta \\
L(x,y)\in (\dfrac{x+y}{y} (1-\epsilon)\dfrac{y}{x} ,\dfrac{x+y}{y} (1+\epsilon)\dfrac{y}{x} ) \\
\Leftrightarrow L(x,y)\in ((1-\epsilon)(1+\dfrac{y}{x} ),(1+\epsilon)(1+\dfrac{y}{x})) \\
\Rightarrow L(x,y)\in ((1-\epsilon)(1+\delta_0(a-\delta_0)),(1+\epsilon)(1+\delta_0(a+\delta_0)))
\end{gathered}
$$

令$\epsilon\to 0,\delta_0\to 0$,则得$x\to +\infty,y\to a$时,$L(x,y)\to 1$,故原式极限为$e$.

</div>

### T15

<div class="cbox">

**5.** 
- (1) 设 $f(x,y) = \sqrt{x^2+y^2}$, 证明 $f(x,y)$ 在 $\mathbb{R}^2$ 上一致连续;
- (2) 设 $f(x,y) = \frac{1}{1-xy}$, 证明 $f(x,y)$ 在 $D: [0,1) \times [0,1)$ 上不一致连续.

</div>

<div class='pbox'>

(1):

$$
\begin{gathered}
|\sqrt{ x_1^2+y_1^2 } -\sqrt{x_2^2+y_2^2}| \\
=|\dfrac{x_1^2+y_1^2-x_2^2-y_2^2}{\sqrt{ x_1^2+y_1^2 } +\sqrt{x_2^2+y_2^2}}|  \\
=|(x_1-x_2)\dfrac{(x_1+x_2)}{\sqrt{ x_1^2+y_1^2 } +\sqrt{x_2^2+y_2^2}}| \\
+|(y_1-y_2)\dfrac{(y_1+y_2)}{\sqrt{ x_1^2+y_1^2 } +\sqrt{x_2^2+y_2^2}}| \\
\le |x_1-x_2|+|y_1-y_2| \\
\le 2\sqrt{(x_1-x_2)^2+(y_1-y_2)^2} \\
=2\delta \\
\text{so } \forall \epsilon>0,\text{let } \delta=\dfrac\epsilon 2 \\
\Rightarrow |(x_1,y_1)-(x_2,y_2)|<\delta \Rightarrow |f(x_1,y_1)-f(x_2,y_2)|<\epsilon
\end{gathered}
$$

(2):

若它一致连续,则其在$\{(x,y)\in D|x=y\}\subset D$一致连续,则$y=\dfrac 1{1-x^2}$一致连续.

但令$x_n=\sqrt{1-\dfrac1n},y_n=\sqrt{1-\dfrac1{n+1}}$,则

$$
\begin{gathered}
\lim_{n \to \infty} |x_n-y_n| \\
=\lim_{n \to \infty} \sqrt{1-\dfrac1n}-\sqrt{1-\dfrac1{n+1}} \\
=\lim_{n \to \infty} \dfrac{\dfrac1n-\dfrac1{n+1}}{\sqrt{1-\dfrac1n}+\sqrt{1-\dfrac1{n+1}}}  \\
=0
\end{gathered}
$$

但

$$
\begin{gathered}
\lim_{n \to \infty} |f(x_n)-f(y_n)| \\
=\lim_{n \to \infty} (n+1)-n=1
\end{gathered}
$$

与一致连续矛盾.故不一致连续.

</div>
