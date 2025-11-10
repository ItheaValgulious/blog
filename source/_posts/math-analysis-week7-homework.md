---
title: Math Analysis Homework - Week 7
tags: [math-analysis,math,homework]
---

# Math Analysis Homework - Week 7

## Class 1

### T1

<div class='cbox'>

$$
\begin{gathered}
f(x)=\dfrac{1+x+x^2}{1-x+x^2} 
\end{gathered}
$$

的四阶配亚诺余项麦克劳林级数是?

</div>

<div class='pbox'>

$$
\begin{gathered}
f(x)=1+\dfrac{2x}{x^2-x+1} \\
\end{gathered}
$$

考虑

$$
\begin{gathered}
\dfrac{1}{1-(x-x^2)} \\
=1+(x-x^2)+(x-x^2)^2+(x-x^2)^3+o((x-x^2)^3) \\
=1+x-x^2+x^2-2x^3+x^3+o(x^3) \\
=1+x-x^3+o(x^3) \\
f(x)=1+2x+2 x^2-2x^4+o(x^4)
\end{gathered}
$$

</div>



### T2

<div class='cbox'>

Solve $a,b$ such that

$$
\begin{gathered}
\lim_{x \to 0} \dfrac{(a+b\cos x)\sin x-x}{x^5}=C\ne 0
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
(a+b\cos x)\sin x-x \\
=(a+b-\dfrac{bx^2}{2}+\dfrac{bx^4}{24}+o(x^5))(x-\dfrac{x^3}{6} +\dfrac{x^5}{120} )-x
\end{gathered}
$$

要求其$0$到$4$阶项系数为零,$5$阶非零,即

$$
\begin{gathered}
\begin{cases}
a+b=1 \\
-\dfrac{a+b}{6} -\dfrac{b}{2} =0 \\
\dfrac{b}{24} +\dfrac{a+b}{120}+\dfrac{b}{12}  \ne 0
\end{cases}
\end{gathered}
$$

得

$$
\begin{gathered}
\begin{cases}
a=\dfrac{4}{3}  \\
b=-\dfrac{1}{3} 
\end{cases}
\end{gathered}
$$

</div>

啥叫x的五阶无穷小啊... 如果理解成$o(x^5)$也没解啊.


### T3

<div class='cbox'>

$$
\begin{gathered}
\lim_{x \to +\infty} (\sqrt[ 6 ]{ x^6+x^5 } -\sqrt[ 6 ]{ x^6-x^5 } )
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\text{let } t=\dfrac{1}{x}  \\
Ans=\lim_{t \to 0} \dfrac{\sqrt[6]{1+t}-\sqrt[ 6 ]{ 1-t } }{t}  \\
=\lim_{t \to 0} \dfrac{(1+t)^{-\frac56}}{6}+\dfrac{(1-t)^{-\frac56}}{6} \\
= \dfrac{1}{3} 
\end{gathered}
$$

</div>



### T4

<div class='cbox'>

$$
\begin{gathered}
\alpha>-1 \\
\lim_{n \to \infty} \prod _{i = 1} ^{n} (1+\dfrac{i}{n^{\alpha+2}} )^{n^\alpha} 
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=\exp \lim_{n \to \infty} n^\alpha \sum _{i = 1} ^{n}  \ln(1+\dfrac{i}{n^{\alpha+2}} ) \\
=\exp \lim_{n \to \infty} n^\alpha \sum _{i = 1} ^{n}  \dfrac{i}{n^{\alpha+2}}  \\
=\exp \lim_{n \to \infty} n^\alpha \dfrac{1}{2n^\alpha} \\
=\sqrt e
\end{gathered}
$$

</div>

## Class 2

### T1

<div class='cbox'>

$$
\begin{gathered}
x_1=\sin x_0>0,x_{n+1}=\sin x_n \\
 \Rightarrow \lim_{n \to \infty} \sqrt{ \dfrac{n}{3}  } x_n=1
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\text{apparently } \lim_{n \to \infty} x_n=0 \\
\lim_{n \to \infty} \dfrac{1}{x_n^2n}  \\
=\lim_{n \to \infty} \dfrac{1}{\sin^2(x_n)} - \dfrac{1}{x_n^2} \\
=\lim_{n \to \infty} \dfrac{x_n^2-\sin^2(x_n)}{x_n^2\sin^2x_n} \\
=\lim_{n \to \infty} \dfrac{x_n^2-(x_n-\dfrac{x_n^3}{6} +O(x^5))^2}{x_n^2(x_n-\dfrac{x_n^3}{6} +O(x^5))^2}    \\
=\lim_{n \to \infty} \dfrac{\dfrac{x_n^4}{3} +o(x_n^4)}{x_n^4+o(x_n^4)} =\dfrac{1}{3}  \\
\Rightarrow \lim_{n \to \infty} \sqrt{ \dfrac{n}{3}  } x_n=1
\end{gathered}
$$

