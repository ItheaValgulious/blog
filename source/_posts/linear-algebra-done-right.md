---
title: Linear Algebra Done Right
tags:
  - math
  - linear-algebra
  - note
  - self-study
date: 2025-10-13 17:49:57
---


# Linear Algebra Done Right

记录大致讲了什么

### 向量空间

我们定义向量空间

<div class='dbox'>

向量空间

向量空间定义在域$F$上,要求支持:
- 加法
- $F$中数的数乘
- **加法单位元(0元)**
- 加法逆元
- 加法交换结合
- 数乘结合
- 加法对数乘分配
- **对加法和数乘封闭**

</div>

加粗部分用于判断子空间,根据$F$区分是否是实向量空间/复向量空间

<div class='dbox'>

子空间

就是子集且是向量空间的对吧

</div>

判定可以看上面

#### 维数

向量空间还应该有维数.于是定义

<div class='dbox'>

线性无关组

$$
\text{Group}  v_1\ldots v_n \in V \text{is linear independet} \Leftrightarrow  \\
\forall \{ c_n \} ,c_i \in F, \\
\sum _{i = 1} ^{n}  c_iv_i = 0 \Leftrightarrow \forall i,c_i=0 
$$

</div>

<div class='dbox'>

张成,张成组

$$
\begin{array}{l}
\operatorname{span}( v_1 \ldots v_n ) = \{ \sum _{i = 1} ^{n}  c_iv_i \} 
\end{array}
$$

张成$V$的组简称张成组

</div>

<div class='dbox'>

基

基=张成组 且 线性无关组

</div>



则按照直觉的,维数应该是张成组长度的最小值,线性无关组长度的最大值,基的长度等等,**下面讨论的是有限维线性空间**.

<div class='cbox'>

- $\dim V$是张成组最小长度
- $\dim V$是线性无关组组最大长度
- $\dim V$是任意一组基的长度

</div>

<div class='pbox'>

首先说明,对一个线性相关的组,我们一定可以去掉一个线性相关项保持张成空间不变(显然).

首先说明 

<div class='cbox'>

任意一组线性无关组长度小于等于任意一组张成组长度:

</div>

<div class='pbox'>

##### Sol1

考虑一个线性无关组和一个张成组,将一个线性无关组的元素加入张成组,则形成的一定是线性相关组,删去一个**张成组中的**元素则保持张成,不断重复这个操作,注意因为被加入的线性无关,所以你想相关一定得带张成组中的,于是可以一直操作.

直到线性无关组全部被加入,则因为每次删掉一个张成组元素,你一定有线性无关组长度不大于它.

##### Sol2

另一个是更常见的证法吧,就是直接用张成组去表示线性无关组的每个向量,列方程线性无关组的某个线性组合和为$0$.

然后发现你列出的方程个数(张成组长度)若小于未知数个数(线性无关组长度),那么必有非零解,就证毕.

</div>

<div class='cbox'>

线性无关组可通过加元素扩展到基,张成组可通过删除元素到基

</div>

<div class='pbox'>

对线性无关组,每次加入一个不属于张成空间的,由于组的长度大小不断增加,而存在一个长度的基,所以你的过程会停止.

同理对张成组每次删掉一个线性相关项不影响张成空间.

</div>

<div class='cbox'>

每组基的长度都相当,具有恰当长度的线性无关组/张成组是基.

</div>

<div class='pbox'>

第一句用小于等于关系,后面两个通过基的长度相等+上一条可以变成基说明.

</div>

<div class='dbox'>

维数

维数就是这个长度为 $\dim V$

</div>

</div>

#### 空间的运算

<div class='dbox'>

空间的和

$$
\begin{array}{l}
U+V = \{ u+v \vert u\in U,v\in V \} 
\end{array}
$$

</div>

加法实际上是并(包含子空间所有向量的最小空间).

并定义直和.

<div class='dbox'>

空间直和

$$
\begin{array}{l}
W = U\oplus V = U + V \\ s.t.\\ 
\forall w \in W, \exists! u\in U,v\in V, u+v=w
\end{array}
$$

</div>

直和相当于不交并,是对空间进行一种分解.

然后直和的判定容易证明只要$0$的表示满足唯一性,并推出当且仅当它们的交只有$0$

<div class='dbox'>

空间的积

就是笛卡尔积.

$$
\begin{array}{l}
U\times V=\{ (u,v) \vert u\in U,v\in V \} 
\end{array}
$$

</div>

其实也可以先扩展一下直和 是等价的.

<div class='dbox'>

仿射空间

$$
\begin{array}{l}
u+V=\{ u+v \vert u+V \}  \\
(u+V)+(w+V)=(u+w) + V \\
\lambda (u+V) = \lambda u + V
\end{array}
$$

</div>

注意如果$u\in V$则不变,$u\not\in V$则是一个没有$0$的空间,在此空间的线性组合变成了$\sum _{i = 0} ^{n}  c_iv_i\ s.t.\ \sum_{i=0}^n c_i=1$.

然后仿射空间关于以上运算是线性空间,其中$0=V$

<div class='dbox'>

空间的商

$$
\begin{array}{l}
U/V={\left\{ u+V \vert u\in U \right\}} 
\end{array}
$$

</div>

可以理解成等价类分类.如果两个向量的差在$V$中则认为他们等价.新的空间中每个元素都是一个等价类.而你仿射空间的变换也可以看成是对代表元做变换.

最后考虑它们的维数,有:

<div class='cbox'>

$$
\begin{array}{l}
\dim U\times V=\dim U\oplus V=\dim U+\dim V \\
\dim U+V = \dim U+\dim V-\dim U\cap V \\
\dim U/V=\dim U-\dim V
\end{array}
$$

</div>

<div class='pbox'>

第一行是显然的.

第二行考虑取$U\cup V$的一组基,再其中添加上$U-V$的基和$V-U$的基.

第三行需要线性映射.

</div>

### 线性映射

#### 线性映射基本性质

<div class='dbox'>

线性映射

线性映射是映射满足:
- 齐性: $\lambda v=\lambda Tv$
- 加性: $T(u+v)=Tu+Tv$

</div>

<div class='dbox'>

线性变换的运算

$$
\begin{array}{l}
(S+T)u=Su+Tu \\
(\lambda T)u=\lambda (Tu) \\
(ST)u=S(T(u))
\end{array}
$$

</div>

符合直觉的.于是你可以说明$\mathcal{L}(U,V)$(由$T:U\to V$组成的集合)是 $\dim U\times \dim V$维的线性空间,他的标准基可以是所有把$U$的一个基映到$V$的一个基的映射.


<div class='dbox'>

值域,零空间

$$
\begin{array}{l}
\text{for linear map } T:U\to V \\
\operatorname{range} T = \{ v \vert v=Tu,u\in U \}  \\
\operatorname{null} T = \{ u \vert Tu=0,u \in U \} 
\end{array}
$$

</div>


<div class='cbox'>

$$
\begin{array}{l}
\dim U=\dim \operatorname{null} T+\dim \operatorname{range} T
\end{array}
$$

</div>

<div class='pbox'>

考虑  $\operatorname{null} T$  的基$u_1\ldots u_n$,并添加$v_1\ldots v_m$扩充到$U$的基.

考虑$Tv_1\ldots Tv_m$若线性相关,$\sum _{i = 1} ^{m}  c_iTv_i=0 \Rightarrow T\sum _{i = 1} ^{m}  c_iv_i=0$,则 $w=\sum _{i = 1} ^{m}  c_iv_i\in \operatorname{null} T,w=\sum _{i = 1} ^{m}  c_iv_i=\sum _{i = 1} ^{n}  d_iu_i$,与$u_i,v_i$构成一组基矛盾.

于是$Tv_i$线性无关,且容易注意到任意$w\in U,Tw=\sum_{i=1}^n c_iTu_i+\sum_{i=1}^m d_iTv_i=\sum_{i=1}^md_iTv_i\in \operatorname{span} (Tv_1\ldots TV_m)$故得证.

</div>


<div class='dbox'>

单射,满射,双射,可逆

- 单射:$Tx\ne Ty \Rightarrow x\ne y$
- 满射: $\forall v\in V,\exists u\in U, Tu=v$ 
- 双射就是同时有两条
- 对于双射$T$的定义$T^{-1}$满足$TT^{-1}=T^{-1}T=I$

</div>

<div class='cbox'>

基本性质

1. 单射等价于只把$0$映射到$0$.
2. 存在$U\to V$单射说明 $\dim U\le \dim V$.
3. $U\to V$有单射说明$V\to U$有满射.
4. $U \to V$存在双射称为$U,V$同构,可以证明任意向量空间同构于某个$F^n$.

</div>

<div class='pbox'>

都挺显然的.

</div>

<div class='cbox'>

$$
\begin{array}{l}
\dim  U/V=\dim U-\dim V
\end{array}
$$

</div>

<div class='pbox'>

定义 $T\in \mathcal{L}( U , U/V )$ 为商变换,把$u$映射到$u+V$.

则

