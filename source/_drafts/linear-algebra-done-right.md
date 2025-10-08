---
title: Linear Algebra Done Right
tags: [linear-algebra,note,self-study]
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
\begin{array}{c}
\mathrm{span}( v_1 \ldots v_n ) = \{ \sum _{i = 1} ^{n}  c_iv_i \} 
\end{array}
$$

张成$V$的组简称张成组

</div>

<div class='dbox'>

基

基=张成组+线性无关组

</div>



则按照直觉的,维数应该是张成组长度的最小值,线性无关组长度的最大值,基的长度等等,**下面讨论的是有限维线性空间**.

<div class='cbox'>

- $\mathrm{dim} V$是张成组最小长度
- $\mathrm{dim} V$是线性无关组组最大长度
- $\mathrm{dim} V$是任意一组基的长度

</div>

<div class='pbox'>

首先说明,对一个线性相关的组,我们一定可以去掉一个线性相关项保持张成空间不变(显然).

首先说明 

<div class='cbox'>

任意一组线性无关组长度小于等于任意一组张成组长度:

</div>

<div class='pbox'>

考虑一个线性无关组和一个张成组,将一个线性无关组的元素加入张成组,则形成的一定是线性相关组,删去一个**张成组中的**元素则保持张成,不断重复这个操作,注意因为被加入的线性无关,所以你想相关一定得带张成组中的,于是可以一直操作.

直到线性无关组全部被加入,则因为每次删掉一个张成组元素,你一定有线性无关组长度不大于它.

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

维数就是这个长度为 $\mathrm{dim} V$

</div>

</div>

#### 空间的运算

<div class='dbox'>

空间的和

$$
\begin{array}{c}
U+V = \{ u+v \vert u\in U,v\in V \} 
\end{array}
$$

</div>

加法实际上是并(包含子空间所有向量的最小空间).

并定义直和.

<div class='dbox'>

空间直和

$$
\begin{array}{c}
W = U\oplus V = U + V \\ s.t.\\ 
\forall w \in W, \exist! u\in U,v\in V, u+v=w
\end{array}
$$

</div>

直和相当于不交并,是对空间进行一种分解.

然后直和的判定容易证明只要$0$的表示满足唯一性,并推出当且仅当它们的交只有$0$

<div class='dbox'>

空间的积

就是笛卡尔积.

$$
\begin{array}{c}
U\times V=\{ (u,v) \vert u\in U,v\in V \} 
\end{array}
$$

</div>

其实也可以先扩展一下直和 是等价的.

<div class='dbox'>

仿射空间

$$
\begin{array}{c}
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
\begin{array}{c}
U/V={\left\{ u+V \vert u\in U \right\}} 
\end{array}
$$

</div>

可以理解成等价类分类.如果两个向量的差在$V$中则认为他们等价.新的空间中每个元素都是一个等价类.而你仿射空间的变换也可以看成是对代表元做变换.

最后考虑它们的维数,有:

<div class='cbox'>

$$
\begin{array}{c}
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
\begin{array}{c}
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
\begin{array}{c}
\text{for linear map } T:U\to V \\
\mathrm{range\ } T = \{ v \vert v=Tu,u\in U \}  \\
\mathrm{null\ } T = \{ u \vert Tu=0,u \in U \} 
\end{array}
$$

</div>


<div class='cbox'>

$$
\begin{array}{c}
\dim U=\dim \mathrm{null\ } T+\dim \mathrm{range\ } T
\end{array}
$$

</div>

<div class='pbox'>

考虑  $\mathrm{null\ } T$  的基$u_1\ldots u_n$,并添加$v_1\ldots v_m$扩充到$U$的基.

考虑$Tv_1\ldots Tv_m$若线性相关,$\sum _{i = 1} ^{m}  c_iTv_i=0 \Rightarrow T\sum _{i = 1} ^{m}  c_iv_i=0$,则 $w=\sum _{i = 1} ^{m}  c_iv_i\in \mathrm{null\ } T,w=\sum _{i = 1} ^{m}  c_iv_i=\sum _{i = 1} ^{n}  d_iu_i$,与$u_i,v_i$构成一组基矛盾.

于是$Tv_i$线性无关,且容易注意到任意$w\in U,Tw=\sum_{i=1}^n c_iTu_i+\sum_{i=1}^m d_iTv_i=\sum_{i=1}^md_iTv_i\in \mathrm{span\ } (Tv_1\ldots TV_m)$故得证.

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
\begin{array}{c}
\dim  U/V=\dim U-\dim V
\end{array}
$$

