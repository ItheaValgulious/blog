---
title: Math Analysis Huashi Xia
tags:
  - math-analysis
  - math
  - self-study
date: 2026-03-02 14:20:17
---


# Math Analysis Huashi Xia

只挑了几点

## 函数项级数

### 不能乱交换

<div class='cbox'>

构造:求极限不保证连续性

</div>

<div class='pbox'>

$f_n=x^n$

</div>

<div class='cbox'>

求导和求极限不交换

</div>

<div class='pbox'>

第一种是我们直接让导函数发散:

$$
\begin{gathered}
f_n(x)=\dfrac{\sin nx}{\sqrt n} 
\end{gathered}
$$

第二种是构造一个不可导点,用极限把很小的弯曲区域变没:

$$
\begin{gathered}
f_n=|x|^{1+\dfrac{1}{n} }
\end{gathered}
$$

</div>

<div class='cbox'>

积分也不行

</div>

<div class='pbox'>

首先可以考虑构造不可积,比如我们选定极限是迪利克雷函数$d(x)$.于是随便取一个比如

$$
\begin{gathered}
f_n(x)=\begin{cases}
1,x=\dfrac pq,q<n \\
0,\text{otherwise}
\end{cases},x\in [0,1]
\end{gathered}
$$

然后它的间断点显然有限所以可积.

那么你自然会想如果补个可积的条件呢?

一个比较容易想到的是一个向右移动的面积为$1$的矩形:

$$
\begin{gathered}
f_n(x)=\begin{cases}
1,x\in [n,n+1] \\
0,\text{otherwise}
\end{cases}
\end{gathered}
$$

现在我们在有限区域内考虑呢?

考虑一个恒定面积,把多余的宽度累到高度上,仍然使得函数列能逐点收敛到$0$:

$$
\begin{gathered}
f_n(x)=\begin{cases}
2^n,x\in [2^{-n},2^{-n+1}] \\
0,\text{otherwise}
\end{cases},x\in (0,1]
\end{gathered}
$$

你分析发现此时不对是因为$0$处发散了,$\lim_{n \to \infty} \lim_{x\to 0} f_n(x)=+\infty$.

于是我们再加条件,如果极限函数可积且函数列一致有界:

</div>

<div class='cbox'>

函数列$f_n \to f$,$f_n,f\in R[a,b],\forall x\in [a,b],n\in Z,|f_n(x)|\le M$

则 $\lim_{n \to \infty} \int_a^b f_n(x) dx = \int_a^b f(x) dx$

</div>

<div class='pbox'>

你发现此时在勒贝格积分是显然的 控制收敛定理(甚至可以去掉黎曼可积的条件)

在黎曼积分下呢?不会做了,发现这个叫 阿泽拉有界收敛定理（Arzelà's Bounded Convergence Theorem）并找到一个初等证明:

首先简化到 $f_n:[0,1]\to [0,1],f_n\to 0,f_n\in R[0,1] \Rightarrow \int_0^1 f_n dx\to 0$.

反证,则存在$\epsilon$,使得$f_n$的一个子列(仍记为$f_n$)满足$\int_0^1 f_ndx>4\epsilon$.

根据黎曼积分定义,对每个$f_n$,可以取一个分割使得$\sum f_n(x) \Delta x>2 \epsilon$.且我们可以让每个区间的$f_n(x)$取最小值,则一定存在一些区间满足$f_n(x)>\epsilon$,且总长度大于$\epsilon$记这些区间的并为$U_n$.我们可以把端点扔了弄成开区间使得$U_n$是开集.$U_n$中的点都$f_n(x)>\epsilon$.我们其实想找一个点被包含在无限个$U_n$中.

此时经典令$V_n=\bigcup_{i>n} U_i$.我们的目标是说明$\bigcap V_n\ne \varnothing$.(这一步好像是处理被无限个包含的经典方法,仿照上下极限)

显然$V_n\supset V_{n+1}$,此时一个结论说,$R$上的任意开集$V$可以被唯一分解成至多可数个不交开区间的并,方法是考虑对任意两个点$a,b$,定义等价关系 $a\sim b \Leftrightarrow [a,b]\subset V$,则每个等价类是一个开区间,就确定了分解.

