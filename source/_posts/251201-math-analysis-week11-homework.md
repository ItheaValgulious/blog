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