</div>

<div class='pbox'>

定义 $T\in \mathcal{L}( U , U/V )$ 为商变换,把$u$映射到$u+V$.

则

$$
\begin{array}{c}
\mathrm{null\ } T=V \\
\mathrm{range\ } T=U/V 
\end{array}
$$

套用上面值域和零空间的维数公式即可.

</div>

#### 线性映射的矩阵

<div class='dbox'>

矩阵

选取$U,V$分别一组基$u_1\ldots u_m$,$v_1\ldots v_n$,可以把线性变换$T$写成$n\times m$的矩阵$\mathcal{M}(T,u_1\ldots u_m,v_1\ldots v_n)=A_{n\times m}$满足

$$
\begin{array}{c}
Tu_i=\sum_{j=1}^n A_{j,i}v_j
\end{array}
$$

</div>

即每一列是一个基向量在像空间中的基的表示.然后有的时候也直接简写$\mathcal M(T)$.

矩阵可以这么定义因为线性变换的线性保证了你可以只用基的变换去描述它,同时基的这种变换也能唯一确定线性变换.

于是可以定义矩阵运算:

<div class='dbox'>


$$
\begin{array}{c}
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
\begin{array}{c}
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
\begin{array}{c}
T_{/U}\in \mathcal L( V/U , V/U ),(T_{/U})(v+U)=(Tv+U) \\
T\vert_U \in \mathcal L( U , U ), T\vert_U v=Tv
\end{array}
$$

</div>

显然$T\vert_U$要求了$U$是不变子空间.

把算子放到更小的空间去研究的方式.


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
\begin{array}{c}
\forall f \in V',T'f=fT
\end{array}
$$

</div>

$T'$是反的可以理解因为$V'$的泛函的输入才是$T$的输出.导致没法根据这几个东西定义一个正的出来.

然后对偶主要解释了:$\mathcal M( T' ) =\mathcal M( T )^{T}$(右上角的$T$是转置的意思).

<div class='cbox'>

对偶映射的运算
$$
\begin{array}{c}
(ST)'=T'S' \\
(S+T)'=S'+T' \\
(\lambda S)'=\lambda S'
\end{array}
$$
</div>

<div class='pbox'>

$$
\begin{array}{c}
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
\begin{array}{c}
\dim U+\dim U^0=\dim V
\end{array}
$$

</div>

<div class='pbox'>

取$U$的基$u_1\ldots u_n$扩充到$V$的基$u_1\ldots u_n,u_{n+1}\ldots u_{n+m}$.并取$V'$的标准基$\varphi_i u_j =[i=j]$,则显然$f\in U^0$要求$f$不能有$\varphi_i,i<n$的分量,而任意$i>n$的分量都可以有.于是得证.

</div>

<div class='cbox'>

$$
\begin{array}{c}

\mathrm{null\ } T'=(\mathrm{range\ } T)^0 \\

\mathrm{range\ } T'=(\mathrm{null\ } T)^0

\end{array}
$$

</div>

<div class='pbox'>

考虑$T'fu=fTu=0$关于所有$u$成立,则$f$的范围是什么.看右侧显然是 $(\mathrm{range\ } T)^0$ 看左侧则是 $(\mathrm{null\ } T')^0$.于是得证.

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

又因为单射等价于 $\mathrm{null\ } T=0$ 所以 $(T-\lambda I)v=0$ 和它不是单射等价.

</div>

<div class='cbox'>

不同本征值对应对本征向量线性不相关.

</div>

<div class='pbox'>

反证,你要利用不同本征值这个性质,于是你设 $v_n \in \mathrm{span}( v_1\ldots v_{n-1} )$ 且$n$为满足条件对最小的.

$$
\begin{array}{c}
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

<div class='dbox'>


考虑

$$
\begin{array}{c}
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
\begin{array}{c}
\mathcal M( T,u_1\ldots u_n ) \text{is upper triangular matrix} \\
\Leftrightarrow \forall i, Tu_i\in \mathrm{span}( u_1\ldots u_i )  \\
\Leftrightarrow \forall i, \mathrm{span}( u_1\ldots u_i ) \text{is invariant space} 
\end{array}
$$

</div>

<div class='pbox'>

感觉是显然的.

</div>

那么考虑什么样的线性映射$T$有一组基$u_1\ldots u_n$有上三角矩阵$A_{n\times n}$.

<div class='cbox'>

$$
\begin{array}{c}
\forall T\in \mathcal L( V , V ), V \text{ is complex vector space} \\
\Rightarrow \exists u_1\ldots u_n,\mathcal M( T,u_1\ldots u_n ) \text{ is upper triangular matrix}
\end{array}
$$