分解之后,我们定义每个开区间是一个节点,如果这个节点被上层的某个开区间包含则连边,可以得到一棵树.

此时你可以让树每层只有有限个节点(如果是可数个区间扔掉一些)并保持每层总长度大于$\dfrac \epsilon 2$,你可以扔掉没有后代的节点,因为由下层的长度保证不会扔空.

此时因为每层都有长度大于$\dfrac \epsilon 2$,所以一定存在一条无限延伸的路.现在:

如果存在一条路最终长度不趋近到$0$,那么显然是有交的(比如考虑区间中点序列的极限点一定是交里面的)

否则路最终长度趋近$0$.注意开区间不能直接用闭区间套.

考虑如果一个点在某一层至少有三个后代(不一定是儿子),那么只要我下一步走的是中间那个点,我就可以把这个开区间收缩成闭区间(因为去掉的端点被左右侧儿子挡着)

而如果这个点在后继所有点长度都维持在两个以内,又已知这两条路长度都趋近于$0$,所以它对总长度的贡献趋近于$0$.

那么形式化的,我们定义坏点是从它出发的所有路的总长度趋近于$0$,这样的点及它的所有后代都可以删了,而不影响我们能找到路的情况.

则现在树上的点都是不坏的,拿出任意一个点,要么有最终也有长度的通路,要么一定有三个后代可以收缩成闭区间.

于是你可以构造一个闭区间套解决问题.

</div>

这个先用开区间性质构造树,再用树的结构构造闭区间套感觉很厉害啊!

### Dini定理

<div class='cbox'>

若闭区间上的函数列 $f_n\to f$,$f_n\in C,f\in C,f_n<f_{n+1}$,则$f_n\rightrightarrows f$

</div>

<div class='pbox'>

因为$f_n$单增,所以$f-f_n$一定是单调减的.

所以很直觉的,对每个点$x_0$,存在$N$使得 $\forall n>N,|f_n(x_0)-f(x_0)|<\delta_0$,因为$f,f_n$连续,这个点一定有一个邻域$U$有$\forall x\in U,|f_N(x)-f_N(x_0)|<\delta_0,|f-f(x_0)<\delta_0|$于是这个邻域内$\forall n>N,|f_n(x)-f(x)| \le |f_N(x)-f(x)|\le |f_N(x)-f_N(x_0)|+|f_N(x_0)-f(x_0)|+|f(x)-f(x_0)|=3\delta_0$.

这就很显然了,叠一个有限覆盖就结束了.对开区间我们就只能内闭一致收敛.

</div>

### Weierstrass 第一逼近定理

<div class='cbox'>

$\forall f\in C[0,1],\epsilon>0,\exists \text{ polynomial }  P(x), \ s.t.\ 
\forall x,|P(x)-f(x)|< \epsilon$

</div>

<div class='pbox'>

定义

$$
\begin{gathered}
B_n(f,x)=\sum_{i=0}^n f(\dfrac i n)x^i(1-x)^{n-i} \binom ni
\end{gathered}
$$

</div>



## 多元函数微分

### 可微的条件

我们知道可微是说你可以被平面近似.

<div class='cbox'>

方向导数均存在且满足条件$\dfrac{df}{dv}=\sum_i f_{x_i} \cos(\theta_i)$不保证函数可微

</div>

<div class='pbox'>

首先如果你可微的话,这个式子是一定满足的,考虑$\cos \theta_i$实际上就是分量$v_i$:

$$
\begin{gathered}
\dfrac{df}{dv} =\lim_{k \to 0} \dfrac{f(x+kv)-f(x)}{k} =\dfrac{Akv+o(kv)}{k}=Av=\sum_i A_{i,.}v=\sum_i (\dfrac{df_i}{dx}) \cdot v_j
\end{gathered}
$$

但是这个满足不一定可微,因为方向导数说的是你看他某一条直线上的一元函数,但直线上对不能让平面上对,实际上他甚至不一定连续啊(经典 $\dfrac{x^2y}{x^4+y^2}$),如果我们让他连续,举例:

