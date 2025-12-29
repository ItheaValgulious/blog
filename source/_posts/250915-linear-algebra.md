---
title: Linear Algebra
tags:
  - math
  - linear-algebra
  - note
date: 2025-09-15 07:55:19
---
# Linear algebra

## A fun question

<div class='cbox'>

In n-D space we can found at most $n+1$ vector $v_1\ldots v_{n+1}$ such that:  $\forall i\ne j,v_iv_j<0$

</div>

<div class='pbox'>

### An example in 3-D space(the one on the book)

The construction is Obviously($CH_4$)

Chosen a vector, the others must be in a semisphere. We say two semisphere is seperated by plane A.

And we notice that: if two vector's shadow on plane A construct a acute angle, their dot product must be positive, transformed it into a 2-D problems which is easy to solve.

### Generalize to n-D

We choose a vector $v_1$, and it can be written as $[1,0,\ldots 0]$(with some rotation)

so $\forall  v_i,i>1, v_iv_1<0 \Rightarrow v_{i,1} < 0 \Rightarrow v_{i,1}v_{j,1}>0 \Rightarrow v_iv_j-v_{i,1}v_{j,1} < 0$

then transformed it into the (n-1)-D situation.

The construction can be easily give during the induction

### Another Proof

given by Bing!

#### Lemma: Radon Partition

<div class='cbox'>

In n-D space, $n+2$ point could be divided to two convex hull with intersection.

</div>

<div class='pbox'>

$n+2$ vector must be dependent: $\exists c_i \ s.t.\ \sum _{i=1}^{n+2} c_i x_i = 0; \sum_i x_i = 0$(the second condition can be satisfied by add another all-1 dimension).

so divide the vector by sign of $c_i$ we got:$v=\sum_{i\in A} c_i x_i = \sum_{j\in B} c_jx_j$,so divide the eqution by $\sum_{i\in A} c_i$, you get one point($v$) in the intersection.

</div>

We noticed $0<v^2=(\sum_{i\in A} c_i x_i) \cdot (\sum_{j\in B} c_jx_j)<0$, contradiction!

</div>

## Operator's Left Inverse and Right Inverse

### Existance

<div class='cbox'>

对算子$T$来说,左逆存在等价于右逆存在.

</div>

<div class='pbox'>

#### Proof 1

注意到左逆存在等价于$T$是单射,右逆存在等价于$T$是满射.

又因为$T$单射等价于$T$满射等价于$T$双射,所以左逆存在等价于右逆存在且两个逆一定相同.

#### Proof 2

左逆推出$T$分解成初等行变换矩阵,然后一个一个取逆推右逆.

</div>


## Union of finite count of proper sub-space isn't V 

<div class='cbox'>

$$
\begin{gathered}
F \text{ is inifinite Field} \\ 
\forall U_1\ldots U_k,U_i \text{ is subspace of } V(F) \\
V\ne \bigcup_{i=1}^k U_i
\end{gathered}
$$

</div>

<div class='pbox'>

考虑归纳,$k=1$成立,设$k-1$个不行,反证,那么可以取$v\notin \bigcup_{i=1}^{k-1} U_i$,必有$v\in U_k$.

再取$u\notin U_k$,令 $S=\{ u+iv \vert i \in R\}$,则对$j<k$,每个$U_j$至多包含一个$S$中的向量(否则$v\in U_j$),而$U_k$必然没有$S$中向量(否则$u\in U_k$),而$S$中有无限个向量,于是$S$不可能被他们包含,得证.

</div>

[think] 而这个定理甚至在有限域下有反例.

## CR分解

<div class='dbox'>

Row Reduced Echelon Form

- 每一行的首个非零元素是 1，这个元素称为“主元”（pivot）。
- 每个主元所在列的其他元素都是 0，也就是说主元是该列唯一的非零元素。
- 每个主元都在其所在行的右边位置，相对于上一行的主元。
- 所有零行（即整行都是 0）都排在非零行的下面

$A$的Row Reduced Echelon Form记为$\operatorname{rref}(A)$

</div>

<div class='cbox'>

设$B=\operatorname{rref}(A)$的主元所在列构成集合$S={i\vert \text{a pivot is in } i}$,设$A=[a_1\ldots a_n]$,则$C=[a_i \vert i \in S]$,$R=B_{1~\operatorname{rank}A,1~m}$(即去除所有全$0$行),满足$A=CR$.

</div>

<div class='pbox'>

我们把它看成用$R$组装$C$的列,那么进行初等行变换不改变列之间的线性关系.

而消元之后呢,看列的话主元所在列显然是标准基,那命题是显然的了.

</div>

## 秩分解

<div class='cbox'>

$A_{n\times m}=P_{n\times n}B_{n\times m}Q_{m\times m}$,其中$B$为只有左上角是一个 $\operatorname{rank} A\times \operatorname{rank} A$ 的单位矩阵其他位置全是$0$.

</div>

<div class='pbox'>

$A$做行变换+列变换消元易得.

能不能换个视角,这个是不是在说,对 $T\in \mathcal L( V , W )$,存在一个$V$的一个基$v_1\ldots v_n$,$W$的一个基$w_1\ldots w_m$使得 $Tv_i=[i\le \operatorname{rank} T]w_i$.

那么先构造$v$,我们先找一个 $\operatorname{null} A$的基$v_{n-r+1}\ldots v_n$,然后再任意扩充出剩下的$v_1\ldots v_n$.

对$w$,显然$Tv_1\ldots Tv_r$线性无关,再扩充$w_{r+1}\ldots w_m$得到一组基.

显然这组基满足需求.

[think] 还是对矩阵基变换理解不到位.

</div>

注意我们把上面那个再搞一搞:$P$的后$m-r$列是没用的,$Q$的后$m-r$行是没用的,都丢到会得到$P=CR$.

而 $P=CR=[c_1\ldots c_r] [r_1^T\ldots r_n^T]^T=\sum _{i = 1} ^{n}  c_ir_i^T$,其中每个$c_ir_i^T$秩为$1$.这就是秩分解的名字.

## Ax=B有解

$$
\begin{gathered}
\exists x,Ax=b \\
\Leftrightarrow \operatorname{rank} A=\operatorname{rank} [A,b] \\
\Leftrightarrow b\in \operatorname{range} A
\end{gathered}
$$

解唯一等价于$\operatorname{null} A=0$等价于$n=\operatorname{rank} A$


## A quiz problem

