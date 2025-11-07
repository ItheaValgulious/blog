---
title: Math Analysis
tags:
  - math-analysis
  - note
  - math
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
\begin{gathered}
    -{\left \vert a \right \vert} {\left \vert b \right \vert} \le ab\le {\left \vert a \right \vert} {\left \vert b \right \vert}
 \Rightarrow  \\
{\left \vert a \right \vert} ^2-2 {\left \vert a \right \vert} {\left \vert b \right \vert}  + {\left \vert a+b \right \vert} ^2
\le a^2+2ab+b^2 
\le {\left \vert a \right \vert} ^2+2 {\left \vert a \right \vert} {\left \vert b \right \vert}  + {\left \vert a+b \right \vert} ^2 \Rightarrow  \\
({\left \vert a \right \vert} -{\left \vert b \right \vert} )^2\le (a+b)^2\le ({\left \vert a \right \vert} +{\left \vert b \right \vert} )^2
\end{gathered}
$$


</div>

向量的模长也满足 也可以用这个做法.

### Cauchy-Schwarz Inequality

<div class='cbox'>

$$
\begin{gathered}
0<x_i \in R  \Rightarrow 
\dfrac{\sum_i x_i}{n} \ge \sqrt[n]{\prod_i x_i} \ge \dfrac{n}{\sum_i \dfrac{1}{x_i} }  
\end{gathered}
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
\begin{gathered}
lim_{n\to \infty} a_n = A  \Leftrightarrow  \\
\forall \epsilon >0 \exists N \ s.t.\ 
n\ge N  \Rightarrow \left \vert a_n-A \right \vert < \epsilon
\end{gathered}
$$

</div>

注意
- $N=N(\epsilon)$
- $N$ 不唯一
- $\epsilon$ 可限制在任意$(0,a),a>0$

#### Eg 1

<div class='cbox'>

$\lim_{n \to \infty} n^{\frac{1}{n} }=1$


</div>

<div class='pbox'>

$$
\begin{gathered}
\vert n^{\frac{1}{n} }-1 \vert  \\
= \vert (\sqrt n \sqrt n)^{\frac{1}{n} } -1 \vert \\
={\left \vert (\prod_i 1 \cdot \sqrt n\sqrt n)^{\frac{1}{n} } -1 \right \vert}  \\
\le {\left \vert \dfrac{n-2+2\sqrt n}{n}  -1 \right \vert}  \\
\le \dfrac{2}{\sqrt n} 
\end{gathered}
$$

Or try this:

$$
\begin{gathered}
{\left \vert n^{\frac{1}{n} }-1 \right \vert} =n^{\frac{1}{n} }-1<\epsilon \\
\Leftarrow  n^{\frac{1}{n}}<(\epsilon+1) \\
\Leftarrow  n<(1+\epsilon)^n \\
\Leftarrow n<1+\epsilon n+\frac{\epsilon^2n(n-1)}{2} 
\end{gathered}
$$

Solve the equation, it's a parabola with upward opening so the solution exists.

</div>

[think] At this stage, we cannot say $\lim g(f(n))=g(\lim f(n))$ which depends on continuity of function. But you sometimes can rewrite the proof with inequality.

## Class 2

### About $Q$

<div class='cbox'>

$$
\begin{gathered}
\sqrt n \in Z \cup Q^C
\end{gathered}
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
\begin{gathered}
f(x):(0,1) \to [0,1]=\begin{cases}
0,x=\dfrac{1}{2} \\
1,x=\dfrac{1}{3} \\
\dfrac{1}{n-2} , x=\dfrac{1}{n} \\
x, \text{otherwise}
\end{cases}

\end{gathered}
$$

</div>

Wow!

#### Cardinality is comparable

<div class='cbox'>

$$
\begin{gathered}
\forall A,B, {\ } \exists f(x):A\to B \\ s.t.\\ 
\text{f is injective or surjective}
\end{gathered}
$$

(承认选择公理)

</div>

<div class='pbox'>

首先选择公理出良序定理,找到$A,B$的良序$(A,<),(B,<)$.

然后进行超限归纳,把$A$,$B$按照良序(保证了每个元素存在序里的后继),最小元素匹配,然后剩下的次小元素匹配,这么做下去.

然后这个看起来进行的是普通的自然数归纳显然是错的. 你需要用超限归纳也就是在序上做归纳.

然后问题来到序是什么.

序的结构是这样的 首先是自然数 自然数定义是$0$定义为空集开始 然后定义$\operatorname{succ}(S)=S \cup \{S\}$

然后定义完所有自然数后 定义$\omega=\bigcup_i i$,就是把所有的自然数的集合并起来(显然它包含所有的自然数). 然后我们可以接下来用后继的定于去定义$\omega+1,\omega+2\ldots$,并且你又可以把它们并起来得到$\omega\times 2$,不断走后继,$\omega,2\omega,3\omega\ldots$可以变成$\omega^2$,又有$\omega^3\ldots \omega^\omega$等等

基本上是每个层次的运算完了之后进下一个层次的序数构造 总之它看起来包含了各种各样的无穷,可以应付所有大小的集合.

然后我们要在序数的结构上做归纳法,就要证明:$x\to \operatorname{succ}(x)$,还要证明极限这一把也对,就是$a_1\ldots a_n \to \cup_i a_i$这个操作(也就是对某个极限序数,如果所有它以前的序数推到它自己)合法,就满足了你可以不断到下一极限.这样推出对全体元素合法. 这就是超限归纳法.

那你对照一下我们的归纳就是一一对应啊,所以是合法的. 就结束了.

然后我们刚才是说明了可以借良序去给两个集合配对,那么你就一定能找到一个对另一个的单射,所以一定可比.

</div>

#### Cantor-Bernstein-Schröder Theorem

<div class='cbox'>

$\operatorname{Card}(A)\le \operatorname{Card}(B),\operatorname{Card}(B)\le \operatorname{Card}(A) \Rightarrow \operatorname{Card}(A)=\operatorname{Card}(B)$

或者表达为

$$
\begin{gathered}
\begin{cases}
\forall A,B,g:A\to B,f:B\to A\\
f,g \text{ is injective} 
\end{cases}
 \Rightarrow \exists h:A \leftrightarrow B \text{ is bijective} 
\end{gathered}
$$

</div>

<div class='pbox'>