$$
\begin{gathered}
f(x,y)=\begin{cases}
0, x=y=0 \\
\dfrac{x^2y}{x^4+y^2} \cdot x,\text{otherwise}
\end{cases}

\end{gathered}
$$

这么写是因为,$\dfrac{x^2y}{x^4+y^2}$是一个常见的说明直线上连续不等于连续的例子,特点是$y=x^2$上是 $\dfrac12$,而其他地方是$0$,乘完了之后发现:

$$
\begin{gathered}
\dfrac{df}{d\vec v}= \dfrac{f(k\vec v)-f(0)}{k}=\dfrac{1}{k}=0
\end{gathered}
$$

但$f(x,x^2)=\dfrac{1}{2}x\ne o(|(x,x^2)|)$,所以不对.

</div>

<div class='cbox'>

偏导数连续则函数可微

</div>

<div class='pbox'>

假设$f(x,y)$的偏导$f_x(x,y),f_y(x,y)\in C(x_0,y_0)$,则:

$$
\begin{gathered}
f(x_0+\Delta x,y_0+\Delta y)-f(x,y) \\
=f(x_0+\Delta x,y_0+\Delta y)-f(x_0+\Delta x,y_0)+f(x_0+\Delta x,y_0)-f(x_0,y_0) \\
=f_y(x_0+\Delta x,\xi_1)\Delta y+o(\Delta y)+f_x(\xi_2,y_0)\Delta x+o(\Delta x) \\
=f_x(\xi_2,y_0)\Delta x+f_y(x_0+\Delta x,\xi_1)\Delta y+o({\sqrt{(\Delta x)^2+(\Delta y)^2}}) \\
\to f_x(x_0,y_0)\Delta x+f_y(x_0,y_0)\Delta y
\end{gathered}
$$

</div>

这里还会讲一个中值定理,但一开始看他感觉很平凡,大概说的是如果在包含$A,B$这条直线的区域上可微就有$f(A)-f(B)=\nabla f(\xi)\cdot \vec{AB}$.你考虑在这条线上的一元拉格朗日中值,然后套上方向导数那个式子.所以实际上也很平凡.

<div class='cbox'>

混合偏导中任意一个连续,且混合偏导都存在,则全都相等

</div>

<div class='pbox'>

设$f_{x,y}$连续,考虑证明$f_{x,y}=f_{y,x}$.

$$
\begin{gathered}
f_{x,y}(x,y)=\lim_{\Delta y \to 0} \lim_{\Delta x\to 0} \dfrac{1}{\Delta y} (\dfrac{f(x+\Delta x,y+\Delta y)-f(x,y+\Delta y)}{\Delta x}-\dfrac{f(x+\Delta x,y)-f(x,y)}{\Delta x} ) \\
=\lim_{\Delta y \to 0} \lim_{\Delta x\to 0} \dfrac{f(x+\Delta x,y+\Delta y)-f(x,y+\Delta y)-f(x+\Delta x,y)+f(x,y)}{\Delta x\Delta y}  \\
=\lim_{\Delta y \to 0} \lim_{\Delta x\to 0} \dfrac{1}{\Delta x} (\dfrac{f(x+\Delta x,y+\Delta y)-f(x+\Delta x,y)}{\Delta y} -\dfrac{f(x,y+\Delta y)-f(x,y)}{\Delta y} ) \\
=\lim_{\Delta y \to 0} \lim_{\Delta x\to 0} \dfrac{f_y(x+\Delta x,y+\xi_1)-f_y(x,y+\xi_2)}{\Delta x} ,(\xi_1,\xi_2\in (0,\Delta y)) \\

\end{gathered}
$$

</div>

### 隐函数定理

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f(\vec x^0,\vec u^0)=\vec 0 \\
\text{在边长为$d$的闭超立方体D中,f连续且有连续偏导} \\
\det J_{f,\vec u}((\vec x^0,\vec u^0) ) \ne 0
\end{cases} \\
\Rightarrow \begin{cases}
f(\vec x,\vec u)=\vec 0 \text{ defines the function } \vec u(\vec x) \\
\vec u(\vec x) \in C(D) \\
J_{\vec u,\vec x}(p)=J_{f,\vec u}(p)^{-1}\times J_{f,\vec x}(p) \\
\vec u \text{ has continuous partial derivative} 
\end{cases}
\end{gathered}
$$

