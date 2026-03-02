---
title: Math Analysis Homework - Week 11
tags:
  - math
  - math-analysis
  - homework
date: 2025-12-01 18:21:57
---


# Math Analysis Homework - Week 11

## Class 1

### T1

计算曲线围成的面积

<div class='cbox'>

$$
\begin{gathered}
x=y^2,y=x^2 \\
y=\sin x,y=\cos x,x=0,x=2\pi \\
x=a(\cos t+t\sin t),y=a(\sin t-t\cos t)(0\le t\le 2\pi),x=a \\
r^2=a^2\cos 2\theta (a>0)
\end{gathered}
$$

</div>

<div class='pbox'>

(1)

$$
\begin{gathered}
S=\int_0^1 (\sqrt x-x^2)dx \\
=(\dfrac{2}{3} x^{\frac32} -\dfrac{x^3}{3} )\vert_0^1 \\
=\dfrac{1}{3}
\end{gathered}
$$

(2)

$$
\begin{gathered}
\int_0^{2\pi} \vert \sin x-\cos x \vert dx \\
=\int_0^{2\pi}\vert \sqrt 2\sin(x-\dfrac{\pi}{4} ) \vert dx \\
=2\sqrt 2\int_0^{\pi}\vert \sin{x} \vert  \\
=4\sqrt 2
\end{gathered}
$$

(3)

$$
\begin{gathered}
S_1 =\dfrac{1}{2}\int_0^{2\pi}(x,y)\times (x+dx,y+dy) \\
=\dfrac{1}{2}\int_0^{2\pi} x(y+dy)-y(x+dx) \\
=\dfrac{1}{2} \int_0^{2\pi}xdy-ydx \\
=\dfrac{a^2}{2} \int_0^{2\pi} ((\cos t+t\sin t)(t\sin t)-(\sin t-t\cos t)(t\cos t))dt \\
=\dfrac{a^2}{2} \int_0^{2\pi} t^2dt \\
=\dfrac{4a^2\pi^3}{3}  \\
S_2=\dfrac{1}{2}\times a^2\times 2\pi \\
=\pi a^2 \\
S=S_1+S_2=\dfrac{4a^2\pi^3}{3} +\pi a^2
\end{gathered}
$$

(4)

$$
\begin{gathered}
\dfrac{1}{2}\int_0^{2\pi} a^2 \vert \cos(2\theta) \vert  d\theta \\
=\dfrac12 2\int_{-\frac\pi4}^{\frac\pi4} a^2 \vert \cos(2\theta) \vert  d\theta \\
=\dfrac12a^2 \sin2\theta \vert_{-\frac\pi4}^{\frac\pi4} \\
=a^2
\end{gathered}
$$




</div>



### T2

<div class='cbox'>

求弧长

$$
\begin{gathered}
y=\ln \cos x,x\in[0,\dfrac{\pi}{3} ] \\
y=\int_{-\sqrt 3}^x \sqrt{3-t^2}dt \\
\theta=\dfrac{1}{2} (r+\dfrac{1}{r} )(1\le r\le 3)
\end{gathered}
$$

</div>

<div class='pbox'>

