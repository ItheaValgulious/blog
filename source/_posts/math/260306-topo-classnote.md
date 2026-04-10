---
title: Topo Basic Note
tags:
  - math
  - topo
  - note
date: 2026-03-06 11:02:06
---

# Topo Basic Note

## 基本概念

### 拓扑与拓扑基与邻域

拓扑就是在一个集合上定义哪些是开集,同时满足对有限交,无限并的封闭性.

于是闭集公里说的是你也可以定义哪些是闭集满足对有限并和无限交的封闭性

邻域有的定义为包含一个点的开集,有的定义为包含一个点的开集的超集,就是是否允许非开集邻域.

<div class='cbox'>

开集等价条件

一个集合是开集等价于其中所有点都有被这个集合包含的邻域

</div>

<div class='pbox'>

左推右显然,右推左就把所有邻域并起来说明相互包含.

</div>

<div class='cbox'>

$U$是$\beta$生成开集的条件

$\beta$是集合$X$上的拓扑基,$U\subset X$是$\beta$生成的拓扑中的开集等价于$\forall x\in U,\exists B_x\in \beta,s.t.\ x\in B_x\subset U$

</div>

<div class='pbox'>

左推右:$U$是一些$B_x$的并,所以$x\in U$一定有$x$属于某个$B_x$.

右推左:把所有$B_x$并起来.

</div>

<div class='cbox'>

生成相同拓扑的充分条件

对拓扑$(X,T)$中的一个开集族$A$,若对$X$中任意开集$U$,$\forall x\in U$,都有$\exists V_x\in A,x\in V_x\subset U$,则$A$是一个拓扑基,且生成的恰好是$(X,T)$

</div>

<div class='pbox'>

验证:显然对所有的$x$你可以找到一个$V$包含他,显然任意两个$V_1,V_2\in A,V_1\subset V_2$是开集可以找到$x\in (V_1\cap V_2)\in A$,是拓扑基.

显然你用开集不可能生成不是开集的东西,显然所有开集都有$U=\bigcup_{x\in U}V_x$,就行了.

</div>

<div class='cbox'>

拓扑基的判定

$B$是拓扑基当且仅当:
- 并集是全集.
- $B$中任意两个集合的交在$B$中或为空.

</div>

<div class='pbox'>

显然

</div>

### 内部,外部

<div class='dbox'>

$$
\begin{gathered}
\operatorname{Int} A = \bigcup_{U\subset A,U \text{ is open}} U \\
\operatorname{Cl} A=\bigcap_{F\supset A,F \text{ is close}} F
\end{gathered}
$$

</div>

感觉内部外部的运算基本是符合直觉的.

<div class='cbox'>

属于闭包的条件

$$
\begin{gathered}
x\in \operatorname{Cl}A \\
\Leftrightarrow \forall x\in U,U \text{ is open} \Leftrightarrow  U\cap A\ne \varnothing
\end{gathered}
$$

</div>

<div class='pbox'>

存在$U$为开集包含$x$且与$A$不交,等价于$(X-U)\supset A$, $\operatorname{Cl}A\subset X-U$,等价于$x$不在闭包中.所以反过来逆否命题也成立.

</div>

这个实际在说,闭包就是不能用一个开集把它和$A$分开的点.

同理可以得到 $x \in \operatorname{Int}A$当且仅当$x$的任意邻域和$X-A$不交.

### 极限,导集

<div class='dbox'>

集合$A$的聚点/极限点:点$x$的任意**去心**邻域都与$A$有交,则$x$是$A$的聚点.

导集:$A$的所有聚点组成的集合$A'$.

点列极限:若对数列$x_n$和点$p$,对 $p$ 的任意邻域总存在$N$使得$n>N$时$x_n$全部落在$U$中则$x_n$的极限是$p$.

</div>

需要注意的是极限点和点列的关系问题:
- 点列不一定只有一个极限点:证明极限点唯一一般是要用到可分性的吧.比如平凡拓扑中任意点列都有任意点当极限点.
- 极限点不一定有点列趋近:比如$R$上可数补拓扑中$R-\{0\}$集合不存在集合趋向$0$:对任意点列,你总可以用一个可数补拓扑把这个数列中后面的所有项都删掉让它落不进去.

