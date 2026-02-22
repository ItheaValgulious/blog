---
title: Math Analysis Huashi Xia
tags: [math-analysis,math,self-study]
---

# Math Analysis Huashi Xia

只挑了几点

## 一致收敛这一块

### Dini定理

<div class='cbox'>

若闭区间上的函数列$f_n$逐点收敛到$f$,$f_n\in C,f\in C,f_n<f_{n+1}$,则$f_n\rightrightarrows f$

</div>

<div class='pbox'>

因为$f_n$单增,所以$f-f_n$一定是单调减的.

所以很直觉的,对每个点$x_0$,存在$N$使得 $\forall n>N,|f_n(x_0)-f(x_0)|<\delta_0$,因为$f,f_n$连续,这个点一定有一个邻域$U$有$\forall x\in U,|f_N(x)-f_N(x_0)|<\delta_0,|f-f(x_0)<\delta_0|$于是这个邻域内$\forall n>N,|f_n(x)-f(x)| \le |f_N(x)-f(x)|\le |f_N(x)-f_N(x_0)|+|f_N(x_0)-f(x_0)|+|f(x)-f(x_0)|=3\delta_0$.

这就很显然了,叠一个有限覆盖就结束了.对开区间我们就只能内闭一致收敛.

</div>

## 多元函数微分

### 可微的条件

我们知道可微是说你可以被平面近似.

<div class='cbox'>

方向导数均存在且满足条件$\dfrac{df}{dv}=\sum_i f_{x_i} \cos(\theta_i)$不保证函数可微

</div>

<div class='pbox'>

首先如果你可微的话,这个式子是一定满足的,考虑$\cos \theta_i$实际上就是分量$v_i$:

$$
\begin{gathered}
\dfrac{df}{dv} =\lim_{k \to 0} \dfrac{f(x+kv)-f(x)}{k} =\dfrac{Akv+o(kv)}{k}=Av=\sum_i A_{i,.}v=\sum_i (\dfrac{df_i}{dx}) \cdot v_j
\end{gathered}
$$

但是这个满足不一定可微,因为方向导数说的是你看他某一条直线上的一元函数,但直线上对不能让平面上对,实际上他甚至不一定连续啊(经典 $\dfrac{x^2y}{x^4+y^2}$),如果我们让他连续,举例:

$$
\begin{gathered}
f(x,y)=\begin{cases}
0, x=y=0 \\
\dfrac{x^2y}{x^4+y^2} \cdot x,\text{otherwise}
\end{cases}

\end{gathered}
$$

这么写是因为,$\dfrac{x^2y}{x^4+y^2}$是一个常见的说明直线上连续不等于连续的例子,特点是$y=x^2$上是 $\dfrac12$,而其他地方是$0$,乘完了之后发现:

$$
\begin{gathered}
\dfrac{df}{d\vec v}= \dfrac{f(k\vec v)-f(0)}{k}=\dfrac{1}{k}=0
\end{gathered}
$$

但$f(x,x^2)=\dfrac{1}{2}x\ne o(|(x,x^2)|)$,所以不对.

</div>

<div class='cbox'>

偏导数连续则函数可微

</div>

<div class='pbox'>

假设$f(x,y)$的偏导$f_x(x,y),f_y(x,y)\in C(x_0,y_0)$,则:

$$
\begin{gathered}
f(x_0+\Delta x,y_0+\Delta y)-f(x,y) \\
=f(x_0+\Delta x,y_0+\Delta y)-f(x_0+\Delta x,y_0)+f(x_0+\Delta x,y_0)-f(x_0,y_0) \\
=f_y(x_0+\Delta x,\xi_1)\Delta y+o(\Delta y)+f_x(\xi_2,y_0)\Delta x+o(\Delta x) \\
=f_x(\xi_2,y_0)\Delta x+f_y(x_0+\Delta x,\xi_1)\Delta y+o({\sqrt{(\Delta x)^2+(\Delta y)^2}}) \\
\to f_x(x_0,y_0)\Delta x+f_y(x_0,y_0)\Delta y
\end{gathered}
$$

</div>

这里还会讲一个中值定理,但一开始看他感觉很平凡,大概说的是如果在包含$A,B$这条直线的区域上可微就有$f(A)-f(B)=\nabla f(\xi)\cdot \vec{AB}$.你考虑在这条线上的一元拉格朗日中值,然后套上方向导数那个式子.所以实际上也很平凡.

<div class='cbox'>

混合偏导中任意一个连续,且混合偏导都存在,则全都相等

</div>

<div class='pbox'>

设$f_{x,y}$连续,考虑证明$f_{x,y}=f_{y,x}$.

$$
\begin{gathered}
f_{x,y}(x,y)=\lim_{\Delta y \to 0} \lim_{\Delta x\to 0} \dfrac{1}{\Delta y} (\dfrac{f(x+\Delta x,y+\Delta y)-f(x,y+\Delta y)}{\Delta x}-\dfrac{f(x+\Delta x,y)-f(x,y)}{\Delta x} ) \\
=\lim_{\Delta y \to 0} \lim_{\Delta x\to 0} \dfrac{f(x+\Delta x,y+\Delta y)-f(x,y+\Delta y)-f(x+\Delta x,y)+f(x,y)}{\Delta x\Delta y}  \\
=\lim_{\Delta y \to 0} \lim_{\Delta x\to 0} \dfrac{1}{\Delta x} (\dfrac{f(x+\Delta x,y+\Delta y)-f(x+\Delta x,y)}{\Delta y} -\dfrac{f(x,y+\Delta y)-f(x,y)}{\Delta y} ) \\
=\lim_{\Delta y \to 0} \lim_{\Delta x\to 0} \dfrac{f_y(x+\Delta x,y+\xi_1)-f_y(x,y+\xi_2)}{\Delta x} ,(\xi_1,\xi_2\in (0,\Delta y)) \\

\end{gathered}
$$





</div>





隐函数定理

## 重积分

面积定义

Peano曲线

变量代换

可积与绝对可积

## 微分形式

## 场论相关

## 傅里叶级数

## 两类欧拉积分