</div>

<div class='pbox'>

Proof 1

归纳,假设对任意维数小于$\dim V$的空间成立,考虑取$T$的任意本征值$\lambda$,则 $U:=\mathrm{range\ } T-\lambda I$,则因为$T$不是单的所以 $\dim U<\dim V$.且 $\forall u \in U,Tu=(T-\lambda I)u+\lambda u\in U$,所以$T$在$U$不变.

于是可以应用归纳结假设,$T\vert_U$在$U$上有一组基$u_1\ldots u_n$使得 $\mathcal M( T\vert_U,u_1\ldots u_n )$ 是上三角矩阵.

将这组基扩展到$V$上成为$u_1\ldots u_n,v_1\ldots v_m$,则对$\forall i$,$Tv_i=(T-\lambda I)v_i+\lambda v_i\in \mathrm{span}( u_1\ldots u_n ) +\mathrm{span}( v_i )\subset \mathrm{span}( u_1\ldots u_n,v_1\ldots v_i )$,于是是上三角矩阵.

</div>

<div class='pbox'>

Proof 2

同样归纳,取任意本征向量 $u,U:=\mathrm{span}( u )$,考虑$T_{/U}$是维数为  $\dim V-1$ 的空间$V/U$上算子.则它有上三角矩阵.于是存在$v_1+U\ldots v_n+U$,使得 $\forall v+U\in V/U,T_{/U}(v+U)\in \mathrm{span}( v_1+U,\ldots,v_n+U )$,也就有$Tv\in \mathrm{span}( v_1,\ldots,v_n )$.

然后现在把$v_1\ldots v_n,u$作为新的基,容易发现 $Tu=\lambda u\in \mathrm{span}( v_1,\ldots,v_n,u )$满足条件.于是存在上三角矩阵.

</div>

都要从维度归纳,第二个自然一点吧:商空间就是抹去若干维度.

[think] 但是第一个从$T-\lambda I$的值域出发是什么个意思?主要利用两个性质:是不变子空间,以及$Tv=(T-\lambda I)v+\lambda v$.是不是相当于把其他向量也拆的"像"本征向量了.


<div class='cbox'>

$T$有逆等价于$T$的上三角矩阵对角线全部非$0$

</div>

<div class='pbox'>

先假设矩阵有逆,设空间$V$基为$v_1\ldots v_n$.

$$
\begin{array}{c}
Tv_1=A_{1,1}v_1 \Rightarrow A_{1,1}\ne 0 \\
Tv_k=u+A_{k,k}v_k,u\in \mathrm{span}( v_1\ldots v_{k-1} ) \\
\text{if } A_{k,k}= 0 \\
Tv_k\in \mathrm{span}( v_1\ldots v_{k-1} ) \\
\because v_1\ldots v_{k-1} \text{ is independent
}  \\
\therefore Tv_1\ldots Tv_{k-1} \text{ is independent, so it is a base}  \\
\therefore Tv_k \in \mathrm{span}( Tv_1\ldots Tv_{k-1} ) \\
\exists c \ s.t.\ 
\sum _{i = 1} ^{k}  c_iTv_i=0 \\
\stackrel{T^{-1}}{\Longrightarrow}\sum _{i = 1} ^{k}  c_iv_i=0 \\
\text{contradiction!} 
\end{array}
$$

再假设$T$关于$V$的基$v_1\ldots v_n$的矩阵为上三角矩阵且对角线元素非$0$.

那么我们知道$Tv_i=A_{i,i}v_i+\sum_{j=1}^{i-1}c_jTv_{j-1}$,其中后一项属于 $\mathrm{span}( v_1\ldots v_{i-1} )$,于是容易发现$Tv_1\ldots Tv_n$线性独立,是一组基,于是$T$是满的,于是$T$可逆.


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
\begin{array}{c}
E(\lambda,T)=\mathrm{null\ } T-\lambda I
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

todo [think] 定性

<div class='cbox'>

- 内积$<u,v>$关于$u$也是线性的.
- $<u,0>=<0,u>=0$

</div>

<div class='pbox'>

第一条用共轭对称性换到后面再换回来:
$$
\begin{array}{c}
a<u_1,v>+b<u_2,v>=a \overline{ <v,u_1> } +b \overline{ <v,u_2> }  \\
=\overline{ <v,au_1+bu_2> }  \\
=<au_1+bu_2,v>
\end{array}
$$

