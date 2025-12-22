---
title: Math Analysis (Class Note) 2
tags:
  - math
  - note
  - math-analysis
date: 2025-12-05 15:59:51
---


# Math Analysis (Class Note) 2

## Class 24

### 定积分的应用

<div class='cbox'>

参数方程的面积


$(x(t),y(t))$围成的面积$S$满足

$$
\begin{gathered}
S=\int_a^b y(x)dx=\int_A^B y(t)x'(t)dt
\end{gathered}
$$

</div>

<div class='pbox'>

显然

</div>

<div class='cbox'>

曲线的弧长

$$
\begin{gathered}
x(t),y(t)\in C^1 \\
\Rightarrow 
\text{length}= \int \sqrt{x'^2(t)+y'^2(t)}dt
\end{gathered}
$$

</div>

<div class='pbox'>

注意要求$C^1$是你要用中值,然后用导数的连续性让他逼近过去.

</div>

然后一些常见划分会得出:

极坐标系下曲线长度

<div class='bbox'>

$$
\begin{gathered}
L=\int \sqrt{(rd\theta)^2+(dr)^2}=\int \sqrt{r'^2+r^2}d\theta
\end{gathered}
$$

</div>



<div class='bbox'>

笛卡尔坐标系下曲线围成的面积

$$
\begin{gathered}
S=\int xdy-ydx
\end{gathered}
$$

</div>



可以用叉乘推.


<div class='cbox'>

极坐标系绕极轴旋转的体积.

$$
\begin{gathered}
V=\int \pi r^3\sin \theta d\theta
\end{gathered}
$$


</div>

<div class='pbox'>

考虑切成一个顶点为原点的三角形.每个三角形旋转出的体积可以用:三角形面积乘质心走过距离.而质心就是三角形重心的走过的圆的半径是好求的.

</div>

## Class 25

### 广义积分

<div class='dbox'>

$$
\begin{gathered}
f\in D(-\infty,+\infty) \Rightarrow \int_a^{\infty}f(x)dx=\lim_{X \to \infty} \int_a^X f(x)dx \\
f\in D[a,b) \Rightarrow \int_a^b f(x)dx=\lim_{X \to b} \int_a^X f(x)dx
\end{gathered}
$$

</div>

<div class='cbox'>

$$
\begin{gathered}
\int_0^{\infty} \dfrac{dx}{(1+x^2)(1+x^\alpha)} 
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=\int_0^1 \dfrac{dx}{(1+x^2)(1+x^\alpha)} +\int_1^\infty \dfrac{dx}{(1+x^2)(1+x^\alpha)}  \\
=\int_0^1 \dfrac{dx}{(1+x^2)(1+x^\alpha)} +\int_0^1 \dfrac{x^{2+\alpha}dx}{(1+x^2)(1+x^\alpha)}\dfrac{1}{x^2}   \\
=\int_0^1 \dfrac{dx}{1+x^2}  \\
=\arctan(1) \\
=\dfrac{\pi}{4} 
\end{gathered}
$$

</div>

<div class='cbox'>

$$
\begin{gathered}
\int_a^b \dfrac{1}{\sqrt{ (x-a)(b-x) } } dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\text{let } x-a=(b-a)\sin^2 t \\
b-x=(b-a)\cos^2 t \\
\int_0^{\frac\pi2} \dfrac{1}{(b-a)\sin t\cos t} 2(b-a)\sin t\cos t dt \\
=\pi
\end{gathered}
$$

</div>

这是为什么呢?要注意到$\sqrt{(x-a)(b-x)}$是圆,然后$\dfrac{dx}{y}=d\theta$


<div class='cbox'>

$$
\begin{gathered}
I=\int_0^{\frac\pi2}\ln \sin xdx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
I=\int_0^{\frac\pi2}\ln \sin xdx=I=\int_0^{\frac\pi2}\ln \cos xdx \\
=\dfrac{1}{2} \int_0^{\frac\pi2} \ln (\dfrac{\sin 2x}{2} )dx \\
=\dfrac{1}{4} \int_0^\pi \ln \sin x dx-\dfrac{\pi}{4}\ln 2 \\
=\dfrac{1}{2} I-\dfrac{\pi}{4} \ln 2 \\
\Rightarrow I=-\dfrac{\pi}{2}\ln 2  
\end{gathered}
$$

</div>

## Class 26

### 续 广义积分

<div class='cbox'>

证明

$$
\begin{gathered}
\int_1^{\infty} \dfrac{\sin x}{x} dx
\end{gathered}
$$

条件收敛

</div>

<div class='pbox'>

先证收敛:

$$
\begin{gathered}
\vert \int_a^b \dfrac{\sin x}{x} dx \vert  \\
={\left \vert -\dfrac{\cos x}{x} \vert_a^b -\int_a^b \dfrac{\cos x}{x^2} dx \right \vert}  \\
\le \dfrac{1}{a} +\dfrac{1}{b}+\int_a^b \dfrac{1}{x^2} dx \\
=\dfrac{2}{a} 
\end{gathered}
$$

是能到无限小的

发散你考虑围绕每个$2\pi$位点取一个小区间,$\dfrac{\vert \sin x \vert }{x}$的最小值在右端点取得,转化到调和级数.

</div>

<div class='cbox'>

$$
\begin{gathered}
\int_1^\infty x^p\sin xdx
\end{gathered}
$$
发散

</div>

<div class='pbox'>

柯西收敛:

$$
\begin{gathered}
\int_{2n\pi+\dfrac{\pi}{4} }^{2n\pi+\dfrac{\pi}{2} } x^p\sin xdx\ge \int_{2n\pi+\dfrac{\pi}{4} }^{2n\pi+\dfrac{\pi}{2} } 1\cdot \dfrac{\sqrt 2}{2} =\dfrac{\sqrt 2}{8} \pi
\end{gathered}
$$

</div>

### 比较判别法

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
\lim \dfrac{f(x)}{g(x)} =A \\
f(x),g(x)>0 \\
\end{cases} \\
\Rightarrow \begin{cases}
A<\infty,\int_a^\infty g<\infty \Rightarrow \int_a^\infty f<\infty \\
A>0,\int_a^\infty g=\infty \Rightarrow \int_a^\infty f=\infty
\end{cases}
 
\end{gathered}
$$

</div>

其他形式都可以转化过来.

<div class='pbox'>

以第一个为例,则存在$X$使得 $x>X \Rightarrow \dfrac{f(x)}{g(x)} <A+1$,然后$\int f\le (A+1)\int g<\infty$

</div>

### 阿贝尔/迪利克雷判别法

<div class='cbox'>

Dirichlet

$$
\begin{gathered}
\begin{cases}
g(x) \text{ is decreasing} ,\lim_{x \to \infty} g(x)=0 \\,
\int_a^x f(t)dt \text{ is bounded} 
\end{cases} \\
\Rightarrow \int_a^\infty f(x)g(x)dx \text{ is convergent} 
\end{gathered}
$$

Abel

$$
\begin{gathered}
\begin{cases}
g(x) \text{ is monotonic and bounded}  \\
\int_a^x f(t)dt \text{ is convergent} 
\end{cases} \\
\Rightarrow \int_a^\infty f(x)g(x)dx \text{ is convergent} 
\end{gathered}
$$

</div>

<div class='pbox'>

我们注意到对Abel那条,因为单调有界,你把界减掉就转化成了第一个.只证第一个.

然后用中值.注意第一中值是要求不提出来的那一项不变号,所以用第二,转化出

$$
\begin{gathered}
\int_a^b f(x)g(x)dx=g(a)\int_a^c f(x)dx+g(b)\int_c^b f(x)dx
\end{gathered}
$$

然后后面那两个积分是有界的,前面那两个$g$是趋近到$0$的,所以任意$[a,b]$上积分都是趋近到$0$的,柯西收敛即可.

</div>

### 练习题

<div class='cbox'>

$$
\begin{gathered}
\int_1^\infty (\dfrac{1}{x} -\ln (\dfrac{1}{x} +\sqrt{ 1+\dfrac{1}{x^2}  } ))dx
\end{gathered}
$$

判断是否收敛.

</div>

<div class='pbox'>

用泰勒展开判断它和$\dfrac1x$的几次方同阶,然后比较判别法.

然后展开的时候你应该展开到小$o$不影响你的结果,即小$o$那块拿出来是收敛的.

</div>

## Class 27

### Egs

<div class='cbox'>

$$
\begin{gathered}
\int_1^\infty x\sin(x^4)dx
\end{gathered}
$$

收敛

</div>

<div class='pbox'>

$$
\begin{gathered}
=\int_1^{\infty}x^{\frac14}\sin x \dfrac{1}{4} x^{-\frac34} \\
=\dfrac{1}{4} \int_1^\infty \dfrac{\sin x}{\sqrt x} dx
\end{gathered}
$$

条件收敛(迪利克雷)

但$x\sin x^4$不趋近于$0$.

</div>

所以广义积分收敛不代表被积函数趋近于$0$.它可以有一些面积很小但值恒定的突起(不断变窄的).如

$$
\begin{gathered}
\int_1^\infty \sum_n \chi_{[n,n+\frac1{n^2}]}
\end{gathered}
$$

是更直观的体现.然后如果你把指示函数做个平滑处理就可以弄成连续的.

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f \text{ is monotonic}  \\
\int_1^\infty f(x)dx<\infty
\end{cases} \\
\Rightarrow f(x)=o(\dfrac{1}{x} ) 
\end{gathered}
$$

</div>

<div class='pbox'>

柯西收敛定理:

$$
\begin{gathered}
\epsilon>{\left \vert \int_a^{2a} f(x) \right \vert} >af(a)=\dfrac{f(a)}{\dfrac{1}{a} } 
\end{gathered}
$$

即证

</div>



<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
\int_1^\infty f(x)dx<\infty \\
f(x)\in UC[1,\infty) \\ 
\end{cases}
\\
\Rightarrow \lim_{x \to +\infty} f(x)=0
\end{gathered}
$$

</div>

<div class='pbox'>

反证,假设存在$x_n>n,f(x_n)>\epsilon$

那么因为一致连续,存在$\delta$使得所有$x\in [x_n-\delta,x_n+\delta]$都大于$\dfrac\epsilon2$.

于是你只要柯西收敛定理取$x-\delta,x+\delta$就推出矛盾.

</div>

<div class='cbox'>

已知$f\in C[0,+\infty),0<a<b$则

(1)
$$
\begin{gathered}
\lim_{x \to +\infty} f(x)=k \\
\Rightarrow \int_0^\infty \dfrac{f(ax)-f(bx)}{x} dx=(f(0)-k)\ln(\dfrac{b}{a} )
\end{gathered}
$$

(2)
$$
\begin{gathered}
\int_0^\infty \dfrac{f(x)}{x} <\infty \\
\Rightarrow \int_0^\infty \dfrac{f(ax)-f(bx)}{x}dx=f(0)\ln \dfrac{b}{a} 
\end{gathered}
$$

</div>

<div class='pbox'>

最重要的是

$$
\begin{gathered}
\int_L^R \dfrac{f(ax)}{x} dx \\
= \int_{La}^{Ra}\dfrac{f(x)}{x} dx \\
\Rightarrow \int_L^R \dfrac{f(ax)-f(bx)}{x} dx \\
=\int_{aL}^{bL}\dfrac{f(x)}{x} dx-\int_{aR}^{bR}\dfrac{f(x)}{x} dx \\
\end{gathered}
$$

然后对(1),两边分别用第一中值即证.对(2),左边用第一中值,右边用柯西收敛变成$0$即证.

</div>

<div class='cbox'>

$$
\begin{gathered}
\int_0^1 x^p(1-x)^qdx
\end{gathered}
$$

的收敛性

</div>

<div class='pbox'>

$0$处有$\dfrac{x^p(1-x)^q}{x^p}=1$然后用$x^p$的收敛性得到$p>-1$,同理$1$处$q>-1$.

</div>

<div class='cbox'>

$$
\begin{gathered}
\int_0^{+\infty} \dfrac{\sin x \ln(1+x)}{x^p}dx 
\end{gathered}
$$

敛散性

</div>

<div class='pbox'>

$0$处等价无穷小显然等价于$x^{2-p}$,$p<3$绝对收敛,$p>3$发散.

正无穷处,显然$p\le 0$发散,$p>0$条件收敛(迪利克雷判别法).

而我们知道$\dfrac{\sin x}{x}$条件收敛,所以$p\le 1$条件收敛.

$p>1$时$\dfrac{\ln x}{x^\epsilon}$的极限是$0$,所以从$x^p$里分出一个$\epsilon$就能看出收敛.

</div>

## Class 28

### 正项级数收敛性

<div class='dbox'>

- 柯西收敛(略)
- 单调有界
- 比较判别法
- 比较法极限形式($\lim_{n \to \infty} \dfrac{a_n}{b_n}$)
- 比值法($\lim_{n \to \infty} \dfrac{a_n}{a_{n-1}}$)
- 根式法($\lim_{n \to \infty} \sqrt[ n ]{ a_n }$)
- 广义比较($\dfrac{a_{n+1}}{a_n}\le \dfrac{b_{n+1}}{b_n}$).(证明是考虑把这一连串乘起来就是$a_n\le b_n \dfrac{a_1}{b_1}$)(哦其实你移动一下不就是$n+1$项两个数列的比比$n$项小吗这直观多了)
- 积分法

</div>

<div class='cbox'>

级数收敛,通项一定收敛到$0$.

</div>

<div class='pbox'>

$S_n-S_{n-1}$收敛到$0$.

</div>

注意这里和积分的区别

<div class='cbox'>

拉贝判别法

$$
\begin{gathered}

\lim_{n \to \infty}  n(\dfrac{a_n}{a_{n+1}} -1)=r \\
r>1 \Rightarrow  \text{convergent}  \\
r<1 \Rightarrow  \text{divergent} 
\end{gathered}
$$

</div>

<div class='pbox'>

收敛这边:

首先变形成 $\dfrac{a_{n+1}}{a_n}\le \dfrac{n}{n+r}$,那么我们其实是去和$b_n=\prod_i^n \dfrac{i}{i+r}$这个级数比较.

取对数:

$$
\begin{gathered}
\ln {\left( \prod_{i=1}^{n-1} \dfrac{i}{i+r}  \right)}  \\
=\sum _{i = 1} ^{n-1} \ln(1-\dfrac{r}{i+r} ) \\
\stackrel{ \ln (1-x)>-\frac x{1-x} } \ge\sum _{i = 1} ^{n}  - \dfrac{r}{i+r} \dfrac{i+r}{i}    \\
=\sum _{i = 1} ^{n}  -\dfrac{r}{i}  \\
\sim -r\ln n \\
\Rightarrow b_n\sim \dfrac{1}{n^r} 
\end{gathered}
$$

于是用$p$判别法就做完了.

</div>

你注意到这个就是把比值判别法是和$a^x$比较变成和$x^p$比较.

<div class='cbox'>

高斯判别法

$$
\begin{gathered}
\dfrac{a_n}{a_{n+1}} =1+\dfrac{1}{n} +\dfrac{l}{n\ln n} +o(\dfrac{1}{n\ln n} )
\end{gathered}
$$

然后$l>1$说明收敛,$l<1$发散.

</div>

<div class='pbox'>

所以延续比值判别法和拉贝判别法,思路过来是和

$$
\begin{gathered}
\dfrac{1}{n\ln^p n} \sim \int_A^{\infty} \dfrac{1}{x\ln^p x} dx = \int_{\ln A}^\infty \dfrac{1}{x^p} dx
\end{gathered}
$$

比较是合理的.于是只要考虑

$$
\begin{gathered}
\dfrac{(n+1)\ln^p(n+1)} {n\ln^p n} \\
=(1+\dfrac{1}{n} )(1+\dfrac{\ln(1+\dfrac{1}{n} )}{\ln n} )^p \\
\sim (1+\dfrac{1}{n} )(1+\dfrac{\dfrac{1}{n} }{\ln n} )^p \\
\sim (1+\dfrac{1}{n} )(1+\dfrac{p}{n\ln n} +o(\dfrac{1}{n\ln n} )) \\
\sim 1+\dfrac{1}{n} +\dfrac{p}{n\ln n} +o(\dfrac{1}{n\ln n})
\end{gathered}
$$

这样就好了.

</div>

这个形式不是很好用,应该改成

$$
\begin{gathered}
((\dfrac{a_n}{a_{n+1}} -1)n-1)\ln n
\end{gathered}
$$

的极限实际上就是那个$l$.

<div class='cbox'>

$$
\begin{gathered}
a_n>0,S_n=\sum _{i = 1} ^{n}  a_i \\
\Rightarrow \sum _{n = 1} ^{\infty}  \dfrac{a_n}{S_n^2} <\infty
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\sum _{n = 1} ^{\infty}  \dfrac{a_n}{S_n^2}  \\
\le \sum _{n = 1} ^{\infty}  \dfrac{S_n-S_{n-1}}{S_nS_{n-1}} 
\end{gathered}
$$

然后列项,显然.

</div>


## Class 29

### Egs

<div class='cbox'>

$$
\begin{gathered}
S_n=\sum _{i = 1} ^{n}  a_i,\sum a_i \text{ is divergent}  \\
\Rightarrow \begin{cases}
\sum \dfrac{a_n}{1+a_n} \text{ is divergent}  \\
\sum \dfrac{a_n}{S_n} \text{ is divergent} 
\end{cases}

\end{gathered}
$$

</div>

<div class='pbox'>

(1):

如果无界是显然的,会有一个子列趋向于$1$.

如果有界把分母放成$M+1$即可.

(2):

这种抽象的东西柯西用的多啊感觉

反正就是柯西,考虑

$$
\begin{gathered}
\sum _{i = l} ^{r} \dfrac{a_i}{S_i} \ge \sum _{i = l} ^{r}  \dfrac{a_i}{S_r} =\dfrac{S_r-S_{l-1}}{S_r} =1-\dfrac{S_{l-1}}{S_r} 
\end{gathered}
$$

那么固定$l$让$r$增大这个东西是趋近于$1$的,就做完了.

</div>

### 非正项级数

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
a_n \text{ is decreasing}  \\
a_n (-1)^n >0
\end{cases} \\
\Rightarrow \sum a_i \text{ is convergent} 
\end{gathered}
$$

</div>

<div class='pbox'>

注意到,$a_n$后面任意长度求和的绝对值都不可能大于$a_n$(可以从后往前归纳),并且$a_n \to 0$,于是柯西.

</div>

注意到柯西出生的时候莱布尼茨已经死了

<div class='cbox'>

Abel 引理

$$
\begin{gathered}
\begin{cases}
\vert S_k \vert =\vert \sum _{i = 1} ^{k}  a_i \vert \le M  \\
b_n \text{ is monotonic} 
\end{cases}
\\
\Rightarrow \vert \sum _{i = 1} ^{n}  a_ib_i \vert \le M(\vert b_1 \vert +2 \vert b_n \vert )
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\vert \sum _{i = 1} ^{n}  a_ib_i \vert \\
={\left \vert \sum _{k = 1} ^{n-1}  S_k(b_k-b_{k-1})+s_nb_n \right \vert}  \\
\end{gathered}
$$

左边那个放成 $M (\vert b_1 \vert +\vert b_n \vert)$,右边那个方成$M\vert b_n\vert$.

</div>



<div class='cbox'>

迪利克雷判别法

$a_n$单调下降收敛到$0$,$b_n$的部分和数列有界,则$\sum a_nb_n$收敛

</div>

<div class='pbox'>

柯西判别法,对中间那一段用上面的阿贝尔引理,就变成了$2M(b_l+2b_r)$.然后显然收敛.

</div>

### Egs

<div class='cbox'>

$$
\begin{gathered}
\sum \dfrac{\cos nx}{n} 
\end{gathered}
$$

条件收敛

</div>

<div class='pbox'>

迪利克雷判别法,你要用到$\sum \cos nx$有界,然后这个是有通项得到所以显然.

然后怎么说明绝对值发散呢?

$$
\dfrac{\cos nx}{n} >\dfrac{\cos^2 nx}{n} =\dfrac{1}{2n} -\dfrac{\sin(2nx)}{2n}
$$

然后第一个的级数发散第二个收敛所以整体发散.

</div>

[think] 似乎带$\sin$的都可以这么做?通过上面一样的做法你至少可以说明如果$a_n>0$递减,那么$\sum a_n\vert \sin n\vert$收敛等价于$\sum a_n$收敛.

<div class='cbox'>

$$
\begin{gathered}
\lim_{n \to \infty} n(\dfrac{a_n}{a_{n+1}} -1)=\lambda>0 \\
\Rightarrow \sum _n  (-1)^n a_n < \infty
\end{gathered}
$$

</div>

<div class='pbox'>

$n>N$时可以让 $n(\dfrac{a_n}{a_{n+1}} -1)\in (\lambda-\epsilon,\lambda+\epsilon),\epsilon<\lambda$

于是

$$
\begin{gathered}
\dfrac{a_{n+1}}{a_n} \in (\dfrac{n}{n+\lambda+\epsilon} ,\dfrac{n}{n+\lambda-\epsilon} )
\end{gathered}
$$

于是

$$
\begin{gathered}
\ln a_n=\ln a_1+\sum _{i = 2} ^{n}  \ln \dfrac{a_{n+1}}{a_n}  \\
<C+\sum _{i = 2} ^{n}  \ln(\dfrac{n}{n+\lambda-\epsilon} ) \\
<C+\sum _{i = 2} ^{n}  -\dfrac{\lambda-\epsilon}{n+\lambda-\epsilon} 
\end{gathered}
$$

于是取极限这个发散到负无穷,$a_n$收敛到$0$.

</div>

## Class 30

### 级数的乘积

<div class='dbox'>

柯西乘积

$$
\begin{gathered}
c_n=\sum_{i} a_ib_{n+1-i}
\end{gathered}
$$

</div>

<div class='cbox'>

$\sum a,\sum b$收敛不能推出$\sum c$收敛

</div>

<div class='pbox'>

因为你重排顺序了.你需要构造某些正负级数.

比如$a_n=b_n=(-1)^n \dfrac1{\sqrt n}$有

$$
\begin{gathered}
c_n=(-1)^{n+1} \sum _{i = 1} ^{n} \dfrac{1}{\sqrt{i(n-i+1)}}  \\
\ge (-1)^{n+1}\sum _{i = 1} ^{n} \dfrac{2}{n+1}  \\
=2\times (-1)^{n+1}  
\end{gathered}
$$

</div>

<div class='cbox'>

若$\sum a,\sum b$其中有一个绝对收敛那么$\sum c$收敛且$(\sum c)=(\sum a)(\sum b)$

</div>

<div class='pbox'>

不妨设$\sum a$绝对收敛,$A_n,B_n,C_n$分别为对应部分和,$A,B,C$为对应极限,则

$$
\begin{gathered}
 C_n  =\sum _{i = 1} ^{n}  c_i  \\
=\sum _{i = 1} ^{n}  a_iB_{n+1-i}  \\
=\sum_{i=1}^n a_i(B_{n+1-i}-B)+\sum _{i = 1} ^{n}  a_iB
\end{gathered}
$$

第二个明显趋向$AB$,看第一个,设$d_n=B_{n+1-i}-B$,存在$N$使得这之后的$d_n<\epsilon_1$,$\sum _{i = N} ^{\infty}  a_i<\epsilon_2$.因为你要用到对一项的放缩所以你要取绝对值:

$$
\begin{gathered}
{\left \vert \sum _{i = 1} ^{n}  a_id_{n+1-i} \right \vert}  \\
\le \sum _{i = 1} ^{n}  \vert a_id_{n+1-i} \vert  \\
=\sum _{i = 1} ^{N}  \vert a_id_{n+1-i} \vert  +\sum _{i = N+1} ^{n}  \vert a_id_{n+1-i} \vert  \\
\le A\epsilon_1+\epsilon_2D
\end{gathered}
$$

其中$D$是$d$的界.

于是对$\epsilon_1,\epsilon_2$取极限就是$0$了.

</div>

[think] 利用收敛级数的性质当然一定要区间和

<div class='cbox'>

$$
\begin{gathered}
\sum a<\infty,\sum b<\infty,\sum c<\infty \\
\Rightarrow (\sum a)(\sum b)=(\sum c)
\end{gathered}
$$

</div>

<div class='pbox'>

仍然用$A_n,B_n,C_n$表示部分和,$A,B,C$表示极限.

我们要证明我们用方形,三角形覆盖全平面的极限是相同的.难以想到的是转化成计算平均值:

考虑

$$
\begin{gathered}
C=\dfrac{1}{n+1} \sum _{i = 0} ^{n}  C_n \\
=\dfrac{1}{n+1} \sum _{i = 0} ^{n} \sum _{j = 0} ^{i} a_{i-j}B_j \\
=\dfrac{1}{n+1} \sum _{j = 0} ^{n} \sum _{i = j} ^{n} a_{i-j}B_j \\
=\dfrac{1}{n+1} \sum _{j = 0} ^{n}  B_jA_{n-j} \\
=AB
\end{gathered}
$$

第一个等号是Stolz,最后一个等号是经典结论(在math-analysis1里面有)

但就是很难想到吧.

</div>

[think] 我们发现从$a*b=c\Rightarrow A*B=C$其实是自然的(求和是卷$1$)是容易的.另外取平均值是提取频率为$0$的分量.

## Class 31

### 无穷乘积

<div class='dbox'>

乘积收敛到非$0$的正数.

</div>

<div class='cbox'>

$$
\begin{gathered}
\prod(1+a_i)<\infty \Leftrightarrow \sum \ln(1+a_i)<\infty
\end{gathered}
$$

</div>

<div class='pbox'>

显然

</div>

<div class='cbox'>

$$
\begin{gathered}
a_n>0 \Rightarrow  \\
\sum \ln(1+a_n) <\infty \Leftrightarrow \sum a_n<\infty
\end{gathered}
$$

</div>

<div class='pbox'>

这不是

$$
\begin{gathered}
\lim_{n \to \infty} \dfrac{\ln(1+a_n)}{a_n} =1
\end{gathered}
$$

吗

</div>

<div class='cbox'>

$$
\begin{gathered}
-1<a_n<0,a_n\to 0 \Rightarrow  \\
\sum \ln(1+a_n)>-\infty \Leftrightarrow \sum a_n>-\infty
\end{gathered}
$$

</div>
<div class='pbox'>

都取负仍然比值判别法结束

</div>

<div class='cbox'>

若$\sum a_n$收敛,则

$$
\begin{gathered}
\sum \ln(1+a_n) \text{ is convergent}  \\
\Leftrightarrow \sum a_n^2 \text{ is convergent} 
\end{gathered}
$$

</div>

<div class='pbox'>

右推左:
$$
\begin{gathered}
\ln(1+a_n)=a_n-\dfrac{a_n^2}{2} +o(a_n^2)
\end{gathered}
$$

第一项收敛是条件,第二项收敛则第三项一定收敛.

左推右:$\ln(1+a_n)-a_n=-\dfrac{a_n^2}{2}+o(a_n^2)\in (-\dfrac{3}{4} a_n^2,-\dfrac{1}{4} a_n^2)$.

其实就是如果一次的不保号就比较恒正的二次.

</div>

### 上极限

<div class='dbox'>

极限点集:

$$
\begin{gathered}
E=\{ a \vert \exists k_n,\lim_{n \to \infty} a_{k_n}=a \} 
\end{gathered}
$$

</div>

<div class='cbox'>

$$
\begin{gathered}
E=\{ a \} \Leftrightarrow \lim_{n \to \infty} a_n=a
\end{gathered}
$$

</div>

<div class='pbox'>

首先一个数列的极限点一定不为空:有界则必有收敛子列,无界就是无穷.

于是任意子列如果极限不为$a$代表$a$的某个邻域外有无限个点,那么它们有一个聚点,于是矛盾.

就证完了.

</div>

