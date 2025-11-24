---
title: Math Analysis Homework - Week 9
tags: [math-analysis,homework,math]
date: 2025-11-23 16:55:40
---

# Math Analysis Homework - Week 9

## Class 1

### T1

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f(x)\in C[a,b], \\
\forall g\in C[a,b],\int_a^b f(x)g(x)dx=0
\end{cases} \\
\Rightarrow f(x)=0
\end{gathered}
$$

</div>

<div class='pbox'>

反证,假设存在$f(x_0)\ne 0$,不妨设是$f(x_0)>0$,则存在$(x_0-\delta,x_0+\delta)$使得$\forall x\in (x_0-\delta,x_0+\delta),f(x)>\dfrac{f(x_0)}2$.

取

$$
\begin{gathered}
g(x)=\begin{cases}
1,\vert x-x_0 \vert <\dfrac{\delta}{2}  \\
\vert x-x_0-\dfrac{\delta}{2}  \vert,\vert x-x_0 \vert \in [\dfrac{\delta}{2},\delta) \\
0,\text{otherwise}
\end{cases} \\
\Rightarrow \int f(x)g(x)dx \ge \dfrac{f(x_0)}{2} \delta>0

\end{gathered}
$$

</div>



### T2

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
a,b>0,f(x)\in C[-a,b] \\
f(x)>0,\int_{-a}^bxf(x)dx=0
\end{cases} \\
\Rightarrow \int_{-a}^b x^2f(x)dx\le ab\int_{-a}^b f(x)dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\int_{-a}^0x^2f(x)dx\le \int_{-a}^0 f(x)(-x)adx=\int_{0}^b f(x)xadx\le \int_0^b f(x)abdx \\
\text{similarily, }\int_{0}^b x^2f(x)dx\le \int_{-a}^0 f(x)abdx  \\
\Rightarrow \int_{-a}^b x^2f(x)dx \\
\le \int_{-a}^0 f(x)abdx+\int_0^b f(x)abdx \\
=ab\int_{-a}^b f(x)dx \\
\end{gathered}
$$

</div>



### T3

<div class='cbox'>

$$
\begin{gathered}
f(x)\in C[0,1],f(x)>0 \\
\Rightarrow \int_0^1 f(x)dx\int_0^1 \dfrac{1}{f(x)} dx\ge 1
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
1=\int_0^1 \sqrt{f(x)}\cdot \dfrac{1}{\sqrt{f(x)}} dx\le (\int_0^1 \sqrt{f(x)}^2dx)^\frac12 (\int_0^1 \dfrac{1}{\sqrt{f(x)}} dx)^\frac12 \\
\Rightarrow \int_0^1 f(x)dx\int_0^1 \dfrac{1}{f(x)} dx\ge 1
\end{gathered}
$$

</div>

### T4

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f(x) \in C[0,\pi] \\
\int_0^\pi f(\theta)\cos \theta d\theta = \int_0^\pi f(\theta)\sin \theta d\theta =0 \\
\end{cases} \\
\Rightarrow \exists x_1,x_2\in (0,\pi),f(x_i)=0
\end{gathered}
$$

</div>

<div class='pbox'>

若$f(x)$无零点,则$f(x)\sin (x)$无变号零点,$\int_0^\pi f(x)\sin x dx\ne 0$,$f$至少一个变号零点.

若$f(x)$恰有一个零点$x_1$.

考虑令$\int_0^\pi f(x)(\sin x\cos \varphi+\cos x\sin \varphi)dx=0=\int_0^\pi f(x)\sin(x+\varphi)dx$,于是令$\phi=-x_1$,则$\int f(x)\sin(x+\varphi)dx$不变号,不为$0$,矛盾,得证.

</div>