$$
\begin{array}{l}
\operatorname{null} T=V \\
\operatorname{range} T=U/V 
\end{array}
$$

套用上面值域和零空间的维数公式即可.

</div>

#### 线性映射的矩阵

<div class='dbox'>

矩阵

选取$U,V$分别一组基$u_1\ldots u_m$,$v_1\ldots v_n$,可以把线性变换$T$写成$n\times m$的矩阵$\mathcal{M}(T,u_1\ldots u_m,v_1\ldots v_n)=A_{n\times m}$满足

$$
\begin{array}{l}
Tu_i=\sum_{j=1}^n A_{j,i}v_j
\end{array}
$$

</div>

即每一列是一个基向量在像空间中的基的表示.然后有的时候也直接简写$\mathcal M(T)$.

矩阵可以这么定义因为线性变换的线性保证了你可以只用基的变换去描述它,同时基的这种变换也能唯一确定线性变换.

于是可以定义矩阵运算:

<div class='dbox'>


$$
\begin{array}{l}
\mathcal M( S ) \mathcal M( T ) = \mathcal M( ST ) \\
\mathcal M( S ) + \mathcal M( T ) = \mathcal M( ST ) \\
\mathcal \lambda\mathcal M( T ) = \mathcal M( \lambda T )
\end{array}
$$

</div>



其中第一行矩阵乘法用坐标写一下可以推出经典的矩阵乘法方式.


#### 算子,不变子空间,商算子和限制算子

这些概念会在本征值那里用到 但从属性上讲和这里线性映射关系更大.

<div class='dbox'>

算子

$$
\begin{array}{l}
T\in \mathcal L( V , V ) 
\end{array}
$$

即映射到自身空间的线性变换.

</div>

<div class='dbox'>

不变子空间

即对算子$T$,有$\forall u\in U, Tu\in U$,则$U$为不变子空间.

</div>

<div class='dbox'>

商算子,限制算子

$$
\begin{array}{l}
T_{/U}\in \mathcal L( V/U , V/U ),(T_{/U})(v+U)=(Tv+U) \\
T\vert_U \in \mathcal L( U , U ), T\vert_U v=Tv
\end{array}
$$

</div>

显然$T\vert_U$要求了$U$是不变子空间.

把算子放到更小的空间去研究的方式.

<div class='cbox'>

$$
\begin{array}{l}
p(x)\in \mathcal{P}  \\
\Rightarrow 
\operatorname{range} p(T),\operatorname{null} p(T)\text{ is invariant for } T
\end{array}
$$

</div>

$$
\begin{array}{l}
u\in \operatorname{range} p(T) \\
\Rightarrow \exists v,p(T)v=u \\
Tu=Tp(T)v=p(T)Tv\in \operatorname{range} p(T) \\
u\in \operatorname{null} p(T) \\
\Rightarrow p(T)u=0 \\
p(T)Tu=Tp(T)u=T0=0
\end{array}
$$


### 对偶

<div class='dbox'>

线性泛函,对偶空间

线性泛函就是$f \in \mathcal L( V , F )$,所有这样的$f$组成线线性空间$V'$是$V$的对偶空间.

</div>

线性泛函可以看成是向量/点的对偶.线性泛函 $\{ \varphi \vert \varphi_i e_j=[i=j] \}$构成对偶空间的基.

<div class='dbox'>

对偶映射

若 $T\in\mathcal L( U , V )$ ,定义 $T'\in \mathcal L( V' , U' )$ 满足

$$
\begin{array}{l}
\forall f \in V',T'f=fT
\end{array}
$$

</div>

$T'$是反的可以理解因为$V'$的泛函的输入才是$T$的输出.导致没法根据这几个东西定义一个正的出来.

然后对偶主要解释了:$\mathcal M( T' ) =\mathcal M( T )^{T}$(右上角的$T$是转置的意思).

<div class='cbox'>

对偶映射的运算
$$
\begin{array}{l}
(ST)'=T'S' \\
(S+T)'=S'+T' \\
(\lambda S)'=\lambda S'
\end{array}
$$
</div>

<div class='pbox'>

$$
\begin{array}{l}
(ST)'f=fST=T'(fS)=T'(S'f) \\
(S+T)'f=f(S+T)=fS+fT=S'f+T'f \\
(\lambda S)'f=f\lambda S=\lambda fS=S'f \\
\end{array}
$$

</div>

<div class='dbox'>

零化子

对线性空间$V$来说,子空间$U$的零化子 $U^0=\{ f \vert f\in V',\forall u\in U,fu=0 \}$.

</div>

注意$U^0$同时依赖$U$和$V$.

<div class='cbox'>

$$
\begin{array}{l}
\dim U+\dim U^0=\dim V
\end{array}
$$

</div>

<div class='pbox'>

取$U$的基$u_1\ldots u_n$扩充到$V$的基$u_1\ldots u_n,u_{n+1}\ldots u_{n+m}$.并取$V'$的标准基$\varphi_i u_j =[i=j]$,则显然$f\in U^0$要求$f$不能有$\varphi_i,i<n$的分量,而任意$i>n$的分量都可以有.于是得证.

</div>

<div class='cbox'>

$$
\begin{array}{l}

\operatorname{null} T'=(\operatorname{range} T)^0 \\

\operatorname{range} T'=(\operatorname{null} T)^0

\end{array}
$$

</div>

<div class='pbox'>

考虑$T'fu=fTu=0$关于所有$u$成立,则$f$的范围是什么.看右侧显然是 $(\operatorname{range} T)^0$ 看左侧则是 $(\operatorname{null} T')^0$.于是得证.

对第二行,左边是任意$T'g=gT$,右边说你这个线性泛函把所有$Tu=0$的映到$0$,恰好是左边的$gT$满足条件.于是得证.

</div>

然后还有一个问题是我们以为$T''=T$,但实际上你甚至不能保证$V$和$V''$是相同的.然后有个典范同构的概念形容他俩的关系就是存在一种不依赖于基的选取的同构(只要定义$T(u)f=fu$,则$u$到$T(u)$是双射.)

### 本征值基础

#### 本征值

<div class='dbox'>

本征值,本征向量

若对算子$T$,$\exists v\ne 0\in V,\lambda\in F\ s.t.\ Tv=\lambda v$,则$\lambda,v$分别为本征值,本征向量.

</div>

就是说算子在这个方向上对变换只有伸缩.

一个本征值可能对应多个线性不相关的本征向量,它们构成本征空间$E(\lambda,T)$

<div class='cbox'>

$\lambda$ 是 $T$的本征值等价于 $T-\lambda I$不是双射,或不是单射/满射

</div>

<div class='pbox'>

首先注意到对算子来说 单射,满射双射等价

又因为单射等价于 $\operatorname{null} T=0$ 所以 $(T-\lambda I)v=0$ 和它不是单射等价.

</div>

<div class='cbox'>

不同本征值对应对本征向量线性不相关.

</div>

<div class='pbox'>

反证,你要利用不同本征值这个性质,于是你设 $v_n \in \operatorname{span}( v_1\ldots v_{n-1} )$ 且$n$为满足条件对最小的.

$$
\begin{array}{l}
v_n=\sum _{i = 1} ^{n-1} c_iv_i \\
Tv_n=\sum _{i = 1} ^{n-1}  Tc_iv_i \\
\lambda_n (\sum _{i = 1} ^{n-1}  c_iv_i)=\sum _{i = 1} ^{n-1}  \lambda_i c_iv_i \\
0=\sum _{i = 1} ^{n-1} (\lambda_i-\lambda_n) c_iv_i
\end{array}
$$

因为$n$是最小的,所以$v_1\ldots v_{n-1}$线性无关,然后你就推出矛盾.

</div>

有此容易说明本征值个数不大于线性空间维数.

<div class='cbox'>

复向量空间中的线性映射一定有本征值

</div>

<div class='pbox'>


考虑

$$
\begin{array}{l}
v\in V,\dim V=n \\
v,Tv,T^2v\ldots T^{n}V \text{ is dependent} \\
\sum _{i = 0} ^{n} c_iT^iv  =0 \\
\stackrel{\text{代数基本定理}}{\Longrightarrow}
(\prod _{i = 1} ^{n} (T-\lambda_i I))v=0
\Rightarrow \exists i,T-\lambda_i I=0 \\
\Rightarrow \lambda_i \text{is a eigenvalue of } T \\
\end{array}
$$

</div>



#### 上三角矩阵

按照上面基的理解,有

<div class='cbox'>

$$
\begin{array}{l}
\mathcal M( T,u_1\ldots u_n ) \text{is upper triangular matrix} \\
\Leftrightarrow \forall i, Tu_i\in \operatorname{span}( u_1\ldots u_i )  \\
\Leftrightarrow \forall i, \operatorname{span}( u_1\ldots u_i ) \text{is invariant space} 
\end{array}
$$

</div>

<div class='pbox'>

感觉是显然的.

</div>

那么考虑什么样的线性映射$T$有一组基$u_1\ldots u_n$有上三角矩阵$A_{n\times n}$.

<div class='cbox'>

