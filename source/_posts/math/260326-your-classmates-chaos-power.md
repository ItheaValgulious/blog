---
title: Your Classmates' Chaos Power
tags:
  - math
  - note
  - chaos
  - math-analysis
date: 2026-03-26 10:44:06
---

# Your Classmates' Chaos Power

## Period 3 Means Period K

首先是一些准备工作:

<div class='dbox'>

$$
\begin{gathered}
f^{(n)}(x)=f^{(n-1)}(f(x)),f^{(0)}(x)=x
\end{gathered}
$$

</div>

<div class='dbox'>

$$
\begin{gathered}
p \text{ is a k-period point}\\
\Leftrightarrow f^{(k)}(p)=p \text{ and } \forall k'\in (0,k),f^{(k')}\ne p
\end{gathered}
$$

</div>

<div class='cbox'>

### Lemma 1

$$
\begin{gathered}
f\in C(I),I \text{ is closed range} , f(I)\supset I \\
\Rightarrow \exists p\in I,f(p)=p
\end{gathered}
$$

</div>

<div class='pbox'>

简单的介值定理,设$I=[a,b]$,考虑$f(x)-x$,则取$f(x)$最大值时一定为正,取$f(x)$最小值位置一定为负,故存在零点.

</div>

<div class='cbox'>

### Lemma 2

$$
\begin{gathered}
f\in C(I) \\
\Rightarrow \forall I_1\subset f(I), \exists I_0\subset I \ s.t.\ 
f(I_0)=I_1,\text{ where } I_0,I_1 \text{ are both closed ranges}  
\end{gathered}
$$

</div>

值域上的闭区间必然可以对应一个定义域上的区间

<div class='pbox'>

设$I_1=[f(a),f(b)]$,则一定存在$c$使得$c=\sup \{x|f(x)=f(a)\}$,由连续知$f(c)=f(a)$,此时一定存在 $d=\inf \{x|f(x)=f(b),x>c\}$ 或存在 $\sup \{x|f(x)=f(b),x<c\}$ ,于是取$c,d$作为$I_0$的两个端点即可.

</div>


<div class='cbox'>

### Lemma 3

$$
\begin{gathered}
\begin{cases}
f\in C(I) \\
\forall \{ M_i \}_{i=1}^n,(n\le \infty),\forall i,I\supset M_i,f(M_i)\supset M_{i+1}
\end{cases} \\
\Rightarrow \exists \{ J_i \} _{i=1}^n ,f^{(i)}(J_i)= M_i,I\supset J_i\supset J_{i+1}
\end{gathered}
$$

</div>

<div class='pbox'>

考虑归纳证明,则如果已经对$n<k$成立,则$\exists J_{k-1},f^{(k-1)}(J_{k-1})= M_{k-1}$,则对$f|_{M_{k-1}}$应用Lemma 2得$\exists I\subset M_{k-1},f(I)=M_k$,再对$f^{(k-1)}$应用Lemma知存在$J_k$使得$f^{(k-1)}(J_k)=I$,于是对$n=k$成立.

归纳边界显然.

</div>


<div class='bbox'>

从而可以得到推论:

$$
\begin{gathered}
\exists x\in I,f^{(i)}(x)\in M_i
\end{gathered}
$$

证明只要对$J$做闭区间套.

它使得我们可以通过找一个区间包含列来找不动点.

</div>




<div class='cbox'>

$$
\begin{gathered}
f \text{ has a 3-period point}  \\
\Rightarrow \exists a,f^{(3)}(a)\le a<f(a)<f^2(a)
\end{gathered}
$$

</div>

<div class='pbox'>

显然

</div>

那么可以开始我们的证明:

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f\in C(I) \\
\exists a \ s.t.\ 
f^{(3)}(a)\le a<f(a)<f^2(a)
\end{cases} \\
\Rightarrow \forall k,\exists b \ s.t.\ 
b \text{ is a k-period point} 
\end{gathered}
$$

</div>

<div class='pbox'>

设$b=f(a),c=f^{(2)}(a),d=f^{(3)}(a)$,$d\le a<b<c$.

设区间$K=[a,b],L=[b,c]$,则显然有$f(K)\supset L,f(L)\supset L,f(L)\supset K$.

于是可以构造出一个$M$的链使得$M_1=K,M_i=L\forall i\in [2,k-1],M_k=K$,于是由Lemma 3存在$J_k$满足$f^{(k)}(J_k)=M_k=K$,一定存在不动点$x_0\in K$.

而同时,对任意$i<k,i|k$,若$f^{(i)}(x_0)=x_0$,则一定有$x_0=f^{(i)}(x_0)\in L$,但$x_0\in K$得$x_0=b$,但此时$f^{(2)}(x_0)=d\notin L$,矛盾.

注意我们的证明对$k=2$是可以照搬成立($K\to L\to K$)的,对$k=1$则是说$f(L)\supset L$就得到了.

</div>

<div class='bbox'>

把找周期点转换到区间以利用连续性,然后区间的嵌套找到了一条关于不动点是怎么跳跃的路.

</div>

## Period 3 Means Chaos

<div class='cbox'>

若满足上面最后一个定理的条件,则存在不可数集$S$满足:
1. $\forall x,y\in S,\limsup_{n \to \infty} |f^{(n)}(x)-f^{(n)}(y)|>0$
2. $\forall x,y\in S,\liminf_{n \to \infty} |f^{(n)}(x)-f^{(n)}(y)|=0$
3. $\forall x\in S,y \text{ is a period point} ,\limsup_{n \to \infty} |f^{(n)}(x)-f^{(n)}(y)|>0$

</div>

