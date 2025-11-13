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

##### Sol 1

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

##### Sol 2

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

##### Sol 3

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