$$
\begin{array}{l}
\forall T\in \mathcal L( V , V ), V \text{ is complex vector space} \\
\Rightarrow \exists u_1\ldots u_n,\mathcal M( T,u_1\ldots u_n ) \text{ is upper triangular matrix}
\end{array}
$$

</div>

<div class='pbox'>

Proof 1

归纳,假设对任意维数小于$\dim V$的空间成立,考虑取$T$的任意本征值$\lambda$,则 $U:=\operatorname{range} T-\lambda I$,则因为$T$不是单的所以 $\dim U<\dim V$.且 $\forall u \in U,Tu=(T-\lambda I)u+\lambda u\in U$,所以$T$在$U$不变.

于是可以应用归纳结假设,$T\vert_U$在$U$上有一组基$u_1\ldots u_n$使得 $\mathcal M( T\vert_U,u_1\ldots u_n )$ 是上三角矩阵.

将这组基扩展到$V$上成为$u_1\ldots u_n,v_1\ldots v_m$,则对$\forall i$,$Tv_i=(T-\lambda I)v_i+\lambda v_i\in \operatorname{span}( u_1\ldots u_n ) +\operatorname{span}( v_i )\subset \operatorname{span}( u_1\ldots u_n,v_1\ldots v_i )$,于是是上三角矩阵.

</div>

<div class='pbox'>

Proof 2

同样归纳,取任意本征向量 $u,U:=\operatorname{span}( u )$,考虑$T_{/U}$是维数为  $\dim V-1$ 的空间$V/U$上算子.则它有上三角矩阵.于是存在$v_1+U\ldots v_n+U$,使得 $\forall v+U\in V/U,T_{/U}(v+U)\in \operatorname{span}( v_1+U,\ldots,v_n+U )$,也就有$Tv\in \operatorname{span}( v_1,\ldots,v_n )$.

然后现在把$v_1\ldots v_n,u$作为新的基,容易发现 $Tu=\lambda u\in \operatorname{span}( v_1,\ldots,v_n,u )$满足条件.于是存在上三角矩阵.

</div>

都要从维度归纳,第二个自然一点吧:商空间就是抹去若干维度.

[think] 但是第一个从$T-\lambda I$的值域出发是什么个意思?主要利用两个性质:是不变子空间,以及$Tv=(T-\lambda I)v+\lambda v$.是不是相当于把其他向量也拆的"像"本征向量了.


<div class='cbox'>

$T$有逆等价于$T$的上三角矩阵对角线全部非$0$

</div>

<div class='pbox'>

先假设矩阵有逆,设空间$V$基为$v_1\ldots v_n$.

$$
\begin{array}{l}
Tv_1=A_{1,1}v_1 \Rightarrow A_{1,1}\ne 0 \\
Tv_k=u+A_{k,k}v_k,u\in \operatorname{span}( v_1\ldots v_{k-1} ) \\
\text{if } A_{k,k}= 0 \\
Tv_k\in \operatorname{span}( v_1\ldots v_{k-1} ) \\
\because v_1\ldots v_{k-1} \text{ is independent
}  \\
\therefore Tv_1\ldots Tv_{k-1} \text{ is independent, so it is a base}  \\
\therefore Tv_k \in \operatorname{span}( Tv_1\ldots Tv_{k-1} ) \\
\exists c \ s.t.\ 
\sum _{i = 1} ^{k}  c_iTv_i=0 \\
\stackrel{T^{-1}}{\Longrightarrow}\sum _{i = 1} ^{k}  c_iv_i=0 \\
\text{contradiction!} 
\end{array}
$$

再假设$T$关于$V$的基$v_1\ldots v_n$的矩阵为上三角矩阵且对角线元素非$0$.

那么我们知道$Tv_i=A_{i,i}v_i+\sum_{j=1}^{i-1}c_jTv_{j-1}$,其中后一项属于 $\operatorname{span}( v_1\ldots v_{i-1} )$,于是容易发现$Tv_1\ldots Tv_n$线性独立,是一组基,于是$T$是满的,于是$T$可逆.


</div>


<div class='cbox'>

$T$的某个基下的上三角矩阵对角线元素是$T$的本征值.

</div>

<div class='pbox'>

考虑$(T-\lambda I)v=0$,则$\lambda$是本征值等价于$T-\lambda I$不是单的,也就不是可逆的,即用上面条件对角线存在$0$,即$\lambda$等于对角线上的某个元素.

</div>

#### 对角矩阵

<div class='dbox'>

本征空间

$$
\begin{array}{l}
E(\lambda,T)=\operatorname{null} T-\lambda I
\end{array}
$$

</div>

<div class='cbox'>

$T$在基$v_1\ldots v_n$下为对角矩阵等价于
- $v_1\ldots v_n$是$T$的$n$个本征向量.
- $\oplus_i E(\lambda_i,T)=V$
- 存在$n$个一维不变子空间直和为$V$

</div>

<div class='pbox'>

这个感觉也是显然的.

</div>

### 内积空间

#### 内积

<div class='dbox'>

内积

二元函数<x,y>:($V,V\to F$)满足:
- 正性: $<v,v>\ge 0$
- 定性: $<v,v>=0 \Leftrightarrow v=0$
- 第二个位置的线性:$<u,v>$关于$v$是线性的
- 共轭对称性:$<u,v>=\overline{<v,u>}$ 

</div>

<div class='cbox'>

- 内积$<u,v>$关于$u$也是线性的.
- $<u,0>=<0,u>=0$

</div>

<div class='pbox'>

第一条用共轭对称性换到后面再换回来:
$$
\begin{array}{l}
a<u_1,v>+b<u_2,v>=a \overline{ <v,u_1> } +b \overline{ <v,u_2> }  \\
=\overline{ <v,au_1+bu_2> }  \\
=<au_1+bu_2,v>
\end{array}
$$

第二条考虑线性映射$0$映到$0$.

</div>

<div class='dbox'>

范数

$\vert\vert v \vert\vert = \sqrt{<v,v>}$定义为向量的范数.

</div>

<div class='cbox'>

也可以用范数定义内积.

</div>

<div class='pbox'>

对实向量空间:

$$
\begin{array}{l}
<u,v>=\dfrac{\vert\vert u+v \vert\vert ^2-\vert\vert u-v \vert\vert ^2}{4} 
\end{array}
$$

对复向量空间:

$$
\begin{array}{l}
<u,v>=\dfrac{\vert\vert u+v \vert\vert ^2-\vert\vert u-v \vert\vert ^2}{4} + \dfrac{\vert\vert u+iv \vert\vert ^2-\vert\vert u-iv \vert\vert ^2}{4}i
\end{array}
$$

拆开验算显然是对的.

</div>





<div class='dbox'>

正交

$u\perp v \Leftrightarrow <u,v>=0$

</div>

<div class='dbox'>

正交分解

$\forall u,v,v=\dfrac{u}{\vert\vert u \vert\vert^2 } <u,v>+(v-\dfrac{u}{\vert\vert u \vert\vert^2 } <u,v>)$

</div>

<div class='cbox'>

$<u,v> {\ } \le {\ } \vert\vert u \vert\vert \vert\vert v \vert\vert$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\text{let} w=\dfrac{u}{\vert\vert u \vert\vert^2 }<u,v>\\

v=w+(v-w),w\perp v-w \\
\Rightarrow v^2=w^2+(v-w)^2\le w^2=\dfrac{<u,v>^2}{\vert\vert u \vert\vert ^2} 
\end{array}
$$

</div>

#### 正交基

<div class='dbox'>

正交基,规范正交基.

正交基是两两正交的基.规范正交基就是两两正交且范数均为$1$的基.

</div>

<div class='cbox'>
格拉姆施密特过程

任意给定一组基$u_1\ldots u_n$,可以构造规范正交基$e_1\ldots e_n$.

</div>

<div class='pbox'>

$$
\begin{array}{l}
v_i=u_i-\sum_{j=1}^{i-1}<u_i,e_j>e_j \\
e_i=\dfrac{v_i}{\vert\vert v_i \vert\vert } 
\end{array}
$$

</div>

其实构造是很好想的,就是对于前$i-1$个正交基的空间,把第$i$个去掉所有和某个基方向相同的分量,剩下的就是新的正交方向.

<div class='cbox'>

若$T$关于$V$上一组基$v_1\ldots v_n$由上三角矩阵,则$T$关于$V$上一组规范正交基有上三角矩阵.

任意复向量空间上算子关于某个规范正交基有上三角矩阵.

</div>

<div class='pbox'>

考虑刚才的构建过程里,每个 $\operatorname{span}( u_1\ldots u_i )$都没有改变,所以是显然的.

而第二条可以由 复向量空间上算子关于某基有上三角矩阵 和 第一条显然推出.

</div>

单列第二条是因为它叫 舒尔定理.

<div class='cbox'>

里斯表示定理

对任意线性泛函$f$存在$u$使得$fv=<u,v>$

</div>

<div class='pbox'>

设$e_1\ldots e_n$是一组规范正交基,则