<div class='cbox'>

$$
\begin{gathered}
A \text{ is a real matrix} , \\
A^TAu=0 \Rightarrow Au=0
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
A=\mathcal M( T )  \\
T^*Tu=0 \\
\Leftrightarrow \forall v,<v,T^*Tu>=0 \\
\Leftrightarrow \forall v,<Tv,Tu>=0 \\
\Leftrightarrow Tu\in (\operatorname{range} T)^\perp \\
\because Tu\in \operatorname{range} T \\
\therefore <Tu,Tu>=0,u=0
\end{gathered}
$$

</div>

[think] 被这个题击败了,当时只想到用 $\operatorname{null} T^*=(\operatorname{range} T)^{\perp}$了,但其实是可以简单翻译过来的.

伴随和共轭转置的关系其实是显然的,内积上伴随的性质也是显然的,所以基础操作没必要用结论.做题的时候错误的感觉算子伴随和矩阵转置的距离过远(因为done right中证明是表示成规范正交基然后拆开用内积的性质,但是不看那套框架的话其实是显然的,另外对$U\oplus U^\perp=V$的证明掌握不好).同时左零空间.

总结就是记住了几何那边的结论但没有很好的联系到代数这边.

## Several Inequations about Rank

<div class='cbox'>

$$
\begin{gathered}
\operatorname{rank} A+B \le \operatorname{rank} A+\operatorname{rank} B \\
\operatorname{rank} AB \le \min \operatorname{rank} A,\operatorname{rank} B \\
A_{m\times n}B_{n\times s}=0 \Rightarrow \operatorname{rank} A+\operatorname{rank} B\le  n
\end{gathered}
$$

</div>

<div class='pbox'>

Obviously

</div>






<div class='cbox'>

$$
\begin{gathered}
\operatorname{rank} AB\ge \operatorname{rank} A_{m\times n}+\operatorname{rank} B_{n\times s}-n
\end{gathered}
$$

</div>

<div class='pbox'>

### Sol 1

矩阵分解:

$$
\begin{gathered}
A=P_1 \begin{bmatrix}
  I_{r_1},0 \\
  0,0
\end{bmatrix}Q_1 \\
B=P_2 \begin{bmatrix}
  I_{r_2},0 \\
  0,0
\end{bmatrix}Q_2 \\
AB=P_1\begin{bmatrix}
  I_{r_1},0 \\
  0,0
\end{bmatrix}Q_1P_2\begin{bmatrix}
  I_{r_2},0 \\
  0,0
\end{bmatrix}Q_2
\end{gathered}
$$

显然$P_1,Q_2$不影响最终的秩直接扔了,而设$D=Q_1P_2=\begin{bmatrix}
  D_1,D_2 \\
  D_3,D_4
\end{bmatrix}$,那么你发现乘完只剩下$D_1$.

而删去矩阵一行或一列秩最多减少$1$,$D_1$看成$D$删掉了 $n-\operatorname{rank} A + n-\operatorname{rank} B$ 行或列得到的.同时 $\operatorname{rank} D=n$,得证.

### Sol 2

考虑

$$
\begin{gathered}
C=\begin{bmatrix}
  I_n,0 \\
  0,AB
\end{bmatrix}
\end{gathered}
$$

显然 $\operatorname{rank} AB+n=\operatorname{rank} C$

对它做行变换可以得到

$$
\begin{gathered}
C \to \begin{bmatrix}
  I_n,0 \\
  A,AB
\end{bmatrix} \\
\to \begin{bmatrix}
  I_n,-B \\
  A,0
\end{bmatrix}=D \\
\end{gathered}
$$

而观察这个$D$容易发现 $\operatorname{rank} D\ge \operatorname{rank} A+\operatorname{rank} B$,于是得证

### Sol 3

考虑我们要证明 $\dim \operatorname{range} AB\ge \dim \operatorname{range} B-\dim \operatorname{null} A$

考虑为什么 $\operatorname{range} B\ne \operatorname{range} AB$,是因为 $\operatorname{range} B$中的不同元素被合成了一个,而这个合成相当于把 差是 $\operatorname{null} A$中的元素的多个元素合成一个.所以有

$$
\begin{gathered}
\dim (\operatorname{range} B)/(\operatorname{range} B\cap \operatorname{null} A)=\dim \operatorname{range} A
\end{gathered}
$$

</div>

显然交集小于 $\operatorname{null} A$ ,得证.

<div class='cbox'>

$$
\begin{gathered}
\operatorname{rank} AC+\operatorname{rank} CB\le \operatorname{rank} C+\operatorname{rank} ACB
\end{gathered}
$$

</div>

<div class='pbox'>

这个结论可以直接由上一个的Sol3弄出来,考虑

$$
\begin{gathered}
\begin{bmatrix} C,0 \\
0,ACB \end{bmatrix}
\end{gathered}
$$

可以简单消元变成

$$
\begin{gathered}
\begin{bmatrix} C,CB \\
AC,0 \end{bmatrix} 
\end{gathered}
$$

于是直接得证.

</div>

[think] 学会这种拼成空间再分块矩阵消元的套路.

<div class='cbox'>

$$
\begin{gathered}
A^2=I \\
\Rightarrow \operatorname{rank} (A-I)+\operatorname{rank} (A+I)=n
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
(A-I)(A+I)=0  \\
\Rightarrow \operatorname{rank} (A-I)+\operatorname{rank} A+I \le n \\
(A+I) - (A-I)=2I  \\
\Rightarrow \operatorname{rank} (A+I)+\operatorname{rank} (A-I)\ge n
\\
\text{Q.E.D}
\end{gathered}
$$

</div>

## Eular Formula

<div class='cbox'>

对平面图$\text{Graph}(n,m)$有$F$个面(不含最外面),证明

</div>

<div class='pbox'>

首先考虑无向图的 Incidence Matrix $M$,容易注意到$M$中的若干行线性无关等价于这个导出子图无环.

于是看出 $\operatorname{rank} M=n-c$,$c$为连通块个数.

又能看出 $v\in \operatorname{null} M^T$等价于$v$中的若干条边串成若干个环,会发现 $\dim \operatorname{null} M^T=F$



</div>

## An Ex Problem

<div class='cbox'>

$$
\begin{gathered}
M=\begin{bmatrix} A,C \\0,B \end{bmatrix}  \\
\operatorname{rank}  M=\operatorname{rank}  A+\operatorname{rank}  B \Leftrightarrow \exists X,Y:AX+YB=C
\end{gathered}
$$

