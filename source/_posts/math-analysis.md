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

$\lim_{n \to \infty} n^{\frac{1}{n} }=1$


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
\begin{array}{c}
{\left \vert a_nb_n-AB \right \vert} = \\
{\left \vert a_nb_n-a_nB+a_nB-AB \right \vert} \\ \\
\le {\left \vert a_N \right \vert} {\left \vert b_n-B \right \vert} +{\left \vert B \right \vert} {\left \vert a_n-A \right \vert} \\
\end{array}
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
\begin{array}{c}
{\left \vert \frac{1}{b_n}-\frac{1}{B}  \right \vert}<\epsilon \\
\Leftarrow {\left \vert B-b_n \right \vert} <\epsilon b_nB \\
\Leftarrow \epsilon'=\frac{\epsilon}{BM+114514} (\vert M\vert>b_n)
\end{array}
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
\begin{array}{c}
\lim_{n \to \infty} \dfrac{\sum_i a_ib_{n-i}}{n} \\
\le \lim_{n \to \infty} M\dfrac{b_{n-i}}{n} =0
\end{array}
$$

$b\ne 0$,$b'_i=b_i-b$,有

$$
\begin{array}{c}
\lim_{n \to \infty} \frac{\sum_i a_ib_{n-i}}{n} =\lim_{n \to \infty} \frac{\sum_i a_ib'_{n-i}}{n} +\frac{\sum_i a_i}{n} b=0+ab
\end{array}
$$

$$
\begin{array}{c}

\end{array}
$$

#### Solution 2

不妨设$a,b>0$,则有界性可以得到后面是$a_n,b_n>0$

考虑影响值的肯定是中间的项,所以直接拆,取$\epsilon$,对$a,b$可以得到$N_1$

$$
\begin{array}{c}
\lim_{n \to \infty} \dfrac{\sum_i a_ib_{n-i}}{n}= \\
=\lim_{n \to \infty} \dfrac{\sum _{i = 1} ^{N_1} a_ib_{n-i}+\sum _{i = 1} ^{N_1} b_ia_{n-i}+\sum _{i = N_1+1} ^{n-N_1-1} a_ib_{n-i} }{n}  \\
=\lim_{n \to \infty} \dfrac{\sum _{i = 1} ^{N_1} a_ib_{n-i}}{n} \\
+ \lim_{n \to \infty} \dfrac{\sum _{i = 1} ^{N_1} b_ia_{n-i}}{n} \\
+\lim_{n \to \infty} \dfrac{\sum _{i = N_1+1} ^{n-N_1-1} a_ib_{n-i}}{n} \\
\in (\lim_{n \to \infty} \dfrac{n-2N_1-1}{n} (a-\epsilon)(b-\epsilon) \\
,\lim_{n \to \infty} \dfrac{n-2N_1-1}{n} (a+\epsilon)(b+\epsilon)) \\
= ((a-\epsilon)(b-\epsilon),(a+\epsilon)(b+\epsilon))
\end{array}
$$

后面显然.`

</div>

## Class 4

### eg1

<div class='cbox'>

$$
\begin{array}{c}
a>1,k\in N^*,\lim_{n \to \infty} \frac{n^k}{a^n} =0
\end{array}
$$

</div>

<div class='pbox'>

$a^n=(1+b)^n$展开会出现$n$的任意次方,然后显然.

</div>

### Stolz

<div class='cbox'>

$$
\begin{array}{c}
\left. \begin{array}{ll}
y_n \uparrow,\lim_{n \to \infty} y_n=\infty \\
\lim_{n \to \infty} \dfrac{x_n-x_{n-1}}{y_n-y_{n-1}} =a\in[-\infty,+\infty]
\end{array} \right\}
 \\
\Rightarrow \lim_{n \to \infty} \dfrac{x_n}{y_n} =a
\end{array}
$$

</div>



<div class='pbox'>

先简化,不妨设$a\ge 0,\frac{\Delta x_n}{\Delta y_n}>0$

然后可以证$a=0$时,你取$\epsilon_1$得$N_1$,变成 $\dfrac{\Delta x_n}{\Delta y_n} <\epsilon$.于是

$$
\begin{array}{c}
\dfrac{x_n}{y_n}  \\
=\dfrac{x_{N_1}+\sum _{i = N_1+1} ^{n}  \Delta x_i}{y_{N_1}+\sum _{i = N_1+1} ^{n}  \Delta y_i}  \\
\le \dfrac{x_{N_1}+\epsilon\sum _{i = N_1+1} ^{n}  \Delta y_i}{y_{N_1}+\sum _{i = N_1+1} ^{n}  \Delta y_i}  \\
\le \dfrac{x_{N_1}+\epsilon\sum _{i = N_1+1} ^{n}  \Delta y_i}{\sum _{i = N_1+1} ^{n}  \Delta y_i}
\end{array}
$$

因为你  $Y=\sum _{i = N_1+1} ^{n} \Delta y_i \to +\infty$,所以一定可以有$\epsilon Y>x_{N_1}$.就能证$<2\epsilon$,你再取一下$\epsilon$就得证了.

然后我说$0<a\in R$时你直接$x'=x-ay$就用结论,$a=+\infty$的时候你取倒数用结论,就做完了. 

</div>

## Class 5

### 单调有界数列有极限

<div class='cbox'>

$$
\begin{array}{c}
\left. \begin{array}{ll}
a_i>a_{i-1} \\
a_i<M
\end{array} \right\}
\Rightarrow 
\lim_{n \to \infty} a_i \text{ exists} 
\end{array}
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
\begin{array}{c}
a_n:=\lim_{n \to \infty} (1+\dfrac{1}{n} )^n = b_n:=\lim_{n \to \infty} \sum _{i = 0} ^{n}  \dfrac{1}{i!}
\end{array}
$$

</div>

<div class='pbox'>

右边那个单调有界都是好证的.证相等:

$$
\begin{array}{c}
a_n=(1+\dfrac{1}{n} )^n=\sum _{i = 0} ^{n}  \dfrac{1}{n^i} \binom{n}{i} \\
=\sum _{i = 0} ^{n}  \dfrac{1}{i!} \prod_{j=0}^{i-1} (1-\dfrac{j}{n} )
<b_n \\
\end{array}
$$

又有

$$
\begin{array}{c}
k<n \Rightarrow 
a_n=\sum _{i = 0} ^{n}  \dfrac{1}{i!} \prod_{j=0}^{i-1} (1-\dfrac{j}{n} )
>\sum _{i = 0} ^{k}  \dfrac{1}{i!} \prod_{j=0}^{i-1} (1-\dfrac{j}{n} )
\end{array}
$$
于是先令$k\to \infty$得到$a_n>b_k$,则$a$逐项大于$b$的一个子列,最后得证.

</div>

重点是把一次到极限拆成两个取极限.但这个为什么对呢.

是好证的,其实就是

<div class='bbox'>

[think] 

$$
\begin{array}{c}
\lim_{a \to \infty} \lim_{b \to \infty} f(a,b) = X
\Rightarrow \lim_{n \to \infty} f(n,n) = X
\end{array}
$$

用定义是显然的.且如果极限都存在(要$f(a,n)$和$f(n,b)$极限存在)的话你还可以看出左式两取极限交换(都是右式)

</div>

<div class='cbox'>

$$
\begin{array}{c}
0<e-\sum _{i = 0} ^{n}  \dfrac{1}{i!} < \dfrac{1}{n\cdot n!} 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{c}
b_n:=\sum _{i = 0} ^{n}  \dfrac{1}{i!} \\
X=b_{n+m}-b_n=\sum _{i = n+1} ^{n+m}  \dfrac{1}{i!}  \\
<\dfrac{1}{(n+1)!} \sum _{i = 0} ^{m-1}  \dfrac{1}{(n+1)^i}<\dfrac{1}{n!\cdot n}   \\ \Rightarrow e-b_n= \lim_{m \to \infty} X<\dfrac{1}{n!\cdot n} 
\end{array}
$$

然后说为什么取极限小于号还是小于号呢?

$$
\begin{array}{c}
X=b_{n+m}-b_n<b_{n+m+k}-b_n<\dfrac{1}{n!\cdot n} 
\\
\stackrel{\lim_{k \to \infty} }{\Longrightarrow}
e-b_n<\dfrac{1}{n!\cdot n} 
\end{array}
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
\begin{array}{c}
\dfrac{p}{q} -b_n<\dfrac{1}{n\cdot n!} 
\stackrel{n=q}{\Longrightarrow}
p(q-1)!-b_q q!<\dfrac{1}{q} 
\end{array}
$$

左边是不为$0$的整数(为$0$与$b$增矛盾),右边是分数

</div>

[think] 一个无理数等价于存在一列分母到无穷的有理数始终有更高阶(相比序列中分母)的余项.

<div class='cbox'>

$$
\begin{array}{c}
(1+\dfrac{1}{n} )^n \uparrow \\
(1+\dfrac{1}{n} )^{n+1} \downarrow
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{c}
(1+\dfrac{1}{n} )^n\cdot 1< (\dfrac{n\cdot (1+\dfrac{1}{n}+1 )}{n+1} )^{n+1}=(1+\dfrac{1}{n+1} )^{n+1}
\end{array}
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
\begin{array}{c}
\forall \epsilon, \exists N \\ s.t.\\ 
\forall n,m>N, \vert a_n-a_m\vert<\epsilon
\Leftrightarrow \lim_{n \to \infty} a_n \text{ exists} 
\end{array}
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
\begin{array}{c}
S=\{ (x,y) \vert x<y \},T\subset S , \cup_{I\in T} I \supset [a,b] \\
\Rightarrow \exists A \in T,\cup_{I\in A} I \supset [a,b],\vert A\vert\in N(\text{not infinity} ) 
\end{array}
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
\begin{array}{c}
\lim_{x \to x_0} f(x) = A  \\
\Leftrightarrow \forall \epsilon, \exists \delta,\\ s.t.\\ 
\forall x, \vert x-x_0 \vert \in (0,\delta), \vert f(x)-A \vert <\epsilon
\end{array}
$$

</div>

<div class='cbox'>

Heine Theorem

$$
\begin{array}{c}
\lim_{x \to x_0} f(x)=A \\
\Leftrightarrow \forall \{ x_n \} ,\lim_{n \to \infty} x_n  = x_0 \\
\lim_{n \to \infty} f(x_n) = A
\end{array}
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
\begin{array}{c}
\lim_{x \to x_0} \text{ exists} \Leftrightarrow \forall \epsilon, \exists \delta,\forall x_1,x_2 \in N^*(x_0,\delta),\vert f(x_1)-f(x_2) \vert < \epsilon
\end{array}
$$

</div>

<div class='pbox'>

正向是显然的.

反向的话你可以用上面Heine转化成数列,则你只需要证所有这样的数列极限相等.

然后你发现你直接取任意两个数列,然后插(奇数偶数项分别放两个数列的元素)就可以直接证明这两个数列极限相等.于是结束.

</div>

<div class='cbox'>

$$
\begin{array}{c}
\left. \begin{array}{ll}
\lim_{x \to x_0} f(x) = A \\
\lim_{t \to t_0} g(t) = x_0 \\
\exists \eta>0, t\in N(t_0,\eta) \Rightarrow g(t)\ne 0
\end{array} \right\} \\
\Rightarrow \lim_{t \to t_0} f(g(t)) = A
\end{array}
$$

</div>

<div class='pbox'>

直接翻译成$\epsilon-\delta$是显然的.

</div>

<div class='cbox'>

$$
\begin{array}{c}
\lim_{ \to _0} \dfrac{\sin(x)}{x} = 1
\end{array}
$$

</div>

<div class='pbox'>

todo

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
\begin{array}{c}
\forall x>0,n\in N^*,\exists! y {\ } s.t. {\ } y^n=x
\end{array}
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
\begin{array}{c}
r=\dfrac{m}{n} =\dfrac{p}{q} \Rightarrow a=(x^m)^{\frac1n}=(x^p)^{\frac1q}=b
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{c}
a^{nq}=x^{nrq},b^{nq}=x^{nrq} \\
\Rightarrow  a^{nq}=b^{nq} \\
\Rightarrow a=b
\end{array}
$$

</div>

下一个目标是实数!

定义$a^x,x\in R$是所有$a^q,q\in Q,q\le x$的上确界就行了吧!

那么你是不是得说说实数这个满足和刚才一样的运算律,也就是:

<div class='cbox'>

$$
\begin{array}{c}
a^xa^y=a^{x+y} \\
(a^x)^y=a^{xy}
\end{array}
$$

</div>

<div class='pbox'>

然后他下课不讲了

todo

</div> 


</div>










## Class Unknown

### Continuous function's maximum/minimum

<div class='cbox'>

$$
\begin{cases}
x\in [a,b],f(x)<M \\
\forall M'<M,\exists x \ s.t.\  f(x)>M'\\ 
\text{f is continuous}
\end{cases}
\Rightarrow \exists x, f(x)=M
$$

</div>

<div class='pbox'>

考虑取任意$M_1<M$,可以得到一个$f(x_1)\in (M_1,M)$,取$M_n>f(x_{n-1})$可得$x_n \in (M_n,M)$,显然$x_n$有界可以取收敛子列$y_n$,则$\lim_{n \to \infty} f(y_n)=f(\lim_{n \to \infty} y_n)$,则于是得证 

</div>

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

不妨设$f(a)\le y \le f(b)$,$=$情况显然,只考虑$f(a)<y<f(b)$.

取 $A=\{ x\vert f(x)<y \}$ 则它有上确界$x_1$.

那么一定存在一个收敛到$x_1$的数列 $\{ z_n \}$ 你就直接发现 $\lim_{n \to \infty}  f(z_n) = f(\lim_{n \to \infty} z_n)$

$\text{Q.E.D}$ 

</div>

### About Periodicty

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
\begin{array}{c}
T:= \{ t \vert t>0,f(x+t)=f(x) \}  \\
t_0:= \min T \\
\end{array}
$$

若$t_0\ne 0$,取 $\{ t_n \},t_i\in T,\lim_{n \to \infty} t_n=t_0$,则 $f(x)=f(x+t_n)=\lim_{n \to \infty} f(x+t_n)=f(x+\lim_{n \to \infty} t_n)=f(x+t_0)$

若$t_0=0$,因为不是常函数, 则$\exists x_0 {\ } s.t. {\ }  f(x_0)\ne f(0)$,因为连续,和极限有保号性你可以说$\forall x\in O(x_0,\delta),f(x)\ne f(0)$,但由$t_0=0$,你可以找到$t<\delta$,那就可以再找到$N$使得$Nt\in (x_0-\delta,x_0+\delta)$,$Nt$一定是周期,但$f(0+Nt)\ne f(0)$,矛盾.

于是得证.

</div>