$$
\begin{array}{l}
fv=f\sum _{i = 1} ^{n}  <v,e_i> e_i \\
=\sum _{i = 1} ^{n}  <v,e_i> fe_i \\
=\sum _{i = 1} ^{n}  <v,fe_i\cdot e_i> \\
=<v,\sum _{i = 1} ^{n}  e_ife_i>
\end{array}
$$

</div>





#### 正交补

<div class='dbox'>

正交补

$U^{\perp}=\{ v \vert <u,v>=0,u\in U,v\in V \}$

</div>

和$U$中向量正交的向量们.

<div class='cbox'>

- $U\oplus U^{\perp}=V$
- $(U^{\perp})^{\perp}=U$

</div>

<div class='pbox'>

取$U$的一组规范正交基$u_1\ldots u_n$,扩充到$V$的一组规范正交基$u_1\ldots u_n,v_1\ldots v_m$.

则容易发现 $U^{\perp}=\operatorname{span}( v_1\ldots v_m )$.

然后第一条是显然的.第二条的话你把$U^{\perp}$的基扩充到$V$的时候扩充$u_1\ldots u_n$就也是显然的.

</div>


<div class='dbox'>

正交投影

$$
\begin{array}{l}
\text{let } u=w_1+w_2,w_1\in U,w_2\in U^{\perp} \\
\Rightarrow P_U=w_1
\end{array}
$$

</div>

即干掉垂直分量,投影到$U$所在超平面上.

<div class='cbox'>

- $P_U$ 是线性变换.
- 对$U$的一组规范正交基$e_1\ldots e_m$,有$P_Uv=\sum_{i=1}^m <v,e_i> e_i$

以及一些很显然的性质.

</div>

<div class='pbox'>

第二条看起来很显然.那么有了第二条第一条也很显然.

</div>


### 伴随,自伴算子,正规算子.

#### 伴随

<div class='dbox'>

伴随

对于算子$T$,若$\forall u,v$,$<Tu,v>=<u,T^*v>$,则$T^*$是$T$的伴随.

</div>

<div class='cbox'>

- $(S+T)^*=S^*+T^*$
- $(\lambda T)^*=\lambda T^*$
- $(ST)^*=T^*S^*$
- $(T^*)^*=T$
- $\operatorname{null} T*=\operatorname{range} T)^{\perp}$

</div>

<div class='pbox'>

前三个用定义带进去即可.

第四个,$<u,T*v>=<Tu,v>=\overline{ <T*v,u> } = \overline{ <v,Tu> } =<Tu,v>$

第五个,考虑是右边对任意$u$,$<Tu,w>=0$的所有$w$,$<Tu,w>=<u,T*w>$,故 $w\in \operatorname{null} T*$

</div>

<div class='cbox'>

$$
\begin{array}{l}
\mathcal M( T^*, v_1\ldots v_m, u_1\ldots u_n) = \overline{ \mathcal M( T ,u_1\ldots u_n,v_1\ldots v_m)^T  }  \\
(v_1\ldots v_m),(u_1\ldots u_n) \text{ are regular orthogonal bases} 
\end{array}
$$

右边说的是转置再把每一项共轭.

</div>

<div class='pbox'>

$$
\begin{array}{l}
<Tu,v>=<u,T^*v> \\
Tu=\sum _{i = 1} ^{m} \sum_{j=1}^n A_{j,i}<u,u_i>v_j \\
<Tu,v> \\
= <\sum _{i = 1} ^{m}\sum_{j=1}^n A_{j,i}<u,u_i>v_j,v>  \\
=\sum _{i = 1} ^{m} \sum_{j=1}^n A_{j,i}<u,u_i><v_j,v> \\
=<u,\sum _{i = 1} ^{m} \sum_{j=1}^n A_{j,i}<v_j,v>u_i> \\
=<u,Tv>
\end{array}
$$

其实就是直接用规范正交基写开直接做.

</div>

#### 自伴算子

<div class='dbox'>

自伴算子

$T=T^*$

</div>

所以这个实空间下就是我们实对称矩阵啊.

<div class='cbox'>