</div>

<div class='pbox'>

首先右推左是显然的.直接消元一下就好了.考虑左推右.

考虑

$$
\begin{gathered}
A:U_1\to V_1,B:U_2\to V_2,C:U_2\to V_1 \\
M:U\to V
\end{gathered}
$$

分解

$$
\begin{gathered}
\operatorname{range} M=\operatorname{range} B\oplus W \\
W=\{ [v,0] \vert [v,0]\in \operatorname{range} M \}  \\
\end{gathered}
$$

那么因为 $[v,0]\in \operatorname{range} M$,则必然是 $[v,0]=M[u_1,u_2]^T$,一定是$Bu_2=0,Au_1+Cu_2=v$.

于是 $W=\operatorname{range} A + C(\operatorname{null} B)$.又因为 $\dim W=\dim \operatorname{range} A$,于是有 $C(\operatorname{null} B) \subset \operatorname{range} A$.

我们再分解 $U_2=\operatorname{null} B \oplus U_3$,此时注意到$B$在$U_3$到 $\operatorname{range} B$是双射,存在$Y',\forall u,YBu=Cu$.然后通过扩充基并任意取值将$Y'$的定义域扩充到$V_2$得到$Y$.

于是$(C-YB)u$对任意$u\in U_3$为$0$,于是 $\operatorname{range} (C-YB)=(C-YB)\operatorname{null} B= C(\operatorname{null} B)$.

现在只考虑 $u\in \operatorname{null} B$,显然$\exists v,Cu=Av$,那么对 $\operatorname{null} B$的一组基$u_1\ldots u_k$这样确定$v_1\ldots v_k$,就可以构造$X'u_i=v_i$满足$Cu=AX'v$.再用同样的方法扩充基并任意取值将$X'$的定义域扩充到$U_2$得到$X$.

于是$C=YB+AX$

</div>

[think] 感觉得到 $C(\operatorname{null} B)=A$这里是容易的.然后这里进行不下去,想到 $\operatorname{null} B$去分解也是自然的. 分解后就要想办法把 $\operatorname{null} B$之外的影响消掉,就用了$C-YB$.而若 $\operatorname{range} A\subset \operatorname{range} B$那么$Ax=BTx$是显然的.

## 投影

<div class='bbox'>

向一个向量投影

$$
\begin{gathered}
a,b\in R^n \\
\dfrac{<a,b>}{<a,a>} a = (\dfrac{a^Tba}{a^T a})= (\dfrac{a\cdot a^T}{a^T a}) b
\end{gathered}
$$

</div>

<div class='cbox'>

向一个平面投影(平面是$C(A)$)

$$
\begin{gathered}
p=A(A^TA)^{-1}A^Tb
\end{gathered}
$$

</div>

<div class='pbox'>

考虑$b$的投影$p\in C(A)$有$(b-p)\in C(A)^\perp$,于是$b-p \in N(A^T)$.

于是$A^Tb=A^Tp$,又$p\in C(A) \Rightarrow \exists x,Ax=p$.

于是$A^Tb=A^TAx$,$A$一定可以用一个满秩的,于是除过去.于是得证.

</div>



<div class='cbox'>

$$
\begin{gathered}
A^TAx=A^Tb
\end{gathered}
$$

一定有解

</div>

<div class='pbox'>

$$
\begin{gathered}
\operatorname{rank} (A^TA,A^Tb) \\
=\operatorname{rank} (A^T(A,b))\le \operatorname{rank} A \\
=\operatorname{rank} AA^T
\end{gathered}
$$

所以这个证明是依赖实数的.

[think] 复数你应该把$A^T$换成$\overline{A^T}$,或者说这个定理本来就应该是$\overline{A^T}$的.

</div>

<div class='cbox'>

$$
\begin{gathered}
P^2=P,P^*=P \Rightarrow P \text{ is a projection}
\end{gathered}
$$

</div>

<div class='pbox'>

显然那$P$只能说  $\operatorname{range} P$ 的投影.

只需证明  $\forall u,(Pu-u)\in (\operatorname{range} P)^\perp$.

$$
\begin{gathered}
\forall v,<Pu-u,Pv>=<PPu-Pu,v>=<Pu-Pu,v>=<0,v> \\
\Rightarrow Pu-u\in (\operatorname{range} P)^\perp
\end{gathered}
$$

得证!

</div>

## QR分解

<div class='cbox'>

$$
\begin{gathered}
\forall A,\exists Q \text{ is orthogonal matrix},R \text{ is upper triangle matrix} \\ s.t.\\ 
A=QR
\end{gathered}
$$

</div>

<div class='pbox'>

考虑$A$可以看成把标准基变成$a_1\ldots a_n$,那我们把$a_1\ldots a_n$这组基用Gram-Schmidt变成$b_1\ldots b_n$,问题就可以变成先把标准基变成$b$,再变成$a$,其中第一步是等距同构,第二步中我们知道$a_1\ldots a_i$和$b_1\ldots b_i$张成空间相同,所以第二步是上三角.

</div>

## determinance

<div class='cbox'>

$$
\begin{gathered}
\det A\det B=\det AB
\end{gathered}
$$

</div>

<div class='pbox'>

Sol1:分块矩阵.

Sol2:都拆成初等变换矩阵再乘.

Sol3:考虑定义函数 $\alpha(B)=\dfrac{\det BA}{\det A}$,容易验证它满足行列式三条公里,于是$\alpha(B)=\det B$

</div>

<div class='cbox'>

Laplace Theorem

$$
\begin{gathered}
\forall S\subset [1,n]\cap Z \\
\det A=\sum _{T\subset [1,n]\cap Z,\vert T \vert =\vert S \vert } A(S,T)C(S,T)
\end{gathered}
$$

其中$A(S,T)$表示子式,$C(S,T)$表示代数余子式

</div>

<div class='pbox'>

注意到你就是把$S$行对应的元素钦定的时候的某个组合,我们可以先用$\sum_{t\in T} t-\sum_{i=1}^{\vert T\vert}i+\sum_{s\in S} s-\sum_{i=1}^{\vert S\vert}i\equiv \sum_{t\in T}t+\sum_{s\in S}s \pmod 2$次交换把这些行列顺序不变的换到前  $\vert S \vert=\vert T \vert$ 行列,则最终符号显然就是此时的符号(即两个行列式内部的符号)再乘上交换操作的符号,于是得证.