其中$J_{a,b}(p)$表示$p$处函数$a$对$b$的 Jaccob Matrix.
要求$u$和$f$的维数相同.

</div>

<div class='pbox'>

这里有两个思路:

一是基于单调性和降维归纳的做法:

我们先考虑最简单的情况:$u,x$是一维,$f:R^2\to R$.

此时由于$x^0$处$\dfrac {df}{du}\ne 0$,不妨设$\dfrac {df}{du}>0$,则由连续性在$x$的小邻域内都有$\dfrac {df}{du}>0$,只看这个小邻域,$f$关于$u$单调.可以找到$\delta$使得$f(x^0,u^0+\delta)>\epsilon,f(x^0,u^0-\delta)<-\epsilon$.又由连续性,又能找到$\delta_1$使得$\forall x\in [x^0-\delta_1,x^0+\delta_1],f(x,u^0+\delta)>\dfrac \epsilon 2>0,f(x,u^0-\delta)<-\dfrac \epsilon2<0$.从而$\forall x\in[x^0-\delta_1,x^0+\delta_1]$,在$u$上使用介值定理都存在唯一一个$u_1$使得$f(x,u_1)=0$.

上面走了一个 $(x^0,u^0)\to (x^0,u^0\pm \delta) \to ([x^0-\delta_1,x^0+\delta_1],u^0\pm \delta)$的过程,完成了对函数和导数局部性质的应用.

对于连续性只需要再跑一遍上面这个流程:对刚才那个范围内的任意一点$(x,u)$,对任意足够小的$\epsilon$,考虑它也处在单调范围内,所以可以找$(x,u\pm \epsilon)$的函数值异号,然后分别用连续性拓展到$x$上的一段,用介值定理说明存在$x^1\in N(x,\delta),|f(x^1)-f(x)|<\epsilon$.

对于导函数,考虑对这个范围内的一点$(x^1,u^1)$,和它邻域内趋近$(x^1,u^1)$的一点$(x,u)$,则由拉格朗日中值:

$$
\begin{gathered}
f(x^1,u^1)=f(x,u)=0 \\
\Rightarrow \exists \xi \ s.t.\ 
\dfrac{df}{dx}(x^1-x)+\dfrac{df}{du}(u^1-u)=0 \\
\Rightarrow \dfrac{u^1-u}{x^1-x}=-\dfrac{\dfrac{df}{dx}(\xi) }{\dfrac{df}{du}(\xi) }  \\
\Rightarrow u'(x)=-\dfrac{\dfrac{df}{dx} }{\dfrac{df}{du} } (x,u)
\end{gathered}
$$

从而可导且连续

然后开始拓展:首先你注意到$\vec x$维度的拓展是容易的:证存在性和连续性的部分只是从原来的$([x^0-\delta_1,x^0+\delta_1],u)$这个区域改写成$(N(\vec x^0),\vec u)$,其实是一样的.而导函数的部分现在是对每维固定住其他的分别走这个流程,也是完全一样的.

要拓展$\vec u$的维度是比较复杂的:$\vec u$的维度和$f$的维度(也就是方程的个数)是对应的,现在你需要处理多个方程.考虑雅可比矩阵行列式不为$0$的意思是,这个地方线性化替代是成立的.所以直接仿照线性化的过程:应用一维的情况,把$\vec u$的第一分量$u_1$看成因变量,其他的看成自变量,用一维的隐函数定理,可以得到$u_1$关于其他所有变量的隐函数,然后用$f(u_1(\ldots),\ldots)$代替原来的$f$就能把维度减$1$.

于是,因为雅可比矩阵不全为$0$一定可以找到一个变量$u_i$满足$\dfrac{f_1}{u_i}\ne 0$,对$f_1,u_i$使用结论,对新函数$f'=f(u_i(\vec u,\vec x),\vec u,\vec x)$求导得到:

$$
\begin{gathered}
\dfrac{df'_j}{du_k}=\dfrac{df_j}{du_i}\dfrac{du_i}{du_k}+\dfrac{df_j}{du_k}   
\end{gathered}
$$

所以矩阵的变化是删掉第一行第$i$列,然后每列加上原来第$i$列的某系数倍,一定仍然满秩.且验证其他条件也均是符合的,可以归纳下去.可以拿到所有的存在性,连续性,连续导数性质.

而要得到求导公式,考虑链式法则:

$$
\begin{gathered}
J_{f,\vec u} J_{\vec u,\vec x}=J_{f,\vec x}
\end{gathered}
$$

然后移过去就完了.

至高Gemini表示另一个做法是使用Banach不动点定理:即压缩映射一定有不动点,内容在250915-math-analysis里面.

所以可以构造压缩映射$\phi(\vec x,\vec u)=\vec u-J_{f,\vec u}(\vec u)^{-1}f(\vec x,\vec u)$,则有:

$$
\begin{gathered}
J_{\phi,\vec u}(\vec u^1)=I-J_{f,\vec u}(\vec u^0)^{-1}J_{f,\vec u}(\vec u^1)
\end{gathered}
$$

则$\vec u^1=\vec u^0$时是全$0$,则由偏导的连续性,存在一个小邻域使得矩阵的模($\sup \dfrac{|A\vec u|}{|\vec u|}$)不超过$\dfrac{1}{2}<1$,于是在这个邻域内是压缩映射.则在这个范围内任意$\vec x$都会由不动点也就是方程的解.

对于连续性,注意不到

$$
\begin{gathered}
|\vec u(\vec x)-\vec u(\vec x^1)|=|\phi(\vec x,\vec u(\vec x))-\phi(\vec x^1,\vec u(\vec x^1))| \\
\le |\phi(\vec x,\vec u(\vec x))-\phi(\vec x,\vec u(\vec x^1))|+|\phi(\vec x,\vec u(\vec x^1))-\phi(\vec x^1,\vec u(\vec x^1))| \\
\le \dfrac{1}{2}|\vec u(\vec x)-\vec u(\vec x^1)|+|\phi(\vec x,\vec u(\vec x^1))-\phi(\vec x^1,\vec u(\vec x^1))|
\end{gathered}
$$

最后一步是压缩映射的性质.最后移项取极限即可得到连续性.

对于可微性,可以对每个分量用中值定理,用思路一做.

总之很麻烦啊!

</div>

## 重积分

### 面积定义

<div class='dbox'>

对于一个平面点集$T$,对它任意进行划分格子,然后定义格子的集合$A$为被完全包含的格子的集合,$B$为与点集有交的格子的集合,$C$为$B-A$.对每个集合内部的格子的面积累加得到$S(A),S(B),S(C)$,则$T$为可求面积的当且仅当$\lim S(C)=0$,定义其面积为$S(A)=S(B)$.

</div>

我们应该给他起个黎曼测度之类的名字的,因为这个可求面积确实只是在这种情况下的定义.

区别在于 黎曼测度只允许你用有限个格子逼近,而勒贝格测度允许你用可数个格子逼近

### Peano曲线

<div class='cbox'>

构造一个线到一个面的区域的连续满映射.

</div>

<div class='pbox'>

peano curve是一类曲线而不是一个.

书上的种类看起来比wikipeida上更容易证明:构造说的是,对于一个等边三角形,连接它的中心和两个顶点构造一条折线,这样联通了它的两个顶点.

现在把一个边长为$1$的定边三角形,取所有边的中点,并过它们做平行于三条边的所有的直线,可以把三角形分成四个小的,定义这个操作为一次分割.

定义曲线$c_n$为进行了$n$次分割后得到$4^n$个三角形,在每个三角形内部进行一次连接,使得最后连出一个经过全部$4^n$个小三角形的曲线.$f_n$为$[0,1]$到这条曲线上长度比例位置点的映射.

现在要证明这个构造是连续且都映射上的.

观察这个递归结构你会发现对任意$m\le n$和$t\in [0,1]$,可以找到边长为$\dfrac 1{2^m}$的三角形同时包含$f_m(t),f_n(t)$,所以$|f_m(t)-f_n(t)|\le \dfrac 1{2^m}$,一致收敛,连续.

要证明满,只需注意对三角形内任意一点,到$c_n$这条线的最短距离一定小于边长$\dfrac 1 {2^n}$,又有$|f_n-f|<\epsilon$,所以可以取$n$拿到$f$像上任意近的点.也就是说三角形内的点都是$f$的像集的聚点.又因为连续映射把紧集映射成紧集,所以$f([0,1])$是闭集,包含它的所有聚点.

</div>

### 变量代换

<div class='cbox'>

$U$是$R^n$上的开集,$D$是其中边界分段光滑的区域,则

$$
\begin{gathered}
\begin{cases}
f(x)\in C(D) \\
g(x) \text{ is a bijection on } D \\
g(x)\in C^1(D)
\end{cases} \\
\Rightarrow \iint_{D} f(g(x))d\Sigma=\iint_{g(D)}f(x)d\Sigma

\end{gathered}
$$

</div>

<div class='pbox'>

<div class='dbox'>

本源映射

若$f(x)$与$x$最多只有一维分量不同,则$f(x)$是本源映射.

</div>

<div class='cbox'>

若$g$是本源映射,则一个小超立方体区域$D_1=\times_{i=1}^n [a_i,b_i]$有


$$
\begin{gathered}
m g(D_1)=\det J_{g,x}(x_0) m(D_1),x_0\in D_1
\end{gathered}
$$

</div>

<div class='pbox'>

因为$g$是双射,我们可以说它$\det J$不为$0$.我们让它在这个小区域内$J$不变号.

考虑$g$的$J$是什么,假设它只改变第$k$维,那么$J$删掉第$k$行/列一定是$I_{n-1}$,而第$k$行是$\dfrac{dg_n}{dx_i}$,第$k$列其他地方都是$0$,而行列式就直接是$\dfrac{dg_n}{dx_n}$.所以它也不为$0$,函数关于第$k$维单调.

不妨设$g$在这一维是单调增,设$D_1$去掉第$k$维的$n-1$维区域是 $D_1'$.考虑:

$$
\begin{gathered}
mg(D_1)=\int_{a_n}^{b_n}\ldots\int_{a_1}^{b_1} (1dx_1\ldots dx_n) \\
=\int\ldots \int(\int_{g(x_1,\ldots,x_{k-1},a_k,x_{k+1},\ldots,x_n)}^{x_1,\ldots,x_{k-1},b_k,x_{k+1},\ldots,x_n}1dx_k)(dx_1\ldots dx_{k-1}dx_{k+1}\ldots dx_n) \\
=(\prod_{i\ne k}(b_i-a_i))(g(x_1,\ldots ,x_{k-1},b_k,x_{k+1},\ldots,x_n)-g(x_1,\ldots,x_{k-1},a_k,x_{k+1},\ldots,x_n)) \\
=\prod_i (b_i-a_i) \dfrac {dg}{dx_k} (x_1,\ldots ,x_{k-1},\xi,x_{k+1},\ldots,x_n),\xi \in [a_k,b_k] \\
=\dfrac {dg}{dx_k} (x_1,\ldots ,x_{k-1},\xi,x_{k+1},\ldots,x_n) mg(D_1) \\
\end{gathered}
$$

</div>

<div class='cbox'>

若$g$是本源映射,则原命题成立

</div>

<div class='pbox'>

我们证明的是小立方体,所以自然要考虑重积分的定义把区域切成小立方体和一些边界的不规则图形,记这些小区域的集合为$\{D_n\}$.

假设现在所有小区域中,那些是小立方体的标号集合是$A$(对应了内部),剩下的小区域的标号集合是$B$.

用定义拆开:

$$
\begin{gathered}
\left(\int\ldots\int\right)_{D}f(g(\vec x))d\Sigma \\
=\lim_{\|T\| \to 0} \sum_{i\in A} f(\xi_i)mg(D_i) + \sum_{i\in B} f(\xi_i)mg(D_i),\xi_i\in g(D_i) \\
\end{gathered}
$$

对第一部分可以直接刚刚证明的结论,因为我们可以保证结论中$x_0$在原来的格子里.但第二部分可能会有$x_0$落在$D$区域外面,但边界很小,所以可以特殊处理:

$$
\begin{gathered}
=\lim_{\|T\| \to 0} \sum_A f(\xi_i) mg(D_i) + \sum_C f(\xi_i) mg(D_i)  \\
+ (\sum_{C} f(\xi_i) mD_i-\sum_{C}f(\xi_i)mg(D_i)) \\
=\lim_{\|T\| \to 0} \sum_A f(\xi_i) m(D_i)|J_{g,x}(\xi_i')| + \sum_C f(\xi_i) m(D_i)|J_{g,x}(\xi_i')|  \\
+ (\sum_{C} f(\xi_i) mD_i-\sum_{C}f(\xi_i)mg(D_i)) \\
\end{gathered}
$$

注意$\xi_i$是$g(D_i)$中的点,而我们可以选取$\xi_i=g(\xi_i')$,则就会变成

$$
\begin{gathered}
=\left(\int\ldots\int\right)_{g(D)}f\cdot J_{g,x} d\Sigma+ \lim_{\|T\| \to 0} (\sum_{C} f(\xi_i) mD_i-\sum_{C}f(\xi_i)mg(D_i))
\end{gathered}
$$

注意到因为$f$有界,$g$的雅可比矩阵因为连续所以有界,设有共同的界$M$,所以后面这个括号的东西有:

$$
\begin{gathered}
|\sum_{C} f(\xi_i) mD_i-\sum_{C}f(\xi_i)mg(D_i)| \\
\le M\sum_C m(D_i)+M^2\sum_C m(D_i)
\end{gathered}
$$

而显然$\sum_C m(D_i)$是趋近于$0$的,所以这部分最后极限是$0$.

于是证毕.

</div>

还可以容易的用Fubini说明对分量置换(仅改变$x_i$分量顺序的变换)是成立的.

<div class='cbox'>

$g\in C^1(D)$在$x$的邻域上可以被分解为有限个本源映射和分量置换映射的复


</div>

<div class='pbox'>

考虑因为雅可比矩阵可逆,可以进行置换使得$\dfrac{dg_n}{dx_n}\ne 0$,于是在小邻域内构造

$$
\begin{gathered}
h(x_1,\ldots,x_n)=(x_1,\ldots,x_{n-1},g_n(x_1,\ldots,x_n))
\end{gathered}
$$

则由反函数定理,这个家伙的雅可比矩阵行列式是$\dfrac{dg_n}{dx_n}\ne 0$,存在反函数$h^{-1}$.而且$h^{-1}$也是只改变$x_n$的本源映射).

显然$g\circ h^{-1}\circ h=g$,但$h$过后$x_n$的分量就已经是$g(x_n)$的值了,所以$g\circ h^{-1}$是不改变$x_n$的变换.

考虑这意味着你可以对$g$再进行置换,考虑如果$g_i$是不改变其中$i$个分量的变换,那么把一个会改变的扔到$x_n$,得到$h_i$,然后因为$x_n\circ h_i^{-1}\circ h_i$,一定是不改变$i+1$个元素的,这样你不断重复就能拆完了.

</div>

现在的问题是对本源映射的分解也都是小区域,所以考虑进行切分:对$U$中的每个点可以找一个开集邻域,再找到一个$D$的有限覆盖.设有限覆盖中开集的最小半径是$\delta$.

那么再去划分网格,当网格中区域的直径最大值小于$\dfrac\delta 2$时,一定每个格都完全被一个邻域完全包含,可以用这个邻域对应的分解套用刚才的证明.最后就证明完了.

</div>

### 可积与绝对可积


## 场论相关

<div class='cbox'>

Green Formula

$$
\begin{gathered}
\begin{cases}
F: R^2 \to R^2 \\
D \text{ is 光滑或分段光滑的简单闭曲线所围的单连通闭区域} \\ 
F\in C^1(D) \\
\end{cases} \\
\Rightarrow \iint_D \nabla \times \vec F =\oint F\cdot dl
\end{gathered}
$$

Gauss Formula

$$
\begin{gathered}
\begin{cases}
F: R^3 \to R \\

\end{cases}

\end{gathered}
$$

</div>


## 微分形式


## 两类欧拉积分


## 傅里叶级数