$$
\begin{array}{l}
T=T^* \Rightarrow T\text{'s eigenvalues}\in R  \\
T=T^* \Leftrightarrow \forall v,<v,Tv> \in R \\
T=T^* \Leftrightarrow (<v,Tv>=0 \Rightarrow T=0)
\end{array} 
$$

注意,前两条对复向量空间成立,最后一条是对实向量空间成立.

</div>

所以说书说伴随类比共轭,自伴算子类比实数啊.

<div class='pbox'>

第一行,根据舒尔定理,$T$有关于规范正交基的上三角矩阵,然后因为矩阵等于共轭转置,于是对角线上对应相等,于是都是实数.

第二行,$<v,Tv>=\overline{ <Tv,v> } = \overline{ <v,T^*v> } =\overline{ <v,Tv> }$可以正推.

反推的话

$$
\begin{array}{l}
\forall v,0 \\
=<v,Tv>-\overline{ v,Tv } \\
=<v,Tv>-<v,T^*v> \\
=<v,(T-T^*)v>=0
\end{array}
$$

这里我们似乎需要点引理:

<div class='cbox'>

复向量空间下,只有$T=0$可以保证$\forall v,<v,Tv>=0$.

</div>

也就是复向量空间下的性质3.

<div class='pbox'>

考虑$T$变成规范正交基下的上三角矩阵,基是$e_1\ldots e_n$,则$Te_1=\lambda_1e_1,<e_1,Te_1>=<e_1,\lambda_1 e_1>=0$得$\lambda_1=0$,$Te_1=0$.

然后你带入$e_1+e_2$,则$T(e_1+e_2)=Te_2=ae_1+be_2,<e_1+e_2,T(e_1+e_2)>=0$得$a=b=0$,$Te_2=0$.

反复重复就得到$\forall i,Te_i=0$,于是$T=0$.

</div>

这样我们就可以从$<v,(T-T^*)v>=0$得到$T=T^*$了.

第三行,考虑
$$
\begin{array}{l}
\forall u,v, \\
<u,Tv>=\dfrac{<u+v,Tu+Tv>-<u-v,Tu-Tv>}{4} 
\end{array}
$$

于是任意$<u,Tv>=0$,$T=0$.


</div>

<div class='cbox'>

投影算子是自伴算子

</div>

<div class='pbox'>

$$
\begin{array}{l}
<P_Uu,v>=<P_Uu,P_Uv+(v-P_Uv)>=<P_Uu,P_Uv>+<P_Uu,(v-P_Uv)>=<P_Uu,P_Uv>=<u,P_Uv>
\end{array}
$$

显然的啦.

</div>





#### 正规算子

<div class='dbox'>

正规算子

$$
\begin{array}{l}
T \text{ is normal} \Leftrightarrow  TT^*=T^*T
\end{array}
$$

</div>

<div class='cbox'>

$$
\begin{array}{l}
T \text{ is normal} \Leftrightarrow \forall v,\vert\vert Tv \vert\vert = \vert\vert T^*v \vert\vert 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
<Tv,Tv>=<T^*Tv,v>=<TT^*v,v>=<T^*v,T^*v>
\end{array}
$$

</div>

<div class='cbox'>

$$
\begin{array}{l}
T \text{ is normal} ,\lambda \text{ is eigen value of } T \Rightarrow T-\lambda I \text{ is normal}  
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
(T-\lambda I)^*=T^*-\overline{ \lambda } I \\
\Rightarrow (T-\lambda I)(T-\lambda I)^* \\
=TT^*-(\lambda+\overline{ \lambda } )T+\lambda \overline{ \lambda } \\
=(T-\lambda I)^*(T-\lambda I) 
\end{array}
$$

</div>



<div class='cbox'>

$$
\begin{array}{l}
T \text{ is normal}, Tv=\lambda v \Rightarrow T^*v=\overline{ \lambda } v 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
(T-\lambda I)v=0 \\
\Rightarrow \vert\vert (T-\lambda I)v \vert\vert =0 \\
\Rightarrow \vert\vert (T-\lambda I)^*v \vert\vert =0 \\
T^*v=\overline{\lambda}v
\end{array}
$$

</div>

<div class='cbox'>

$$
\begin{array}{l}
T \text{ is normal} \Rightarrow \text{eigen vectors of } T \text{ are orthogonal} 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\text{let } Tu=\lambda_1 u,Tv=\lambda_2 v \\
(\lambda_2-\lambda_1)<u,v> \\
=<u,\lambda_2 v>-<\overline{ \lambda_1 } u,v> \\
=<u,Tv>-<T^*u,v>  \\
=0
\end{array}
$$

</div>

### 谱定理

<div class='cbox'>

复谱定理

复向量空间上,算子正规等价于存在一组由本征向量组成的规范正交基

</div>

<div class='pbox'>

反向推是显然的:对角矩阵之间乘法是交换的.

正向推:

首先舒尔定理得到一个规范正交基使得矩阵 $\mathcal M( T ) =M$ 是上三角的.

现在利用$A=MM^*=M^*M$.

考虑 $\sum_{i=1}^n \vert M_{i,i} \vert ^2=<M_{1,.},\overline{M_{1,.}}>=<M_{.,1},\overline{M_{.,1}}>=\vert M_{1,1} \vert ^2$

于是直接说明了$M_{1,i}=0,i>1$.

然后再考虑$A_{2,2}$是第二行第二列,可以同理得到$<M_{2,i}=0,i>2$

于是重复上述过程可以证明$M$是对角矩阵,得证.

</div>

<div class='cbox'>

实谱定理

实向量空间上,算子自伴等价于存在一组本征向量组成的规范正交基

</div>

<div class='pbox'>

反向推依然是显然的,考虑正向.

考虑归纳,先假设对所有小于$n$维命题成立.$1$维显然成立.

取一个规范的本征向量,把它作为基的第一个向量$n_1$,设  $U=\operatorname{span}( n_1 )$,则$T$在$U$上不变.

注意到

<div class='cbox'>

$$
\begin{array}{l}
u\in U \Rightarrow Tu\in U \\
\Leftrightarrow v\in U^{\perp},Tv\in U^\perp
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
u\in U,v\in U^{\perp} \\
\Rightarrow <Tu,v>=0 \\
\Rightarrow <u,Tv>=0 \\
\Rightarrow Tv\in U^{\perp}
\end{array}
$$

</div>

于是$T$在$U^{\perp}$上不变,那么对$T\vert_{U^{\perp}}$应用归纳假设,它存在一个由本征向量构成的规范正交基.

现在直接把$n_1$加入进去,显然这是一组本征向量构成的规范正交基.

**然后我们发现自己忽略了一件事:我们没有证明这个本征向量是能取出来的.**

<div class='cbox'>

实向量空间上的自伴算子存在本征值.

</div>

<div class='pbox'>

考虑经典技巧,对任意$v\in V$,$v,Tv,T^2v\ldots T^nv$线性相关,存在$f(x)\in \mathcal{P}_n \ s.t.\ f(T)v=0$

将$f$质因式分解,

$$
\begin{array}{l}
f(x)=a\prod_i (x-\lambda_i)\prod_i (x^2+b_ix+c_i) \\
f(T)v=a\prod_i (T-\lambda_i I)\prod_i (T^2+b_iT+c_iI)v=0
\end{array}
$$

由于$T^2+b_iT+c_i$不可分解,有$b_i^2-4c<0$

我们假设$T$没有本征值,则$T-\lambda_i I$是单的.

而 

$$
\begin{array}{l}
<(T^2+b_iT+c_i)v,v> \\
=<((T+\dfrac{b_i}{2}I )^2+(c-\dfrac{b^2}{4}))v,v> \\
=<(T+\dfrac{b_i}{2} I)^2v,v>+(c-\dfrac{b^2}{4})v^2 \\
=(Tv+\dfrac{b_iv}{2} )^2+(c-\dfrac{b^2}{4}  )v^2 \\
>0
\end{array}
$$

于是它也是单的,则$f(T)$是单的,和$f(T)v=0$矛盾

所以其实$T$有本征值是某个$\lambda_i$

</div>

</div>

### 正算子,平方根,等距同构

<div class='dbox'>

正算子

$$
\begin{array}{l}
T \text{ is positive} \Leftrightarrow 
\begin{cases}
\forall v,<v,Tv>\ge 0 \\
T \text{ is self-adjoint} 
\end{cases}
\end{array}
$$

</div>

你会发现正算子其实对应了矩阵中的半正定矩阵.

<div class='dbox'>

平方根

$$
\begin{array}{l}
T=R^2 \Leftrightarrow R \text{ is squre root of T} 
\end{array}
$$

</div>

<div class='cbox'>

下列条件等价:

$$
\begin{array}{l}
T \text{ is positive} \\ 
T \text{ is self-adjoint and each T's eigenvalues is not negative} \\
T \text{ has positive squre root}  \\
T \text{ has adjoint squre root}  \\
\exists R,T=R^*R
\end{array}
$$

</div>

<div class='pbox'>

由第一行推第二行:显然自伴,只要说明本征值非负.

由刚才谱定理,作为自伴矩阵它有规范正交基下的对角形式.而对角形式下,取一个本征向量$v$乘它,如果对应本征值$\lambda<0$则$<v,Tv>=\lambda v^2<0$,矛盾.于是得证.

第二行推第三行:仍然在对角形式下操作,把对角线每个元素算术平方根,容易发现你得到一个正平方根.

第三行推四行是显然.

第四行推第五行显然,因为对自伴算子$R$满足$T=R^2$且$R=R^*$

第五行推第一行,首先容易验证$(R^*R)^*=R^*(R^*)^*=R^*R$,$T$是自伴.再考虑$<v,R^*Rv>=<Rv,Rv>\ge 0$于是得证.

</div>


<div class='cbox'>

正算子有唯一的正平方根.

</div>

于是可以记$T$的唯一正平方根为$\sqrt T$

<div class='pbox'>

首先由之前从 $T \text{ is positive} \Rightarrow T=S^2,S \text{ is positive}$中我们会证存在性(对角矩阵然后给每个本征值开根).

现在考虑已经有一个正平方根$S$,取$S$的本征向量构成的规范正交基$e_1\ldots e_n$,再取$T$的本征向量$v$,有

$$
\begin{array}{l}
\left. \begin{array}{ll}
Tv=\lambda v \\
v=\sum _{i = 1} ^{n}  <v,e_i>e_i
\end{array} \right\} \\
\Rightarrow 
Tv=\sum _{i = 1} ^{n}  \lambda <v,e_i> \\
R^2v=\sum _{i = 1} ^{n} \lambda_i^2 <v,e_i>e_i=Tv=\sum _{i = 1} ^{n}  \lambda <v,e_i> \\
\Rightarrow \sum _{i = 1} ^{n}  (\lambda_i^2-\lambda)<v,e_i>e_i=0 \\
\Rightarrow \forall i,<v,e_i>\ne 0:\lambda_i^2=\lambda \\
\Rightarrow Rv=\lambda_i v=\sqrt{\lambda} v
\end{array}
$$

于是可以证明$R$对$T$的每个本征向量的作用都与前面通过对角线直接取平方根构造出的$R_0$相同,故$R=R_0$


</div>

<div class='dbox'>

等距同构

$$
\begin{array}{l}
T \text{ is an isometry} \Leftrightarrow \forall v,\vert\vert Tv \vert\vert =\vert\vert v \vert\vert  
\end{array}
$$

</div>

<div class='cbox'>

下列条件等价:

$$
\begin{array}{l}
T \text{ is an isometry}  \\
\forall u,v,<Tu,Tv>=<u,v> \\
\forall \text{orthonormal base } e, Te_1\ldots Te_n \text{ is orthonormal}  \\
\exists \text{orthonormal base } e, Te_1\ldots Te_n \text{ is orthonormal} \\
TT^*=I \\
T^*T=I \\
T^*=T^{-1}
\end{array}
$$

</div>

<div class='pbox'>

第一行等价第二行:我们之前证过可以由范数计算内积,于是保范数和保内积等价.

前两行推第三行是显然的:$<Te_i,Te_j>=<e_i,e_j>=0$,同时长度显然也不变.

第三行推第四行是显然的.

第四行推第五行:考虑$\forall u,v:<u,Tv>=<T^*u,v>=<TT^*u,Tv>$,于是$<(TT^*-I)u,v>=0$,可以说明$TT^*=I$

于是$T^*=T^{-1}$,而证明群里的逆元是交换的是经典的,于是后三条是一起的.

最后,如果$T^*=T^{-1}$,$\vert\vert Tv \vert\vert^2=\sqrt{<Tv,Tv>}=\sqrt{<T^*Tv,v>}=\vert \vert v\vert \vert$,得证.

</div>


<div class='cbox'>

复向量空间下

$$
\begin{array}{l}
T \text{ is an isometry}  \\
\Leftrightarrow \exists \text{orthonormal base }e, \\
\forall i, Te_i=\lambda_i e_i,\vert \lambda_i \vert =1 
\end{array}
$$

</div>

<div class='pbox'>

首先证明逆向,则在基$e$下$T$是对角矩阵且对角线元素模长为$1$,容易验证$TT^*=I$,说明$T$是等距同构.或者你慢慢写验证保持范数也是简单的.

然后正向:取$T$的本征向量构成的规范正交基,于是$T$是对角矩阵且$TT^*=I$,也是显然的.

</div>

### 极分解,奇异值分解

<div class='cbox'>

极分解

$$
\begin{array}{l}
T=S\sqrt{T^*T},S \text{ is isometry} 
\end{array}
$$

</div>

<div class='pbox'>

首先我们之前说明过$T^*T$是正的,于是这个平凡根存在.且

$$
\begin{array}{l}
\vert\vert Tv \vert\vert =\sqrt{<Tv,Tv>}=\sqrt{<T^*Tv,v>} \\
=\sqrt{<\sqrt{T^*Tv},\sqrt{T^*T}v>}=\vert\vert \sqrt{T^*T}v \vert\vert
\end{array}
$$

于是$S$可以是等距同构的,在 $\operatorname{range} \sqrt{T^*T} \to \operatorname{range} T$上我们定义:

$$
\begin{array}{l}
S_1\sqrt{T^*T}v=Tv
\end{array}
$$

$$
\begin{array}{l}
S_1\sqrt{T^*T}(v_1+v_2)=T(v_1+v_2) \\
\Rightarrow S_1(\sqrt{T^*T}v_1)+S_1(\sqrt{T^*T}v_2)=Tv_1+Tv_2 \\
S_1\sqrt{T^*T}kv_1=kTv_1
\end{array}
$$

这样可以说明$S_1$是线性变换.

并且
$$
\begin{array}{l}
\sqrt{T^*T}v_1= \sqrt{T^*T}v_2 \\
\Leftrightarrow  \vert\vert \sqrt{T^*T}(v_1-v_2) \vert\vert =0 \\
\Leftrightarrow  \vert\vert T(v_1-v_2) \vert\vert =0 \\
\Leftrightarrow  Tv_1=Tv_2
\end{array}
$$

于是$S_1$是单射.显然也是满射.于是$S_1$是双射.

于是

$$
\begin{array}{l}
\dim \operatorname{range} \sqrt{T^*T}=\dim \operatorname{range} T \\
\Rightarrow \dim (\operatorname{range} \sqrt{T^*T})^\perp=\dim (\operatorname{range} T)^\perp
\end{array}
$$

于是可以从 $(\operatorname{range} \sqrt{T^*T})^\perp$和$(\operatorname{range} T)^\perp$中分别取一组规范正交基$e_1\ldots e_n$,$f_1\ldots f_n$,那么只要让

$$
\begin{array}{l}
S_2\in \mathcal L( (\operatorname{range} \sqrt{T^*T})^\perp , (\operatorname{range} T)^\perp ) \\
S_2(\sum_i c_ie_i)=\sum_i c_if_i
\end{array}
$$

并最后让$S=S_1+S_2$即可.

$$
\begin{array}{l}
\text{Q.E.D}
\end{array}
$$

</div>

<div class='dbox'>

奇异值

$T$的奇异值即$\sqrt{T^* T}$的本征值,且每个值$\lambda$重复$\dim E(\lambda,\sqrt{T^ *T})$次.

</div>

<div class='cbox'>

奇异值分解

对算子$T$设$s_1\ldots s_n$是$T$的奇异值,则存在两组规范正交基$e_1\ldots e_n$,$f_1\ldots f_n$,使得$Tv=\sum_i s_i<v,e_i>f_i$.

</div>

<div class='pbox'>

哦$\sqrt{T^*T}$好在它是正的,于是谱定理可以找到一组基$e$使得$\sqrt{T^*T}e_i=s_ie_i,\sqrt{T^*T}v=\sum_i s_i<v,e_i>e_i$.

那么极分解$T=S\sqrt{T^*T}$,于是

$$
\begin{array}{l}
Tv=S\sqrt{T^*T}v \\
=S\sum_i s_i<v,e_i>e_i \\
=\sum_i s_i<v,e_i>Se_i \\
=\sum_i s_i<v,e_i>f_i
\end{array}
$$

因为$S$是等距同构所以把规范正交基变换成规范正交基.

</div>


### 零空间链,幂零算子,广义本征空间

<div class='cbox'>

$$
\begin{array}{l}
{0}=\operatorname{null} T^0,\operatorname{null} T^i \subset \operatorname{null} T^{i+1} \\
\operatorname{null} T^i= \operatorname{null} T^{i+1} \Rightarrow \forall j>i,\operatorname{null} T^j=\operatorname{null} T^i \\
\operatorname{null} T^{\dim V}=\operatorname{null} T^{\dim V+1}  \\
\end{array}
$$

</div>

<div class='pbox'>

前两行是显然的

第三行也是显然的:$U$的真子空间的维数必须小于$U$.

</div>

<div class='cbox'>

$$
\begin{array}{l}
V=\operatorname{null} T^{\dim V} \oplus \operatorname{range} T^{\dim V}
\end{array}
$$

</div>

<div class='pbox'>

首先维数满足条件,并且交是 $\{ 0 \}$,所以成立.

</div>


<div class='dbox'>

幂零算子

即$T$满足$\exists n,T^n=0$(显然可以让$n=\dim V$)

</div>

<div class='cbox'>

存在一组基使得算子的矩阵为严格上三角矩阵.

</div>

<div class='pbox'>

先取 $\operatorname{null} T$ 的基,不够就加入 $\operatorname{null} T^2$ 零空间的基扩充,然后加 $\operatorname{null} T^3$的,直到加到$n$个.

注意到对来自 $\operatorname{null} T^k$ 的基$e$,$Te\in \operatorname{null} T^{k-1}$,于是是严格上三角矩阵.

</div>

<div class='dbox'>

广义本征向量

$$
\begin{array}{l}
\exists n,(T-\lambda I)^nv=0 \\
\Leftrightarrow v \text{ is generalized eigen vector of } T.
\end{array}
$$

</div>

<div class='cbox'>

$$
\begin{array}{l}
(T-\lambda I)^n v=0 \Rightarrow \lambda \text{ is eigenvalue of } T
\end{array}
$$

</div>

<div class='pbox'>

因为显然$T-\lambda I$不是单的.

</div>


<div class='dbox'>

广义本征空间

$$
\begin{array}{l}
G(\lambda,T)=\operatorname{null} (T-\lambda I)^{\dim V}
\end{array}
$$

</div>

就是广义本征向量的张成空间.


<div class='cbox'>

不同广义本征空间中的向量线性无关.

$$
\begin{array}{l}
v_i\in G(\lambda_i,T) \\
\Rightarrow \{ v_n \} \text{ is linear independent} 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\text{let } k=\max {i\vert (T-\lambda_1 I)^i v_1\ne 0} \\
\text{let } w=(T-\lambda_1 I)^k v_1 \\
\Rightarrow Tw=\lambda_1w \\
\text{let } F=(T-\lambda_1I)^k\prod_i (T-\lambda_iI)^n \\
\sum _{i = 1} ^{n}  c_iv_i=0 \\
\Rightarrow F\sum _{i = 1} ^{n}  c_iv_i=0 \\
\Rightarrow Fc_1v_1=0 \\
\Rightarrow c_1w=0 \\
\Rightarrow c_1=0
\end{array}
$$

于是对所有$v_i$做一遍可以得到$c$全是$0$,得证.

</div>

<div class='cbox'>

任意复向量空间上的算子$T$的所有本征值$\lambda_1\ldots \lambda_k$满足

$$
\begin{array}{l}
\bigoplus_i G(\lambda_i,T)=V \\
\sum_i \dim G(\lambda_i,T)=\dim V \\
\exists e_1\ldots e_n,e_i \text{ is generalized eigenvector} ,\{ e_n \} \text{ is basis of } V \\
(T-\lambda_iI)\vert_{G(\lambda_i,T)} \text{is nilpotent} 
\end{array}
$$

</div>

<div class='pbox'>

先证第一行.

归纳,因为$T$有本征值,取一本征值$\lambda$,则 $V=G+\operatorname{range} (T-\lambda I)$, $U=\operatorname{range} T-\lambda I$ 在$T$下不变,于是对$T\vert_U$给出$U$的分解再加上$G(\lambda,T)$即可.

显然$T\vert_U$不会有$\lambda$作为本征值.证明是成立的.

第一行成立后第二行第三行是显然的.第四行不需要第一行就是显然的.

</div>

为什么你不能对普通本征空间这么干而必须广义呢?因为普通本征空间没有 $\operatorname{null} T-\lambda I\oplus \operatorname{range} T-\lambda I=V$的性质,你分解的时候递归不下去(去掉$E(\lambda,I)$剩下的不是不变子空间)

<div class='dbox'>

代数重数,几何重数

$$
\begin{array}{l}
\text{代数重数} =\dim G(\lambda,T) \\
\text{几何重数} =\dim E(\lambda,T)
\end{array}
$$

</div>

<div class='cbox'>

若$T$有本征值$\lambda_1\ldots \lambda_m$,则存在一组基使得 $\mathcal M( T ) =\operatorname{Diag}(A_1,\ldots,A_m)$其中每个$A$为对角线上全为$\lambda$的上三角矩阵.

</div>

<div class='pbox'>

我们已经说明了$V=\bigoplus_i G(\lambda_i,T)$,则取所有广义本征向量做基就有 $A_i=\mathcal M( T\vert_{G(\lambda_i,T)} )$,又因为

我们知道$T\vert_{G(\lambda_i,T)}-\lambda_i I$是幂零的,于是它有一个严格上三角,那么你再加回去$\lambda_i I$就满足条件了.

</div>

我们希望进一步改进这个结果,就要改进幂零算子的结构:

<div class='cbox'>

幂零算子$N$满足,存在$v_1\ldots v_k\in V,m_1\ldots m_k\in N$使得:
- $v_1,Nv_1,\ldots, N^{m_1}v_1,v_2,Nv_2,\ldots, N^{m_2}v_2,\ldots,Nv_n,\ldots N^{m_k}v_n$是$V$的基.
- $\forall i,N^{m_i+1}v_i=0$

</div>

你可以发现,在这组基下,幂零算子被干成了分块对角矩阵,且每个块内只有对角线上面一条对角线是$1$,其余位置是$0$.

<div class='pbox'>

考虑归纳法,归纳就要找不变子空间,比如找到  $\operatorname{range} N$ ,显然  $\dim \operatorname{range} N<\dim V$ ,于是 $N\vert_{\operatorname{range} N}$ 有这样一组基 $v_1\ldots v_k\in \operatorname{range} N,m_1\ldots m_k\in N$ 满足基的条件.

$$
\begin{array}{l}
v_i\in\operatorname{range} N \\
\Rightarrow \exists u_i,Nu_i=v_i
\end{array}
$$ 

于是用$u_1\ldots u_k$替换$v_1\ldots v_k$并加入他们自己,得到 $N^{m_1}u_1,\ldots, u_1,\ldots, N^{m_k}u_k,\ldots, u_k = \{ e_n \}$.

考虑若  $\sum _{i = 1} ^{n}  c_ie_i=0$ ,则 $0=\sum _{i = 1} ^{n}  c_iNe_i$ ,但$Ne_i$是 $\operatorname{range} V$ 的基是不相关的.于是$e$线性无关.

那么考虑又添加 $w_1\ldots w_l$ 扩充得 $e_1\ldots e_n,w_1\ldots w_l$ 是基.对任意$w$,一定有 $w\notin \operatorname{range} N$,而现在的唯一问题是$Nw$可能不为$0$,注意到因为 $\operatorname{span}( \{ Ne_i \}  ) =\operatorname{range} N$,于是  $\exists x\in \operatorname{span}( \{ e_i \}  ) ,Nx=Nw$,于是取$e_{n+i}=w_i-x_i$即可.

于是你构造出了$N$的基,归纳得证.

</div>

[think] 归纳解决存在基满足xx的问题是有效的(复向量的上三角,两种谱定理,到这个Jordan分解等等),要有条件构造不变子空间.

同时这个是在说,幂零矩阵满足存在一组基使得它的矩阵是分块对角矩阵,且每个块只有对角线上方的一行斜线元素都是$1$,其他都是$0$.

<div class='cbox'>

Jordan分解

存在一组基$e$满足 

$$
\begin{array}{l}
\mathcal M( T,e ) =\operatorname{Diag}(A_i\ldots A_k), \\
A_i=\lambda_i I+
\begin{bmatrix}
    0,1,0\ldots,0 \\
    0,0,1,\ldots,0 \\
    \ldots \\
    0,0,\ldots,0,1 \\
    0,0,\ldots,0,0
\end{bmatrix}
\end{array}
$$

</div>

<div class='pbox'>

水到渠成了.

每个块$A_i$对应了一个$T\vert_{G(\lambda_i,T)}$,而已知$T\vert_{G(\lambda_i,T)}-I$是幂零的,而刚才说过幂零矩阵有由只有对角线上方一斜线是$1$的块构成的分块对角矩阵,再加上$\lambda I$就是这样了.

</div>



### 平方根

<div class='cbox'>

$I+N$有平方根

</div>

<div class='pbox'>

$$
\begin{array}{l}
(1+x)^{\frac{1}2}=\sum _{i = 0} ^{\infty} \binom{\frac12}{i}x^i \\
\text{let } S_n(x)=\sum _{i = 0} ^{2} \binom{\frac12}{i}x^i \\
\forall k<n,[x^k]S_n^2(x)=
\sum _{i = 0} ^{k} \binom{\frac12}{i}\binom{\frac12}{k-i} =\binom{1}{k}=[k\le 1]
\end{array}
$$

于是$S_n(x)$和$\sqrt{1+x}$的前$k$项一样,而$N$是幂零的保证了它没有某项以后的,于是只要取一个$S_n(N)$就是$\sqrt{I+N}$.

</div>


<div class='cbox'>

$C$上可逆算子有平方根.

</div>

<div class='pbox'>

约旦分解,给每个$\lambda I+N$形式找一个平方根,再拼回来.

</div>

### 特征多项式和极小多项式

<div class='dbox'>

特征多项式

$$
\begin{array}{l}
p(z)=\prod _{i = 1} ^{k}  (z-\lambda_i)^{c_i} \\
c_i=\dim E(\lambda_i,T)
\end{array}
$$

</div>

<div class='cbox'>

特征多项式的次数和零点

$$
\begin{array}{l}
\deg p(z)=\dim V \\
p(z)=0 \Leftrightarrow z \text{ is eigenvalue of } T
\end{array}
$$

</div>

<div class='pbox'>

显然吧.

</div>

<div class='cbox'>

Caylay-Hamilton Theorem

$T$的特征多项式$p(z)$满足$p(T)=0$

</div>

<div class='pbox'>

因为$T$可以拆成广义本征空间直和上的$T\vert_{G(\lambda_i,T)}$,而$T\vert_{G(\lambda_i,T)}$是幂零的,于是$(T\vert_{G(\lambda_i,T)}-\lambda_iI)^{\dim G(\lambda_i,T)}=0$.

而$p(T)$显然包含这个因子,于是每个$G(\lambda_i,T)$上都有$p(T\vert_{G\lambda_i,T})=0$,于是$p(T)=0$

</div>

<div class='dbox'>

极小多项式

对于$T$,$p(z)$是满足最高次项为$1$且$p(T)=0$的多项式中次数最小的一个.

</div>

<div class='cbox'>

极小多项式唯一

</div>

<div class='pbox'>

$$
\begin{array}{l}
\text{assume }p,q \text{ is minimal polynomial}  \\
p(T)=0,q(T)=0,\deg p=\deg q \\
\Rightarrow (p-q)(T)=0,\deg p-q<\min(\deg p,\deg q)
\end{array}
$$

于是和$p,q$极小矛盾,得证.

</div>


<div class='cbox'>

任意满足$q(T)=0$的多项式是极小多项式$p(z)$的倍式.

</div>

<div class='pbox'>

考虑$q \bmod p=f,f\ne 0$,则$f(T)=q(T)-kp(T)=0$且$\deg f<\deg p$,则与$p$极小矛盾.得证.

</div>

<div class='cbox'>

$T$的本征值是其极小多项式$p(z)$的零点

</div>

<div class='pbox'>

若$Tv=\lambda v$,$p(T)=0$,则$p(T)v=p(\lambda)v=0$,于是$p(\lambda)=0$.

若$p(\lambda)=0$且$\lambda$不是本征值,则$T-\lambda I$是满秩的,则设$p(T)=(T-\lambda I)q(T)$,$p(T)=0 \Leftrightarrow q(T)=0$,与$p$极小矛盾.

得证.

</div>



### 实向量空间复化

<div class='dbox'>

复化

$V$的复化是$V_C=V\times V$,但是把$(u,v)$写作$u+iv$.

$T$的复化是$T_C(u+iv)=Tu+iTv$

</div>

<div class='dbox'>

共轭

$\overline{ u+iv } =u-iv$

$\overline{ T } v=\overline{ T(\overline{ v } ) }$ 

</div>

容易验证 $\overline{ T }$之间的加法,数乘,复合( $\overline{ S } \circ \overline{T}=\overline{ST}$ )运算是有共轭的性质的.

知乎老哥提醒大家, 复向量空间取共轭的操作是依赖额外结构的,不是所有复向量空间都是某个实向量空间的复化.

<div class='cbox'>

实向量空间上每个算子都有一维或二维不变子空间

</div>

<div class='pbox'>

考虑它的复化$T_C$一定有本征值,设为$\lambda=a+bi$.

那么对任意$u+vi$,$T(u+vi)=(a+bi)(u+vi)=au-bv + i(av+bu)$

于是$u,v$张成的二维不变子空间在$T$下不变.

</div>

<div class='cbox'>

- 复化保持基不变
- 复化保持矩阵不变
- 复化保持极小多项式不变
- 复化后的实本征值是复化前的本征值
- 复本征值以共轭的形式成对出现,重数相等

</div>

<div class='pbox'>

第一条,对一组基$e_1\ldots e_n$,有 $u\in \operatorname{span}( e ) ,v\in \operatorname{span}( ie_1,\ldots,ie_n )$,得证.

第二条,因为基不变所以矩阵不变.

第三条,考虑$p(T)=0$显然有$p(T_C)=0$.而若$q(T_C)=0$,取每个系数的实部得到新的多项式$r(T_C)$一定有$r(T_C)v=0,\forall v\in V$.于是若$p$是$T$的极小多项式,那么不能存在$q(T_C)=0$且$\deg q<\deg p$,于是$p$也是$T_C$的极小多项式.

这也保证了复化出来的变换的极小多项式系数都是实数.

第四条,本征值是极小多项式的零点,极小多项式不变故本征值不变.

第五条,极小多项式系数都是实数于是在实数下可以分解成若干一次项和二次函数的乘积,分别对应了单独出现的实本征值和成对出现的复本征值.

</div>

<div class='dbox'>

$T$的特征多项式定义为$T_C$的特征多项式.

</div>

我们要说明这个定义的合理性:

<div class='cbox'>

$T_C$的特征多项式系数都是实数.

</div>

<div class='pbox'>

考虑:

<div class='cbox'>

$\lambda$与 $\overline{ \lambda }$重数相同.

</div>

<div class='pbox'>

$$
\begin{array}{l}
(T-\lambda I)^kv=0 \\
\Rightarrow \overline{ (T-\lambda I)^k v } =0 \\
(T-\overline{\lambda}I)^k \overline{ v }=0
\end{array}
$$

于是若$v_1\ldots v_k$是$G(\lambda,T)$的基,那么 $\overline{ v_1 } ,\ldots, \overline{v_n}$是$G(\overline{\lambda},T)$的基,得证.

</div>

于是你只要把成对出现的$(x-\lambda)(x-\overline{\lambda})$合成一个就可以得到实系数二次式.

于是系数全是实的.

</div>

### 实空间的正规算子

我们定义

<div class='dbox'>

内积的复化

$$
\begin{array}{l}
<a+bi,c+di> \\
=<a+bi,c>+i<a+bi,d>
=\overline{ <c,a+bi> } +i \overline{ <d,a+bi> }  \\
=<a,c>-<b,c>i+i<a,d>+<b,d> \\
=(<a,c>+<b,d>) + i(<a,d>-<b,c>)
\end{array}
$$

</div>

<div class='cbox'>

我们定义的复化的内积也满足内积的定义.

$(T_C)^*=(T^*)_C$

正规算子的复化还是正规算子.

</div>

<div class='pbox'>

第一条容易验证是对的.

第二条考虑

$$
\begin{array}{l}
<T(a+bi),c+di> \\
=(<Ta,c>+<Tb,d>+i(<Ta,d>-<Tb,c>)) \\
=(<a,T^*c>+<b,T^*d>+i(<a,T^*d>-<b,T^*c>)) \\
=<a+bi,T^*(c+di)>
\end{array}
$$

第三条考虑$TT^*=T^*T,T_C(T_C)^*=T_C(T^*)_C=(TT^*)_C=(T^*T)_C=T_C(T_C)^*$

</div>



<div class='cbox'>

$$
\begin{array}{l}
T \text{ is normal}  \\
\Leftrightarrow \exists e_1\ldots e_n \text{ is orthonormal basis }, \\
\mathcal M( T,e ) = \operatorname{Diag}(A_1\ldots A_k) , \\
A_k= [x] \text{ or } A=\begin{bmatrix}
    a\ -b \\
    b\ a
\end{bmatrix}
\end{array}
$$

</div>

<div class='pbox'>

于是我们复化得到$T_C$,$T_C$是正规的,有谱定理,存在一组本征向量构成的规范正交基.

考虑规范正交基的每个本征值$\lambda_i$

若$\lambda_i\in R,(a+bi)\in E(\lambda_i,T_C)$,则$T(a+bi)=\lambda_i a+\lambda_i bi$,于是可以分离实部虚部,则$a,b\in E(\lambda_i,T)$.

若$\lambda_i=a+bi\not\in R$,有$a-bi$也是重数相等的本征值,从两个对应的本征空间中分别取一个向量$c+di,c-di$.

$$
\begin{array}{l}
\left. \begin{array}{ll}
T(c+di)=(a+bi)(c+di) \\
T(c-di)=(a-bi)(c-di)
\end{array} \right\} \\
\Rightarrow 
\begin{cases}
Tc=ac-bd \\
Td=bc+ad
\end{cases} \\
\end{array}
$$

