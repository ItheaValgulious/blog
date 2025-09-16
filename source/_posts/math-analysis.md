---
title: Math Analysis
tags:
  - math-analysis
  - note
date: 2025-09-15 07:55:19
---

# Math analysis

## Class 1 Some Inequality and Def of limit

### Triangle Inequality

<div class='cbox'>

$$
a,b\in R  \Rightarrow {\left \vert {\left \vert a \right \vert} -{\left \vert b \right \vert}   \right \vert}  \le  {\left \vert a+b \right \vert} \leq {\left \vert a \right \vert} + {\left \vert b \right \vert}
$$

</div>

<div class='pbox'>

$$
\begin{array}{c}
    -{\left \vert a \right \vert} {\left \vert b \right \vert} \le ab\le {\left \vert a \right \vert} {\left \vert b \right \vert}
 \Rightarrow  \\
{\left \vert a \right \vert} ^2-2 {\left \vert a \right \vert} {\left \vert b \right \vert}  + {\left \vert a+b \right \vert} ^2
\le a^2+2ab+b^2 
\le {\left \vert a \right \vert} ^2+2 {\left \vert a \right \vert} {\left \vert b \right \vert}  + {\left \vert a+b \right \vert} ^2 \Rightarrow  \\
({\left \vert a \right \vert} -{\left \vert b \right \vert} )^2\le (a+b)^2\le ({\left \vert a \right \vert} +{\left \vert b \right \vert} )^2
\end{array}
$$


</div>

向量的模长也满足 也可以用这个做法.

### Cauchy-Schwarz Inequality

<div class='cbox'>

$$
\begin{array}{c}
0<x_i \in R  \Rightarrow 
\dfrac{\sum_i x_i}{n} \ge \sqrt[n]{\prod_i x_i} \ge \dfrac{n}{\sum_i \dfrac{1}{x_i} }  
\end{array}
$$


</div>

<div class='pbox'>

显然 取$x_i=\dfrac{1}{x_i}$能用左边不等式推右边 只证左边

归纳,$2$的幂次显然吧

对非$2$的幂次$n$,用$X=\sqrt[n]{\prod_i x_i}$补完,直接套

</div>

### Array's Limit

<div class='cbox'>

$$
\begin{array}{c}
lim_{n\to \infty} a_n = A  \Leftrightarrow  \\
\forall \epsilon >0 \exists N \ s.t.\ 
n\ge N  \Rightarrow \left \vert a_n-A \right \vert < \epsilon
\end{array}
$$

</div>

注意
- $N=N(\epsilon)$
- $N$ 不唯一
- $\epsilon$ 可限制在任意$(0,a),a>0$

#### Eg 1

<div class='cbox'>

$\lim_n n^{\frac{1}{n} }=1$


</div>

<div class='pbox'>

$$
\begin{array}{c}
\vert n^{\frac{1}{n} }-1 \vert  \\
= \vert (\sqrt n \sqrt n)^{\frac{1}{n} } -1 \vert \\
={\left \vert (\prod_i 1 \cdot \sqrt n\sqrt n)^{\frac{1}{n} } -1 \right \vert}  \\
\le {\left \vert \dfrac{n-2+2\sqrt n}{n}  -1 \right \vert}  \\
\le \dfrac{2}{\sqrt n} 
\end{array}
$$

Or try this:

$$
\begin{array}{c}
{\left \vert n^{\frac{1}{n} }-1 \right \vert} =n^{\frac{1}{n} }-1<\epsilon \\
\Leftarrow  n^{\frac{1}{n}}<(\epsilon+1) \\
\Leftarrow  n<(1+\epsilon)^n \\
\Leftarrow n<1+\epsilon n+\frac{\epsilon^2n(n-1)}{2} 
\end{array}
$$

Solve the equation, it's a parabola with upward opening so the solution exists.

</div>

[think] At this stage, we cannot say $\lim g(f(n))=g(\lim f(n))$ which depends on continuity of function. But you sometimes can rewrite the proof with inequality.

## Class 2

### About $Q$

<div class='cbox'>