<div class='cbox'>

$$
\begin{gathered}
\operatorname{Cl}A=A\cup A'
\end{gathered}
$$

</div>

<div class='pbox'>

用刚才关于点属于闭包的性质: $x\in \operatorname{Cl}A$等价于$x$的任意邻域里有$A$中的点,而$A'$是任意去心邻域里有$A$中的点,则并上$A$就一样了,很显然吧.

</div>

### 子空间

<div class='dbox'>

若$(X,T)$是一个拓扑,若$A\subset X$,定义 $(A,\{ S\cap A|S\in T \})$ 是$A$上的拓扑.

</div>

容易验证它确实是个拓扑.且若$A$是开/闭的,则子集的开/闭集在外面也是开/闭集.

<div class='cbox'>

原空间$(X,T)$的一组基$B$,对子空间$A$交后得到的也是子空间的一组基

</div>

<div class='pbox'>

我们用上面那个判定拓扑基的条件,对于子空间的每个开集$V\cap A,\forall x\in V$,存在$x\in B_i\subset V$,于是$\forall x\in V\cap A\forall x x\exists B_i\in (B_i\cap A)\subset (V\cap A)$,即证.

</div>`

### 连续,同胚

<div class='dbox'>

连续映射:对任意$f(x)$的邻域$U$,存在$x$的邻域$V$使得$f(V)\subset U$则称$f$在点$x$连续. 

同胚:若$f:A\to B$连续且为双射,则$f$是同胚,$A,B$是同胚的.

</div>

<div class='cbox'>

连续的充要条件是把开集拉回开集,即 $U\text{ is open} \Rightarrow   f^{-1}(U) \text{ is open}$

</div>

<div class='pbox'>

必要性:只要对$U$中每个点$x$使用定义得到$x\in f(V_x)\subset U$,说明$f^{-1}(U)=\bigcup_x V_x$即可.

充分性:直接令$V=f^{-1}(U)$

</div>

那么也等价于把闭集拉回闭集.

也可以容易的说明连续函数复合仍然连续.

<div class='cbox'>

若 $\lim_{n \to \infty} x_n=x$,则 $\lim_{n \to \infty} f(x_n)=f(x)$

</div>

<div class='pbox'>

拆定义,则对任意$f(x)$的邻域,$f^{-1}(f(x))$是$x$的邻域,$x_n$只有有限项在这外面,则$f(x_n)$只有有限项在$f(x)$的任意邻域外面,就行了

</div>

书上还有一条性质是,连续映射满足 $x\in \operatorname{Cl}A$则$f(x)\in \operatorname{Cl}f(A)$.也是直接用定义就能证.

<div class='cbox'>

焊接引理

如果$A,B\subset X$是$X$的闭子空间,$X=A\cup B$,有$f:A\to Y$,$g:B\to Y$,且$f,g$分别连续,$f=g$在$A\cap B$成立,

则

$$
\begin{gathered}
h(x):X\to Y=\begin{cases}
f(x),x\in A \\
g(x),x\in B
\end{cases}
\end{gathered}
$$

是连续映射

</div>

<div class='pbox'>

几乎是显然的:$h$把$Y$中的闭集拉回$A,B$中的闭集,而**因为$A,B$是闭子空间,$A,B$中的闭集也是$X$中的闭集**,然后再并起来也是闭集,于是得证.

</div>


todo:同胚保持边界 

### 乘积拓扑

<div class='dbox'>

乘积空间

对拓扑空间$(X,T)$和$(Y,S)$,其乘积空间$X\times Y$上的拓扑是由所有形如$U\times V$的集合生成的,其中$U\in T,V\in S$.

</div>

那么这个定义合法需要:

<div class='cbox'>

$B=\{U\times V| U\in T,V\in S\}$构成一组拓扑基

</div>

<div class='pbox'>

首先因为$X\times Y\in B$,所以显然全覆盖了.

只要验证$B$中任意两个集合的交,容易发现$(U_1\times V_1)\cap (U_2\times V_2)=(U_1\cap U_2)\times (V_1\cap V_2)$,于是任意两个的交也在$B$中,得证.

</div>

<div class='cbox'>

拓扑基的乘积是乘积空集的拓扑基

</div>

<div class='pbox'>

设$(X,T)$的拓扑基为$B_X$,$(Y,S)$的拓扑基为$B_Y$,令$B=\{U\times V| U\in B_X,V\in B_Y\}$.仍然验证两条拓扑基判定:你发现第一条显然,第二条和上个定理一样显然,得证.

</div>

<div class='cbox'>

对$X,Y$各自相同的子空间$A\subset X,B\subset Y$,$A\times B$的乘积拓扑与$A\times B$作为$X\times Y$的子空间诱导的拓扑相同

</div>

<div class='pbox'>

子空间的拓扑基是拓扑基中的集合直接对应到子空间,所以由子空间诱导的拓扑的基是

$$
\begin{gathered}
\{(U\times V)\cap (A\times B)| U\in T,V\in S\}
\end{gathered}
$$

而乘积拓扑的基是

$$
\begin{gathered}
\{(U\cap A)\times (V\cap B)| U\in T,V\in S\}
\end{gathered}
$$

于是直接相等.

</div>

### 可分性

<div class='dbox'>

$T_1$可分:对任意两个不同的点$x,y$,存在邻域$x\in U,y\in V$满足$y\notin U,y\notin V$.

$T_2$可分:对任意两个不同的点$x,y$,存在邻域$x\in U,y\in V$满足$U\cap V=\varnothing$.

$T_3$可分:对任意点$x$和闭集$F$满足$x\notin F$,存在邻域$x\in U,F\subset V$满足$U\cap V=\varnothing$.

$T_4$可分:对任意两个不交的闭集$F_1,F_2$,存在邻域$F_1\subset U_1,F_2\subset U_2$满足$U_1\cap U_2=\varnothing$.

</div>

<div class='cbox'>

$T_2$可分对子空间

若$(X,T)$是$T_2$,则$X$的任意子空间也是$T_2$.

</div>

<div class='pbox'>

显然.把你用$X$的$T_2$找到的和子空间交一下就好了.

</div>

<div class='cbox'>

$T_2$可分的两个空间乘积也是$T_2$可分的.

</div>

<div class='pbox'>

同样显然.把你用$X,Y$的$T_2$找到的对应相乘即可.

</div>

<div class='cbox'>

度量空间是T4可分的

</div>

<div class='pbox'>

todo

</div>



### 开映射,闭映射

<div class='dbox'>

把开/闭集映到开/闭集的映射称为开/闭映射

</div>

<div class='cbox'>

$$
\begin{gathered}
p:X\times Y\to X,(x,y)\mapsto x
\end{gathered}
$$

是开映射

</div>

<div class='pbox'>

显然,考虑$U\subset X\times Y$是开集,那么拆分到拓扑基知$U=\bigcup_a (U_a\times V_a)$,于是$p(U)=\bigcup_a U_a$是开的.

</div>

## 后面的内容

后来的课上觉得不喜欢边听边记...

## 20260409

<div class='dbox'>

局部紧

空间是局部紧当且仅当对任意点都存在一个紧集包含它的开邻域.

</div>

<div class='cbox'>

一点紧致化

若$(X,T)$是T2空间,令$Y=X\cup \{\infty\},T'=T\cup \{Y-C | C \text{ is compact in X}\}$.



</div>

<div class='pbox'>

$(Y,T')$是拓扑空间:简单集合运算(紧集在这做任意交,有限并都是紧的,且T2保证紧集是闭集).容易验证.

$(Y,T')$在$X$上诱导的子拓扑是一样的:T2空间中紧集是闭集,所以$Y-C$都是开集,而显然$T'$也没有比$X$多什么开集.

$(Y,T')$是紧的:对一个$Y$的开覆盖,你包含了$\infty$的那个开集一定是一个$Y-C$,所以剩下的是一个$X$的紧集.那么它的开覆盖一定有限覆盖就完事了.

如果$X$是局部紧则$Y$是T2:任意两个$X$中的点都是原来就能分开的,只要证明和$\infty$能分开,而你写出来发现这恰好就说的局部紧的定义.

如果$X$不是紧的,则$\overline{X}=Y$:转成找 $\operatorname{Int}\{ \infty \}$,而因为$X$不紧所以这个点不是开集,于是只能是空集.

</div>