于是$T$在$c,d$长成的二维子空间不变.

因为你复的情况是有$n$个本征值的,于是你这么做能得到$V$的子空间分解$U_1\ldots U_k$,$\dim U_k\le 2$.

且对于$\dim U_k=2$,就用$d,c$做基它的矩阵看起来是

$$
\begin{array}{l}
\begin{bmatrix}
    b, a \\
    -a, b
\end{bmatrix}
\end{array}
$$

即为所证.

</div>

<div class='cbox'>

$$
\begin{array}{l}
T \text{ is isometry}  \\
\Leftrightarrow \exists e_1\ldots e_n \text{ is orthonormal basis}  \\
\mathcal M( T,e ) =\operatorname{Diag}(A_1\ldots A_k), \\
A_k=[x] \text{ or } A=\begin{bmatrix}
    \cos\theta\ -\sin\theta \\
    \sin\theta\ \cos\theta
\end{bmatrix}
\end{array}
$$

</div>

<div class='pbox'>

整个证明流程与正规完全一致.只不过最后那个矩阵中 $\vert a +bi\vert=1$,所以能化出来$\cos,\sin$形式.

</div>



### 矩阵

<div class='cbox'>

基变更公式

设两组基$e_1\dots e_n$,$f_1\ldots f_n$,$M$是$T$在$f$下的矩阵,有矩阵$A$满足

