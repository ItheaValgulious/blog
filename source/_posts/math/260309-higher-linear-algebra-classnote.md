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

## 20260330

<div class='cbox'>

$$
\begin{gathered}
T:V\to W \\
T \text{ is injective} \Leftrightarrow T' \text{ is surjective} \\
T \text{ is surjective } \Leftrightarrow T' \text{ is injective} 
\end{gathered}
$$

</div>

<div class='pbox'>

感觉最简单的方法是考虑单射等价于左逆存在,满射等价于右逆存在,而你惊喜的发现:

$$
\begin{gathered}
(T')^{-1}_{L/R} =(T^{-1}_{R/L})'
\end{gathered}
$$

于是就证完了.

</div>

<div class='cbox'>

在$F^{2\times 2}$中,$\det (A+B)-\det A-\det B$是双线性型

</div>

<div class='pbox'>

你可以直接设8个未知数算一下.

那么这是为什么呢?因为发现恰好在$F^{2\times 2}$上$\det$是一个二次型,而任意二次型$Q$可以通过极化诱导一个双线性型:$B(X,Y)=Q(X+Y)-Q(X)-Q(Y)$

</div>

<div class='cbox'>

双线性型$B(V_1,V_2,F)\cong \mathcal{L}(V_1,V_2')\cong \mathcal{L}(V_1,\mathcal{L}(V_2,F))$.

</div>

<div class='pbox'>

看最右边那个形式你就悟了:就是经典的多变量函数都可以通过构造固定某个参数的方法同构到低维变量,什么多叉树转二叉树之类的内容.

就是你直接把$B(x,y)$映射到$x\mapsto (y\mapsto B(x,y))$就是同构.

</div>

<div class='dbox'>

- alternating:$\varphi(v,v)=0,\forall v\in V$
- symmetric:$\varphi(u,v)=\varphi(v,u)$
- reflexive:$\varphi(u,v)=0 \Leftrightarrow \varphi(v,u)=0$

</div>

AI似乎认为reflexive还有其他意思,但我们先按这个来. 

<div class='cbox'>

$$
\begin{gathered}
\varphi\in B(V,V,F) \\
\varphi \text{ is reflexive} \Rightarrow \varphi \text{ is alternating or symmetric} 
\end{gathered}
$$

</div>

<div class='pbox'>

我有一坨大粪.大粪思路是你先拿任意两个$u,v$,考虑$(au+bv)\otimes (cu+dv)$的值,然后分析一通得到只看这两个向量的子空间是交替或对称的.然后你再考虑两个三项的乘去证明如果$u$对$v$是交替,对$w$是对称,且都不是$0$,就会出问题.

不那么大粪的做法是你可以先考虑既然$\ker \varphi(a,b)=\ker \varphi(b,a)$所以它俩只差一个常数,然后再检验两个检验三个之类的.

</div>

## 20260409

<div class='cbox'>

设:

$$
\begin{gathered}
t=\begin{bmatrix} 1&0\\0&-1 \end{bmatrix} \otimes e_1 +\begin{bmatrix} 0&1\\1&0 \end{bmatrix} \otimes e_2 \\
=M_1\otimes e_1+M_2\otimes e_2
\end{gathered}
$$

证明 $\operatorname{rank}_R t>2$

</div>

<div class='pbox'>

假设$t=a\otimes A+b\otimes B$,其中$a,b\in R,A,B\in R^{2\times 2}$,则因为$a,b$可以分解:$a=\sum x_ie_i,b=\sum y_ie_i$,于是我们看到$M_1,M_2$是$A,B$的线性组合.

而因为$M_1,M_2$线性无关,所以它张成空间是二维的包含$A,B$,所以反过来$A,B$也是$M_1,M_2$的线性组合.且$A,B$的秩是$1$:你解$|mA+nB|=0$发现没有实数非$0$解,得证.

</div>

## 20260413

发现忘记张量积的笔记了.写写:

<div class='dbox'>

张量积

对空间$V_1,V_2$,若存在双线性映射$T:V_1\times V_2\to X$使得对任意双线性映射$\varphi:V_1\times V_2\to W$,存在唯一线性映射$Q:X\to W$满足$\varphi=Q\circ T$,则$X$为张量积,记作$X=V_1\otimes V_2$.

</div>

容易发现根据定义,张量积是唯一的(在同构意义下)(否则你直接令$T$和$\varphi$分别是两个张量积对应的那个双线性映射即可)

<div class='cbox'>

张量积的商构造

</div>

<div class='pbox'>

简单粗暴.

定义$X=F^{V_1\times V_2}$上的有限支撑空间(只有有限多个不为$0$).这相当于其中的每个元素你可以写成$\sum_i c_i (v_1,v_2),c_i\in F,v_i\in V_i$其中$i$不一定可数多.

然后定义$X$上的等价关系$\sim$是你可以把它们根据双线性的规则变得相同,那么这个规则其实很少:

令
$$
\begin{gathered}
R=\operatorname{span}(  \\
\{
\delta_{v_1+u,v_2}-\delta_{v_1,v_2}-\delta_{v_1+u,v_2}, \\
\delta_{v_1,v_2+w}-\delta_{v_1,v_2}-\delta_{v_1,w}, \\
\delta_{cv_1,v_2}-c\delta_{v_1,v_2}, \\
\delta_{v_1,cv_2}-c\delta_{v_1,v_2}  \\
|\forall v_1,v_2,c,u\}
) 
\end{gathered}
$$

这里$\delta_{a,b}$表示它把$V_1\times V_2$中的$(a,b)$映成$1$其他全部映成$0$.

则$X/\sim=X/R$是满足条件的张量积.

</div>

我感觉是显然的.

<div class='cbox'>

设$F(S)$是$S$的free vector space over S.即

$$
\begin{gathered}
F(S)=\{ f:S\to F,f \text{ has finite support}  \} 
\end{gathered}
$$

则$F(S_1)\otimes F(S_2)=F(S_1\times F_2)$

</div>

<div class='pbox'>

验证泛性质定义即可.

</div>

注意对任何一个向量空间你把$S_1$取成它的基就可以用它来定义任意两个向量空间的张量积.它实际上是物理那个基直接做笛卡尔积的扩展.

这里还讲了个有趣的东西

<div class='bbox'>

可以用$7$次乘法做2阶方阵相乘.

考虑矩阵乘法是一个双线性映射,且可以定义成一种张量乘法:

好吧我们直接定义成指标缩并,那么你发现此时张量的秩对应了你进行乘法的次数,然后它找到了一个秩是$7$的分解结束.

</div>

## 20260415

<div class='cbox'>

任意对称多项式可以被唯一分解基本对称多项式的多项式.

基本多项式是$e_k=\sum_{|S|=k} \prod_{i\in S} x_i$.

</div>

<div class='pbox'>

存在性考虑递归降次.

如果我们定义次数是先按次数和,再定义单项式的比较是先按次数和,再按次数序列的字典序的话.你就要构造一个最大项和它相同的东西.不妨设对称多项式$f$最大项是$\prod_{i=1}^n x_i^{c_i}$,$c_{n+1}=0$.

注意到因为对称,所以所有$\{c_i\}$集合对用的项一定同时出现,所以取出来的最大项一定是$c_1\ge c_2\ge \ldots \ge c_n$.

那么我们构造$g=\prod_{i=1}^n x_i^{c_i-c_{i+1}}$,则确实第一项相等,且多项式次数相等.我们只需要保证不存在一个字典序更大的项.然后你观察一下这个构造发现它确实能做到:考虑当你乘一个$e_i$的时候,让字典序最大的乘法一定是它自身那个字典序最大的项.而我们构造出来的$g$中的首项恰恰是每个字典序最大的项乘起来的,所以是对的.

唯一性考虑假设你$P(e_1,\ldots e_n)$是分解目标,只需要证明$P(e_1,\ldots e_n)=0 \Leftrightarrow P=0$(这两个都是多项式意义等于$0$).

那么你发现$\prod e_i^{c_i}$的最大项一定是互不相同的,于是最大的最大项消不掉.于是就只有最大项等于$0$一条路了.

</div>

**看起来这其中最重要的是满足两个多项式的乘积的最大项一定是原来各自最大项的乘积**.

然后讲了一下手算分解的方法就是你先把可能的$\prod_i e_i$项写出来然后待定系数.待定系数的时候用代入值快速拿等式.