</div>

<div class='cbox'>

求

$$
\begin{gathered}
\det M \\
M_{i,j} = \begin{cases}
a,i=j \\
b,i\ne j
\end{cases}
\end{gathered}
$$

</div>

<div class='pbox'>

### Sol1

考虑消元,注意到每行的和是一样的,所以我们把第一列变成所有列的和,然后用它去消后面的,模拟一下即可.

### Sol2

考虑$M=(a-b)I+xB$,其中$B=(b)_{i,j}$,应用公式

$$
\begin{gathered}
\operatorname{d} \det(M)=\operatorname{trace} (\operatorname{adj} A \operatorname{d} A)
\end{gathered}
$$

右边三项全是好算的,于是可以把导数对$x$积分积回去.

### Sol3

考虑$M=B+(a-b)I$,若$Bv=\lambda v,则显然有$(B+(a-b)I)v=(\lambda+a-b)v$,于是求出$B$的特征值,就可以直接得到$M$的特征值算行列式.

</div>

<div class='cbox'>

$$
\begin{gathered}
\operatorname{rank} A=a \\
\Leftrightarrow \begin{cases}
\vert T \vert =\forall \vert S \vert > a,\det A_{S,T}=0 \\
\exists \vert S \vert =\vert T \vert =a,\det A_{S,T}\ne 0
\end{cases}

\end{gathered}
$$

</div>

<div class='pbox'>

首先如果存在$\det A_{S,T}=\ne 0$,那么$S$对应的这些行必然是满秩的,所以 $\operatorname{rank} A\ge a$.

而如果 $\operatorname{rank} A>a$,那么选出$a$个线性无关行,再从这里面找到$a$个线性无关列,这就是一个行列式非$0$的矩阵.

于是得证.

</div>

<div class='cbox'>

$$
\begin{gathered}
\operatorname{rank} A=n-1 \Leftrightarrow \operatorname{rank} C=1 \\
\operatorname{rank} A<n-1 \Leftrightarrow \operatorname{rank} C=0
\end{gathered}
$$

</div>

<div class='pbox'>

由上一个conclusion,第二行是显然的(全0).

对于第一行,考虑$AC^T$=0,于是 $AC^T=0,\operatorname{rank} A+\operatorname{rank} C^T\le n$ ,又有 $\operatorname{rank} C\ne 0$ 因为至少有一个非$0$.

</div>

<div class='cbox'>

$$
\begin{gathered}
A_{m\times n},B_{n\times m},m\le n \\
\Rightarrow \det AB=\sum _{\vert S \vert =m,S\subset [1,n]} \det A_{[1,m]\cap Z,S}\det B_{S,[1,m]\cap Z}
\end{gathered}
$$

</div>

<div class='pbox'>

考虑矩阵

$$
\begin{gathered}
\det \begin{bmatrix}
  I_n&B \\
  A&0
\end{bmatrix}=\det
\begin{bmatrix}
  I_n&B \\
  0&-AB
\end{bmatrix}
\end{gathered}
$$

右边的行列式是$(-1)^m\det (AB)$,考虑左边用拉普拉斯定理,则显然你的子式的列只能选$A$里面的,而它的余子式就是$B$左边再加上若干列,若第$i$列没被子式选,则这列一定要选$i$行的元素,于是$B$中恰好只有$S$中的行能选.

对于符号,Laplace中的是$\sum_{i\in S} i+\dfrac{m(n+1+n+m)}2$,算代数余子式行列式的时候还有一个$\sum_{i\notin S} i-\dfrac{(n-m)(n-m+1)}2$,然后这些加起来是同余$m$的.

这样符号一乘正好是$0$.

</div>

行列式与导数:容易注意到行列式每行不会有两个乘到一起,而最终的行列式是$n$行各取一个数乘起来,于是遵循导数求导乘积的法则,或者说把每一行求导其他行不变再加起来.

## Another Quiz Problem

<div class='cbox'>

$$
\begin{gathered}
\forall A_{m\times n},\exists B_{n\times m}\ s.t.\ 
ABA=A
\end{gathered}
$$

</div>

<div class='pbox'>

### Sol 1

$$
\begin{gathered}
A=P\begin{bmatrix}
  I_k&0 \\
  0&0
\end{bmatrix}Q
\end{gathered}
$$

于是让

$$
\begin{gathered}
B=Q^{-1}\begin{bmatrix}
  I_k&0 \\
  0&0
\end{bmatrix}P^{-1}
\end{gathered}
$$

### Sol 2

考虑一个任意情况,对任意集合$X,Y$和任意映射$f$,你可以找到一个$g$使得$f\circ g\circ f=f$

显然的,因为你可以让$g$把$f$的像映射到任意一个原像.

那么这个显然的在说什么呢?它实际上在说,对任意一个$f$,我们可以找到$X,Y$各自的一个子集$X',Y'$,使得$f$限制在$X'\to Y'$是双射.于是$g$是这上面的逆,而这之外的随意映射就可以满足$fgf=f$.

然后你再看第一个证明,那么中间那个有$I_k$的矩阵实际上就是,$I_k$对应了$X'\to Y'$的双射部分,这也是上面的做法为啥有道理.

</div>

## Circulant Matrix's det

<div class='cbox'>

$$
\begin{gathered}
\forall a_0\ldots a_{n-1} \\
A_{i,j}=a_{i+j-2\bmod n} \\
\Rightarrow \det A=\prod _{i = 1} ^{n} \sum _{j = 1} ^{n} w_n^{ij}c_j
\end{gathered}
$$

</div>

<div class='pbox'>

首先我们让$P_n$是循环移位$P(x_0,\ldots, x_n)=(x_1,\ldots, x_n,x_0)$,那么有

$$
\begin{gathered}
A=\sum _{i = 0} ^{n-1}  a_iP^i
\end{gathered}
$$

那么因为所有$P$乘法的时候是保持不变子空间的,也就是说$A$的特征值就是$P$的特征值带入$f(x)=\sum_{i=0}^{n-1}a_ix^i$,所以只需要看$P$的特征值.

考虑$Px=\lambda x$,那么$x_{i+1\bmod n}=\lambda x_i$,于是你乘一圈就有$\lambda^n=1$,能相应的构造出$x_i=w_n^{il},\lambda=w_n^l$这样的特征向量和特征值.

于是$P$的特征值就是单位根,带进去就得证.

</div>