$$
\begin{array}{l}
Af_i=\sum _{j = 1} ^{n}  A_{j,i}e_j
\end{array}
$$

则$AMA^{-1}$是$T$在$e$下的变换矩阵.

</div>

<div class='pbox'>

你直接尝试理解就好了:$Av$就是把$f$表示下的向量变成了$e$表示的向量.

</div>

另外,我们设$E=[e_1\ldots e_n]$,$F=[f_1\ldots f_n]$,则$A=F^{-1}E$.(其实就是到标准基的基变换).



<div class='dbox'>

迹

$$
\begin{array}{l}
\operatorname{trace} T=\sum _{i = 1} ^{n}  \lambda_i
\operatorname{trace} \mathcal M( T ) =\sum _{i = 1} ^{n}  \mathcal M( T ) _{i,i}
\end{array}
$$

注意$\lambda$按代数重数重复.实向量空间的先复化.

</div>

<div class='cbox'>

$$
\begin{array}{l}
\operatorname{trace} AB=\operatorname{trace} BA
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\sum _{i = 1} ^{n} (AB)_{i,i}=\sum _{i = 1} ^{n} \sum _{j = 1} ^{n}  A_{i,j}B_{j,i} \\
\sum _{i = 1} ^{n}  (BA)_{i,i}=\sum _{i = 1} ^{n}  \sum _{j = 1} ^{n}  B_{i,j}A_{j,i}
\end{array}
$$