$S$中的任意两点无限次接近,无限次分离,且始终不趋近于一个周期点.

<div class='pbox'>

可以构造区间列 $\{ M_i \}_{i=1}^\infty$,满足:
- $M_i=K$ 或 $M_i\subset L,f(M_i)\supset M_{i+1}$.
- $M_i=K \Rightarrow i \text{ is a square number}$.

(显然$f(M_i)\supset M_{i+1}$对$M_i=K$也是成立的.)

(同时注意到若$M_i=K$,则$M_{i+1}\ne K,M_{i+2}\ne K$,由平方数保证.)

则定义 $P(\{ M_i \},n)=\sum _{i = 1} ^{n} [M_i=K]$,定义密度是 $\rho(\{ M_i \})=\lim_{n \to \infty} \dfrac{P(\{ M_i \} ,n^2)}{n}$.

通过很简单的方法容易构造出指定密度的序列:对每个$n=k^2$先算一下密度然后如果当前密度太小就让$M_n=K$,否则$M_n=L$,即可.

记$M^r=\{ M_i \}_{i=1}^\infty$表示一个满足$\rho(M^r)=r$的集合.

由Lemma3推论,$\exists x_r,f^{(n)}(x)=M^r_n$,令 $S=\{ x_r|r\in (\dfrac34,1) \}$.

现在考虑证明1,那么$\forall a,b$,由于密度不同,存在无数个$n$使得$[M^a_n=K]\ne [M^b_n=K]$(区间类型不同).

若$x\in K=[a,b],f^2(x)\in L=[b,c]$,但$f^2(b)=d\le a$,由于$f^2$连续,则 $\exists \delta>0 \ s.t.\ f^2(x)<b,\forall x\in [b-\delta,b]$,从而$x<b-\delta$.

于是当$x^a,x^b$所在区间类型不同时必然有$|f^{(n)}(x^a)-f^{(n)}(x^b)|> \delta$,于是1得证.

---

对$3$也是一样的:由我们的构造保证了$S$中的点与周期点在迭代中一定有无数次所在区间类型不同.

然后再证明结论2,此时论文/你的同学 说你要想一个神秘构造:你拿到一个区间序列:

$$
\begin{gathered}
\forall \{ I_i=[l_i,r_i] \}_{i=1}^\infty \\ s.t.\\ 
\begin{cases}
[l_i,r_i]\subset [l_{i-1},r_{i-1}]\subset L=[b,c] \\
f([l_i,r_i])=[l_{i-1},r_{i-1}] \\
f(l_i)=r_{i-1},f(r_i)=l_{i-1}
\end{cases}
\end{gathered}
$$

<div class='cbox'>

这串区间一定存在

</div>

<div class='pbox'>

归纳,现在要在$I_n[l_n,r_n]$的基础上构造$I_{n+1}=[l_{n+1},r_{n+1}]$.

因为$f(l_n)=r_{n-1},f(r_n)=l_{n-1},l_n\in [l_{n-1},r_{n-1}]$,由介值定理,存在$r_{n+1}\in [l_n,r_n]$使$f(r_{n+1})=l_n$.

然后因为$f(l_n)=r_{n-1},f(r_{n+1})=l_n,r_n\in (l_n,r_{n-1})$,由介值定理知存在$l_{n+1}\in [l_n,r_{n+1}]$使得$f(l_{n+1})=r_n$

于是存在$[l_{n+1},r_{n+1}]$.

归纳边界平凡(可以对$I_1=L,I_0=[d,c]$用上面的归纳做一步).

</div>

这是实际上是在说你构造一串区间,使得如果这一步$x\in I_k$,则一定有$f(x)\in I_{k-1}$.

设$[l^*,r^*]=\bigcap_i I_i$,则一定有$f(l^*)=r^*,f(r^*)=l^*$.

然后你开始构造$M$,若$M_{n^2}=K,M_{(n+1)^2}=K$,则对中间的这么构造:

$$
\begin{gathered}
M_{n^2+2i-1}=[l_{(2n)+1-(2i-1)},l^*] \\
M_{n^2+2i}=[r^*,r_{(2n)+1-(2i)}]
\end{gathered}
$$

![1774492897319](/imgs/your_classmates_chaos_power/1774492897319.svg)

于是你发现它满足$M$的所有要求,且假设有两个点$x^a,x^b$满足$M^a_{n^2}=M^b_{n^2}=M^a_{(n+1)^2}=M^b_{(n+1)^2}=K$,那么在$[n^2,(n+1)^2]$次迭代中他们一直处于同一个区间,于是两个点距离会不超过$|M_{n^2+1}|$,而这个区间的长度$l^*-l_{2n+2}$是递减且趋近于$0$的,所以只要存在无穷次,这两个点在相邻两次同时落在$K$里,就能说明他们无穷此任意接近.

而这时候就是我们之前密度限制的作用了:$K$的频率是$r$,那么非$K$的频率是$(1-r)$,那么如果把$(n,n+1)$绑定起来,$M_{n^2}=M_{(n+1)^2}=K$的频率就至少是$1-2*(1-r)=2r-1$,因为一个非$K$至多破坏两个$(n,n+1)$的二元组,使其不满足条件.

那么现在对频率$a,b$,他俩的频率分别是$2a-1$,$2b-1$,我们设$M^a,M^b$中满足$(n,n+1)$满足条件的集合分别是$A,B$,那么$A\cap B$的频率$p\ge 2a-1+2b-1-1=2(a+b)-3$,因为$a,b>\dfrac34$,得$p>0$,故$A\cap B$有无穷个元素,他们俩确实会无穷次落到我们刚才用$I$给他制定的轨道里.

于是就得证了.

</div>