## A Determinance about Vandermonde plus 1

<div class='cbox'>

求

$$
\begin{gathered}
\det A,A_{i,j}=x_i^j+1
\end{gathered}
$$

</div>

<div class='pbox'>

容易想到用线性性去拆分,如果我们对列拆分,你发现你就是要求$A$有一列换成全$1$之后的矩阵的行列式的和,我们设第$i$列换掉之后的矩阵是$B_i$.

考虑Cramer's Rule,你注意到设$Ay=b$,其中$b$是全$1$向量,则$y_i=\dfrac{\det B_i}{\det A}$,于是我们实际上是求$y_i$,

如果我们这里用$y=A^{-1}b$我们可以得到一个结论:

$$
\begin{gathered}
\det(A+uv^T)=\det A(1+v^TA^{-1}u)
\end{gathered}
$$

然后对这个题,我们也不知道$A^{-1}$,所以你仍然要想办法求$y_i$.

碰到范德蒙德矩阵一定要想多项式,于是你想到$P(z)=\sum_{i=1}^n y_iz^i$,则$P(x_i)=1$,于是$P(z)=A\prod_i (z-x_i)$,于是你能通过比较常数项求出$A$,然后再计算$P(1)$就能求出$\sum y_i$了.

</div>

[think] 碰到范德蒙德矩阵一定要想多项式

<div class='cbox'>

$$
\begin{gathered}
\det(A+uv^T)=\det A(1+v^TA^{-1}u)
\end{gathered}
$$

</div>

<div class='pbox'>

一个是上面提到的证法.

或者考虑

$$
\begin{gathered}
\det(I+uv^T)=(1+v^Tu)=(1+u^Tv)
\end{gathered}
$$

这个可以直接考虑$uv^T$特征值是$n-1$个$0$和一个$v^Tu$(对应特征向量$u$).
$A^{-1}v^T$

然后$\det (A+Auv^T)=\det A(1+u^Tv)$