交换求和号显然相等.

</div>

<div class='cbox'>

$$
\begin{array}{l}
\operatorname{trace} T=\operatorname{trace} \mathcal M( T ) 
\end{array}
$$

</div>

<div class='pbox'>

实空间先复化.考虑复空间.

那么有一组基使得 $\mathcal M( T )$ 是上三角矩阵$A$,此时显然成立.

而根据基变换公式,任意一组基下的 $\mathcal M( T ) =QAQ^{-1}$.

$$
\begin{array}{l}
\operatorname{trace} QAQ{-1}=\operatorname{trace} AQQ^{-1}=\operatorname{trace} A=\operatorname{trace} T
\end{array}
$$

</div>

<div class='dbox'>

行列式

定义为$\prod_i \lambda_i$.同样按重数重复.同样复化.

</div>

<div class='cbox'>

$T$的特征多项式等于$\det(zI-T)$

</div>

<div class='pbox'>

考虑在$T$有一组基是上三角矩阵,此时容易看出$zI-T$的特征值就是所有$z-\lambda_i$,结束.

</div>

<div class='cbox'>

$$
\begin{array}{l}
\det M=\sum _{p} \prod _{i = 1} ^{n}  M_{i,p_i}(-1)^{\operatorname{rev}(p)}
\end{array}
$$

</div>

<div class='pbox'>

很难的啊

证明路径大概是,我们先说明行列式的$\det(AB)=\det A\det B$,然后通过分解$M=LU$算出是特征值之积这样.

而这个公式是怎么来的呢,大概是我们先规定有:

- 多重线性:对每一行线性(齐性和加性)
- 交替:交换两行,行列式取反
- 单位:$\det I=1$

通过这三条可以容易的算出来行列式的这个表示,每行线性你就把一行拆成对$n$个这一行只有一个元素其余都是$0$的矩阵累加,再把这个非零元提到矩阵外面变成常数,每一行都这么干,则问题就变成了若干个全$1$的置换矩阵乘上系数,你再发现置换矩阵的行列式根据第二条第三条性质会写成排列逆序对就做完了.

那怎么说明矩阵乘积的行列式不变呢?

这里gemini用的方法是定义函数 $F(A)=\dfrac{AB}{\det B} )$,证明它满足行列式的三条规定,而三条规定等价于行列式,于是$F(A)=\det A$.

第三条显然,第一条第二条考虑$AB$本来就是$B$乘上$A$的每一行拼起来所以也显然.

然后你就可以推出这种定义和特征根乘积定义的等价性了.

</div>

第三版的内容到此结束.剩下的随缘更.