</div>



### T2

<div class='cbox'>

$$
\begin{gathered}
f\in D^2[a,b],f'_+(a)=f'_-(b)=0 \\
\Rightarrow \exists \xi \in (a,b) \ s.t.\ 
\vert f''(\xi) \vert \ge \dfrac{4}{(b-a)^2} \vert f(b)-f(a) \vert 
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
g(x)=\begin{cases}
f(x),x\in [a,b] \\
f(a)+\dfrac{f''_+(a)}{2}(x-a)^2,x\in (-\infty,a) \\
f(b)+\dfrac{f''_-(b)}{2}(x-b)^2,\in (b,+\infty)
\end{cases} \\
g(x)=g(x_0)+(x-x_0)g'(x_0)+\dfrac{(x-x_0)^2g''(\xi)}{2}  \\
x=\dfrac{a+b}{2},x_0=a,b \Rightarrow  \\
g(\dfrac{a+b}{2})=g(a)+\dfrac{(a-b)^2g''(\xi_1)}{8} \\
g(\dfrac{a+b}{2})=g(b)+\dfrac{(a-b)^2g''(\xi_2)}{8}  \\
\Rightarrow \vert \dfrac{g''(\xi_1)-g''(\xi_2)}{2} \vert =\dfrac{4}{(b-a)^2} \vert g(b)-g(a) \vert  \\
\max \vert g''(\xi_1) \vert ,\vert g''(\xi_2) \vert \ge \vert \dfrac{g''(\xi_1)-g''(\xi_2)}{2}  \vert  \\
\Rightarrow \max \vert g''(\xi_1) \vert ,\vert g''(\xi_2) \vert\ge \dfrac{4}{(b-a)^2} \vert g(b)-g(a) \vert \\
\Rightarrow \max \vert f''(\xi_1) \vert ,\vert f''(\xi_2) \vert\ge \dfrac{4}{(b-a)^2} \vert f(b)-f(a) \vert
\end{gathered}
$$

</div>



### T3

<div class='cbox'>

$$
\begin{gathered}
f\in C^2[a,b],f(a)=f(b)=0 \\
\Rightarrow \begin{cases}
\max_{x\in [a,b]}\vert f(x) \vert \le \dfrac{1}{8} (b-a)^2\max_{x\in [a,b]}\vert f''(x) \vert  \\
\max_{x\in [a,b]} \vert f'(x) \vert \le \dfrac{1}{2} (b-a)\max_{x\in [a,b]}\vert f''(x) \vert 
\end{cases}
\end{gathered}
$$

</div>

<div class='pbox'>

(1):

$$
\begin{gathered}
\text{let } x_0 \ s.t.\ 
\vert f(x_0)\vert =\max\vert  f(x)\vert \\
\text{if } x_0\in \{ a,b \}: \text{Obviously}  \\
f(x_0)\in (a,b),f'(x_0)=0 \\
f(x)=f(x_0)+\dfrac{f''(\xi)}{2} (x-x_0)^2 \\
\Rightarrow \begin{cases}
0=f(a)=f(x_0)+\dfrac{f''(\xi_1)}{2} (a-x_0)^2 \\
0=f(b)=f(x_0)+\dfrac{f''(\xi_2)}{2} (b-x_0)^2
\end{cases} \\
(b-x_0)+(x_0-a)=b-a \\
\Rightarrow \min (a-x_0)^2,(b-x_0)^2 \le (\dfrac{a-b}{2} )^2 \\
\Rightarrow \vert f(x)\vert \le \dfrac{1}{8} (b-a)^2(\max \vert f''(\xi_1)\vert ,\vert f''(\xi_2)\vert) \\
\le \dfrac{1}{8} (b-a)^2\max_{x\in [a,b]}\vert f''(x) \vert
\end{gathered}
$$

(2):

$$
\begin{gathered}
\text{let } M=\max \vert f''(x) \vert  \\
\begin{cases}
0=f(a)=f(x)+f'(x)(a-x)+\dfrac{f''(\xi_1)}{2} (a-x)^2 \\
0=f(b)=f(x)+f'(x)(b-x)+\dfrac{f''(\xi_2)}{2} (b-x)^2 \\