第二条考虑线性映射$0$映到$0$.

</div>

<div class='dbox'>

范数

$\vert\vert v \vert\vert = <v,v>$定义为向量的范数.

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

$<u,v><\vert\vert u \vert\vert \vert\vert v \vert\vert$

</div>

<div class='pbox'>

$$
\begin{array}{c}
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
\begin{array}{c}
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

考虑刚才的构建过程里,每个 $\mathrm{span}( u_1\ldots u_i )$都没有改变,所以是显然的.

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
\begin{array}{c}
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

则容易发现 $U^{\perp}=\mathrm{span}( v_1\ldots v_m )$.

然后第一条是显然的.第二条的话你把$U^{\perp}$的基扩充到$V$的时候扩充$u_1\ldots u_n$就也是显然的.

</div>


<div class='dbox'>

正交投影

$$
\begin{array}{c}
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

### 自伴算子,正规算子

<div class='dbox'>

伴随

对于算子$T$,若$\forall u,v$,$<Tu,v>=<u,T^*v>$,则$T^*$是$T$的伴随.

</div>

<div class='cbox'>

- $(S+T)^*=S^*+T^*$
- $(\lambda T)^*=\lambda T^*$
- $(ST)^*=T^*S^*$
- $T^*^*=T$
- $\mathrm{null\ } T*=\mathrm{range\ } T)^{\perp}$

</div>

<div class='pbox'>

前三个用定义带进去即可.

第四个,$<u,T*v>=<Tu,v>=\overline{ <T*v,u> } = \overline{ <v,Tu> } =<Tu,v>$

第五个,考虑是右边对任意$u$,$<Tu,w>=0$的所有$w$,$<Tu,w>=<u,T*w>$,故 $w\in \mathrm{null\ } T*$

</div>

<div class='cbox'>

$$
\begin{array}{c}
\mathcal M( T^*, v_1\ldots v_m, u_1\ldots u_n) = \overline{ \mathcal M( T ,u_1\ldots u_n,v_1\ldots v_m)^T  }  \\
(v_1\ldots v_m),(u_1\ldots u_n) \text{ are regular orthogonal bases} 
\end{array}
$$

右边说的是转置再把每一项共轭.

</div>

<div class='pbox'>

$$
\begin{array}{c}
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

<div class='dbox'>

自伴算子

$T=T^*$

</div>

所以这个也是我们实对称矩阵啊.

<div class='cbox'>

$$
\begin{array}{c}
T=T^* \Rightarrow \begin{cases}
T\text{'s eigenvalues}\in R  \\
\forall v,<v,Tv> \in R \\
<v,Tv>=0 \Rightarrow T=0
\end{cases}

\end{array}
$$

</div>

所以说书说伴随类比共轭,自伴算子类比实数啊.

<div class='pbox'>

todo

</div>

<div class='dbox'>

正规算子

$$
\begin{array}{c}
T \text{ is normal} \Leftrightarrow  TT^*=T^*T
\end{array}
$$

</div>

<div class='cbox'>

$$
\begin{array}{c}
T \text{ is normal} \Leftrightarrow \forall v,\vert\vert Tv \vert\vert = \vert\vert T^*v \vert\vert 
\end{array}
$$

</div>

<div class='pbox'>

todo

</div>


<div class='cbox'>

$$
\begin{array}{c}
T \text{ is normal}, \lambda \text{is eigen value of } T  \\
\Rightarrow \lambda \text{is eigen value of } T^* 
\end{array}
$$

</div>

<div class='pbox'>

todo

</div>

<div class='cbox'>

$$
\begin{array}{c}
T \text{ is normal} \Rightarrow \text{eigen vectors of } T \text{ are orthogonal} 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{c}
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

取一个规范的本征向量,把它作为基的第一个向量$n_1$,设  $U=\mathrm{span}( n_1 )$,则$T$在$U$上不变.

注意到

<div class='cbox'>

$$
\begin{array}{c}
u\in U \Rightarrow Tu\in U \\
\Leftrightarrow v\in U^{\perp},Tv\in U^\perp
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{c}
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
\begin{array}{c}
f(x)=a\prod_i (x-\lambda_i)\prod_i (x^2+b_ix+c_i) \\
f(T)v=a\prod_i (T-\lambda_i I)\prod_i (T^2+b_iT+c_iI)v=0
\end{array}
$$

由于$T^2+b_iT+c_i$不可分解,有$b_i^2-4c<0$

我们假设$T$没有本征值,则$T-\lambda_i I$是单的.

而 

$$
\begin{array}{c}
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