### T5

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f\in C[a,b],f(x)\ge 0 \\
M=\max f([a,b])
\end{cases}\\
\Rightarrow \lim_{n \to \infty} (\int_a^b f^n(x)dx)^\frac1n=M 
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\int_a^b f^n(x)\le (b-a)M^n  \\
\Rightarrow \lim_{n \to \infty} (\int_a^b f^n(x)dx)^\frac1n\le \lim_{n \to \infty} ((b-a)M^n)^\frac1n=M  \\
\text{let } f(x_0)=M \\
f(x)\in C[a,b] \Rightarrow \forall p<1,\exists \delta,\ s.t.\  \\

\forall x \in (x_0-\delta,x_0+\delta)\cap [a,b],f(x)>pM  \\
\Rightarrow \int_a^b f^n(x)dx>2\delta(pM)^n \\
\Rightarrow \forall p\in(0,1),
\lim_{n \to \infty} (\int_a^b f^n(x)dx)^\frac1n>\lim_{n \to \infty} (2\delta(pM)^n)^\frac1n=pM \\
\Rightarrow \lim_{n \to \infty} (\int_a^b f^n(x)dx)^\frac1n\ge M \\
\Rightarrow \lim_{n \to \infty} (\int_a^b f^n(x)dx)^\frac1n= M \\
\end{gathered}
$$

</div>



### T6

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f \in C[a,b],f(x)\ge 0 \\
f(x) \text{ is strictly increasing}  \\
\forall p,\exists x_p\in [a,b] \\
f^p(x_p)=\dfrac{1}{b-a} \int_a^b f^p(t)dt
\end{cases} \\
\Rightarrow \lim_{p \to +\infty} x_p =b
\end{gathered}
$$

</div>

<div class='pbox'>

$f$严格单增且连续则$f^{-1}$存在且连续,故只需证

$$
\begin{gathered}
f(b)=\lim_{p \to +\infty} f(x_p)=\lim_{p \to +\infty} (\dfrac{1}{b-a} \int_a^b f^p(t)dt)^\frac1p \\
\end{gathered}
$$

而

$$
\begin{gathered}
\lim_{p \to +\infty} (\dfrac{1}{b-a} \int_a^b f^p(t)dt)^\frac1p
=\lim_{p \to +\infty} (\dfrac{1}{b-a} )^\frac1p (\int_a^b f^p(t)dt)^\frac1p \\
\xlongequal{by T5}\lim_{p \to +\infty} (\dfrac{1}{b-a} )^\frac1p M^\frac1p \\
=M=f(b)
\end{gathered}
$$



</div>