\end{cases} \\
\Rightarrow
f'(x)(b-a)=\dfrac{f''(\xi_1)}{2} (a-x)^2-\dfrac{f''(\xi_2)}{2} (b-x)^2 \\
\vert f'(x) \vert \le \dfrac{1}{2(b-a)} \vert f''(\xi_1)(a-x)^2-f''(\xi_2)(b-x)^2 \vert  \\
\le \dfrac{1}{2(b-a)}M\vert (a-x)^2+(b-x)^2 \vert  \\
\le \dfrac{1}{2(b-a)}M(a-b)^2  \\ \\
=\dfrac{1}{2} (b-a)\max_{x\in [a,b]}\vert f''(x) \vert 
\end{gathered}
$$

</div>



### T4

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f(x),g(x)\in C^{+\infty}(-1,1) \\
\forall n\in{\mathbb N},\vert f^{(n)}(x)-g^{(n)}(x) \vert \le n! \vert x \vert 
\end{cases} \\
\Rightarrow f(x)=g(x),x\in (-1,1)
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
F(x)=f(x)-g(x) \\
\vert F^{(n)}(x) \vert \le n!\vert x \vert  \\ \\
n=0 \Rightarrow \vert F(x) \vert \le \vert x \vert,F(0)=0 \\
\vert F(x) \vert={\left \vert \sum _{i = 0} ^{n}  \dfrac{F^{(i)}(0)}{i!} x^i+\dfrac{F^{(n+1)}(\xi)}{(n+1)!} x^{n+1} \right \vert} \\
\le \vert \dfrac{F^{n+1}(\xi)}{(n+1)!}x^{n+1} \vert  \\
\le \vert x^{n+2} \vert \\

F(x)=\lim_{n \to \infty} \vert F(x) \vert \le \lim_{n \to \infty} \vert x^{n+2} \vert =0 \\

\end{gathered}
$$

</div>



### T5

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f(x)\in D^2[0,1] \\
f(0)=f(1)=0 \\
\min_{x\in [0,1]}f(x)=-1
\end{cases} \\
\Rightarrow \exists \xi,f''(\xi)\ge 8
\end{gathered}
$$

</div>

<div class='pbox'>


$$
\begin{gathered}
\text{let } x_0 \ s.t.\ 
\vert f(x_0)\vert =\max\vert  f(x)\vert \\
\text{if } x_0\in \{ 0,1 \}: \text{Obviously}  \\
f(x_0)\in (0,1),f'(x_0)=0 \\
f(x)=f(x_0)+\dfrac{f''(\xi)}{2} (x-x_0)^2 \\
\Rightarrow \begin{cases}
0=f(0)=f(x_0)+\dfrac{f''(\xi_1)}{2} x_0^2 \\
0=f(1)=f(x_0)+\dfrac{f''(\xi_2)}{2} (1-x_0)^2
\end{cases} \\
(-x_0)+(x_0-1)=0+1 \\
\Rightarrow \min x_0^2,(1-x_0)^2 \le (\dfrac{0+1}{2} )^2 \\
\Rightarrow \vert f(x)\vert \le \dfrac{1}{8} (\max \vert f''(\xi_1)\vert ,\vert f''(\xi_2)\vert) \\
\Rightarrow \text{let } f(x)=-1,\exists \xi,f''(\xi)\ge 8
\end{gathered}
$$


</div>



### T6

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f(x)\in D^n(x_0-\delta,x_0+\delta) \\
\forall i \in [2,n-1],f^{(i)}(x_0)=0 \\
f^{(n)}(x_0)\ne 0,f^{(n)}(x) \text{ is continuous at } x_0 \\
0<\vert h \vert <\delta \Rightarrow f(x_0+h)-f(x_0)=hf'(x_0+\theta h),\theta\in (0,1) \\

\end{cases} \\
\Rightarrow \lim_{h \to 0} \theta = (\dfrac{1}{n})^{\frac{1}{n-1} }
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
f(x_0+h)-f(x_0)=\dfrac{f^{(n)}(\xi_1)h^n}{n!}  \\
f'(x_0+\theta h)=f^{(n)}(\xi_2)\dfrac{(\theta h)^{n-1}}{(n-1)!}  \\
f(x_0+h)-f(x_0)=hf'(x_0+\theta h) \\
\Rightarrow f^{(n)}(\xi_2)\dfrac{\theta^{n-1}}{(n-1)!}=\dfrac{f^{(n)}(\xi_1)}{n!} \\
\Rightarrow \theta = (\dfrac{f^{(n)}(\xi_1)}{f^{(n)}(\xi_2)})^{\frac1{n-1}}(\dfrac{1}{n} )^{\frac1{n-1}} \\
\lim_{h \to 0} \theta = (\dfrac{1}{n}) ^{\frac1{n-1}}