所以让$u'=A^{-1}u$,那么式子就成了$\det (A+u'v^T)=\det A(1+v^TA^{-1}u')$.即我们所证的.

</div>


## about eigen values

<div class='cbox'>

相似矩阵有相同的特征多项式

</div>

<div class='pbox'>

$$
\begin{gathered}
\det QAQ^{-1}-\lambda I \\
=\det QAQ^{-1}-Q\lambda I Q^{-1}  \\
= \det Q(A-\lambda I)Q^{-1} \\
=\det A-\lambda I
\end{gathered}
$$

</div>

显然的吧,因为都是一个线性变换在不同的基下的.

<div class='cbox'>

对称矩阵的特征向量一定垂直

</div>

<div class='pbox'>

首先你可以谱定理启动.

否则考虑

$$
\begin{gathered}
v_1Av_2=v_1\lambda_2 v_2 \\
(v_1Av_2)^T=\lambda_1 v_1v_2
\end{gathered}
$$

于是就得证了.

</div>


<div class='cbox'>

特征多项式的$n-i$项系数等于:$(-1)^i\times \text{sum of all A's principle minor of order i}$

</div>

<div class='pbox'>

观察$A-\lambda I$显然.

</div>

## 实谱定理(矩阵版)

<div class='cbox'>

任意对称矩阵$A$可以写成$A=PDP^{-1}$,其中$D$是对角矩阵,$P$是正交矩阵.

</div>

<div class='pbox'>

首先复化,考虑$A$的一组特征值特征向量$Av=\lambda v$,则 $v^TA\overline{v}=\overline\lambda \vert\vert v \vert\vert$,同时取共轭得这个还等于 $\lambda \vert\vert v \vert\vert$,于是能证明$\lambda \in R$.

然后我们说明了$A$的特征值都是实的,我们取$v_1$是一个特征值,并将其扩充到一组标准正交基$v_1,v_2\ldots v_n$,于是

$$
\begin{gathered}
A[v_1\ldots v_n]=[v_1\ldots v_n]
\begin{bmatrix}
\lambda_1&x \\
0&A_1
\end{bmatrix}
\end{gathered}
$$

其中$x$和$A_1$是任意向量/矩阵,而中间$v_1\ldots v_n$是一个正交矩阵设为$B$,则右边那个分块矩阵是$B^{-1}AB=B^TAB$,于是这个也是对称的,从而$x=0$,$A_1$是对称矩阵,从而可以归纳到$n-1$维.归纳得证.

这里$x=0$就是$T$在$U^\perp$不变,$A_1$对称就是$T$限制仍然是自伴.

</div>

## 二次型

### 惯性定理 Inertia Theorem

<div class='cbox'>

任意二次型$A$通过任意可逆矩阵$P$合同变换到对角矩阵$PDP^T$,$D$的对角线上$0$的个数,正数个数,负数个数都是确定的(与$P$无关).

</div>

<div class='pbox'>

首先$0$的个数是确定的,因为这是矩阵的秩.

考虑在两组基下,假设它们对角型正数的个数分别为$a,b$,负数是$r-a,r-b$,不妨设$a<b$.

那么我们不考虑$0$的那部分限制到$r$维的空间上考虑,则你可以找到一个$a$维的空间,上面值都是正的(要求所有负惯性指数位置都是负的),再找一个$r-b$上面都是负的.而$a+r-b>r$所以这俩空间有交,爆炸了.

[think] 注意到正惯性指数是最大的子空间满足这里面的值带进去都是正的.

</div>

<div class='cbox'>

所有顺序主子式大于$0$等价于正定

</div>

<div class='pbox'>

考虑对角化的过程,如果已经消除了左上角$k\times k$的矩阵,接下来这些地方就不会动了.然后你消$(k+1)\times (k+1)$的左上角,注意到我们前面已经进行的行列变换都是在前$k$行进行的,所以前面所有的操作都不会改变当前$(k+1)\times (k+1)$矩阵的行列式,直到你消完.于是每个顺序主子式对应的子矩阵消前和消后的行列式是一样的.

</div>

## SVD

### PCA(主成分分析)

你有若干个向量$a_i$(若干个点)

先让$a$都减去平均值得到$a'$令$A=[a_1'\ldots a_n']$,令$B=AA^T$,你发现$B_{i,j}=\operatorname{Var}(x_i,x_j)$(两维的协方差.)

<div class='cbox'>

对$A$进行SVD分解$A=UDV$,则若$s_1$对应的方向$v_1$,直线$tv_1$是最小化每个点到直线距离(垂线段距离)平方的直线.

</div>

<div class='pbox'>

设最优方向为单位向量$n$.

$$
\begin{gathered}
L=\sum (x_i-n<x_i,n>)^2 \\
=\sum a_i^2+n^2<a_i,n>^2-2<a_i,n><a_i,n> \\
=(\sum a_i^2)-(\sum_i<a_i,n>^2)
\end{gathered}
$$

只要最大化第二项.考虑

$$
\begin{gathered}
\sum_i <a_i,n>^2 \\
=n^T(\sum a_i a_i^T)n \\
=n^T(AA^T)n
\end{gathered}
$$

这是二次型,把$AA^T$谱分解就看出显然最大值在它最大的特征值对应特征向量方向,也就是$v_1$方向.

你还可以看出这个值是$\sum a_i^2-s_1^2$

</div>

### SVD求伪逆

$A=U\Sigma V^T$,$A^+=V\Sigma^+ U^T$,其中$\Sigma^+$是把所有非零对角线元素变成倒数再取转置.

### 用SVD逼近

<div class='cbox'>

$$
\begin{gathered}
A=UDV^T=\sum_i u_is_iv_i^T \\
\Rightarrow \min_{\operatorname{rank} C=k} \Vert A-C \Vert =  s_{k+1}
\end{gathered}
$$

</div>

<div class='pbox'>

设$A_{m\times n},V_{n\times n},U_{m\times m},D_{m\times n}$

考虑对$A$分解得$A=UDV^T$,则我们让$D$只保留前$k$个特征值,其余设为$0$得到$D'$,令$C=UD'V^T$,则显然$A-C$的SVD分解就是$U(D-D')V^T$,其最大的奇异值恰为$s_{k+1}$(就是只用前$k$个奇异值去逼近啦).

然后只需要证明这是最小值.考虑$A$的前$k+1$个右奇异向量($v_1\ldots v_k$)张成的子空间和$B$的零空间的交( $\dim \operatorname{null} B=n-\operatorname{rank} B=n-k$,故必然有交)中的单位向量$x$.

而

$$
\begin{gathered}
\Vert (A-B)x \Vert^2  \\
=\Vert Ax \Vert^2  \\
=x^TA^TAx \\
=x^TVD^2V^Tx \\
=(V^Tx)^TD^2(V^Tx) \\
\ge s_{k+1}^2
\end{gathered}
$$

于是得证.

</div>

[think] 证明最小化的时候从分析矩阵结构改为找一个向量.因为这个向量显然一定可以在前$k+1$维(这个每个维度都放大需求倍数的空间中任何一个向量也都被放大需求倍数).

## 多项式

### 有理域可约多项式

<div class='dbox'>

$$
\begin{gathered}
f(x)= \sum _{i = 0} ^{n}  a_ix^i \text{ is primitive }  \\
\Leftrightarrow \gcd(a_0,\ldots ,a_n)=1
\end{gathered}
$$

</div>



<div class='cbox'>

Gauss's Lemma

$$
\begin{gathered}
f,g \text{ are primitive } \Rightarrow fg \text{ are primitive} 
\end{gathered}
$$

</div>

<div class='pbox'>

考虑反证,如果$fg$有公质因数$p$,且$p\not\vert g$,证明$p\vert f$.

令$f,g,fg$对应的系数列分别是$a_n,b_n,c_n$.

那么直接递推就好了,我们假设$p \vert \gcd(f_0,\ldots ,f_A,g_0,\ldots,g_B)$(没有取$-1$)

那么考虑$c_{A+B+2}$,它一定有一项是$f_{A+1}g_{B+1}$,且其他的项一定都被$p$整除,于是你一定可以让$A$或$B$加$1$.

这样走$n+m+1$步一定可以把$A$或$B$弄满.

</div>

<div class='cbox'>

$$
\begin{gathered}
f(x)\in Z[x],f \text{ is primitive}  \\
\Rightarrow
(f(x) \text{ is inreducible in Z[x]}  \Leftrightarrow f(x) \text{ is inreducible in Q[x]} )
\end{gathered}
$$

</div>

<div class='pbox'>

考虑如果$f(x)=f_1(x)f_2(x),f_1,f_2\in Q[x]$.

那么你显然可以有$f_i(x)=g_i(x)\dfrac {p_i}{q_i}$.且$g_1,g_2 \text{ is primitive}$.

那么$f(x)=\dfrac{p_1p_2}{q_1q_2}g_1(x)g_2(x)$,其中$g_1g_2$还是$\text{primitive}$的,$q_1q_2f(x)=p_1p_2g_1(x)g_2(x)$.

考虑两侧的系数的最大公因数相等,那只能是$q_1q_2=p_1p_2$了.

</div>

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f(x)=x^n+\sum _{i = 0} ^{n-1}  a_ix^i,a_i\in Z \\
\exists p \ s.t.\\ 
\forall 0\le i\le n-1 ,p | a_i \\
p^2 \not| a_0
\end{cases} \\
\Rightarrow f(x) \text{ is irreducible in Q[x]} 
\end{gathered}
$$

</div>

<div class='pbox'>

反证,考虑$f=f_1f_2$设它们的系数分别是$b_n,c_n$,根据上面高斯引理的证明归纳过程,$p|a_0$,那么$p|b_0c_0$,那么因为$p$只能整除其中的一个,由上面那个由$(A,B)$推到$(A+1,B)$或$(A,B+1)$的过程,你有一边走不了,最终就直接得到$p\vert b_n$或$p\vert c_n$了.

但是显然$p\not| f$,它是有系数是$1$的!矛盾.

你看一下下面那个模$p$的性质于是这个东西另一个证法是先模$p$,那么$f(x)\equiv x^n$,于是它被拆了之后只能是$x^i x^{n-i}$,但这说明拆出来的两项常数项模$p$都是$0$,和$p^2\not|a_0$矛盾.

</div>

<div class='cbox'>

$$
\begin{gathered}
p\in P,f(x)=\sum _{i = 0} ^{p-1}  x^i \\
\Rightarrow  f(x) \text{ is irreducible}
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
f(x)=\dfrac{x^p-1}{x-1}  \\
\xlongequal{ y=x-1 } \dfrac{(y+1)^p-1}{y}  \\
=\sum _{i = 0} ^{p-1} y^i \binom{p}{i+1}
\end{gathered}
$$

此时用上面定理.

</div>

<div class='cbox'>

若首一多项式$f$在$Z[x]$上可约则$f$在$F_p[x]$上可约

</div>

<div class='pbox'>

显然,因为你把$Z[x]$上那两个因子分别模$p$就好了.首一主要是防止你模$p$的时候$f$模成常数.

</div>


## Smith Standard Form

Smith标准型是说环上元素的矩阵,相抵于一个只有主对角线上有$d_1\ldots d_r,0\ldots,0$的矩阵且满足$d_{i+1}\vert d_i$.

<div class='cbox'>

定义$D_i$是所有$i$阶子式的gcd,则$d_i=\dfrac{D_i}{D_{i-1}}$.

</div>

<div class='pbox'>

如果我们消完了的$d$有整除链的性质,那么最后是显然满足条件的,只需要证明$D_i$在初等行变换下不变:
- 交换两行/列或给一行/列乘$\pm 1$(环上,其他的没逆)显然不影响
- 把一行/列乘$k$加到另一行/列,此时若一个子式同时包含或不包含涉及到的两行则它不变,如果只包含一个则用线性性相当于给他加上另一个子式,不改变$\gcd$.

而只要证明存在一种消法消成整除链,你发现如果消完了不是整除链你总可以用辗转相减变成$d_i=\gcd(d'_1,\ldots,d'_i)$弄成整除链,于是得证.

</div>

这里$d$叫不变因子(invariant factors),$D$叫行列式因子(determinant factors).

然后如果这个环是UFD,定义初等因子$element factors$是把每个$d$做素分解得到的每个$p_i^{c_i}$,不进行合并.


## Jordan Standard Form

<div class='cbox'>

你可以把矩阵弄成只有分块对角矩阵,且每个块只有对角线上有相同的值,对角线上方的一条斜线都是$1$.

</div>



### Proof1:初等变换

<div class='pbox'>

记$E(i,j,a)$表示$I$的基础上$(i,j)$位置为$a$的初等变换矩阵.而容易注意到$E(i,j,a)^{-1}=E(i,j,-a)$.

所以当我们做$E(i,j,k)AE(i,j,-k)$这个相似变换我们是:

给$A$的第$i$行加上$k$倍第$j$行,再给第$j$列加上$k$倍第$i$列.

对一个上三角矩阵,我们发现进行这样一次操作,$A_{i,j}$加上了$k(A_{i,i}-A_{j,j})$,且这一步对上三角矩阵只影响$x<i,y>j$的位置(一个右上角).所以你可以以一定的顺序消掉这样的元素,得到一个分块对角矩阵,每个块对角线元素相同.

那么每个块都可以表示成$\lambda I+N$,$N$是幂零的.而当你对这个子空间进行换基的时候$\lambda I$不变所以只要找$N$的变换.

你发现对于$N$,你仍然进行过上面这种操作就可以简单的用某一行的$1$把同行后面的所有数消掉,所以你从第一行开始从上往下消.如果遇到一行它的$1$不在副对角线你可以做交换把它换到前面来,这样都弄完了就得到标准的约旦标准型了.

</div>

### Proof2

<div class='cbox'>

两矩阵$A,B$相似等价于特征矩阵$A-\lambda I,B-\lambda I$相抵.

</div>

<div class='pbox'>

首先如果$A=PBP^{-1}$,那么

$$
\begin{gathered}
A-\lambda I=PBP^{-1}-P\lambda IP^{-1}=P(B-\lambda I)P^{-1}
\end{gathered}
$$

成立.

再看另一边:

考虑现在$V(A-\lambda I)=(B-\lambda I)W$,$V,W$是可逆的$\lambda$矩阵.

直接设 $V=\sum _{i = 0} ^{m} V_i\lambda^i,W=\sum _{i = 0} ^{m}  W_i\lambda^i$.

那么

$$
\begin{gathered}
\begin{cases}
-V_m=-W_m \\
V_kA-V_{k-1}=BW_k-W_{k-1} \\
V_0A=W_0B
\end{cases}
\end{gathered}
$$

然后你发现可以盯着一边看去做一个相消,就是给$V_iA$的那个等式右乘$A^i$,则左边是$0$,右边是?

$$
\begin{gathered}
\sum BW_iA^i-W_{i-1}A^i \\
=B(\sum W_iA^i)-\sum (W_iA^i)A \\
=0
\end{gathered}
$$

于是设$P=\sum W_iA^i$就有$BP=PA$.

那么你把$V,W$取逆分别移到另一边是$(A-\lambda I)W^{-1}=V^{-1}(B-\lambda I)$.再走一遍能得到$AQ=QB$.

然后能看出$A^kQ=QB^k$,$Q=W^{-1}(B)$,$PA^k=B^kP$.

那么

$$
\begin{gathered}
PQ \\
=W(A)Q \\
=\sum_i W_iA^iQ \\
=\sum_i W_iQB^i \\
=\sum_i W_i(\sum_j W^{-1}_jB^j)B^i \\
=\sum_i \sum_j W_iW^{-1}_jB^{i+j} \\
=WW^{-1}(B) \\
=I
\end{gathered}
$$

</div>

[think] 你看那个神秘的求和是不自然的,你注意到如果我们对一开始的$V(A-\lambda I)=(B-\lambda I)W$去代入$\lambda =A$会很妙,然后所谓的代入实际上对应了取模,所以算$(B-\lambda I)W \bmod (A-\lambda I)$,算这个的时候拆开$W$乘上$B$算,因为没有交换律不保证余数可乘.

[think] 好吧上面那个think说的你直接代入就可以的,这种时候你要规定代入方向,然后$(B-\lambda I)W=BW(\lambda)-\lambda W(\lambda)$,此时你代入$\lambda=A$因为是右代入所以你要先把$\lambda W$变成$W\lambda$.

[think] 后面这个$=I$也可以直接通过代入看出来,或者再逐项系数展开.

<div class='cbox'>

不变因子组和初等因子组是双射

</div>


<div class='pbox'>

考虑Smith标准型,那么从矩阵角度,分块对角矩阵有两个块,问题是现在不满足整除链,那么只要每次,对所有素因子,取其最高次组成一个作为不变因子,就可以重排出一个大矩阵的整除链,于是得证.

</div>

<div class='cbox'>

若$V=W_1\oplus W_2$,则$T$的初等因子就是$T|_{W_1}$的初等因子与$T|_{W_2}$的初等因子的和(多重集的和).

</div>

<div class='pbox'>

考虑你有矩阵$A$和矩阵$B$都已经是Smith标准型,然后你要把它们拼起来.

此时考虑行列式因子$D$,因为$A,B$是对角阵拼完了还是对角阵,所以只有主子式不是$0$,此时$k$阶行列式一定是$A$里取若干个元素$B$里取若干个元素的乘积,又因为整除链的存在,所以取的时候一定分别是$A,B$里最低次的若干个.

那么因为是直接乘积再取gcd,现在只考虑所有不变因子$d$某个特定素因子的次数就成了,新的大矩阵的$D$对应的次数是原来两个小的min+卷积,因为整除链所以$D$的次数是凸的,所以是闵和,所有作为斜率的那个$d$的初等因子的次数一定都保留到了新的结果里,就完事了.

</div>

<div class='dbox'>

有理标准型

把矩阵的不变因子的友矩阵作为分块对角矩阵的块

</div>

由于上面说初等因子是直接拼,而初等因子确定不变因子,所以你这么拼是对的.


<div class='cbox'>

最大的不变因子是极小多项式

</div>

<div class='pbox'>

首先友矩阵的极小多项式是它的特征多项式,因为取$[1,0,0,\ldots,0]$,那么你发现友矩阵的前$n-1$次方作用到它身上是线性无关的,所以特征多项式的次数必须是$n$次的.

然后你转乘上面的有理标准型,就显然.

</div>

于是这种证法说你考虑一个Jordan块正好对应了一个不变因子$(x - \lambda_i)^n$

## 准素分解

<div class='cbox'>

$T$的极小多项式是$m(x)=\prod_i p_i(x)^{c_i}$,$p_i$是互不相同的不可约多项式,则$V=\oplus_i W_i$,且 $W_i=\operatorname{null} p_i^{c_i}(T)$.

</div>

<div class='pbox'>

不变性是显然的,我们发现对一个$W_i$,其极小多项式是$p_i^{c_i}$,考虑其中一个$v$,$p_i^{c_i}(T)v=0$,那么显然$p_i^{c_i}(T)Tv=Tp_i^{c_i}(T)v=0$.

$$
\begin{gathered}
\text{let } f_i=\dfrac{m(x)}{p_i^{c_i}(x)}  \\
\text{if } u\in W_1\cap W_2\oplus \ldots\oplus W_n\ne \emptyset \\
u\in W_1 \Rightarrow p_1^{c_1}(T)u=0 \\
u\in W_2\oplus \ldots\oplus W_n \Rightarrow f_i(T)u=0 \\
\because f_i \perp p_1^{c_1} \\
\therefore \exists s(x),t(x),s(x)p_1^{c_1}(x)+t(x)f_i(x)=1 \\
s(T)p_1^{c_1}(T)u+t(T)f_i(T)u=Iu=u \\
\Rightarrow u=0
\end{gathered}
$$

这说明是直和,再说明直和是整个空间:

$$
\begin{gathered}
\gcd(f_1,\ldots,f_n)=1 \\
\Rightarrow \exists a_i,\sum_i a_i(x)f_i(x)=1 \\
\Rightarrow \sum_i a_i(T)f_i(T)=I \\
\text{let } E_i=a_i(T)f_i(T) \\
\end{gathered}
$$

显然$E_iE_j(T)=0$,又因为

$$
\begin{gathered}
\text{let } E_i(v)=w \\
p_i^{c_i}(T)w=p_i^{c_i}(T)a_i(T)f_i(T)v \\
=a_i(T)m(T)=0 \\
\Rightarrow \operatorname{range} E_i \subset W_i \\
(\sum_j E_j)E_i=E_i \Rightarrow E_i^2=E_i \\
\forall w\in W_i,
\sum_j E_j(T)w=w \\
\end{gathered}
$$
而你$E_j,j\ne i$的像空间的直和与$W_i$无交,所以一定只能是$E_i(w)=w$

这样实际证明了$E_i$就是像每个空间的投影,且和为$I$,于是得证.

</div>

<div class='cbox'>

对任意线性变换$T$,$\exists v$使得任意满足$p(T)v=0$的$p$是极小多项式的倍式.

</div>

<div class='pbox'>

首先如果$p=p_i^{c_i}$,那么是显然的,否则$p$就不是这个了.

否则用准素分解,则你得到若干个$p_i^{c_i}$,每个对应一个向量$v_i$,考虑直接把它们加起来$v=\sum_i v_i$,那么:

$0=g(T)\sum_i v_i=\sum_i g(T)v_i$,因为后面每一项分别在$W_i$中,所以一定有$g(T)v_i=0$,所以在每个子空间中的极小多项式$p_i^{c_i}$都是$g(T)$的因子,于是$m|g$,又因为$g$是整个的零化多项式所以$g|m$.得证.

</div>

## 循环分解

<div class='cbox'>

对线性变换$T$,找到$v$使得 $g(T)v=0 \Rightarrow p|g$,其中$p$为极小多项式.然后找到最大的$k$使得$v,Tv,\ldots T^kv$线性无关,设 $W_1=\operatorname{span}( v,Tv,\ldots T^kv )$,设$W_1\oplus W=V$,则继续对$W$重复就得到一串不变子空间,且极小多项式构成整除链.

</div>

<div class='pbox'>

前面我们已经证明了一定有这样的$v$,同时容易看出$T|_{W_1}$的极小多项式是$p$,现在就是证明我们这么找出$W_1$后一定存在满足条件的不变子空间$W$.

考虑构造线性泛函$f$满足$fT^kv=1$,其他的基全设$0$.

则 $W=\bigcap_{i=0}^k \operatorname{null} fT^i$.

设$\varphi:F^n\to F^k,\varphi(v)=[fv,fTv,\ldots fT^kv]$,$W=\operatorname{null} \varphi$.显然是线性变换.

显然$W$是不变子空间.我们要证明$W_1\oplus W=V$.

考虑$\varphi|_{W_1}:F^k\to F^k$,且显然是双射(直接把$T^kv$带进去就是线性无关的),于是零空间只有$0$,于是$W_1\cap W=\{0\}$.

接下来证$W_1+W=V$,你再考虑$\varphi$的值域既然是$k$,零空间自然是$n-k$维,于是$\dim W+\dim W_1=n$,得证.

这就结束了.

</div>

[think] 显然$f$就是提取那一维系数,那$\varphi$是什么玩意呢?它是一个用零空间区分$W_1$和$W$的映射,