$$
\begin{array}{c}
\sqrt n \in Z \cup Q^C
\end{array}
$$

</div>

<div class='pbox'>

$p^2=q^2n$ Integer factorization

More natural than textbook but it doesn't depend on Integer factorization.

</div>

<div class='cbox'>

$\dfrac{p}{q}$ is finite decimal or repeating decimal

</div>

<div class='pbox'>

Simulate how the division is done and consider the remainder will be repeated.

</div>

### About Cardinality

#### A Example

<div class='cbox'>

Find a bijection of $[0,1]$ and $(0,1)$

</div>

<div class='pbox'>


$$
\begin{array}{c}
f(x):(0,1) \to [0,1]=\begin{cases}
0,x=\dfrac{1}{2} \\
1,x=\dfrac{1}{3} \\
\dfrac{1}{n-2} , x=\dfrac{1}{n} \\
x, \text{otherwise}
\end{cases}

\end{array}
$$

</div>

Wow!

#### Cardinality is comparable

<div class='cbox'>

$$
\begin{array}{c}
\forall A,B, {\ } \exists f(x):A\to B \\ s.t.\\ 
\text{f is injective or surjective}
\end{array}
$$

(承认选择公理)

</div>

<div class='pbox'>

首先选择公理出良序定理,找到$A,B$的良序$(A,<),(B,<)$.

然后进行超限归纳,把$A$,$B$按照良序(保证了每个元素存在序里的后继),最小元素匹配,然后剩下的次小元素匹配,这么做下去.

然后这个看起来进行的是普通的自然数归纳显然是错的. 你需要用超限归纳也就是在序上做归纳.

然后问题来到序是什么.

序的结构是这样的 首先是自然数 自然数定义是$0$定义为空集开始 然后定义$\mathrm{succ}(S)=S \cup \{S\}$

然后定义完所有自然数后 定义$\omega=\bigcup_i i$,就是把所有的自然数的集合并起来(显然它包含所有的自然数). 然后我们可以接下来用后继的定于去定义$\omega+1,\omega+2\ldots$,并且你又可以把它们并起来得到$\omega\times 2$,不断走后继,$\omega,2\omega,3\omega\ldots$可以变成$\omega^2$,又有$\omega^3\ldots \omega^\omega$等等

基本上是每个层次的运算完了之后进下一个层次的序数构造 总之它看起来包含了各种各样的无穷,可以应付所有大小的集合.

然后我们要在序数的结构上做归纳法,就要证明:$x\to \mathrm{succ}(x)$,还要证明极限这一把也对,就是$a_1\ldots a_n \to \cup_i a_i$这个操作(也就是对某个极限序数,如果所有它以前的序数推到它自己)合法,就满足了你可以不断到下一极限.这样推出对全体元素合法. 这就是超限归纳法.

那你对照一下我们的归纳就是一一对应啊,所以是合法的. 就结束了.

然后我们刚才是说明了可以借良序去给两个集合配对,那么你就一定能找到一个对另一个的单射,所以一定可比.

</div>

#### Cantor-Bernstein-Schröder Theorem

<div class='cbox'>

$\mathrm{Card}(A)\le \mathrm{Card}(B),\mathrm{Card}(B)\le \mathrm{Card}(A) \Rightarrow \mathrm{Card}(A)=\mathrm{Card}(B)$

或者表达为

$$
\begin{array}{c}
\left. \begin{array}{ll}
\forall A,B,g:A\to B,f:B\to A\\
f,g \text{ is injective} 
\end{array} \right\}
 \Rightarrow \exists h:A \leftrightarrow B \text{ is bijective} 
\end{array}
$$

</div>

<div class='pbox'>

考虑从任意元素$u\in A$可以引出一条链:$u\to f(u)\to g(f(u)\to f(g(f(u)))\to \ldots$.
同理$v \in B$开始的链$v\to g(v)\to f(g(v))\to g(f(g(v)))\to \ldots$.

注意到所有元素一定都在某条链上(映射).每个点度数一定至多一进一出(单射).

于是每条链上构造一个双射(显然的)拼起来即可.

$\text{Q.E.D}$ 

</div>