\end{gathered}
$$

</div>

## Class 3

### T1

<div class='cbox'>

$$
\begin{gathered}
\int (\dfrac{2-x^3}{x^2} )^2dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=\int \dfrac{4}{x^4} dx+\int \dfrac{x^6}{x^4} dx-\int \dfrac{4x^3}{x^4}dx \\
=-\dfrac{4}{3x^3} +\dfrac{x^3}{3} -4\ln x+C
\end{gathered}
$$

</div>

### T2

<div class='cbox'>

$$
\begin{gathered}
\int \dfrac{\cos 2x}{\sin x-\cos x} dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=\int \dfrac{\cos^2 x-\sin ^2 x}{\sin x-\cos x} dx \\
=\int (-\cos x-\sin x)dx \\
=\cos x-\sin x+C
\end{gathered}
$$

</div>

### T3

<div class='cbox'>

$$
\begin{gathered}
\int \tan^2 xdx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=\int (\sec^2x-1)dx \\
=\tan x-x+C
\end{gathered}
$$

</div>

### T4

<div class='cbox'>

$$
\begin{gathered}
\int (2^x+3^x)^2dx \\
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=\int (4^x+2\times 6^x+9^x)dx \\
=\dfrac{2^{2x-1}}{\ln 2}+\dfrac{2\times 6^x}{\ln 6} +\dfrac{9^x}{2\ln 3} +C
\end{gathered}
$$

</div>

### T5

<div class='cbox'>

$$
\begin{gathered}
\int \dfrac{1}{x^4(1+x^2)} dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=\int \dfrac{-x^2+1}{x^4} dx+\int \dfrac{1}{1+x^2} dx \\
=\int -\dfrac{1}{x^2} dx+\int \dfrac{1}{x^4} dx+\int \dfrac{1}{1+x^2} dx \\
=\dfrac{1}{x} -\dfrac{1}{3x^3} +\arctan(x)+C
\end{gathered}
$$

</div>

### T6

<div class='cbox'>

$$
\begin{gathered}
\int x\cos xdx \\
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=\int xd\sin x \\
=x\sin x-\int \sin xdx \\
=x\sin x+\cos x+C
\end{gathered}
$$

</div>



### T7

<div class='cbox'>

$$
\begin{gathered}
\int e^x\cos xdx \\
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\int e^x\cos xdx
=\int e^xd\sin x \\
=e^x\sin x-\int e^x\sin x \\
=e^x\sin x+e^x\cos x-\int e^x\cos x \\
\Rightarrow \int e^x\cos xdx=\dfrac{e^x(\sin x+\cos x)}{2} +C
\end{gathered}
$$

</div>

### T8

<div class='cbox'>

$$
\begin{gathered}
\int x^n\ln xdx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\int x^n\ln xdx \\
=\dfrac{x^{n+1}}{n+1} \ln x-\int \dfrac{x^n}{n+1} dx \\
=\dfrac{x^{n+1}}{n+1} \ln x-\dfrac{x^{n+1}}{(n+1)^2} 
\end{gathered}
$$

</div>

### T9

<div class='cbox'>

$$
\begin{gathered}
\int x\arctan xdx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=\dfrac{1}{2} \int \arctan x dx^2 \\
=\dfrac{1}{2} x^2\arctan x-\dfrac{1}{2} \int (1-\dfrac{1}{1+x^2}) dx \\
=\dfrac{1}{2} x^2\arctan x-\dfrac{1}{2} x+\dfrac{1}{2} \arctan x+C
\end{gathered}
$$

</div>

### T10

<div class='cbox'>

$$
\begin{gathered}
\int \dfrac{e^{\arctan x}}{(1+x^2)^\frac32} dx \\ 
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\text{let }x=\tan t \\
ans=\int e^t \cos tdt \\
=\dfrac{e^t}{2} (\sin t+\cos t)+C \\
=\dfrac{e^{\arctan x}}{2} (\dfrac{1+x}{\sqrt {1+x^2}} )+C

\end{gathered}
$$

</div>

### T11

<div class='cbox'>

$$
\begin{gathered}
\int \dfrac{\arctan x}{x^2} dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=-\dfrac{\arctan x}{x} +\int \dfrac{1}{x(1+x^2)} dx \\
=-\dfrac{\arctan x}{x} +\int \dfrac{dx^2}{2x^2(1+x^2)} \\
=-\dfrac{\arctan x}{x}+\dfrac{1}{2} \ln\dfrac{x^2}{1+x^2} +C
\end{gathered}
$$

</div>

### T12

<div class='cbox'>

