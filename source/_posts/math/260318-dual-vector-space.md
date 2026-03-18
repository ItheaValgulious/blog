---
title: Bigger Dual Vector Space
tags:
  - linear-algebra
  - math
  - whims
date: 2026-03-18 18:38:03
---

# Bigger Dual Vector Space

好我们都知道对偶空间是什么了,由于有限维向量空间一定同构于自己的对偶空间,且同构于$F^n$后还可以定义内积后用Reisz表示定理,所以此时这个对偶空间看起来很废物.

但是无限维的时候对偶空间是有意义的,实际上我们发现无限维向量空间行对偶空间和原空间一定不相等,事实上,一定比原空间大.

这里的大是维数上的,但因为无穷,所以定义维数是基的集合的基数.

设$F$上的向量空间$V$有一组基数维$\kappa$的基,考虑$V'$.

容易发现$V'\cong F^\kappa$,这是因为线性映射等价于你对基的每一个元素都指定一个$F$中的元素作为值.所以我们实际上是要考虑$F^\kappa$的大小.然后我不会,所以看看万能的AI:

## $\dim V=\kappa \Rightarrow\dim V'=|F|^\kappa$

我们上面已经知道$V'\cong F^\kappa$.

首先考虑$F^\kappa$的元素总数就是$|F|^\kappa$,所以显然不大于这个值,所以只需构造出这么多个向量:

考虑取一个大小为$\kappa$的集合$S$,给其中每个元素$s$设一个变量$x_s$,得到$V$同构的一个多项式空间$P=F[\{x_s|s\in S\}]$,其中$x_s\in S$代表一个变量,也就是说这是一个$|S|$元多项式.

考虑这个空间的维数,这个空间的维数就是其单项式的种类,则考虑单项式包含的变量是$S$的一个有限子集,次数是整数,故其基数为:

$$
\begin{gathered}
\sum_{i=0}^\infty \kappa^i \aleph_0^i \\
=\sum _{i = 0} ^{\infty}  \kappa \aleph_0 \\
=\kappa \aleph_0 \aleph_0 \\
=\kappa
\end{gathered}
$$

基的大小相等,所以$V\cong P$(由集合势的定义知存在一组基的同构),所以$V'\cong P'$.

尝试直接构造:考虑一个赋值函数$\varphi_a:p(x)\mapsto p(a),p(x)\in P$,其中$a$是对每个变元$x_s$赋一个值,是一个$|F|^\kappa$大小的东西.下面尝试证明他们线性无关:

注意线性无关的定义是有限的:设存在 $\{c_n\}$ 使得$\sum_{i=1}^n c_i \varphi_{a_i}=0$,这代表$\forall p(x)\in P,\sum_{i=1}^n c_i p(a_i)=0$,为了证明$c_i=0$,只需要对每个$a_i$构造一个$p_i(x)$使得

$$
\begin{gathered}
p_{a_i}(a)=\begin{cases}
1 ,a=a_i \\
0,\text{otherwise}
\end{cases}
\end{gathered}
$$

如果有这种东西那么就显然了那么一代入就显然了.考虑构造.

然后我们发现,因为你有互不相同的$n$个$a_i$,那么一定可以选取$m<\infty$个点使得$\exists |A|=m$,$A$是一个指标集,使得$a_i$在$A$集合上就可以互相区分.而我们可以让我们构造的$p$只包含这些$A$对应的变元.所以下面讨论的都是只考虑$A$中的变元.下面只构造$p_1$:

考虑任意$a_i$和$a_1$,一定存在$L_i$使得$L_ia_i\ne L_ia_1$,则:

$$
\begin{gathered}
p_1(x)=\prod_{i=2}^n \dfrac{L_i(x)-L_i(a_1)}{L_i(a_i)-L_i(a_1)} 
\end{gathered}
$$

你发现这个满足条件,于是构造出来了,于是线性无关,于是存在那样一个线性无关组,于是得证.

所以$\dim V'=|F|^\kappa$.

## $|V|=\dim V$?

然后我说你这个空间怎么和基一样大?如果我们设一组基大小为$\kappa$,则全空间大小有

$$
\begin{gathered}
|V|=\sum _{i = 1} ^{n} \kappa^i |F|^i=\max \aleph_0,\kappa,|F|
\end{gathered}
$$

哦所以你发现$\kappa$大的时候还真是和基一样大的.