(1)
$$
\begin{gathered}
\int_0^{\frac\pi3}\sqrt{1+y'^2}dx \\
=\int_0^{\frac\pi3}\sqrt{1+\tan^2x}dx \\
=\int_0^{\frac\pi3}\sec xdx \\
=(\ln \vert \sec x+\tan x \vert) \vert_0^{\frac\pi3} \\
=\ln(2+\sqrt 3)
\end{gathered}
$$

(2)
$$
\begin{gathered}
\int_{-\sqrt 3}^{\sqrt 3} \sqrt{1+y'^2}dx \\
=\int_{-\sqrt 3}^{\sqrt 3} \sqrt{4-x^2}dx \\
=\int_{-\frac\pi3}^{\frac\pi3}4\cos^2 tdt \\
=\int_{-\frac\pi3}^{\frac\pi3}2(1+\cos 2t)dt \\
=(2x+\sin 2x)\vert_{-\frac\pi3}^{\frac\pi3} \\
=\dfrac{4}{3} \pi+\sqrt 3
\end{gathered}
$$

(3)
$$
\begin{gathered}
\int_A^B \sqrt{r'^2+r^2}d\theta \\
=\int_1^3 \sqrt{1+r^2(\dfrac{1}{2} -\dfrac{1}{2r^2} )^2}dr \\
=\int_1^3 \dfrac{r^2+1}{2r} dr \\
=2+\dfrac{\ln 3}{2} 
\end{gathered}
$$

</div>



### T3

<div class='cbox'>

过点 $P(1,0)$ 作抛物线 $y=\sqrt{x-2}$ 的切线，求该切线与抛物线及 $x$ 轴所围成的平面图形绕 $x$ 轴、$y$ 轴旋转而成的旋转体体积.

</div>

<div class='pbox'>

$$
\begin{gathered}
x=y^2+2
\end{gathered}
$$

切线:$y=\dfrac{1}{2} x-\dfrac{1}{2} \Leftrightarrow x=2y+1$

绕y:

$$
\begin{gathered}
\pi\int_0^1 ((y^2+2)^2-(2y+1)^2) dy \\
=\dfrac{6\pi}{5} 
\end{gathered}
$$

绕x:

$$
\begin{gathered}
\pi\int_2^3 ((\dfrac{1}{2} x-\dfrac{1}{2} )^2-(\sqrt{x-2})^2)dx+\dfrac{1}{3} 1\times \pi\times \dfrac{1}{2^2}  \\
=\dfrac{1}{6} \pi
\end{gathered}
$$

</div>



### T4

<div class='cbox'>

求心形线的一段 $r=a(1+\cos\theta) \left(0 \leqslant \theta \leqslant \frac{\pi}{2}\right)$ 与 $\theta = \frac{\pi}{2}$ 和极轴所围成图形绕极轴旋转一周所得立体的体积.

</div>

<div class='pbox'>

$$
\begin{gathered}
\int_a^b y^2dx \\
=\pi\int_{\frac\pi2}^0 r^2\sin^2 t(r'\cos t-r\sin t)dt \\
=-\pi\int_0^{\frac\pi2} r^2\sin^2 t(r'\cos t-r\sin t)dt \\
=-\pi (\int_0^{\frac\pi2} (r^2r'dt)(\sin^2t\cos t)-\int_0^{\frac\pi2} r^3\sin^3dt) \\
=-\pi (\dfrac{r^3}{3}\sin^2t\cos t\vert_0^{\frac\pi2}-\int_0^{\frac\pi2} \dfrac{r^3}{3} (2\sin t\cos^2 t-\sin^3)dt-\int_0^{\frac\pi2} r^3\sin^3 dt) \\
=\int_0^{\frac\pi2} \dfrac{2\pi}{3}r^3 \sin tdt
\end{gathered}
$$

所以

$$
\begin{gathered}
V=\int_0^{\frac \pi2} \dfrac{2\pi}{3} a^3(1+\cos \theta)^3\sin \theta d\theta \\
=\int_0^{\frac \pi2} \dfrac{2\pi}{3} a^3(1+\cos \theta)^3d(1+\cos\theta) \\
=\dfrac{5}{2} \pi a^3
\end{gathered}
$$

</div>



### T5

<div class='cbox'>


证明：图形 $0 \leqslant y \leqslant y(x), a \leqslant x \leqslant b$ 绕 $y$ 轴旋转所得的旋转体体积为
$$ V_y = 2\pi \int_a^b xy(x)\mathrm{d}x. $$
并由此计算：
(1) 由 $y=x(x-1)^2$, $y=0$ 所围图形绕 $y$ 轴旋转所得的旋转体体积;
(2) 由 $y=\sin x \; (0 \leqslant x \leqslant \pi)$, $y=0$ 所围图形绕 $y$ 轴旋转所得的旋转体体积.


</div>

<div class='pbox'>

微元法,取一个内径为$x$,外径为$x+dx$,高为$y$的圆环柱体,体积为$\pi y((x+dx)^2-x^2)=2\pi yxdx+y\pi(dx)^2\approx 2\pi yxdx$,累加即得.

(1)

$$
\begin{gathered}
V=2\pi\int_0^1 x^2(x-1)^2 dx \\
=2\pi \int_0^1 (x^4-2x^3+x^2)dx \\
=\dfrac{\pi}{15} 
\end{gathered}
$$

(2)

$$
\begin{gathered}
V=2\pi \int_0^\pi x\sin xdx \\
=2\pi^2
\end{gathered}
$$

</div>

## Class 2

### T1
<div class="cbox">

1. 计算下列反常积分：
$$
\begin{gathered}
(5) \int_0^{+\infty} \frac{1+x^2}{1+x^4} \mathrm{d}x
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=\int_0^{+\infty} \dfrac{1+\dfrac{1}{x^2} }{x^2+\dfrac{1}{x^2} } dx \\
\text{let }t=x-\dfrac{1}{x}  \\
Ans=\int_{-\infty}^{+\infty} \dfrac{1}{t^2+2}dt  \\
\text{let } t=\sqrt 2\tan t \\
Ans=\int_{-\frac{\pi}2}^{\frac{\pi}2} \dfrac{\sqrt 2\sec^2 t}{2\sec^2 t} dt \\
=\dfrac{\sqrt 2\pi}{2} 
\end{gathered}
$$



</div>



### T2
<div class="cbox">

1. 计算下列反常积分：
$$
\begin{gathered}
(6) \int_0^{+\infty} \frac{x \mathrm{e}^{-x}}{\left(1+\mathrm{e}^{-x}\right)^2} \mathrm{d}x
\end{gathered}
$$  

</div>

<div class='pbox'>

$$
\begin{gathered}
\int \dfrac{e^{-x}}{(1+e^{-x})^2} dx \\
=\int -\dfrac{dt}{(1+t)^2}  \\
=\dfrac{1}{1+t}+C \\
=\dfrac{1}{1+e^{-x}}+C \\
\text{let } C=-1 \\

\Rightarrow Ans=\dfrac{-xe^{-x}}{1+e^{-x}}\vert_0^{+\infty} -\int_0^{+\infty} \dfrac{-e^{-x}}{1+e^{-x}}dx \\
=  0+\ln 2 \\
=\ln 2
\end{gathered}
$$

</div>




### T3
<div class="cbox">

2. 判断下列无穷积分的敛散性：
$$
\begin{gathered}
(4) \int_0^{+\infty} \frac{x}{\mathrm{e}^x + \mathrm{e}^{-x}} \mathrm{d}x
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\le \int_0^{\infty} \dfrac{x}{e^x}  \\
\le \int_0^\infty \dfrac{x}{1+x+\dfrac{x^2}{2}+\dfrac{x^3}{6} }  \\
\le \int_0^1 \dfrac{x}{e^x}+\int_1^\infty \dfrac{6}{x^2}   \\
\le 1+\int_1^{\infty} \dfrac{6}{x^2} 
\end{gathered}
$$

第二项收敛.所以收敛.

</div>



### T4
<div class="cbox">

2. 判断下列无穷积分的敛散性：
$$
\begin{gathered}
(5) \int_1^{+\infty} \left[ \ln\left(1+\frac{1}{x^2}\right) - \frac{1}{1+x^2} \right] \mathrm{d}x
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\ln(1+\dfrac{1}{x^2} )-\dfrac{1}{1+x^2}  \\
=\dfrac{1}{x^2}-\dfrac{1}{2x^4}+o(\dfrac{1}{x^5} ) -\dfrac{1}{x^2} +\dfrac{1}{x^4}  \\
=\dfrac{1}{2x^4} +o(\dfrac{1}{x^5} ) \\
\Rightarrow \lim_{x \to \infty} \dfrac{\left[ \ln\left(1+\frac{1}{x^2}\right) - \frac{1}{1+x^2} \right]}{\dfrac{1}{2x^4} } =1 \\
\Rightarrow \text{Convergent} 
 
\end{gathered}
$$

</div>



### T5
<div class="cbox">

2. 判断下列无穷积分的敛散性：
$$
\begin{gathered}
(6) \int_1^{+\infty} x\left(1-\cos\frac{1}{x^2}\right)^p \mathrm{d}x, \quad p \in \mathbb{R}
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\cos \dfrac{1}{x^2} =1-\dfrac{1}{2x^4}+o(x^5) \\
\Rightarrow \lim_{x \to \infty} \dfrac{x(1-\cos \dfrac{1}{x^2} )^p}{x^{1-4p}} =C\in (0,\infty) \\
\int_1^{+\infty} x(1-\cos \dfrac{1}{x^2} )^p\begin{cases}
\text{ is convergent} ,p>\dfrac{1}{2}  \\
\text{ isn't convergent} ,p\le \dfrac{1}{2} 
\end{cases}

\end{gathered}
$$

</div>



### T6
<div class="cbox">

3. 判断下列无穷积分的敛散性（含绝对收敛性与条件收敛性）：
$$
\begin{gathered}
(3) \int_1^{+\infty} \sin\left(\frac{\sin x}{x}\right) \mathrm{d}x
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\int_a^b \sin(\dfrac{\sin x}{x} )dx \\
=\sum_{i=A}^B \int_{k\pi}^{(k+1)\pi}\sin(\dfrac{\sin x}{x} )dx \\
+\int_a^{A\pi}\sin(\dfrac{\sin x}{x} )dx+\int_{B\pi}^b \sin(\dfrac{\sin x}{x} )dx
\end{gathered}
$$

其中第一项因为正负交替且递减,求和式绝对值小于第一项$\int_{k\pi}^{(k+1)\pi}\sin (\dfrac{\sin x}x)$.于是这三项都为$\int_c^d \sin \dfrac{\sin x}x<2\pi \dfrac{1}{x}$,从而小于$\dfrac{6\pi}{a}$,应用柯西收敛准则得知手收敛.

而

$$
\begin{gathered}
\int_1^{+\infty}{\left \vert  \sin \dfrac{\sin x}{x} dx \right \vert}  \\
> \int_1^{+\infty} {\left\vert \dfrac{\sin x}{x}dx\right \vert} -{\left\vert\int_1^{+\infty}\dfrac16(\dfrac{\sin x}{x} )^3dx \right \vert} 
\end{gathered}
$$

第一项发散,第二项收敛,故发散.

条件收敛.

</div>



### T7
<div class="cbox">

3. 判断下列无穷积分的敛散性（含绝对收敛性与条件收敛性）：
$$
\begin{gathered}
(4) \int_1^{+\infty} \frac{\cos(x^p)}{x} \mathrm{d}x, \quad p \in \mathbb{R}
\end{gathered}
$$

</div>

<div class='pbox'>

$p>0$时.

$$
\begin{gathered}
=\int_1^{+\infty}\dfrac{\cos x}{x^{\frac1p}}x^{\frac1p-1} dx \\
=\int_1^{+\infty}\dfrac{\cos x}{x} dx \\
\end{gathered}
$$

$\cos x$积分有界,$\dfrac{1}{x}$递减且收敛到$0$,原式收敛.

绝对值:

$$
\begin{gathered}
\vert \dfrac{\cos x}{x} \vert \ge \dfrac{\sin (x+\frac\pi2)}{x+\frac\pi2} 
\end{gathered}
$$

而后一项积分发散.

故原式条件收敛.

$p\le 0$时,$\lim_{x\to +\infty}\cos x^p=1$

于是取$X$足够大使$\cos x^p>\dfrac{1}{2}$,$\int_X^{+\infty}\dfrac{\cos(x^p)}{x} dx>\dfrac{1}{2}\int_X^{+\infty}\dfrac1x=\infty$,发散.

</div>



### T8
<div class="cbox">

4. 设 $P_m(x)$ 和 $P_n(x)$ 分别为 $m$ 和 $n$ 次多项式，并且当 $x \geqslant a$ 时，$P_n(x) > 0$. 试研究
$$
\begin{gathered}
\int_a^{+\infty} \frac{P_m(x)}{P_n(x)} \sin x \mathrm{d}x
\end{gathered}
$$
的绝对收敛性和条件收敛性.

</div>

<div class='pbox'>

不妨设$x\to +\infty$时$P_m(x)>0$

若$m\ge n$,$\lim_{x\to \infty}\dfrac{P_m(x)}{P_n(x)}=A>0$

$$
\begin{gathered}
\exists X,x>X \Rightarrow \dfrac{P_m(x)}{P_n(x)} >B(B<A) \\
\Rightarrow {\left \vert \int_{2n\pi+\frac\pi4}^{2n\pi+\frac\pi2} \dfrac{P_m(x)}{P_n(x)} \sin xdx \right \vert}  \\
>\dfrac{\sqrt 2B\pi}{8}
\end{gathered}
$$

发散.

若$m<n-1$,

$$
\begin{gathered}
\int {\left \vert \dfrac{P_m(x)}{P_n(x)} \sin x \right \vert} \le \int {\left \vert \dfrac{1}{x^r}  \right \vert}<+\infty, (r>1)
\end{gathered}
$$

绝对收敛

若$m=n-1$,

$$
\begin{gathered}
\dfrac{P_m(x)}{P_n(x)}=\dfrac{1}{x} +o(\dfrac{1}{x})
\end{gathered}
$$

其中第一部分最后条件收敛,第二部分最后收敛,故整体条件收敛.

</div>



### T9
<div class="cbox">

5. 证明无穷积分的对数判别法：设 $f(x) \in C[1, +\infty)$ 且恒正，若 $\lim_{x\to+\infty} \frac{\ln f(x)}{\ln x} = -\lambda$，则当 $\lambda > 1$ 时无穷积分 $\int_1^{+\infty} f(x) \mathrm{d}x$ 收敛.

</div>

<div class='pbox'>

$$
\begin{gathered}
\lim_{x \to +\infty} \dfrac{\ln f(x)}{\ln x} =-\lambda \\
\Rightarrow  \exists 1<a<\lambda,X \ s.t.\ 
x>X \Rightarrow \dfrac{\ln f(x)}{\ln x} <-a, \\
\Rightarrow f(x)<\dfrac{1}{x^a}
\end{gathered}
$$

应用比较判别法,$\int_1^{\infty}\dfrac{1}{x^a}$收敛,得证.

</div>



### T10
<div class="cbox">

6. 设在 $[a, +\infty)$ 上满足：$g(x) \leqslant f(x) \leqslant h(x)$，且 $\int_a^{+\infty} g(x) \mathrm{d}x$ 与 $\int_a^{+\infty} h(x) \mathrm{d}x$ 收敛，请问 $\int_a^{+\infty} f(x) \mathrm{d}x$ 是否收敛？

</div>

<div class='pbox'>

$$
\begin{gathered}
f(x)-g(x)\le h(x)-g(x)<+\infty \\
f(x)=g(x)+(f(x)-g(x))<+\infty
\end{gathered}
$$

收敛.

</div>



### T11
<div class="cbox">

8. 设函数 $f(x)$ 在 $[a, +\infty)$ 上单调减少且趋于 0. 证明：无穷积分 $\int_a^{+\infty} f(x) \mathrm{d}x$ 与 $\int_a^{+\infty} f(x)\sin^2 x \mathrm{d}x$ 同敛散.

</div>

<div class='pbox'>

$$
\begin{gathered}
I_1=\int_a^{+\infty}f(x)dx \\
I_2=\int_a^{+\infty}f(x)\sin^2 xdx\le I_1
\end{gathered}
$$

故$I_1$收敛推出$I_2$收敛.

若$I_1$发散,因为$f$递减,则

$$
\begin{gathered}
F(x)=\int_a^x f(t)dt \\
F(x)<C+4\sum_{i=a} \int_{2i\pi+\frac{\pi}4}^{2i\pi+\frac{3\pi}4}f(t)dt=C+G(x)
\end{gathered}
$$

而

$$
\begin{gathered}
\int_a^x f(t)dt\sin^2 tdt \\
=
H(x) \\
>\sum_{i=a} \int_{2i\pi+\frac\pi4}^{2i\pi+\frac{3\pi}4}f(t)\sin^2tdt \\
>\sum_{i=a} \int_{2i\pi+\frac\pi4}^{2i\pi+\frac{3\pi}4}f(t)\dfrac{1}{2}dt \\
=\dfrac{1}{2} G(x)
\end{gathered}
$$

于是$F(x)<kH(x)$推出$I_2$发散.


</div>



### T12
<div class="cbox">

9. 设函数 $f(x)$ 在 $[a, +\infty)$ 上连续可微，且无穷积分 $\int_a^{+\infty} f(x) \mathrm{d}x$ 与 $\int_a^{+\infty} f'(x) \mathrm{d}x$ 都收敛. 证明：$\lim_{x\to+\infty} f(x) = 0$.

</div>

<div class='pbox'>

$$
\begin{gathered}
\exists X,\forall c,d>X,
{\left \vert \int_c^d f'(x)dx \right \vert} =\vert f(d)-f(c) \vert <\epsilon
\end{gathered}
$$

于是$f(x)$收敛,设收敛到$a$,若$a\ne 0$,存在$0<b<\vert a\vert$

则

$$
\begin{gathered}
\exists X,\forall x>X,\vert f(x) \vert >b,\forall x_1,x_2>X,f(x_1)f(x_2)>0 \\
\vert \int_{a}^\infty f(x)dx \vert =\int_{a}^\infty \vert f(x) \vert dx>\int_a^{\infty}bdx=+\infty
\end{gathered}
$$

矛盾.于是得证.

</div>