考虑从任意元素$u\in A$可以引出一条链:$u\to f(u)\to g(f(u)\to f(g(f(u)))\to \ldots$.
同理$v \in B$开始的链$v\to g(v)\to f(g(v))\to g(f(g(v)))\to \ldots$.

注意到所有元素一定都在某条链上(映射).每个点度数一定至多一进一出(单射).

于是每条链上构造一个双射(显然的)拼起来即可.

$\text{Q.E.D}$ 

</div>

其实这些应该算集合论还是什么?

## Class 3 Properties of Limit

- Uniqueness:Obviously
- Local boundedness: 取$\epsilon=1$得$N$,$N$后面显然,前面有限项也显然.
- About subsequence:
  - about any subsequence
  - about some subsequence whose union is the sequence

### Limitaion's Calculation

$$
\lim_{n \to \infty} a_n=A,\lim_{n \to \infty} b_n=B
$$

<div class='cbox'>

$$
\lim_{n \to \infty} a_nb_n=AB
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
{\left \vert a_nb_n-AB \right \vert} = \\
{\left \vert a_nb_n-a_nB+a_nB-AB \right \vert} \\ \\
\le {\left \vert a_N \right \vert} {\left \vert b_n-B \right \vert} +{\left \vert B \right \vert} {\left \vert a_n-A \right \vert} \\
\end{gathered}
$$

显然$a_n,b_n$有界,令$M$是他俩共同的界,取$\epsilon'=\dfrac{1}{114514M+114514}$用到$a_n,b_n$上即证.

</div>

<div class='cbox'>

$$
\lim_{n \to \infty} \frac{a_n}{b_n} =\frac{A}{B} 
$$

</div>

<div class='pbox'>

先上一个保号性干掉分母上出现$0$的事.

证取倒数:
$$
\begin{gathered}
{\left \vert \frac{1}{b_n}-\frac{1}{B}  \right \vert}<\epsilon \\
\Leftarrow {\left \vert B-b_n \right \vert} <\epsilon b_nB \\
\Leftarrow \epsilon'=\frac{\epsilon}{BM+114514} (\vert M\vert>b_n)
\end{gathered}
\\
\text{Q.E.D}
$$

那转化到乘法是显然的.

</div>

### 无穷小

基本就是收敛到$0$的数列啊.

### Eg

<div class='cbox'>

$$
\begin{cases}
\lim_{n \to \infty} a_n=a \\
\lim_{n \to \infty} b_n=b
\end{cases} \\
\Rightarrow \lim_{n \to \infty} \frac{\sum_i a_ib_{n-i}}{n}=ab
 
$$

</div>

<div class='pbox'>

#### Solution 1

$b=0$时,考虑$a有界M$.

$$
\begin{gathered}
\lim_{n \to \infty} \dfrac{\sum_i a_ib_{n-i}}{n} \\
\le \lim_{n \to \infty} M\dfrac{b_{n-i}}{n} =0
\end{gathered}
$$

$b\ne 0$,$b'_i=b_i-b$,有

$$
\begin{gathered}
\lim_{n \to \infty} \frac{\sum_i a_ib_{n-i}}{n} =\lim_{n \to \infty} \frac{\sum_i a_ib'_{n-i}}{n} +\frac{\sum_i a_i}{n} b=0+ab
\end{gathered}
$$

$$
\begin{gathered}

\end{gathered}
$$

#### Solution 2

不妨设$a,b>0$,则有界性可以得到后面是$a_n,b_n>0$

考虑影响值的肯定是中间的项,所以直接拆,取$\epsilon$,对$a,b$可以得到$N_1$

$$
\begin{gathered}
\lim_{n \to \infty} \dfrac{\sum_i a_ib_{n-i}}{n}= \\
=\lim_{n \to \infty} \dfrac{\sum _{i = 1} ^{N_1} a_ib_{n-i}+\sum _{i = 1} ^{N_1} b_ia_{n-i}+\sum _{i = N_1+1} ^{n-N_1-1} a_ib_{n-i} }{n}  \\
=\lim_{n \to \infty} \dfrac{\sum _{i = 1} ^{N_1} a_ib_{n-i}}{n} \\
+ \lim_{n \to \infty} \dfrac{\sum _{i = 1} ^{N_1} b_ia_{n-i}}{n} \\
+\lim_{n \to \infty} \dfrac{\sum _{i = N_1+1} ^{n-N_1-1} a_ib_{n-i}}{n} \\
\in (\lim_{n \to \infty} \dfrac{n-2N_1-1}{n} (a-\epsilon)(b-\epsilon) \\
,\lim_{n \to \infty} \dfrac{n-2N_1-1}{n} (a+\epsilon)(b+\epsilon)) \\
= ((a-\epsilon)(b-\epsilon),(a+\epsilon)(b+\epsilon))
\end{gathered}
$$

后面显然.`

</div>

## Class 4

### eg1

<div class='cbox'>

$$
\begin{gathered}
a>1,k\in N^*,\lim_{n \to \infty} \frac{n^k}{a^n} =0
\end{gathered}
$$

</div>

<div class='pbox'>

$a^n=(1+b)^n$展开会出现$n$的任意次方,然后显然.

</div>

### Stolz

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
y_n \uparrow,\lim_{n \to \infty} y_n=\infty \\
\lim_{n \to \infty} \dfrac{x_n-x_{n-1}}{y_n-y_{n-1}} =a\in[-\infty,+\infty]
\end{cases}
 \\
\Rightarrow \lim_{n \to \infty} \dfrac{x_n}{y_n} =a
\end{gathered}
$$

</div>



<div class='pbox'>

先简化,不妨设$a\ge 0,\frac{\Delta x_n}{\Delta y_n}>0$

然后可以证$a=0$时,你取$\epsilon_1$得$N_1$,变成 $\dfrac{\Delta x_n}{\Delta y_n} <\epsilon$.于是

$$
\begin{gathered}
\dfrac{x_n}{y_n}  \\
=\dfrac{x_{N_1}+\sum _{i = N_1+1} ^{n}  \Delta x_i}{y_{N_1}+\sum _{i = N_1+1} ^{n}  \Delta y_i}  \\
\le \dfrac{x_{N_1}+\epsilon\sum _{i = N_1+1} ^{n}  \Delta y_i}{y_{N_1}+\sum _{i = N_1+1} ^{n}  \Delta y_i}  \\
\le \dfrac{x_{N_1}+\epsilon\sum _{i = N_1+1} ^{n}  \Delta y_i}{\sum _{i = N_1+1} ^{n}  \Delta y_i}
\end{gathered}
$$

因为你  $Y=\sum _{i = N_1+1} ^{n} \Delta y_i \to +\infty$,所以一定可以有$\epsilon Y>x_{N_1}$.就能证$<2\epsilon$,你再取一下$\epsilon$就得证了.

然后我说$0<a\in R$时你直接$x'=x-ay$就用结论,$a=+\infty$的时候你取倒数用结论,就做完了. 

</div>

## Class 5

### 单调有界数列有极限

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
a_i>a_{i-1} \\
a_i<M
\end{cases}
\Rightarrow 
\lim_{n \to \infty} a_i \text{ exists} 
\end{gathered}
$$

</div>

<div class='pbox'>

取 $\{a_i\}$上确界$M_0$,则任意$\epsilon$,取$M'=M_0-\epsilon$,由确界知$\exists i \ s.t.\ 
a_i\in (M',M_0]$,则$\forall n>i,\vert a_n-M\vert<\epsilon$.

然后书上因为没教你上确界,试图用无限小数说明.那其实就是你一位一位考虑,就先这一位增加到最大,然后进入下一位,容易发现最后区间长度趋近于$0$

其实无限小数就是区间套啊.

</div>

### e

<div class='cbox'>

$$
\begin{gathered}
a_n:=\lim_{n \to \infty} (1+\dfrac{1}{n} )^n = b_n:=\lim_{n \to \infty} \sum _{i = 0} ^{n}  \dfrac{1}{i!}
\end{gathered}
$$

</div>

<div class='pbox'>

右边那个单调有界都是好证的.证相等:

$$
\begin{gathered}
a_n=(1+\dfrac{1}{n} )^n=\sum _{i = 0} ^{n}  \dfrac{1}{n^i} \binom{n}{i} \\
=\sum _{i = 0} ^{n}  \dfrac{1}{i!} \prod_{j=0}^{i-1} (1-\dfrac{j}{n} )
<b_n \\
\end{gathered}
$$

又有

$$
\begin{gathered}
k<n \Rightarrow 
a_n=\sum _{i = 0} ^{n}  \dfrac{1}{i!} \prod_{j=0}^{i-1} (1-\dfrac{j}{n} )
>\sum _{i = 0} ^{k}  \dfrac{1}{i!} \prod_{j=0}^{i-1} (1-\dfrac{j}{n} )
\end{gathered}
$$
于是先令$k\to \infty$得到$a_n>b_k$,则$a$逐项大于$b$的一个子列,最后得证.

</div>

重点是把一次到极限拆成两个取极限.但这个为什么对呢.

是好证的,其实就是

<div class='bbox'>

[think] 

$$
\begin{gathered}
\lim_{a \to \infty} \lim_{b \to \infty} f(a,b) = X
\Rightarrow \lim_{n \to \infty} f(n,n) = X
\end{gathered}
$$

用定义是显然的.且如果极限都存在(要$f(a,n)$和$f(n,b)$极限存在)的话你还可以看出左式两取极限交换(都是右式)

</div>

<div class='cbox'>

$$
\begin{gathered}
0<e-\sum _{i = 0} ^{n}  \dfrac{1}{i!} < \dfrac{1}{n\cdot n!} 
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
b_n:=\sum _{i = 0} ^{n}  \dfrac{1}{i!} \\
X=b_{n+m}-b_n=\sum _{i = n+1} ^{n+m}  \dfrac{1}{i!}  \\
<\dfrac{1}{(n+1)!} \sum _{i = 0} ^{m-1}  \dfrac{1}{(n+1)^i}<\dfrac{1}{n!\cdot n}   \\ \Rightarrow e-b_n= \lim_{m \to \infty} X<\dfrac{1}{n!\cdot n} 
\end{gathered}
$$

然后说为什么取极限小于号还是小于号呢?

$$
\begin{gathered}
X=b_{n+m}-b_n<b_{n+m+k}-b_n<\dfrac{1}{n!\cdot n} 
\\
\stackrel{\lim_{k \to \infty} }{\Longrightarrow}
e-b_n<\dfrac{1}{n!\cdot n} 
\end{gathered}
$$

[think] 对单调数列让一个独立变量趋近无穷说明严格不等号.

有个魔怔法,你先去下一条证明$e$是无理数再回来说取不了等.



</div>

<div class='cbox'>

$e\not \in Q$

</div>

<div class='pbox'>

假设$e=\dfrac{p}{q}$

$$
\begin{gathered}
\dfrac{p}{q} -b_n<\dfrac{1}{n\cdot n!} 
\stackrel{n=q}{\Longrightarrow}
p(q-1)!-b_q q!<\dfrac{1}{q} 
\end{gathered}
$$

左边是不为$0$的整数(为$0$与$b$增矛盾),右边是分数

</div>

[think] 一个无理数等价于存在一列分母到无穷的有理数始终有更高阶(相比序列中分母)的余项.

<div class='cbox'>

$$
\begin{gathered}
(1+\dfrac{1}{n} )^n \uparrow \\
(1+\dfrac{1}{n} )^{n+1} \downarrow
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
(1+\dfrac{1}{n} )^n\cdot 1< (\dfrac{n\cdot (1+\dfrac{1}{n}+1 )}{n+1} )^{n+1}=(1+\dfrac{1}{n+1} )^{n+1}
\end{gathered}
$$

第二个取倒数同理.

</div>

从这个出发可以说明$\ln$的切线放缩系列不等式.

### 有界数列必有单调子列

<div class='cbox'>

有界数列有收敛子列

</div>

<div class='pbox'>

可以考虑后缀max,取出一个单调子列.

也可以区间套,每次进有无穷多项的区间.

</div>

## Class 6

### Cauchy Convergance Theorem

<div class='cbox'>

Cauchy Convergance Theorem

$$
\begin{gathered}
\forall \epsilon, \exists N \\ s.t.\\ 
\forall n,m>N, \vert a_n-a_m\vert<\epsilon
\Leftrightarrow \lim_{n \to \infty} a_n \text{ exists} 
\end{gathered}
$$

</div>

<div class='pbox'>

右推左是显然的.

首先容易得到有界.于是它有收敛子列.

然后你其他的项到你的收敛子列的距离拿柯西的条件放缩一下就证完了.

或者也可以闭区间套.

</div>

### 确界原理

<div class='cbox'>

有上界的数集一定有上确界.

</div>

<div class='pbox'>

来闭区间套,二等分,如果上面的(包含边界)有就取上面,否则取下面,框出一个数.

然后来看,比他小的不是上界是好说的(取个区间即可).怎么说明它是上界呢?

考虑任何一个数,递归后一定有某一次它在下半区间(包含中点),那就证完了.

可能甚至不如无穷小数简洁 反正本质相同.

</div>

### 有限覆盖定理

<div class='cbox'>

$$
\begin{gathered}
S=\{ (x,y) \vert x<y \},T\subset S , \cup_{I\in T} I \supset [a,b] \\
\Rightarrow \exists A \in T,\cup_{I\in A} I \supset [a,b],\vert A\vert\in N(\text{not infinity} ) 
\end{gathered}
$$

</div>

<div class='pbox'>

反证,设$[A,B]$不能被有限覆盖.

闭区间套 二等分 则一定有一半区间也是不能被有限覆盖的.递归到不能被有限覆盖的区间,最后弄出一个数.

但包含这个数的极小区间显然可以被有限覆盖.矛盾,得证.

</div>

很棒的啊,它完全不关心你无穷覆盖的结构而是到数的结构去了.

## Class 7

### Funciton's Limits

<div class='dbox'>

$$
\begin{gathered}
\lim_{x \to x_0} f(x) = A  \\
\Leftrightarrow \forall \epsilon, \exists \delta,\\ s.t.\\ 
\forall x, \vert x-x_0 \vert \in (0,\delta), \vert f(x)-A \vert <\epsilon
\end{gathered}
$$

</div>

<div class='cbox'>

Heine Theorem

$$
\begin{gathered}
\lim_{x \to x_0} f(x)=A \\
\Leftrightarrow \forall \{ x_n \} ,\lim_{n \to \infty} x_n  = x_0 \\
\lim_{n \to \infty} f(x_n) = A
\end{gathered}
$$

</div>

<div class='pbox'>

正向是显然的.

反向你就反证,然后极限不存在就翻译成 

$$
\exists \epsilon, \forall \delta, \exists x,\vert x-x_0 \vert  \\
\vert f(x)-A \vert \ge \epsilon
$$

于是你取一个极限是$0$的$\delta$,得到一列收敛到$x_0$的$x$,然后用这个数列就矛盾了.

</div>

然后你可以用这种方法,把函数极限的各种性质转化到数列极限,四则运算,夹逼等.

<div class='cbox'>

柯西收敛

$$
\begin{gathered}
\lim_{x \to x_0} \text{ exists} \Leftrightarrow \forall \epsilon, \exists \delta,\forall x_1,x_2 \in N^*(x_0,\delta),\vert f(x_1)-f(x_2) \vert < \epsilon
\end{gathered}
$$

</div>

<div class='pbox'>

正向是显然的.

反向的话你可以用上面Heine转化成数列,则你只需要证所有这样的数列极限相等.

然后你发现你直接取任意两个数列,然后插(奇数偶数项分别放两个数列的元素)就可以直接证明这两个数列极限相等.于是结束.

</div>

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
\lim_{x \to x_0} f(x) = A \\
\lim_{t \to t_0} g(t) = x_0 \\
\exists \eta>0, t\in N(t_0,\eta) \Rightarrow g(t)\ne 0
\end{cases} \\
\Rightarrow \lim_{t \to t_0} f(g(t)) = A
\end{gathered}
$$

</div>

<div class='pbox'>

直接翻译成$\epsilon-\delta$是显然的.

</div>

<div class='cbox'>

$$
\begin{gathered}
\lim_{ \to _0} \dfrac{\sin(x)}{x} = 1
\end{gathered}
$$

</div>

<div class='pbox'>

通过$\sin(x)\le x \le \tan(x)$同时除以$x$得到:

$$
\begin{gathered}
\begin{cases}
\dfrac{\sin(x)}{x} \le 1 \\
\dfrac{\sin(x)}{x} \ge \cos(x)
\end{cases} \\
\stackrel{\text{Squeeze Theorem}}{\Longrightarrow} \\
\lim_{x \to 0} \dfrac{\sin(x)}{x} =1
\end{gathered}
$$

</div>

<div class='cbox'>

$$
\begin{gathered}
R(x)=\begin{cases}
1,x=0 \\
\dfrac{1}{q}, x=\dfrac{p}{q}  \\
0,x\notin Q
\end{cases}
\Rightarrow \lim_{x \to x_0} R(x)=0
\end{gathered}
$$

</div>

<div class='pbox'>

首先显然是周期函数可以只看$[0,1]$.

其次对于任意$x_0$,对$\epsilon$,对所有 $n\le \dfrac{1}{\epsilon}$,令 $\delta=\dfrac{1}{2} \min_{j\le n,i\le j} \{ \vert \dfrac{i}{j} -x_0 \vert  \}$即可保证,该区间$[x-\delta,x+\delta]$内没有分母比$n$小的有理数,于是就证明了.

</div>





## Ex Class 1

### 定义指数函数

<div class='cbox'>

承认确界原理,实数的四则运算,$<$关系,等式性质等.

定义指数函数$下a^x(a>0),x\in R$

</div>

<div class='pbox'>

首先良好的定义$x\in N$的情况.

然后尝试定义 $x=\dfrac{1}{k},k\in N$的情况,那么要证明

<div class='cbox'>

$$
\begin{gathered}
\forall x>0,n\in N^*,\exists! y {\ } s.t. {\ } y^n=x
\end{gathered}
$$

</div>

<div class='pbox'>

那么构造 $E=\{ t \vert t^n<x \}$,容易证明:
- 非空:$\dfrac{x}{1+x}\in E$
- 有上界:$(x+1)^n>x$

于是确界存在,设上确界为$y$,尝试证明$y^n=x$.

假设$y^n<x$,设$h\in (0,\min(1,\dfrac{x-y^n}{n(y+1)^{n-1}}))$.

于是发现$(y+h)^n-y^n<hn(y+h)^{n-1}<x-y^n$

于是$(y+h)^n<x,y+h\in E$,与$y$是上确界矛盾.

再假设$y^n>x$,设$h=\dfrac{y^n-x}{ny^{n-1}}$.

则$y^n-(y-h)^n<hny^{n-1}=y^n-x$,即$(y-h)^n>x$,故$y-h$也是$E$的上界,与上确界矛盾.

于是就证明出$y^n=x$.

</div>


那么现在我们能定义 $a^x,x\in Q$. 了吗?

不行.接下来你要证明有理数约不约分结果是一样的.即:

<div class='cbox'>

$$
\begin{gathered}
r=\dfrac{m}{n} =\dfrac{p}{q} \Rightarrow a=(x^m)^{\frac1n}=(x^p)^{\frac1q}=b
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
a^{nq}=x^{nrq},b^{nq}=x^{nrq} \\
\Rightarrow  a^{nq}=b^{nq} \\
\Rightarrow a=b
\end{gathered}
$$

</div>

下一个目标是实数!

定义$a^x,x\in R$是所有$a^q,q\in Q,q\le x$的上确界就行了吧!

那么你是不是得说说实数这个满足和刚才一样的运算律,也就是:

<div class='cbox'>

$$
\begin{gathered}
a^xa^y=a^{x+y} \\
(a^x)^y=a^{xy}
\end{gathered}
$$

</div>

<div class='pbox'>

然后他下课不讲了

todo

</div> 


</div>

## Class 8

### 等价无穷小替换

重点就是你只能替换形如$F(x)P(x)\to F(x)Q(x)(P(x)\sim Q(x))$.

你不能替换$F(x,P(x))\to F(x,Q(x))$这种.

这样正确性就保证了.

然后对$F(x)(P(x)+H(x))\to F(x)(Q(x)+H(x))$是合法的,当且仅当你低次项没消掉.

然后通用就是你换的时候带上配亚诺余项就不会错了.


### 反函数连续性


<div class='cbox'>

连续函数的反函数是连续的.

$$
\begin{gathered}
f(x) \text{ is continuous} ,f\circ f^{-1}=x \\
\Rightarrow f^{-1} \text{is continuous} 
\end{gathered}
$$

</div>

<div class='pbox'>

#### Sol1

$$
\begin{gathered}
\lim_{y \to y_0} f^{-1}(y)=f^{-1}(y_0)=x_0 \\
\Leftrightarrow \forall \{ y_n \} ,\lim_{n \to \infty} y_n=y_0 \ s.t.\ 
\lim_{n \to \infty} f^{-1}(y)=x_0 \\
\text{Contrapose! Assume} \exists \epsilon,\forall \delta,\exists y_1\in N^*(y_0,\delta),\vert f^{-1}(y_1)-x_0 \vert > \epsilon. \\
\exists \{ x_n \} ,x_n=y_1(\delta). \\
x_n \text{is bounded} \Rightarrow \exists \{ i_n \} , \\
x_{i_n} \text{is convergent} ,\lim_{n \to \infty} x_{i_n}=X\ne x_0 \\
\lim_{n \to \infty} f(x_{i_n})=f(X) \\
\because \lim_{n \to \infty} f(x_n) =\lim_{n \to \infty} y_n=y_0 \\
\therefore f(X)=y_0=f(x_0),X\ne x_0  \\
\text{Contradiction to injection} 
\end{gathered}
$$

[think] 这里为什么数列这么好用呢?感觉因为函数极限的定义不是对称的,但  $\lim_{n \to \infty} x_n=x_0,\lim_{n \to \infty} y_n=y_0$ 这个关系是对称的.

#### Sol2

容易证明连续函数是单射必须严格单调.

对$x_0$的任意邻域$N$,$f(N)$也是$y_0$的邻域,于是 $\forall \epsilon,x\in N(x_0,\epsilon) \Rightarrow y\in f(N(x_0,\epsilon))$,把这个翻译成$\epsilon-\delta$.

[think] 考虑的是连续函数把邻域变成邻域(或者说连续函数把闭集映到闭集,于是在一边有极限在另一边也有)吧.

</div>

所以证连续其实是用不着单调的. 不过我们知道连续函数单射一定是单调的.

### 初等函数都是连续函数


<div class='cbox'>

初等函数都是连续函数

</div>

<div class='pbox'>

$x^a=e^{a\ln x}$,于是只要证:
- 指数函数和三角函数是连续的
- 连续函数的反函数是连续的

指数:

$$
\begin{gathered}
\lim_{x \to x_0} e^x = e^{x_0} \lim_{x \to x_0}  e^{x-x_0} = e^{x_0} \lim{x\to 0} e^x \\
\Rightarrow e^x \text{ is continuous} \Leftrightarrow e^x \text{ is continuous at } 0 \\
\lim_{x \to 0} e^x=0  \\
\Leftrightarrow \forall x_n,\lim_{n \to \infty} e^{x_n} = 0,\lim_{n \to \infty} x_n=0 \\
\lim_{n \to \infty} n^{\frac{1}{n}}=1 \Rightarrow  \lim_{n \to \infty} e^{x_n}=0
\end{gathered}
$$

三角:

$$
\begin{gathered}
\lim_{\Delta x \to 0} \sin(x+\Delta x)=\sin x\cos \Delta x+\cos x\sin \Delta x \\
=\sin x
\end{gathered}
$$

反函数用前面的方法.

</div>

## Class 9


### Intermediate value theorem

<div class='cbox'>

$$
\begin{cases}
x\in [a,b], f\text{ is continuous} \\
y\in [f(a),f(b)]
\end{cases} \Rightarrow \exists x_0, f(x_0)=y
$$

</div>

<div class='pbox'>

#### Sol1

不妨设$f(a)\le y \le f(b)$,$=$情况显然,只考虑$f(a)<y<f(b)$.

取 $A=\{ x\vert f(x)<y \}$ 则它有上确界$x_1$.

那么要证明$f(x_1)=y$,考虑:

若$f(x_1)<y$,则 $\lim_{x \to x_1} f(x)=y \Rightarrow \epsilon=y-f(x_1),\forall x\in (x_1-\delta,x_1+\delta)\Rightarrow f(x)\in (f(x_1)-\epsilon,f(x_1)+\epsilon)<y$,于是$\exists x_2>x_1,f(x_2)<y$,与$x_1$上确界矛盾.故$f(x_1)\le y$.

同理$f(x_1)\ge y$,于是$f(x_1)=y$.

那么一定存在一个收敛到$x_1$的数列 $\{ z_n \}$ 你就直接发现 $\lim_{n \to \infty}  f(z_n) = f(\lim_{n \to \infty} z_n)$

$\text{Q.E.D}$ 

[think] 核心在 $x_0=\sup \{ x \vert f(x)<y \}$,即先看到构造$x_0$的方式.

#### Sol2

另一个做法是闭区间套,把区间二等分,那么把平凡情况讨论掉后,一定有$(f(a)-y)(f(b)-y)<0$,那么现在区间中点$m$处,$f(m)=y$直接结束,否则递归到值域区间包含$y$的一边.

如果过程没有在中间停止,那么闭区间套定理,$\exists !\xi$在所有的区间中.考虑区间序列$[a_n,b_n]$,那么显然$f(a_n)-p$和$f(b_n)-p$符号始终不变且相异,于是对$a,b$分别取极限可以证$f(\xi)$收敛到$y$.

[think] 讲题顺序很迷惑(这个证明是Class 11讲零点存在弄出来的). 不过你注意到**这个闭区间套证法是可以证明其他几条连续函数性质的(闭区间上一致连续,有界,极值定理都是可以的).**

</div>


### 间断点分类.

<div class='dbox'>

$$
\begin{gathered}
\text{when } 
\lim_{x \to x_0} f(x)=f(x_0) \text{ not satisfied} 
\end{gathered}
$$

分类:

- $f(x_0^+)\ne f(x_0^-)$:跳跃间断点
- $f(x_0^+)=f(x_0^-)\ne f(x_0)$:可去间断点
- $f(x_0^+) \text{ or } f(x_0^-) \text{ not exists}$:无穷间断点


</div>

<div class='cbox'>

在$[a,b]$上有定义的单调函数的间断点必然是跳跃间断点.

</div>

<div class='pbox'>

那么先证明左右极限存在:若$x_0$是间断点,这里和介值定理的证明是一样的:

$$
\begin{gathered}
\text{let } S=\{ f(x)\vert x\in[a,x_0) \}  \\
A=\sup S \\
\text{if }A<f(x_0),\text{by limit's local sign-preserving property}  \\
\exists x_1\in N^*(x_0),x_1>x_0,f(x_1)<A,\text{Contradiction!} \\
\text{same for } A>f(x_0) \\
\therefore A=f(x_0)  \\
\stackrel{\text{Heine Theorem}}{\Longrightarrow}
\lim_{x \to x_0^-}f(x)=A \\
\text{same for } B=\lim_{x \to x_0^+}f(x)=B  \\
\forall x_1<x_0,x_2>x_0,f(x_1)<f(x_2) \\
f(x_1)<f(x_0) \stackrel{\lim_{x_1 \to x_0} }{\Longrightarrow}A\le f(x_0) \\
f(x_2)>f(x_0)\stackrel{\lim_{x_2\to x_0}}{\Longrightarrow}B\ge f(x_0) \\
\therefore A=B \Rightarrow A=f(x_0)=B \\
\therefore A\ne B
\end{gathered}
$$

</div>

[think] 这个证明和介值定理证明那里都走了:构造集合,确界存在,确界等于某值,构造集合里极限为确界的收敛数列,连续性 的流程, 似乎是推出集合边界极限的套路.

<div class='cbox'>

在$[a,b]$上有定义的单调函数的间断点必然至多可数个.

</div>

<div class='pbox'>

对$x_1,x_2$两个跳跃间断点:

$$
\begin{gathered}
f(x_1^-)<f(x_1^+)\le f(x_2^-)<f(x_2^+)
\end{gathered}
$$

于是每个间断点$x_i$对应一个$(f(x_i^-),f(x_i^+))$,且不同$x_i$对应区间互不相交.

于是每个区间可以对应一个不同的有理数,有理数至多可数.

</div>

[think] 于是任何一个区间的不交划分只有可数个.(禁止$[a,a]$的情况)

## Ex Class 2

其实这节课在Class 10后面 但讲间断点的话和这里更近.

<div class='cbox'>

$$
\begin{gathered}
\forall f(x), x\in (a,b),f \text{ has at most countable point of discontinuity of the first kind} 
\end{gathered}
$$

</div>

<div class='pbox'>

首先我们考虑右极限大于左极限的间断点,证明它们是可数的.

对于一个间断点$x_0$,$\lim_{x \to x_0^-} f(x)=A,\lim_{x \to x_0^+} f(x)=B$,显然我们可以找到$p\in Q,p\in (A,B)$.

而由于极限保号性,你也容易找到$q,r\in Q$使得$\forall x\in (q,x_0),f(x)<p,\forall x\in (x_0,r),f(x)>p$.

考虑是否可能有两个间断点$x_1<x_2$对应相同的$p,r,q$,那么显然$q<x_1<x_2<r$,但是$(x_1,r)$中的值小于$p$,$(q,x_2)$中的值大于$p$,而这两个区间有交,所以不可能有两个间断点对应相同的$p,r,q$,那么这些间断点可以单射到$Q^3$上是可数的.

而对于左极限小于右极限的间断点同理可得.

接下来考虑左右极限相等的间断点,让$p\in (A,f(x_0))$,而$q,r$满足$(q,x_0),(x_0,r)$有$f(x)<p$,那么考虑有两个相同的这样的$p,q,r$的$x_1,x_2$,你会发现$f(x_1)$和$f(x_2)$不能都小于$p$你就爆炸了.所以也是不同的间断点对应不同的数对.

于是都是可数的.总和也是可数的.

</div>



## Class 10

### Some Limits' Calculation


<div class='bbox'>

$$
\begin{gathered} \\
f\to 1,g\to \infty \\
\lim f^g=e^{\lim g\ln f}=e^{\lim g(f-1)}
\end{gathered}
$$

</div>

<div class='cbox'>

$$
\begin{gathered}
\lim_{x \to \infty} (1+\dfrac{1}{x} )^x=e
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\lim_{x \to +\infty} (1+\dfrac{1}{x} )^x\in 
((1+\dfrac{1}{[x]+1} )^{[x]},(1+\dfrac{1}{[x]} )^{[x]+1}) \\
\text{let } e_n=\lim_{n \to \infty} (1+\dfrac{1}{n} )^n \\
\lim_{x \to +\infty} (1+\dfrac{1}{[x]+1} )^{[x]} \\
=\lim_{n \to \infty}  e_{[x]+1}(1+\dfrac{1}{[x]+1})^{-1} \\
=e \\
\lim_{x \to +\infty} (1+\dfrac{1}{[x]} )^{[x]+1} \\
=\lim_{n \to \infty}  e_{[x]}(1+\dfrac{1}{[x]} ) \\
=e \\
\stackrel{\text{ Squeeze Theorem }}{\Longrightarrow}
\lim_{x \to +\infty} (1+\dfrac{1}{x} )^x=e \\
\lim_{x \to -\infty} (1+\dfrac{1}{x} )^x \\
=\lim_{x \to +\infty}(1+\dfrac{1}{-x} )^{-x} \\
=\lim_{x \to +\infty}(\dfrac{x}{x-1}  )^x \\
=\lim_{x \to +\infty}(1+\dfrac{1}{x-1}  )^x \\
=e
\end{gathered}
$$

</div>

真麻烦.一句话就是取整夹你.

<div class='cbox'>

$$
\begin{gathered}
\lim_{x \to 1} \dfrac{m}{x^m-1} -\dfrac{n}{x^n-1} 
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\lim_{x \to 1} \dfrac{m}{x^m-1} -\dfrac{n}{x^n-1} 
=\lim_{x \to 1} \dfrac{m(x^n-1)-n(x^m-1)}{(x^m-1)(x^n-1)}  \\
=\lim_{x \to 1} \dfrac{m(n(x-1)+\dfrac{n(n-1)}{2} (x-1)^2)}{mn(x-1)^2}  \\
-\dfrac{-n(m(x-1)+\dfrac{m(m-1)}{2} (x-1)^2)}{mn(x-1)^2} \\
=\lim_{x \to 1} \dfrac{mn^2-nm^2}{2nm}  \\
=\dfrac{n-m}{2} 
\end{gathered}
$$

</div>

### Uniform Continuity

<div class='dbox'>

Uniform Continuity

$$
\begin{gathered}
f(x) \text{ is uniformly continuous in } [a,b]  \\
\Leftrightarrow 
\forall \epsilon>0,\exists \delta,\forall x_1,x_2\in [a,b], \\
\vert x_1-x_2 \vert <\delta \Rightarrow \vert f(x_1)-f(x_2) \vert <\epsilon
\end{gathered}
$$

</div>

<div class='bbox'>

Not Uniform Continuity

$$
\begin{gathered}
\exists \epsilon,s_n,t_n, \\
\vert s_n-t_n \vert < \dfrac{1}{n} ,\vert f(s_n)-f(t_n) \vert >\epsilon
\end{gathered}
$$

</div>



<div class='cbox'>

$$
\begin{gathered}
f(x)=\sqrt{ x } \text{ is uniformly continuous in } [0,+\infty) 
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
x_1>x_2 \Rightarrow  \\
\vert \sqrt{x_1}-\sqrt{ x_2 } \vert  ={\left \vert \dfrac{x_1-x_2}{\sqrt{ x_1 } +\sqrt{ x_2 } }  \right \vert} < {\left \vert \dfrac{x_1-x_2}{\sqrt{x_1-x_2}}  \right \vert} =\sqrt{ x_1-x_2 }<\sqrt \delta 
\end{gathered}
$$

</div>

<div class='cbox'>

$$
\begin{gathered}
f(x)=\dfrac{1}{x} \text{ is not uniformly continuous in } (0,1)
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\dfrac{1}{n} -\dfrac{1}{2n} <\dfrac{1}{n} , \\
y(\dfrac{1}{n} )-y(\dfrac{1}{2n} )=n\ge 1
\end{gathered}
$$

</div>

### 闭区间连续函数性质

<div class='cbox'>

闭区间上的连续函数一致连续

</div>

<div class='pbox'>

反证

$$
\begin{gathered}
\exists \epsilon,s_n,t_n,\vert s_n-t_n \vert <\dfrac{1}{n} ,\vert f(s_n)-f(t_n) \vert >\epsilon \\
\end{gathered}
$$

取$s_n,t_n$的收敛子列$s'_n,t'_n$:

$$
\begin{gathered}
\text{let} x_0=\lim_{n \to \infty} s'_n=\lim_{n \to \infty} s_n=\lim_{n \to \infty} t'_n=\lim_{n \to \infty} t_n \in [a,b] \\
\lim_{n \to \infty} f(s'_n)=\lim_{n \to \infty} f(t_n')=f(x_0) \\
\Rightarrow \lim_{n \to \infty} \vert f(s'_n)-f(t'_n) \vert =0
\end{gathered}
$$

</div>

<div class='cbox'>

闭区间上连续函数一定有界.

</div>

<div class='pbox'>

#### Sol1

反证,设无界,$\exists x_n$满足$f(x_n)>n$,取$x_n$的收敛子列,那么 $f(\lim_{n \to \infty} x_n)=\infty$矛盾.

#### Sol2

用上面一致连续,那么区间的值域跨度不超过 $\dfrac{b-a}{\delta} \epsilon$.

</div>

<div class='cbox'>

闭区间上连续函数一定能取到最大值最小值.

$$
\begin{cases}
M=\sup \{ f(x) \vert x\in [a,b] \} \\ 
\text{f is continuous}
\end{cases}
\Rightarrow \exists x\in [a,b], f(x)=M
$$

</div>

<div class='pbox'>

考虑取任意$M_1<M$,可以得到一个$f(x_1)\in (M_1,M)$,取$M_n>f(x_{n-1})$可得$x_n \in (M_n,M)$,显然$x_n$有界可以取收敛子列$y_n$,则$\lim_{n \to \infty} f(y_n)=f(\lim_{n \to \infty} y_n)$,则于是得证 

</div>



## Class 11

### Continuous Function's Periodicty

<div class='cbox'>

$$
\begin{cases}
f(x)\text{ is a periodic function that isn't constant} \\
f(x)\text{ is continuous} 
\end{cases} \\
\Rightarrow f(x)\text{ has min positive period} 
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
T:= \{ t \vert t>0,f(x+t)=f(x) \}  \\
t_0:= \inf T \\
\end{gathered}
$$

若$t_0\ne 0$,取 $\{ t_n \},t_i\in T,\lim_{n \to \infty} t_n=t_0$,则 $f(x)=f(x+t_n)=\lim_{n \to \infty} f(x+t_n)=f(x+\lim_{n \to \infty} t_n)=f(x+t_0)$

若$t_0=0$,因为不是常函数, 则$\exists x_0 {\ } s.t. {\ }  f(x_0)\ne f(0)$,因为连续,和极限有保号性你可以说$\forall x\in O(x_0,\delta),f(x)\ne f(0)$,但由$t_0=0$,你可以找到$t<\delta$,那就可以再找到$N$使得$Nt\in (x_0-\delta,x_0+\delta)$,$Nt$一定是周期,但$f(0+Nt)\ne f(0)$,矛盾.

于是得证.

</div>

### Directive

导数的定义,初等函数求导,导数的四则运算.

## Class 12

### 极限里换元

<div class='cbox'>

$$
\begin{gathered}
u(x) \text{ is continuous},\lim_{u \to u_0} G(u)=A  \\
\Rightarrow \lim_{x \to x_0} G(u(x)) = A
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\forall \epsilon,\exists \delta, u(x)\in N^*(u(x),\delta_1) \Rightarrow G(u(x))\in N(A,\epsilon) \\
\Rightarrow \forall \epsilon,\exists \delta,x\in N^*(x_0,\delta) \Rightarrow u(x)\in N(u(x),\delta_1) \\
\end{gathered}
$$

这里有一点小小的问题,不过你发现只要定义$G_1(u(x_0))=G_1(u_0)=A$即可避免,因为条件里这个点反正是任意的.

于是结束.

</div>

### 复合函数求导(链式法则)

<div class='cbox'>

$$
\begin{gathered}
(f(g(x)))'=f'(g(x))g'(x)
\end{gathered}
$$

</div>

<div class='pbox'>

#### Sol

用上面的极限换元一换就出来啦

#### My Sol

$$
\begin{gathered}
f(x)=f(x_0)+f'(x_0)(x-x_0)+o(x-x_0) \\
g(x)=g(x_0)+g'(x_0)(x-x_0)+o(x-x_0) \\
\lim_{x \to x_0} \dfrac{f(g(x))-f(g(x_0))}{x-x_0}  \\
=\lim_{x \to x_0} \dfrac{f(g(x_0)+g'(x_0)(x-x_0)+o(x-x_0))-f(g(x_0))}{x-x_0} \\
=\lim_{x \to x_0} \dfrac{f'(g(x_0))(g'(x_0)(x-x_0)+o(x-x_0))}{x-x_0} \\
+\dfrac{o(g'(x_0)(x-x_0)+o(x-x_0))}{x-x_0}  \\
=\lim_{x \to x_0} f'(g(x_0))g'(x_0)+\dfrac{o(g'(x_0)(x-x_0)+o(x-x_0))}{x-x_0}      \\
\end{gathered}
$$

而满足$o(x-x_0)\le\epsilon(x-x_0)$的$x$是$x_0$的一个邻域,于是

$$
\begin{gathered}
\lim_{x \to x_0} \dfrac{o(g'(x_0)(x-x_0)+o(x-x_0))}{x-x_0}  \\
\le \lim_{x \to x_0} \dfrac{ o((g'(x_0)+\epsilon)(x-x_0))}{x-x_0}  \\
=0
\end{gathered}
$$

得证.

只能说很暴力.

</div>

### 莱布尼茨求导公式

<div class='cbox'>

$$
\begin{gathered}
(uv)^{(n)}=\sum _{i = 1} ^{0} \binom{n}{i} u^{(i)}v^{(n-i)}
\end{gathered}
$$

</div>

<div class='pbox'>

归纳

</div>

据说一般用在有一个高阶导数是$0$的情况

<div class='cbox'>

$$
\begin{gathered}
\arctan^{(50)}(0)=0
\end{gathered}
$$

</div>

<div class='pbox'>

#### Sol 1

$$
\begin{gathered}
\arctan'(x)=\dfrac{1}{1+x^2}  \\
\Rightarrow (1+x^2)\arctan'(x)=1 \\
0=((1+x^2)\arctan'(x))^{(n)} \\
=(1+x^2)\arctan^{(n+1)}(x)+\binom{n}{1}2x\arctan^{(n)}(x)+\binom{n}{2}2\arctan^{(n-1)}(x) \\
\stackrel{ x=0 }{\Longrightarrow} \arctan^{(n+1)}(0)+n(n-1) \arctan^{(n-1)}(0)=0
\end{gathered}
$$

于是有递推,得到是$0$.

#### Sol 2

注意到一阶导是偶函数,又求了奇数次变成奇函数,所以说$0$.

#### Sol 3

对

$$
\begin{gathered}
\dfrac{1}{1+x^2}=\dfrac{1}{(x-i)(x+i)} =\dfrac{1}{(1-ix)(1+ix) }  \\
=\dfrac{1}{2i} (\dfrac{1}{x-i}-\dfrac{1}{x+i})
\end{gathered}
$$

于是可以对两个分数分别求导.复变函数从实数轴上逼近的导数当然就是原函数的导数.

</div>

## Class 13

### 中值定理

#### Theorems

<div class='dbox'>

极值点

$f(x_0)$是极大值当且仅当存在$\delta,\forall x\in N^*(x,\delta),f(x)<f(x_0)$

</div>

极值和最值既不充分也不必要.

最值是极值当且仅当最值在区间内部,端点不行.


<div class='cbox'>

Fermat Theorem

$f(x_0)$是极值点,$f'(x_0)$存在则$f'(x_0)=0$

</div>


<div class='pbox'>

不妨设是极大值.

$$
\begin{gathered}
f'(x_0^-)=\lim_{x \to x_0^-} \dfrac{f(x)-f(x_0)}{x-x_0} \ge 0 \\
f'(x_0^+)=\lim_{x \to x_0} \dfrac{f(x)-f(x_0)}{x-x_0} \le 0 \\
\Rightarrow f'(x_0)=f'(x_0^-)=f'(x_0^+)=0
\end{gathered}
$$

</div>

<div class='cbox'>

Rolle's Theorem

$$
\begin{gathered}
\begin{cases}
f(x) \in C[a,b] \\
x\in (a,b) \Rightarrow  \exists f'(x) \\
f(a)=f(b)
\end{cases} \\
\Rightarrow 
\exists \xi\in (a,b),f'(\xi)=0
\end{gathered}
$$

</div>

<div class='pbox'>

用连续函数最值定理,并且在$f$不是常函数由$f(a)=f(b)$显然有至少一个最值在中间取.这个最值是极值.极值处费马定理,得证.

</div>

<div class='cbox'>

Lagrange Mean Value Theorem

$$
\begin{gathered}
\begin{cases}
f(x) \in C[a,b] \\
x\in (a,b) \Rightarrow  \exists f'(x)
\end{cases} \\
\Rightarrow \exists \xi\in (a,b),f'(\xi)=\dfrac{f(a)-f(b)}{a-b}
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\text{let } F(x)=f(x)-\dfrac{f(a)-f(b)}{(a-b)} (x-a)
\end{gathered}
$$

然后直接 Rolle's Theorem.

</div>

<div class='cbox'>

Cauchy Mean Value Theorem

$$
\begin{gathered}
\begin{cases}
f(x) \in C[a,b] \\
x\in (a,b) \Rightarrow  \exists f'(x) \\
g(x)\in C[a,b] \\
x\in (a,b) \Rightarrow  \exists g'(x) \\
\forall (a',b'),x\in (a',b'),g'(x)\not \equiv 0
\end{cases} \\
\exists \xi \in (a,b),\dfrac{f'(\xi)}{g'(\xi)} =\dfrac{f(a)-f(b)}{g(a)-g(b)} 
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\text{let } F(x)=f(x)-\dfrac{f(a)-f(b)}{g(a)-g(b)} (g(x)-g(a))
\end{gathered}
$$

Rolle's Theorem 启动

</div>

#### Usage

他说你应该在研究导函数零点的时候用Rolle,研究函数和导函数关系用Lagrange,研究两个函数的时候用Cauchy

<div class='cbox'>

$$
\begin{gathered}
\lim_{x \to +\infty} f'(x)=0 \Rightarrow \lim_{x \to +\infty} \dfrac{f(x)}{x} =0
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
x>A>X \\
\Rightarrow 
\vert f(x)-f(A) \vert <\epsilon_1(x-A) \\
\Rightarrow \vert \dfrac{f(x)}{x} \vert  <\dfrac{f(A)-\epsilon_1A}{x} +\epsilon_1
\end{gathered}
$$

其实从这就能看出来了,同时取极限则 $\lim_{x \to +\infty} \vert \dfrac{f(x)}{x} \vert$小于任意正数,于是是$0$.

</div>



<div class='cbox'>

$$
\begin{gathered}
\forall a>b,\exists \xi \in (a,b),ae^b-be^a=(1-\xi)e^\xi(a-b)
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\Rightarrow \dfrac{\dfrac{e^b}{b} -\dfrac{e^a}{a} }{\dfrac{1}{b} -\dfrac{1}{a}} =(1-\xi)e^{\xi}
\end{gathered}
$$

然后柯西中值结束.

</div>


<div class='cbox'>

$$
\begin{gathered}
\exists \xi\in C[a,b],\exists f''(x) \\
\Rightarrow \exists \xi \in (a,b), \\
f(b)+f(a)-2f(\dfrac{a+b}{2})=(\dfrac{b-a}{2})^2f''(\xi)
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\text{let } F(x)=f(x)-f(x-\dfrac{b-a}{2}) \\
F(b)-F(\dfrac{a+b}{2} )=f(b)+f(a)-2f(\dfrac{a+b}{2}) \\
=\dfrac{b-a}{2} (F'(\xi_1)-F'(\xi_1-\dfrac{b-a}{2} )) \\
=(\dfrac{b-a}{2} )^2F''(\xi)
\end{gathered}
$$

</div>

我们注意到如果你上来不构造函数对$f(b)-f(mid),f(mid)-f(a)$分别用拉格朗日中值是做不出来的.这么干限制强(要求值对应相等而非差相等)显然就不如分开.

<div class='cbox'>

$$
\begin{gathered}
f(x)\in C[1,+\infty),\exists f'(x) \\
e^{-x}f'(x) \text{ is bounded in } [1,+\infty) \\
\Rightarrow e^{-x}f(x) \text{ is bounded in }  (1,+\infty)
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\dfrac{f(x_1)-f(x_2)}{e^{x_1}-e^{x_2}} =\dfrac{f'(\xi)}{e^{\xi}}\le M  \\
e^{-x}f(x)\le \dfrac{f(x)-f(1)}{e^x} +f(1) \\
\le \dfrac{f(x)-f(1)}{e^x-e^1} +f(1) \\
= \dfrac{f'(\xi)}{e^\xi}+f(1) \\
\le M+f(1) 
\end{gathered}
$$

</div>

<div class='cbox'>

$$
\begin{gathered}
f(x)\in C(0,1],\exists f'(x) \\
\exists\lim_{x \to 0^+} \sqrt xf'(x) \\
\Rightarrow f(x) \in UC(0,1] 
\end{gathered}
$$

</div>

<div class='pbox'>



</div>

## Class 14

### Darbox Theorem

<div class='cbox'>

$$
\begin{gathered}
\forall x\in [a,b], \\
\exists f'(x) \\
\Rightarrow \begin{cases}
\forall v\in [f'(a),f'(b)],\exists \xi,f'(\xi)=v \\
f'(x) \text{ has no discontinuity of first kind} 
\end{cases}
\end{gathered}
$$

</div>

<div class='pbox'>

(1)

先不妨设$f'(a)<0<f'(b)$

由定义容易说明$a,b$不是极小值.

于是存在最值定理,$(a,b)$中存在最值$x$,于是存在$f'(x)=0$

其他情况显然可以规约过来.

(2)

考虑对一个间断点$x_0$

第一类间断点所以有左右极限$L,R$,那么$\forall \epsilon\exists \delta, x \in (x_0-\delta,x_0) \Rightarrow f'(x_0)\in N(L,\epsilon)$.同理有$\forall x\in(x_0,x_0+\delta) \Rightarrow f'(x)\in N(R,\epsilon)$.

于是可以取$\epsilon$使得两个邻域不交,则这个小区间上至少越过了一个值.对$[x_0-\dfrac{\delta}{2},x_0+\dfrac{\delta}{2}]$用(1)


</div>

### 单调性

<div class='cbox'>

$$
\begin{gathered}
f(x)\in C[a,b],\forall x\in [a,b]-D,f'(x)>0 \\
D \text{ is finite set}  \\
\Rightarrow f(x) \text{ is strictly increasing at }[a,b] 
\end{gathered}
$$

</div>

<div class='pbox'>

$\forall x_1<x_2$,把$D$在$(x_1,x_2)$中的点排序得到$d_1\ldots d_k$,令$d_0=x_1,d_k=x_2$,显然有

$$
\begin{gathered}
f(x_2)-f(x_1)=\sum _{i = 1} ^{k+1}  f(d_i)-f(d_{i-1}) \\
=\sum _{i = 1} ^{k+1}  f'(\xi_i) (d_i-d_{i-1}) \\
>0
\end{gathered}
$$

每个区间都有闭区间连续开区间可导推导闭区间上中值定理.

</div>

<div class='cbox'>

$$
\begin{gathered}
p,q>1,a,b>0,\dfrac{1}{p} + \dfrac{1}{q} =1 \\
\Rightarrow \dfrac{a^p}{p} +\dfrac{b^q}{q} \ge ab
\end{gathered}
$$

</div>

<div class='pbox'>

也是求偏导啊.

然后下节课讲了凸函数之后还有个做法说的是

$$
\begin{gathered}
f(x)=\ln x,x_1=a^p,x_2=a^q
\end{gathered}
$$

用琴声.

</div>

<div class='cbox'>

$$
\begin{gathered}
ab\le \epsilon a\ln a+\dfrac{\epsilon}{e} e^{\frac{b}{\epsilon} }
\end{gathered}
$$

</div>




<div class='pbox'>

求偏导,代入结束.

$$
\begin{gathered}
f(b)=\epsilon a\ln a+\dfrac{\epsilon}{e} e^{\frac{b}{\epsilon}}-ab \\
f'(b)=e^{\frac{b}{\epsilon} -1}-a \\
a_0=e^{\frac{b_0}{\epsilon}-1} \\
f(b_0)=(b-\epsilon)e^{\frac{b}{\epsilon}-1 }+\dfrac{\epsilon}{e} e^{\frac{b}{\epsilon}}-be^{\frac{b}{\epsilon}-1} \\
=\dfrac{\epsilon}{e} e^{\frac{b}{\epsilon}}-\epsilon e^{\frac{b}{e}-1 } \\
=0
\end{gathered}
$$

</div>

这节课其实是讲单调性和导数关系的,只是看起来比较高中能记的不多.

## Class 15

### 凹凸性

定义成了

<div class='dbox'>

Convex/Concave function

$$
\begin{gathered}
f(x) \text{ is convex function} \Leftrightarrow  \\
\forall x,y\in D,\lambda \in (0,1) \\
f(\lambda x+(1-\lambda)y)\le \lambda f(x)+(1-\lambda)f(y)
\end{gathered}
$$

</div>

<div class='cbox'>

$$
\begin{gathered}
f(x) \text{ is convex} \Leftrightarrow  \\
\forall \{ x_n \} ,\{ \lambda_n \},
f(\dfrac{\sum _{i = 1} ^{n}  \lambda_ix_i}{\sum _{i = 1} ^{n}  \lambda_i} )\le \dfrac{\sum _{i = 1} ^{n}  \lambda_if(x_i)}{\sum _{i = 1} ^{n}  \lambda_i} 
\end{gathered}
$$

</div>

<div class='pbox'>

归纳显然.

</div>

<div class='cbox'>

$$
\begin{gathered}
f(x) \text{ is convex} ,\exists f'(x) \\
\Leftrightarrow f'(x) \text{ is increasing} 
\end{gathered}
$$

</div>

<div class='pbox'>

显然凸性等价于

$$
\begin{gathered}
x_1<x_2<x_3 \Rightarrow  \\
\dfrac{f(x_1)-f(x_2)}{x_1-x_2} <\dfrac{f(x_2)-f(x_3)}{x_2-x_3} 
\end{gathered}
$$

这个定理反向用拉格朗日中值是显然的.对正向:

$$
\begin{gathered}
\forall x_1<x_2 \\
f'(x_1)=\lim_{x \to x_1^-} \dfrac{f(x_1)-f(x)}{x_1-x} \le \dfrac{f(x_1)-f(x_2)}{x_1-x_2} \\
\text{same for} f'(x_2)\ge \dfrac{f(x_1)-f(x_2)}{x_1-x_2}  
\end{gathered}
$$

于是结束.

</div>

<div class='cbox'>

$$
\begin{gathered}
\sum _{i = 1} ^{n}  a_ib_i\le (\sum _{i = 1} ^{n}  a^p )^{\frac1p}(\sum _{i = 1} ^{n}  b^q)^{\frac1q}
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
(\dfrac{a_i}{(\sum _{i = 1} ^{n}  a^p)^{\frac{1}{p}}} )(\dfrac{b_i}{(\sum _{i = 1} ^{n}  b^q)^{\frac{1}{q}}} )
\le \dfrac{1}{p} \dfrac{a_i^p}{\sum _{i = 1} ^{n}  a^p}+\dfrac{1}{q} \dfrac{b_i^q}{\sum _{i = 1} ^{n}  b^q} 
\end{gathered}
$$

同时累加即证.

</div>

## Ex Class 3

<div class='cbox'>

对这样的常微分方程:

$$
\begin{gathered}
y'=\Phi(x,y) \\
y(a)=0
\end{gathered}
$$

若

$$
\begin{gathered}
\exists A,\forall y_1,y_2, \\
\vert \Phi(x,y_1)-\Phi(x,y_2) \vert \le A \vert y_1-y_2 \vert 
\end{gathered}
$$

则微分方程的解唯一.

</div>

<div class='pbox'>

假设存在两个解$y_1(x),y_2(x)$,令$g(x)=y_2(x)-y_1(x)$有

$$
\begin{gathered}
g'(x)=\vert \Phi(x,y_2)-\Phi(x,y_1) \vert \le A \vert y_2-y_1 \vert =A g(x)
\end{gathered}
$$

于是由作业[Math Analysis Homework Week5-Class1-T6](/post/math-analysis-week5-homework/)易证$g(x)=0$

</div>

<div class='dbox'>

压缩映射

$$
\begin{gathered}
f(x) \text{ is contraction } \Leftrightarrow  \\

\exists A\in (0,1),\forall x_1,x_2 \\
\vert f(x_1)-f(x_2) \vert \le A\vert x_1-x_2 \vert 
\end{gathered}
$$

</div>

<div class='cbox'>

$$
\begin{gathered}
f(x) \text{ is contraction},\{ x_n \} \ s.t.\ 
x_{n+1}=f(x_n)  \\
\Rightarrow  \lim_{n \to \infty} x_n=X\land X \text{ is the unique fixed point of }f 
\end{gathered}
$$

</div>

<div class='pbox'>

考虑任意数列 $\{ x_n \}$,则

$$
\begin{gathered}
\forall n<m \\
\vert x_m-x_n \vert =\sum _{i = n} ^{m-1} \vert x_{i+1}-x_i  \vert  \\
\le \sum _{i = 1} ^{m-1} \vert x_1-x_2 \vert A^{n+i-1} \\
\le \vert x_1-x_2 \vert \dfrac{A^n}{1-A}  \\
\to 0
\end{gathered}
$$

于是$x_n$收敛,且同时取极限能看出极限是不动点.

考虑如果由两个不动点$X_1,X_2$,那么 $\vert X_1-X_2 \vert \le A\vert f(X_1)-f(X_2) \vert=A\vert X_1-X_2 \vert$,可以得到$X_1=X_2$,得证.

</div>

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f\in C^2[a,b],f'(x)\ge \delta>0,f''(x)\in (0,M),f(X)=0 \\
x_1\in (X,b),x_{n+1}=x_n-\dfrac{f(x_n)}{f'(x_n)} 
\end{cases} \\
\Rightarrow \begin{cases}
\lim_{n \to \infty} x_n=X \\
\exists N,n>N \Rightarrow (x_n-X)\sim (x_{n-1}-X)^2
\end{cases}

\end{gathered}
$$

</div>

就是牛顿迭代

<div class='pbox'>

显然$f'(x)>0$得到$f$增.

尝试证明 $x_n>X$,即$f(x_n)>0$.



</div>



### L' Hopital

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f,g \in C^1(a,b),g'(x)\ne 0 \\
\lim_{x \to a^+} f(x)=\lim_{x \to a^+} g(x)=0
\end{cases} \\
\Rightarrow \lim_{x \to a^+} \dfrac{f(x)}{g(x)} =\lim_{x \to a^+} \dfrac{f'(x)}{g'(x)}
\end{gathered}
$$

</div>

<div class='pbox'>

不妨设$f(a)=g(a)=0$

然后你可以对一个$[a,\dfrac{a+b}{2}]$用柯西中值,有

$$
\begin{gathered}
\exists \xi\in (a,x) \\ s.t.\\ 
\dfrac{f(x)-f(a)}{g(x)-g(a)}=\dfrac{f'(\xi)}{g'(\xi)}   \\
\therefore \lim_{x \to a^+} \dfrac{f(x)}{g(x)} =\lim_{x \to a^+} \dfrac{f'(\xi)}{g'(\xi)}=\lim_{\xi \to a^+} \dfrac{f'(\xi)}{g'(\xi)} 
\end{gathered}
$$

</div>

[think] 为什么 $\lim_{x \to a^+} f(x)=\lim_{\xi \to a^+} f(\xi)$若$\xi\in (a,x)$.因为你转换到数列上,就是对任意$x$趋近到$a$的序列你可以找到一个$\xi$趋近到$a$的序列.

你还可以对无穷区间用:对$(a,+\infty)$,考虑复合 $\dfrac1x$

$$
\begin{gathered}
\lim_{x \to +\infty} \dfrac{f(x)}{g(x)}=\lim_{x \to 0} \dfrac{f(\dfrac{1}{x} )}{g(\dfrac{1}{x})} \\
=\lim_{x \to 0} \dfrac{-\dfrac{1}{x^2} f'(\dfrac{1}{x})}{-\dfrac{1}{x^2} g'(\dfrac{1}{x} )} \\
=\lim_{x \to +\infty} \dfrac{f'(x)}{g'(x)}   
\end{gathered}
$$


另外,考虑若$g,f\to \infty$,可以


$$
\begin{gathered}
\dfrac{g}{f} =\dfrac{\dfrac{1}{f} }{\dfrac{1}{g} } = \dfrac{\dfrac{f'}{f^2} }{\dfrac{g'}{g^2} }=\dfrac{g^2f'}{f^2g'}   \\
\Rightarrow \dfrac{f'}{g'} =\dfrac{f}{g} 
\end{gathered}
$$

于是也可以对 $\dfrac{\infty}{\infty}$用?但问题在于这样要求预先知道 $\dfrac{f}{g}$极限存在,所以考虑下面的结论.


<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f,g \in C^1(a,b),g'(x)\ne 0 \\
\lim_{x \to a^+} g(x)=+\infty
\end{cases} \\
\Rightarrow \lim_{x \to a^+} \dfrac{f(x)}{g(x)} =\lim_{x \to a^+} \dfrac{f'(x)}{g'(x)}
\end{gathered}
$$

</div>

<div class='pbox'>

Solution 1

你先转化成对于任意趋近到$a^+$且满足$g(x)$单调的序列$x$,然后有

$$
\begin{gathered}
\lim_{n \to \infty} \dfrac{f(x_n)}{g(x_n)} \\
\xlongequal{Stolz}\lim_{n \to \infty} \dfrac{f(x_n)-f(x_{n-1})}{g(x_n)-g(x_{n-1})} \\
=\lim_{n \to \infty} \dfrac{(x_n-x_{n-1})f'(\xi_n)}{(x_n-x_{n-1})g'(\xi_n)},\xi_n\in (x_{n-1},x_n) \\
=\lim_{n \to \infty} \dfrac{f'(\xi_n)}{g'(\xi_n)}  \\
=\lim_{x \to a^+} \dfrac{f'(x)}{g'(x)} 
\end{gathered}
$$

但是海涅要求对任意的序列$x$怎么办呢?

考虑一个数列的一个性质:若数列的任何一个子列都有一个子列趋近到$A$,则原数列也趋近到$A$,这个反证是容易的.

那么而对于你这个任意数列的任意子列,显然都能再取一个子列使得$g(x)$单调,于是得证.

Solution 2

我们现在的问题是$f(a)$没有任何信息,所以想办法取$c\in (a,a+\delta)$,然后对$x\in(a,c)$ 用 $[x,c]$ 用柯西证明

你有

$$
\begin{gathered}
\dfrac{f(x)-f(c)}{g(x)-g(c)} =\dfrac{f'(\xi)}{g'(\xi)}  \\
\Rightarrow \dfrac{f(x)}{g(x)} =\dfrac{f'(\xi)}{g'(\xi)} -\dfrac{g(c)}{g(x)} (x-c)+\dfrac{f(c)}{g(x)} 
\end{gathered}
$$

然后第二项,第三项显然趋近于$0$.

然后你同时趋向于$a$就得证了.

</div>

[think] 但是我还是喜欢第一种. 因为它一直保持着$\dfrac{f}{g}$的结构()

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f\in C^1(a,+\infty),\alpha>0 \\
\lim_{x \to +\infty} (\alpha f(x)+xf'(x))=\beta \\

\end{cases} \\
\Rightarrow \lim_{x \to +\infty} f(x)=\dfrac{\alpha}{\beta} 

\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\lim_{x \to +\infty}f(x) \\
=\lim_{x \to +\infty}\dfrac{f(x)x^\alpha}{x^\alpha}   \\
=\lim_{x \to +\infty}\dfrac{f(x)\alpha x^{\alpha-1}+f'(x)x^\alpha}{\alpha x^{\alpha-1}} \\
=\dfrac{\alpha}{\beta} 
\end{gathered}
$$

如果你好奇如何注意到,那么考虑解微分方程用的那个积分因子,对$P(x)f(x)+f'(x)$应该使用$e^{\int P(x)dx}$

</div>

## Class 16

### Taylor's Formula With Peano Reminder

<div class='cbox'>

$$
\begin{gathered}
f(x)=\sum _{i = 0} ^{n}  \dfrac{f^{(i)}(x_0)}{i!} (x-x_0)^i+o((x-x_0)^n)
\end{gathered}
$$

</div>

<div class='pbox'>

减过来变成

$$
\begin{gathered}
\dfrac{f(x)-\sum _{i = 0} ^{n}  \dfrac{f^{(i)}}{i!}(x-x_0)^i }{(x-x_0)^{n}} 
\end{gathered}
$$

然后洛$n-1$次.

</div>




<div class='cbox'>

设$f^{(k)}(x_0)\ne 0$中$k$为满足条件的最小正整数,则若$k$为奇数$x_0$不是极值点.若$k$为偶数则$x_0$是极值点.

</div>

<div class='pbox'>

$$
\begin{gathered}
\lim_{x \to x_0} \dfrac{f(x)-f(x_0)}{(x-x_0)^k} =\dfrac{f^{(k)}(x_0)}{k!} \ne 0
\end{gathered}
$$

于是邻域内 $\dfrac{f(x)-f(x_0)}{(x-x_0)^k}$和$f^{(k)}(x_0)$同号.

</div>


### Taylor's Formula With Lagrange/Cauchy Reminder

<div class='cbox'>

$$
\begin{gathered}
f(x)=\sum _{i = 0} ^{n}  \dfrac{f^{(i)}}{i!} (x-x_0)^i + \dfrac{f^{(n+1)}(\xi)}{(n+1)!} (x-x_0)^{n+1}
\end{gathered}
$$

$$
\begin{gathered}
f(x)=\sum _{i = 0} ^{n}  \dfrac{f^{(i)}}{i!} (x-x_0)^i + \dfrac{f^{(n+1)}(\xi)}{n!} (x-x_0)(x-\xi)^n
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\text{let } F(t,x)=\sum _{i = 0} ^{n}  \dfrac{f^{(i)}(t)}{i!} (x-t)^i \\
\dfrac{\delta F}{\delta t}=f'(t)+\sum _{i = 1} ^{n}  \dfrac{f^{(i+1)}(t)}{i!} (x-t)^i-\dfrac{f^{(i)}(t)}{(i-1)!} (x-t)^{i-1} \\
=\dfrac{f^{(n+1)(t)}}{n!} (x-t)^n \\
f(x)-T_n(x) \\
=F(x,x)-F(x_0,x) \\
=(x-x_0)\dfrac{\delta F}{\delta t}(\xi) \\
=\dfrac{f^{(n+1)}}{n!} (x-x_0)(x-\xi)^n  \\
\dfrac{f(x)-T_n(x)}{(x-x_0)^n} \\
=\dfrac{F(x,x)-F(x_0,x)}{(x-x_0)^n-(x_0-x_0)^n} \\
=\dfrac{\dfrac{\delta F}{\delta x} (\xi)}{n(\xi-x_0)^{n-1}}  \\
\Rightarrow f(x)-T_n(x)= \dfrac{f^{(n+1)}(\xi)}{n!} (x-x_0)(x-\xi)^n
\end{gathered}
$$

</div>

<div class='cbox'>

$$
\begin{gathered}
f\in C^2[0,1],\vert f(x) \vert \le 1,\vert f''(x) \vert \le 2 \\
\Rightarrow \vert f'(x) \vert \le 3
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
f(a)=f(x)+f'(x)(a-x)+\dfrac{f''(\xi)(a-x)^2}{2} 
\end{gathered}
$$

带入$a=1$和$0$然后解方程,把范围带进去.

</div>



<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f\in C^3[a,+\infty) \\
\exists \lim_{x \to +\infty} f(x)=A,\lim_{x \to +\infty} f'''(x)=B \\

\end{cases}
\Rightarrow  \\
\lim_{x \to +\infty} f'(x)= \lim_{x \to +\infty} f''(x)=\lim_{x \to +\infty} f'''(x)=0
\end{gathered}
$$

</div>

<div class='pbox'>

考虑展开

$$
\begin{gathered}
f(x+d)=f(x)+f'(x)d+\dfrac{f''(x)d^2}{2} +\dfrac{f'''(x+\theta d)d^3}{6}
\end{gathered}
$$

然后随便取几个固定$d=1,-1,2$,让$x$到无穷,解方程就能解出来.

这里有个点是因为你不保证导数存在你得先趋近无穷再解方程.

</div>

[think] 当我们试图拿几个数的多项式表示函数,那函数相关条件自然都变成这几个数的多项式的方程.

## Class 17

### 不定积分

<div class='dbox'>

找反导数

$$
\begin{gathered}
F(x)=\int f(x)dx \Leftrightarrow F'(x)=f(x)
\end{gathered}
$$

</div>


<div class='cbox'>

$$
\begin{gathered}
\int \sec dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=\int \dfrac{\cos x}{\cos^2 x}dx \\
=\int \dfrac{d\sin x}{(1+\sin x)(1-\sin x)}  \\
=\int \dfrac{1}{2} (\dfrac{1}{1-\sin x} +\dfrac{1}{1+\sin x} d\sin x ) \\
=\dfrac{1}{2} \ln \vert \dfrac{1+\sin x}{1-\sin x} \vert  +C \\
=\ln \vert \sec x+\tan x \vert +C
\end{gathered}
$$

</div>

### 分部积分

<div class='cbox'>

$$
\begin{gathered}
\int udv=uv-\int vdu
\end{gathered}
$$

</div>

<div class='pbox'>

求导的乘法法则,同时积分一下.

</div>





<div class='cbox'>

$$
\begin{gathered}
\int (\dfrac{1}{x} -\dfrac{1}{x^2} )e^xdx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=\int \dfrac{e^x}{x} dx+\int d(\dfrac{1}{x} )e^x \\
=\int \dfrac{e^x}{x} dx+\dfrac{e^x}{x} -\int \dfrac{e^x}{x}+C  \\
=\dfrac{e^x}{x} +C
\end{gathered}
$$

</div>

<div class='cbox'>

$$
\begin{gathered}
\int \sec^3 x dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\int \sec^3 xdx=\int \sec x d\tan x \\
=\sec x\tan x-\int \tan^2 x\sec x \\
=\sec x\tan x-\int \sec^3 xdx+\int \sec xdx \\
\Rightarrow \int \sec^3 xdx=\dfrac{1}{2} (\sec x\tan x+\int \sec x) \\=\dfrac{1}{2} (\sec x\tan x+\ln (\sec x+\tan x))+C
\end{gathered}
$$

</div>

### 换元积分

换就不好了......

<div class='cbox'>

$$
\begin{gathered}
\int \dfrac{3\sin x+\cos x}{\sin x+2\cos x} dx \\
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
3\sin x+\cos x=(\sin x+2\cos x)-(\cos x-2\sin x) \\
\int \dfrac{3\sin x+\cos x}{\sin x+2\cos x} dx \\
=x-\int \dfrac{d(\sin x+2\cos x)}{\sin x+2\cos x}  \\
=x-\ln \vert \sin x+2\cos x \vert 
\end{gathered}
$$

</div>

<div class='cbox'>

$$
\begin{gathered}
\int \dfrac{x\arctan x}{(1+x^2)^2} dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=\dfrac{1}{2} \int \dfrac{\arctan x}{(1+x^2)^2} d(x^2+1) \\
=\dfrac{1}{2} \int \arctan x d(\dfrac{1}{1+x^2}) \\ 
=\dfrac{\arctan x}{2(1+x^2)}-\dfrac{1}{2} \int \dfrac{dx}{(1+x^2)^2}   \\
\text{let } x=\tan t \\
=\dfrac{\arctan x}{2(1+x^2)}-\dfrac{1}{2} \int \dfrac{\sec^2 x}{\sec^4 x}dx \\
=\dfrac{\arctan x}{2(1+x^2)}-\dfrac{1}{2} \int \dfrac{\sec^2 x}{\sec^4 x}dx \\
=\dfrac{\arctan x}{2(1+x^2)}-\dfrac{1}{2} \dfrac{2-\sin2t}{4}
\end{gathered}
$$

然后换成$x$就行了 懒得写了.

</div>




