---
title: Fun Math Stories
tags: [math,whims,note]
---
# Fun Math Stories

记录一些科普.

## 20260304

怎么解方程:

### Intro

解三次方程:

<div class='cbox'>

$x^3+ax+b=0$

</div>

显然三次方程都可以通过平移缩放先变成这个样子.

<div class='pbox'>

设$x=(u+v)$,则:

$$
\begin{gathered}
(u+v)^3+a(u+v)+b=0 \\
\Leftrightarrow (u^3+v^3)+(3uv+a)(u+v)+b=0
\end{gathered}
$$

此时因为我们只要$u+v$,所以可以规定$3uv=-a$,于是只要解:

$$
\begin{gathered}
\begin{cases}
3uv=-a \\
u^3+v^3=-b
\end{cases}
\end{gathered}
$$

对第一个两边同时立方,得到一个$u^3,v^3$的方程,可以把它俩解出来.

</div>

### Think

考虑三次方程应该有$3$个解,设为$x_1,x_2,x_3$.而$u,v$会有$9$组解,我们看到最后$u,v$都是开立方算出来的,所以$u$的解一定是$u,wu,w^2u$,$v$有$v,wv,w^2v$,但是$uv=-a$限制了其中只有:$(u,v),(wu,w^2v),(w^2u,wv)$这3组.

那么由

$$
\begin{gathered}
\begin{cases}
x_1=u+v \\
x_2=wu+w^2v \\
x_3=w^2u+wv
\end{cases}
\end{gathered}
$$

那么此时可以反解出$u$和$v$是什么.然后因为$w$和$x$之间都有一些关系所以形式很多,其中有一个是:

$$
\begin{cases}
u = \frac{1}{3}(x_1 + \omega^2 x_2 + \omega x_3) \\
v = \frac{1}{3}(x_1 + \omega x_2 + \omega^2 x_3)
\end{cases}
$$

它有一定的对称性:交换$x_1,x_2$你会发现$u$变成$w^2v$,$v$变成$wu$.于是你发现$u^3,v^3$对任意的$x$的变换是不变的.

这里需要思考对称性:我们知道韦达定理,所以任意$a,b,c$都是关于$x_1,x_2,x_3$的任意交换完全对称的,也就是说只用$a,b,c$的线性组合是无法区分3个根的.

所以如果你想找一些中间变量的话,它首先一定是可以区分根的,而若表示到系数上又必须是不可区分的.

### More