$$
\begin{gathered}
\int \cos \ln xdx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\xlongequal{t=\ln x}\int e^t\cos tdt \\
=\dfrac{e^t}{2} (\sin t+\cos t)+C \\
=\dfrac{x}{2} (\sin \ln x+\cos \ln x)+C
\end{gathered}
$$

</div>

### T13

<div class='bbox'>

$$
\begin{gathered}
\int e^{5x}dx \\
=\dfrac{e^{5x}}{5} +C
\end{gathered}
$$

</div>

### T14

<div class='cbox'>

$$
\begin{gathered}
\int \dfrac{dx}{\cos^2 7x} 
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=\int \sec^2(7x)dx \\
=\dfrac{\tan(7x)}{7} +C
\end{gathered}
$$

</div>

### T15

<div class='cbox'>

$$
\begin{gathered}
\int \cos^3 x\sin xdx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=\int \dfrac{1+\cos 2x}{2} \dfrac{\sin 2x}{2} dx \\
=-\int \dfrac{1+\cos 2x}{8} d(\cos 2x) \\
=-\dfrac{\cos 2x}{8} -\dfrac{\cos^2 2x}{16} 
\end{gathered}
$$

</div>

### T16

<div class='cbox'>

$$
\begin{gathered}
\int \dfrac{\sqrt{ \tan x+1 } }{\cos^2 x} dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=\int \sqrt{ \tan x+1 } d\tan x \\
=\dfrac{2}{3} (1+\tan x)^{\frac32}+C
\end{gathered}
$$

</div>



### T17

<div class='cbox'>

$$
\begin{gathered}
\int \tan^4 xdx \\
=\int \tan^2 x(\sec^2 x-1)dx \\
=\int \tan^2 d\tan x-\int (\sec^2 x-1)dx \\
=\dfrac{\tan^3 x}{3} -\tan x+x+C
\end{gathered}
$$

</div>

### T18

<div class='cbox'>

$$
\begin{gathered}
\int \dfrac{\sin \sqrt x}{\sqrt x} dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=\int 2\sin \sqrt xd\sqrt x \\
=-2\cos \sqrt x+C
\end{gathered}
$$

</div>



### T19

<div class='cbox'>

$$
\begin{gathered}
\int \dfrac{1+\sqrt{ 1-x^2 } }{1-\sqrt{ 1-x^2 } } dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=\int \dfrac{(1+\sqrt{1-x^2})^2}{x^2} dx \\
=-\dfrac{2}{x} -x+\int \dfrac{2\sqrt{1-x^2}}{x^2} dx \\
\text{let } x=\cos t \\
=-\dfrac{2}{x} -x-\int \dfrac{2\sin^2 t}{\cos^2 t}dt  \\
=-\dfrac{2}{x} -x-\int 2\sec^2 tdt+\int 2dt \\
=-\dfrac{2}{x} -x-2\tan t+2t+C \\
=-\dfrac{2}{x} -x-\dfrac{2\sqrt{1-x^2}}{x} +2\arccos x
\end{gathered}
$$

</div>



### T20

<div class='cbox'>

$$
\begin{gathered}
\int \dfrac{\sin x+\cos x}{\sqrt[ 3 ]{ \sin x-\cos x } } dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=\int (\sin x-\cos x)^{-\frac13}d(\sin x-\cos x)   \\
=\dfrac{3}{2} (\sin x-\cos x)^{\frac23}
\end{gathered}
$$

</div>



### T21

<div class='cbox'>

$$
\begin{gathered}
\int \sqrt{ \dfrac{\ln (x+\sqrt{ 1+x^2 } )}{1+x^2}  } dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=\int \sqrt{ \ln(x+\sqrt{1+x^2}) } d(\ln(x+\sqrt{1+x^2}))  \\
=\dfrac{2}{3}\ln(x+\sqrt{1+x^2})^{\frac32}
\end{gathered}
$$

</div>



### T22

<div class='cbox'>

Calculate the recurrence relation of

$$
\begin{gathered}
I_n=\int \dfrac{x^n}{\sqrt{ 1-x^2 } } dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
x=\sin t \\
I_n=\int \sin^n tdt \\
I_n=-\sin^{n-1}t\cos t+\int (n-1)\sin^{n-2}t\cos^2 t \\
=-\sin^{n-1}t\cos t+\int(n-1)\sin^{n-2}t(1-\sin^2 t)dt \\
=-\sin^{n-1}t\cos t+(n-1)I_{n-2}-(n-1)I_n \\
\Rightarrow I_n=-\dfrac{1}{n} \sin^{n-1}t\cos t+\dfrac{n-1}{n} I_{n-2}
\end{gathered}
$$

</div>