### T7

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f(x)\in C[0,1]\cap D(0,1) \\
f(1)=2\int_0^\frac12 xf(x)dx
\end{cases} \\
\Rightarrow \exists \xi\in (0,1) \\
f(\xi)+\xi f'(\xi)=0
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\text{let }  g(x)=xf(x) \\
g(1)=2\int_0^\frac12 g(x)dx=2\times \dfrac{1}{2} g(\xi),\xi\in (0,\dfrac{1}{2} ) \\
g(1)=g(\xi) \xRightarrow{\text{Rolle's Theorem} }\exist \xi',g'(\xi')=0=f(\xi)+\xi f'(\xi)
\end{gathered}
$$

</div>



### T8

<div class='cbox'>

$$
\begin{gathered}
\lim_{n \to \infty} \int_0^{\frac\pi2}\sin^n xdx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=\lim_{n \to \infty} \int_0^{\frac\pi2-\delta_n}\sin^n xdx+\int_{\frac\pi2-\delta_n}^{\frac\pi2}\sin^n xdx \\
=\lim_{n \to \infty} (\dfrac{\pi}{2} -\delta)\sin^n \xi+\delta_n\sin^n\xi_2 \\
\le \lim_{n \to \infty} \dfrac{\pi}{2}\cos^n(\delta_n)+\delta_n \\
\text{let }\delta_n=\text{max } v \\ s.t.\\ 
\cos^n(v)<\dfrac{1}{n}  \\
\Rightarrow \lim_{n \to \infty} \delta_n=\lim_{n \to \infty} \arccos((\dfrac{1}{n} )^\frac1n)=\arccos(1)=0 \\
\Rightarrow Ans=\lim_{n \to \infty} \dfrac{\pi}{2} \cos^n(\delta_n)+\delta_n=0
\end{gathered}
$$

</div>



### T9

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f(x) \text{ is integrable on any limited range}  \\
\lim_{x \to +\infty} f(x)=l
\end{cases}
\\
\Rightarrow \lim_{x \to +\infty} \dfrac{1}{x} \int_0^x f(t)dt=l
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\exists X,x>X \Rightarrow \vert f(x)-l \vert <\epsilon \\
\lim_{x \to +\infty} \dfrac{1}{x} \int_0^x f(t)dt \\
=\lim_{x \to +\infty} \dfrac{1}{x} (\int_0^X f(t)dt+\int_X^x f(t)dt) \\
=\lim_{x \to +\infty} \dfrac{1}{x} \int_X^xf(t)dt \\
\in(\lim_{x \to +\infty} \dfrac{1}{x} (l-\epsilon)(x-X),\lim_{x \to +\infty} (l+\epsilon)(x+X )) \\
=(l-\epsilon,l+\epsilon)
\end{gathered}
$$

因为对任意$\epsilon>0$均成立,于是得证.

</div>



### T10

<div class='cbox'>

$$
\begin{gathered}
f(x) \text{ is integrable on } [A,B] \\
\Rightarrow \forall a<b \in (A,B) \\
\lim_{h \to 0} \int_a^b \vert f(x+h)-f(x) \vert dx=0
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\forall T=\{ a=t_0<\ldots< t_n=b \}  \\
\lim_{\vert\vert T \vert\vert  \to 0} \sum _{i = 1} ^{n} w_i(t_i-t_{i-1})=0 \\(w_i=\sup_{x,y \in [t_{i-1},t_i]} f(x)-f(y))
\end{gathered}
$$

对一个$h$,按长度$h$分割得到$\forall i<n,t_i-t_{i-1}=h$的$T$,则$\forall x\in [t_{i-1},t_i]$,$\vert f(x+h)-f(x)\vert\le w_i+w_{i+1}$,于是

$$
\begin{gathered}
\lim_{h \to 0} \int_a^b \vert f(x_h)-f(x) \vert dx\le \lim_{h \to 0} \sum_{i=1}^{n-1}(t_i-t_{i-1})(w_i+w_{i+1})+(t_n-t_{n-1})w_n \\
\le \lim_{h \to 0} 2 \sum _{i = 1} ^{n}w_i(t_i-t_{i-1}) \\
=\lim_{\vert\vert T \vert\vert  \to 0} 2w_i(t_i-t_{i-1}) \\
=0
\end{gathered}
$$

</div>



### T11

<div class='cbox'>

$$
\begin{gathered}
\lim_{x \to +\infty} \dfrac{\int_0^x (\arctan t)^2dt}{\sqrt{1+x^2}} 
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\xlongequal{\text{L'Hospital} }
\lim_{x \to +\infty} \dfrac{\sqrt{1+x^2}\arctan^2 x}{x}  \\
=\lim_{x \to +\infty} \sqrt{ 1+\dfrac{1}{x^2}  } \arctan^2 x \\
=\dfrac{\pi^2}{4} 
\end{gathered}
$$

</div>



### T12

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
b>0,f(x) \in C[0,b] \\
f(x) \text{ is strictly increasing}
\end{cases}  \\
\Rightarrow 2\int_0^b xf(x)dx\ge b\int_0^b f(x)dx 
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\int_0^b f(x)(2x-b)dx \\
=-\int_0^\frac{b}2f(x)(b-2x)dx+\int_\frac{b}2^bf(x)(2x-b)dx \\
=\int_0^\frac{b}2 f(x)(b-2x)(f(b-x)-f(x))dx\ge 0
\end{gathered}
$$

</div>



### T13

<div class='cbox'>

$$
\begin{gathered}
f(x)\in D[0,1],f(0)=0,f'(x)\in[0,1] \\
\Rightarrow \int_0^1 f^3(x)dx\le (\int_0^1 f(x)dx)^2
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\text{let } F(x)=\int_0^x f^3(t)dt-(\int_0^x f(t)dt)^2 \\
F'(x)=f^3(x)-2(\int_0^x f(t)dt)f(x) \\
\text{let } F_1(x)=f^2(x)-2\int_0^x f(t)dt \\
F_1'(x)=2f(x)f'(x)-2f(x)\le 0 \\
\Rightarrow F_1'(x)\le F_1'(0)=0 \\
\Rightarrow F'(x)<0 \\
\Rightarrow F(x)<F(0)=0 \\
\text{Q.E.D}
\end{gathered}
$$

</div>



### T14

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f(x) \in C[0,+\infty) \\
x>0 \Rightarrow \int_0^x f(t)dt=\dfrac{1}{2} xf(x)
\end{cases} \\
\Rightarrow f(x)=cx,x>0
\end{gathered}
$$

</div>

<div class='pbox'>

$x=0$时,显然同样$\int_0^x f(t)dt=\dfrac{1}{2}xf(x)$,这个式子对$[0,+\infty)$成立.

两边同时求导,$f(x)=\dfrac{1}{2} f(x)+\dfrac{1}{2} xf'(x)$,于是

$$
\begin{gathered}
f(x)=xf'(x) \\
\dfrac{f(x)-xf'(x)}{x^2} =0 \\
\Rightarrow (\dfrac{f(x)}{x} )'=0 \\
\Rightarrow f(x)=cx
\end{gathered}
$$


</div>



### T15

<div class='cbox'>

$$
\begin{gathered}
f(x) \in C[0,+\infty),f(x)>0 \\
\Rightarrow \phi(x)=\dfrac{\int_0^x tf(t)dt}{\int_0^x f(t)dt} \text{ is strictly increasing} 
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\int_0^x tf(t)dt<\int_0^x xf(t)dt \\
\Rightarrow 
\phi'(x)=\dfrac{xf(x)\int_0^x f(t)dt-f(x)\int_0^x tf(t)dt}{(\int_0^x f(t)dt)^2}>0 \\
\text{Q.E.D}
\end{gathered}
$$

</div>



### T16

<div class='cbox'>

$$
\begin{gathered}
\int_0^1 (2x-1)e^{x^2-1}dx
\end{gathered}
$$

</div>

<div class='pbox'>

等价于积$\int_0^1 e^{x^2}dx$,感觉做不了.

</div>




### T17

<div class='cbox'>

$$
\begin{gathered}
\lim_{n \to \infty} \sum _{k = 1} ^{n}  \sqrt{ \dfrac{(n+k)(n+k+1)}{n^4}  } 
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=\lim_{n \to \infty} \sum _{k = 1} ^{n}  \dfrac{1}{n} \sqrt{ (\dfrac{k}{n} +1)(\dfrac{k+1}{n} +1) } \\
\end{gathered}
$$

令$f(x)=x,T=\{ t_i=1+\dfrac in \},\xi_i=\sqrt{(\dfrac{k}{n} +1)(\dfrac{k+1}{n} +1)}$,于是原式就是

$$
\begin{gathered}
\int_1^2 xdx=\dfrac{3}{2}
\end{gathered}
$$

</div>



### T18

<div class='cbox'>

$$
\begin{gathered}
\forall x\in[-1,+\infty),f(x)=\int_{-1}^x \dfrac{e^{\frac1t}}{t^2(1+e^\frac1t)^2} dt \\
\Rightarrow  f(x)=?
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\text{let } u=e^{\frac1t} \\
f(x)=-\int_{\frac1e}^{\frac1{e^x}} \dfrac{1}{(1+u)^2} du \\
=\dfrac{1}{e^\frac1x+1} -\dfrac{e}{e+1},x<0 \\
f(0)=1-\dfrac{e}{1+e} =\dfrac{1}{1+e}  \\
x>0 \Rightarrow f(x)=f(0)+f(x)-f(0^+)=\dfrac{1}{e^\frac1x+1} -\dfrac{e}{1+e} +1
\end{gathered}
$$

</div>

## Class 2

### T1

<div class='cbox'>

$$
\begin{gathered}
\int_0^1 \vert 1-2x \vert dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=2\int_0^{\frac12}(1-2x)dx \\
=2(x-x^2\vert^{\frac12}_0)dx \\
=\dfrac{1}{2} 
\end{gathered}
$$

</div>



### T2

<div class='cbox'>

$$
\begin{gathered}
\int_{-\frac\pi2}^{\frac\pi2} \sqrt{ \cos x-\cos^3 x } dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=-2\int^{\frac\pi2}_{0} \sqrt{ \cos x } d\cos x \\
=-\dfrac{4}{3} \cos^{\frac32} x \vert_0^{\frac\pi2} \\
=\dfrac{4}{3} 
\end{gathered}
$$

</div>



### T3

<div class='cbox'>

$$
\begin{gathered}
\int_{\frac1e}^e \vert \ln x \vert dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=-\int_{\frac1e}^1 \ln xdx+\int_1^e \ln xdx \\
=-(x\ln x-x)\vert_{\frac1e}^1+(x\ln x-x)\vert_1^e \\
=1-\dfrac{2}{e}+1 \\
=2-\dfrac{2}{e} 
\end{gathered}
$$

</div>



### T4

<div class='cbox'>

$$
\begin{gathered}
\int_0^\pi e^x \cos^2 xdx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=e^x\cos^2 x \vert_0^\pi+\int_0^\pi e^x 2\cos x\sin xdx \\
=e^\pi-1+\int_0^\pi e^x \sin 2x dx \\
\end{gathered}
$$

$$
\begin{gathered}
\int_0^\pi e^x \sin 2xdx \\
=\dfrac{1}{2}\int_0^{2\pi }e^{\frac{x}{2} }\sin xdx \\
=(e^{\frac x2}\sin x\vert _0^{2\pi})-\int_0^{2\pi}e^{\frac x2}\cos xdx \\
=(e^{\frac x2}\sin x\vert _0^{2\pi})-(2e^{\frac x2}\cos x\vert_0^{2\pi})-2\int_0^{2\pi}e^{\frac x2}\sin xdx \\
\Rightarrow \int_0^\pi e^x\sin 2xdx=-\dfrac{2}{5} e^\pi+\dfrac{2}{5} 
\Rightarrow Ans=\dfrac{3}{5} e^\pi-\dfrac{3}{5} 
\end{gathered}
$$

</div>



### T5

<div class='cbox'>

$$
\begin{gathered}
\int_1^e (x\ln x)^2 dx \\
=(\dfrac{1}{3} x^3\ln^2 x-\dfrac{2}{9} x^3\ln x+\dfrac{2}{27} x^3)\vert_1^e \\
=\dfrac{5e^3-2}{27} 
\end{gathered}
$$

</div>

### T6

<div class='cbox'>

$$
\begin{gathered}
\int_0^1 (1-x^2)^n dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
x=\sin t \\
\int_0^1 (1-x^2)^n dx \\
=\int_0^{\frac{\pi}{2}} \cos^{2n+1}tdt
\end{gathered}
$$

$$
\begin{gathered}
I_m=\int_0^{\frac{\pi}{2}}\cos^m tdt \\
=\sin t\cos^{m-1}t\vert_0^{\frac{\pi}{2}}+(m-1)\int_0^{\frac{\pi}{2}}\sin^2 t\cos^{m-2}tdt \\
=+(m-1)\int_0^{\frac{\pi}{2}}\cos^{m-2}tdt-(m-1)\int_0^{\frac{\pi}{2}}\cos^m tdt \\
=+(m-1)I_{m-2}-(m-1)I_m \\
\Rightarrow I_m=\dfrac{m-1}m I_{m-2} \\
I_1=1 \\
Ans=I_{2n+1}=\dfrac{(2n)!!}{(2n+1)!!} 
\end{gathered}
$$

</div>

### T7

<div class='cbox'>

$$
\begin{gathered}
\int_0^{\frac\pi4}\cos^7 (2x)dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=\dfrac{1}{2}\int_0^{\frac\pi2}\cos^7 xdx \\
=\dfrac{1}{2} I_7 \\
=\dfrac{8}{35} 
\end{gathered}
$$

</div>



### T8

<div class='cbox'>

$$
\begin{gathered}
\int_0^{\frac\pi4}\ln(1+\tan x)dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
I \\
=\int_0^{\frac\pi4}\ln(1+\tan x)dx \\
=\int_0^{\frac\pi4}\ln(1+\tan(\dfrac{\pi}4-x))dx \\
=\int_0^{\frac\pi4}\ln(1+\dfrac{1-\tan x}{1+\tan x} )dx \\
=\int_0^{\frac\pi4}(\ln2-\ln (1+\tan x))dx\\
=\dfrac{\pi}{4} \ln 2-I \\
\Rightarrow I=\dfrac{\pi}{8} \ln 2
\end{gathered}
$$

</div>



### T9

<div class='cbox'>

$$
\begin{gathered}
\int_0^{\frac\pi2}\dfrac{1}{1+\tan^\alpha x} dx(\alpha>0)
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
I=\int_0^{\frac\pi2}\dfrac{1}{1+\tan^\alpha x} dx \\
=\int_0^{\frac\pi2}\dfrac{\tan \alpha x}{1+\tan \alpha x} dx \\
=\int_0^\frac\pi21dx-\int_0^\frac\pi2 \dfrac{dx}{1+\tan \alpha x}  \\
=\dfrac{\pi}{2} -I \\
\Rightarrow I=\dfrac{\pi}{4} 
\end{gathered}
$$

</div>



### T10

<div class='cbox'>

$$
\begin{gathered}
\int_0^{n\pi} x \vert \sin x \vert dx,n\in N
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
I_k=\int_{k\pi}^{(k+1)\pi} x \vert \sin x \vert dx \\
=\int_{(k-1)\pi}^{k\pi} (x+\pi) \vert \sin (x+\pi) \vert dx \\
=\int_{(k-1)\pi}^{k\pi} x \vert \sin x \vert dx
+\pi\int_{(k-1)\pi}^{k\pi}\vert \sin x \vert  \\
=I_{k-1} +2\pi \\
I_0=\int_0^\pi x\sin xdx \\
=(-x\cos x+\sin x) \vert_0^\pi \\
=\pi \\
\Rightarrow Ans=\sum _{i = 0} ^{n-1}  I_i \\
=n^2\pi
\end{gathered}
$$

</div>



### T11

<div class='cbox'>

$$
\begin{gathered}
f(x)\in C(R), \\
\text{calculate }  \dfrac{d}{dx} \int_0^x tf(x^2-t^2)dt
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
F(x)=\int_0^x tf(x^2-t^2)dt \\
\text{let } s=x^2-t^2,ds=-2tdt \\
F(x)=\int_{x^2}^0 \dfrac{-1ds}{2} f(s) \\
=\int_0^{x^2} \dfrac{1}{2} f(s)ds \\
F'(x)=2x \dfrac{1}{2} f(x^2)=xf(x^2)
\end{gathered}
$$

</div>



### T12

<div class='cbox'>

$$
\begin{gathered}
f(x)\in C(R), \\
f(x)=x+2\int_0^1 f(t)dt \\
\text{calculate }  f(x)
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
f'(x)=1 \Rightarrow f(x)=x+C \\
x+C=x+2\int_0^1 (t+C)dt \\
=x+2(\dfrac{t^2}{2} +Ct)\vert_0^1 \\
=x+1+2C \\
\Rightarrow C=-1,f(x)=x-1
\end{gathered}
$$

</div>