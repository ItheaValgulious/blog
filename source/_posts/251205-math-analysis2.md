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

