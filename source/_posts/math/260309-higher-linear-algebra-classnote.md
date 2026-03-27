---
title: Maybe Higher Linear Algebra
tags:
  - math
  - linear-algebra
  - note
date: 2026-03-09 20:12:21
---


# Maybe Higher Linear Algebra

## 20260304

<div class='cbox'>

如果$V$中的$a_1\ldots a_n$线性相关,则存在$W$空间中的$w_1,w_2\ldots w_n$使得$\varphi(a_i)=w_i$的线性映射不存在
</div>

<div class='pbox'>

不妨设$\exists c_i\ne 0,\sum_i a_ic_i=0$.

只要让$w_1\ldots w_{n-1}$全是$0$,$w_n\ne 0$就完事了.

</div>

## 20260309

<div class='cbox'>

任意线性空集$V$有一组Hamel基

</div>

<div class='pbox'>

$$
\begin{gathered}
\text{let } X=\{\text{all linearly independent set of V} \} \\
\end{gathered}
$$

定义偏序是$X$上的包含关系.

则对任意一条链$A_1\subset A_2\subset \ldots$,考虑$A=\bigcup_i A_i$,考虑证明$A\subset X$:

假设$A$线性相关,则其中有限个元素线性相关,则存在一个$A_i$包含这全部有限个元素,但$A_i$都是线性无关的,所以矛盾.

则根据 Zorn's Lemma,任何链有极大元,所以一定存在最大元$B$.

又因为若$B$不能张成$V$,则拿出任意一个 $v\notin \operatorname{span}( B )$,则 $B\cup \{ v \}$线性无关,与$B$是最大元矛盾.

所以$B$是一组基.

---

我声称另一种做法是考虑直接把整个$V$良序化,然后照抄有限维的方法一个一个加元素,把原来的归纳改成超限归纳.

</div>

<div class='cbox'>

双射是可逆的

</div>

<div class='pbox'>

设$f$是双射.先不管线性的限制定义其逆是$g:f(a)\mapsto a$.

只要证明$g$是线性的:

$$
\begin{gathered}
ax+by=ax+by \\
\Rightarrow f\circ g(ax+by)=af\circ g(x)+bf\circ g(y) \\
=f(ag(x)+bg(y)) \\
\Rightarrow g(ax+by)=ag(x)+bg(y)
\end{gathered}
$$

</div>

课上为什么能证半天

然后讲了个同维度线性空间是同构的.显然的.


## 20260312

<div class='cbox'>

$$
\begin{gathered}
K_1\subset K_2\subset K_3 \text{ are number fileds}  \\
\dim_{K_1} K_2 =n, \dim_{K_2} K_3=m \\
\text{then } \dim_{K_1} K_3 =nm
\end{gathered}
$$

这里$\dim_{F}K$的意思是$K$作为$F$上的向量空间的维数.

</div>

<div class='pbox'>

$\dim_{K_i} K_j=n$等价于$K_j$线性空间同构于$K_i^n$,于是两个双射一复合你就有$K_3$到$K_1^nm$的双射.

</div>

<div class='cbox'>

证明$R[x]_{\le n}$上平移映射$f(x)\mapsto f(x+a)$可以用求导映射的多项式表示

</div>

<div class='pbox'>

泰勒展开

</div>

<div class='cbox'>

若$A^n=0,A^{n-1}\ne 0$,则$A$可以写成只有对角线上方一格处为$1$,其他地方为$0$的矩阵.

</div>

<div class='pbox'>

1. 极小多项式+有理标准型,启动!

2. 取$A^{n-1}v\ne 0$的那个$v$,用$A^iv$当基.

</div>

<div class='cbox'>

证明对无限域上的有限维线性空间$V$,其中的任意$n$个互不相同的算子$T_1\ldots T_n$,存在一个$v$使得$T_i v$互不相同

</div>

<div class='pbox'>

考虑此时的一个结论是任意个真子线性空间的并不是$V$.

我们把$\{T_i=T_j\}$的子空间都拿出来,它们的并不是$V$,随便找一个外面的,结束.

</div>

## 20260323

<div class='cbox'>

$(U^0)^0=U$(准确的说,自然同构)

$(U_1+U_2)^0=U_1^0\cap U_2^0$ 

</div>

<div class='pbox'>

第一个$U\subset (U^0)^0$是显然的.那么有限维空间只要靠维数就行了,无限维呢?

第二个,显然有$(U_1+U_2)^0\subset U_1^0\cap U_2^0$.反过来$U_1+U_2$中的元素都可以写成$u_1+u_2,u_1\in U_1,u_2\in U_2$,然后就没事了.

</div>

<div class='cbox'>

$(U^0)^0\not \cong U$ 当且仅当$U$是无限维

</div>


<div class='pbox'>

我们发现$V^*/U^0\cong U^*$,于是$(V^*/U^0)^*\cong (U^*)^*$,但同时,若$f(U^0)=0$,则$f=g\circ h$,其中$h$是商映射$(V^*\to V^*/U^0)$,于是$f$和$g$有双射,$f\in (U^0)^0$,$g\in (V^*/U^0)^*$,于是$(V^*/U^0)^*\cong (U^0)^0$,这就证明了$(U^*)^*\cong (U^0)^0$,于是不可能同构.

</div>

利用了商空间的泛性质:把$U$映成$0$的都可以拆成$V\to V/U$和后面的.

## 20260326

<div class='cbox'>

定义单纯形是一组仿射无关的向量$v_1\ldots v_k$的凸包,仿射无关即$v_i-v_1$线性无关,凸包即$\{\sum_{i=1}^k c_iv_i|c_i\ge 0,\sum_i c_i=1\}$

多面体是若干个不等式和等式的解集,即

$$
\begin{gathered}
\{ x|Ax=b,Cx\ge d \} 
\end{gathered}
$$

证明单纯形是多面体

</div>

<div class='pbox'>

考虑先把凸包平移$-v_1$,即:

$$
\begin{gathered}
S-v_1=\{ \sum_{i=2}^k c_i(v_i-v_1) | c_i\ge 0,\sum c_i\le 1 \} 
\end{gathered}
$$

此时存在矩阵$M$满足$\forall v\in S,M(v-v_1)=[c_2,\ldots c_k]$.所以你直接用$M$,然后再乘一个暴露出来这些$c$的就能构造不等式限制.

这个$M$是$S-v_1$这个子空间到$F^k$的映射,为了你规定$v-v_1$在这个子空间里,你取这个子空间的零化空间的一组基,把它们等于$0$这件事用$A,b$等式限制即可.

</div>

