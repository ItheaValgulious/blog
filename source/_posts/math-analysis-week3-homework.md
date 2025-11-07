---
title: Math Analysis Homework - Week 3
tags:
  - math-analysis
  - homework
  - math
date: 2025-10-11 15:58:54
---


# Math Analysis Homework - Week 3

## Class 1

### T1

<div class='cbox'>

$$
\begin{gathered}
\text{Calculate left/right limits of }f(x)=\dfrac{2^{\frac{1}{x} }-1}{2^{\frac{1}{x} } +1}  (x_0=0)
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
x\to 0^+,\dfrac{1}{x} \to +\infty,\lim_{x \to 0^+} = f(x)=\dfrac{1-2^{-\frac{1}{x}}}{1+2^{-\frac1x}}=1 \\
x\to 0^-,\dfrac{1}{x} \to -\infty,2^{\frac{1}x}\to 0,\lim_{x \to 0^-} f(x)=-1 
\end{gathered}
$$

</div>

### T2

<div class='cbox'>

$$
\begin{gathered}
\lim_{x \to 0} \dfrac{\sqrt{ 1+x } -\sqrt{ 1-x } }{x}  
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\sqrt{1+x}-1\sim\dfrac{x}{2} \\
\lim_{x \to 0} \dfrac{\sqrt{ 1+x } -\sqrt{ 1-x } }{x} \\
=\lim_{x \to 0}\dfrac{(\sqrt{ 1+x }-1) -(\sqrt{ 1-x }-1) }{x} \\
=\lim_{x \to 0}\dfrac{\frac{x}{2}+\frac{x}{2}}{x}  \\
=1
\end{gathered}
$$

</div>


### T3

<div class='cbox'>

$$
\begin{gathered}
\lim_{x \to 1} \dfrac{\sum _{i = 1} ^{m}  x^i -m}{x-1} 
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\text{let } f_m(x)=\dfrac{\sum _{i = 1} ^{m}  x^i-m}{x-1}  \\
\lim_{x \to 1} f_1(x)=1 \\
f_n(x)-f_{n-1}(x)=\dfrac{x^m-1}{x-1}=\sum _{i = 0} ^{m-1}  x^i \\
\therefore \lim_{x \to 1} f_n(x)=\lim_{x \to 1} f_1(x)+\sum _{i = 2} ^{n}  f(i)-f(i-1) \\
=1+\sum _{i = 2} ^{n}  i \\
=\dfrac{n(n+1)}{2}   
\end{gathered}
$$

</div>

### T4

<div class='cbox'>

$$
\begin{gathered}
\lim_{n \to \infty} \prod_{i=1}^n \cos\dfrac{x}{2^i} 
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\prod _{i = 1} ^{n}  \cos\dfrac{x}{2^i}  \\
=\dfrac{\sin\dfrac{x}{2^n}\prod _{i = 1} ^{n}  \cos\dfrac{x}{2^i}}{\sin\dfrac{x}{2^n} } \\
=\dfrac{sin(x)}{2^n\sin\dfrac{x}{2^n} } \\
\sin\dfrac{x}{2^n} \sim\dfrac{x}{2^n}  \\
\Rightarrow \lim_{n \to \infty} \dfrac{sin(x)}{2^n\sin\dfrac{x}{2^n} } \\
=\dfrac{\sin(x)}{x} 
\end{gathered}
$$

</div>


### T5

<div class='cbox'>

$$
\begin{gathered}
\lim_{x \to \infty} (\sin\dfrac{1}{x} +\cos\dfrac{1}{x} )^x 
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\lim_{x \to \infty} (\sin\dfrac{1}{x} +\cos\dfrac{1}{x} )^x  \\
=\lim_{x \to \infty} e^{x\ln(\sin\frac{1}{x}+\cos\frac1x)} \\
=e^{\lim_{x \to \infty} x\ln(\sin\frac{1}{x}+\cos\frac1x)} \\
=e^{\lim_{x \to \infty} x(\sin\frac{1}{x}+(\cos\frac1x-1))} \\
=e^{\lim_{x \to \infty} x(\frac{1}{x}+(1-\frac{1}{2x^2} -1))} \\
=e
\end{gathered}
$$

</div>


### T6

<div class='cbox'>

$$
\begin{gathered}
\lim_{x \to 0} x \lbrack \dfrac{1}{x}  \rbrack 
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\begin{cases}
x\lbrack \dfrac{1}{x}  \rbrack \in (1-x,1] \\
\lim_{x \to 0} 1-x=\lim_{x \to 1} 1=1
\end{cases} \\
\stackrel{\text{Squeeze Theorem}}{\Longrightarrow}
\lim_{x \to 0} x \lbrack \dfrac{1}{x}  \rbrack =1 
\end{gathered}
$$

</div>


### T7

<div class='cbox'>

$$
\begin{gathered}
\lim_{x \to \infty} (\dfrac{1+x}{3+x}  )^x
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
(\dfrac{1+x}{3+x}  )^x
=(1-\dfrac{2}{x+3} )^x \\
\text{let } t=-\dfrac{x+3}{2},x=-2t-3  \\
(1+\dfrac{2}{x+3} )^x=(1+\dfrac{1}{t} )^{-2t-3} \\
\therefore \lim_{x \to \infty} (1+\dfrac{2}{x+3} )^x \\
=\lim_{t \to \infty} (1+\dfrac{1}{t} )^{-2t} \\
=e^{-2}
\end{gathered}
$$

</div>


### T8

<div class='cbox'>

$$
\begin{gathered}
\lim_{x \to 0} (\dfrac{a^x+b^x+c^x}{3} )^\frac{1}{x}
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\lim_{x \to 0} (\dfrac{a^x+b^x+c^x}{3} )^\frac{1}{x} \\
=\exp \lim_{x \to 0} \dfrac{\ln(\dfrac{a^x+b^x+c^x}{3} )}{x}  \\
=\exp \lim_{x\to 0}\dfrac{(\dfrac{a^x+b^x+c^x}{3} )-1}{x} \\
a^x=e^{x\ln(a)}=1+x\ln(a)+o(x) \\
\therefore
=\exp \lim_{x \to 0} \dfrac{x\ln a+x\ln b+x\ln c}{x} \\
=\exp \dfrac{\ln(abc)}{3} \\
=\sqrt[ 3 ]{ abc }  

\end{gathered}
$$

</div>


### T9

<div class='cbox'>

$$
\begin{gathered}
\lim_{x \to 0} \dfrac{x\tan^4x}{\sin^3x(1-\cos x)} 
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\lim_{x \to 0} \dfrac{x\tan^4x}{\sin^3x(1-\cos x)}  \\
=\lim_{x \to 0} \dfrac{x\sin x}{\cos^3x(1-\cos x)}  \\
=\lim_{x \to 0} \dfrac{x^2}{\cos^3x\dfrac{x^2}{2} }  \\
=2
\end{gathered}
$$

</div>

### T10


<div class='cbox'>

$$
\begin{gathered}
\lim_{x \to 0} \dfrac{\sqrt{ 1+x^4 } -1}{1-\cos^2x} 
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\lim_{x \to 0} \dfrac{\sqrt{ 1+x^4 } -1}{1-\cos^2x}  \\
=\lim_{x \to 0} \dfrac{x^4}{2x^2} \\
=\lim_{x \to 0} \dfrac{x^2}{2}  \\
=0 
\end{gathered}
$$

</div>


### T11

<div class='cbox'>

solve a,b:

$$
\begin{gathered}
\lim_{x \to +\infty} (\sqrt{ x^2-x+1 } -ax-b)=0
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\sqrt{ x^2-x+1 }=\sqrt{(x-\dfrac{1}{2} )^2+\dfrac{3}{4} } \\
\text{let } t=x-\dfrac{1}{2}  \\
\lim_{x \to \infty} \sqrt{ x^2-x+1 } -(x-\dfrac{1}{2} ) \\
=\lim_{x \to \infty} \sqrt{ t^2+\dfrac{3}{4}  }-\sqrt{ t^2 }  \\
=\lim_{x \to \infty} \dfrac{3}{4(\sqrt{t^2+\frac{3}{4}}+\sqrt{t^2})}   \\
=0
\end{gathered}
$$

</div>

### T12

<div class='cbox'>

$$
\begin{gathered}
f(x_0^-)<f(x_0^+) \Rightarrow \exists \delta>0,\forall x\in (x_0-\delta,x_0),\forall y\in (x_0,x_0+\delta),f(x)<f(y)
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\lim_{x \to x_0^-} f(x)<\lim_{x \to x_0^+} f(x) \\
\text{let } \epsilon=\dfrac{f(x_0^+)-f(x_0^-)}{3} ,\exists \delta=\min(\delta_1,\delta_2) \\ s.t.\\ 
\forall x\in (x_0-\delta,x_0), \vert f(x)-f(x_0^-) \vert <\epsilon, \\
\forall y\in (x_0,x_0+\delta), \vert f(y)-f(x_0^+) \vert <\epsilon \\
\therefore f(x)<f(x_0^-)+\epsilon<f(x_0^+)-\epsilon<f(y)
\end{gathered}
$$

</div>

### T13

<div class='cbox'>

$$
\begin{gathered}
f \text{ is periodic function} ,\lim_{x \to \infty} f(x)=0 \\
\Rightarrow f(x)=0
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\text{let } T \text{ is a period of } f \\
\forall x_0,\epsilon,
\exists X>x_0 \ s.t.\ 
x>X \Rightarrow f(x)<\epsilon \\
\text{let } n=\lbrack \dfrac{X-x_0}{T} +100 \rbrack  \\
\Rightarrow  f(x_0)=f(x_0+nT)<\epsilon \\
\Rightarrow \lim_{x \to x_0} f(x)=0 \\
\Rightarrow f(x)=0
\end{gathered}
$$

</div>

### T14

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
f(x),x\in(0,1) \\
x\to 0^+ \Rightarrow f(x)=o(1) \\
f(x)-f(\dfrac{x}{2} )=o(x)
\end{cases}
\Rightarrow x\to 0^+ ,f(x)=o(x)
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\forall \epsilon, \\
\text{let }\epsilon_1=\dfrac{\epsilon}{8}\\
\exists \delta \ s.t.\ 
x<\delta \Rightarrow 
\vert f(x)-f(\dfrac{x}{2} )\vert <\epsilon_1x \\
\therefore
\vert f(x)\vert = \vert f(\dfrac{x}{2^n} )+\sum _{i = 0} ^{n-1} ( f(\dfrac{x}{2^i} )-f(\dfrac{x}{2^{i+1}} ) )\vert   \\
\le \vert f(\dfrac{x}{2^n} )\vert  + \sum _{i = 0} ^{n-1} \vert  f(\dfrac{x}{2^i} )-f(\dfrac{x}{2^{i+1}} ) \vert  \\
<\vert f(\dfrac{x}{2^n} )\vert  + \sum _{i = 0} ^{n-1}  \dfrac{\epsilon_1x}{2^i}  \\
<\vert f(\dfrac{x}{2^n} )\vert  + 2\epsilon_1x \\
\therefore \vert f(x)\vert =\lim_{n \to \infty} \vert f(x)\vert  \\
\le \lim_{n \to \infty} (\vert f(\dfrac{x}{2^n} )\vert +2\epsilon_1x) \\
= 0 + 2\epsilon_1x \\
= 2\epsilon_1x \\
< \epsilon x \\ 
\Rightarrow x\to 0^+ \Rightarrow  f(x)=o(x) 
\end{gathered}
$$

</div>

### T15

<div class='cbox'>

$$
\begin{gathered}
\begin{cases}
a,b>1,f(x) \text{ is bounded in } N^*(0) \\
f(ax)=bf(x)
\end{cases} \\
\Rightarrow \lim_{x \to 0} f(x)=f(0)
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
f(ax)=bf(x) \\
\Leftrightarrow f(\dfrac{x}{a} )=\dfrac{f(x)}{b} \\
a,b>1,f(x) \text{ is bounded in } N^*(0)  \\
\Rightarrow \exists M,\delta_0,\vert x \vert <\delta_0 \Rightarrow  \vert f(x) \vert <M \\
\forall \epsilon,\text{let }\delta=\dfrac{\delta_0}{a^n},n=\log_b(\frac{M}{\epsilon})+1 \\
\Rightarrow x<\delta \Rightarrow f(x)=\dfrac{f(a^nx)}{b^n},\vert a^nx \vert < \delta_0 \\
\Rightarrow f(a^nx)< M \\
\Rightarrow f(x)<\dfrac{M}{b^n} <\epsilon \\
\Rightarrow \lim_{x \to _0}  f(x)=0 \\
f(a0)=bf(0) \Rightarrow f(0)=0 \\
\therefore \lim_{x \to 0} f(x)=0
\end{gathered}
$$

</div>

## Class 2

### T1

<div class='cbox'>

solve a,b such that

$$
\begin{gathered}
f(x)=\lim_{n \to \infty} \dfrac{x^{2n-1}+ax^2+bx}{x^{2n}+1} \text{ is continuous} 
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
x>1 \Rightarrow f(x)=\dfrac{1}{x}   \\
\Rightarrow \lim_{x \to 1^+} f(x)=1 \\
x\in (-1,1) \Rightarrow f(x)=ax^2+bx  \\
\Rightarrow \lim_{x \to 1^-} f(x)=ax^2+bx \\
\therefore f(1)=\dfrac{1+a+b}{2} =1=a+b \\
x<-1 \Rightarrow f(x)=\dfrac{1}{x}  \\
\Rightarrow \lim_{x \to -1^-} f(x)=-1 \\
\lim_{x \to -1^-} f(x)=\lim_{x \to -1^+} f(x)=f(-1) \\
\Rightarrow -1=a-b=\dfrac{-1+a-b}{2}  \\
\therefore
\begin{cases}
a=0 \\
b=1
\end{cases}

\end{gathered}
$$

</div>

### T2

<div class='cbox'>

$$
\begin{gathered}
f(x)=\begin{cases}
x^a\sin\dfrac{1}{x} ,x>0 \\
e^x+b,x\le 0
\end{cases}
\end{gathered}
$$

survey continuouity of $f(0)$

</div>

<div class='pbox'>

$$
\begin{gathered}
f(0)=b+1 \\
\lim_{x \to 0^-} f(x)=b+1 \\
\text{if } a> 0,\lim_{x \to 0^+} f(x)=x^a\sin\dfrac{1}{x} \in(-x^a,x^a) \\
\lim_{x \to 0^+} f(x)=0 \\
\text{if } a\le 0,\lim_{x \to 0^+} f(x)=\lim_{x \to 0^+} x^a\sin\dfrac{1}{x} \text{ not exists} 
\\
\therefore a>0,b=-1: f(x) \text{ is continuous at } x=0 \\
\text{else } f(x) \text{ is discontinuous at } x=0
\end{gathered}
$$

</div>

### T3

<div class='cbox'>

$$
\begin{gathered}
\lim_{x \to 0} \dfrac{(1+x)(1+2x)(1+3x)-1}{x} 
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
(1+x)(1+2x)(1+3x)-1=6x+o(x) \\
\Rightarrow \lim_{x \to 0} \dfrac{(1+x)(1+2x)(1+3x)-1}{x}  \\
=\lim_{x \to 0} \dfrac{6x+o(x)}{x}  \\
=6
\end{gathered}
$$

</div>

### T4

<div class='cbox'>

$$
\begin{gathered}
\lim_{x \to 1} \dfrac{\sqrt[ m ]{ x } -1}{\sqrt[ n ]{ x } -1} ,m,n\in N^*
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\sqrt[n]{ 1+(x-1) } -1 \\
=\dfrac{x-1}{n} +o(x-1) \\
\Rightarrow \lim_{x \to 1} \dfrac{\sqrt[ m ]{ x } -1}{\sqrt[ n ]{ x } -1} =\dfrac{\frac{x-1}{m}+o(x-1)}{\frac{x-1}{n}+o(x-1)} =\dfrac{n}{m} 
\end{gathered}
$$

</div>



### T5

<div class='cbox'>

$$
\begin{gathered}
\lim_{x \to 1} \dfrac{(1-\sqrt x)(1-\sqrt[ 3 ]{ x } )\ldots (1-\sqrt[n]{ x } )}{(1-x)^{n-1}},n\in N_{+} 
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
1-\sqrt[k]{ x }=1-\sqrt[k]{ 1+(x-1) }=-\dfrac{x-1}{k}+o(x-1)  
\end{gathered}
$$

$$
\begin{gathered}
\lim_{x \to 1} \dfrac{\prod _{i = 2} ^{n} (1-\sqrt[ i ]{ x } ) }{(1-x)^{n-1}} \\
=\lim_{x \to 1} \dfrac{\prod _{i = 2} ^{n} \dfrac{1-x}{i}  }{(1-x)^{n-1}} \\
=\dfrac{1}{n!} 
\end{gathered}
$$

</div>

### T6

<div class='cbox'>

$$
\begin{gathered}
\lim_{x \to \frac{\pi}{4} } (\tan x)^{\tan 2x}
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\lim_{x \to \frac{\pi}{4} } (\tan x)^{\tan 2x}= \\
\lim_{x \to \frac{\pi}{4} } \exp (\tan 2x\ln (\tan x)) \\
=\lim_{x \to \frac{\pi}{4} } \exp (2\dfrac{\tan x}{1-\tan^2 x} (\tan x-1)) \\
=\lim_{x \to \frac{\pi}{4} } \exp -\dfrac{2\tan x}{1+\tan x}  \\
=\dfrac{1}{e} 
\end{gathered}
$$

</div>



### T7

<div class='cbox'>

$$
\begin{gathered}
\lim_{x \to 0} (2e^{\frac{x}{1+x}}-1)^{\frac{1+x^2}x}
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\lim_{x \to 0} (2e^{\frac{x}{1+x}}-1)^{\frac{1+x^2}x} \\
=\lim_{x \to 0} \exp \dfrac{1+x^2}{x} \ln(2e^{\frac{x}{1+x}}-1) \\
=\lim_{x \to 0} \exp 2\dfrac{1+x^2}{x} (e^{\frac{x}{1+x}}-1) \\
=\lim_{x \to 0} \exp 2\dfrac{1+x^2}{x} \dfrac{x}{1+x} \\
=e^2
\end{gathered}
$$

</div>



### T8

<div class='cbox'>

$$
\begin{gathered}
\vert x \vert <1,\lim_{n \to \infty} {\left( 1+\dfrac{\sum _{i = 1} ^{n}  x^i}{n}  \right)} ^n
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\sum _{i = 1} ^{n}  x^i=\dfrac{x^{n+1}-x}{x-1}  \\
\lim_{n \to \infty} {\left( 1+\dfrac{\sum _{i = 1} ^{n}  x^i}{n}  \right)} ^n \\
= \lim_{n \to \infty} {\left( 1+\dfrac{x^{n+1}-x}{n(x-1)}  \right)} ^n \\
=\lim_{n\to \infty} \exp n\ln {\left( 1+\dfrac{x^{n+1}-x}{n(x-1)}  \right)} \\
=\exp \lim_{n \to \infty} n \dfrac{x^{n+1}-x}{n(x-1)}  \\
=\exp \dfrac{-x}{x-1}  \\
=e^{\frac{x}{1-x} }
\end{gathered}
$$

</div>



### T9

<div class='cbox'>

$$
\begin{gathered}
f\in C(0,+\infty),f(x^2)=f(x) \Rightarrow \exists c,f(x)=c
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\forall x_0,\text{let } a_n=x_0^{\frac{1}{2^{n-1}}} \\
f(a_n)=f(\sqrt{a_{n-1}})=f(a_{n-1}),f(a_1)=f(x_0) \\
\Rightarrow f(a_n)=f(x_0) \\
\lim_{n \to \infty} a_n=1 \\
\Rightarrow 
f(1)=\lim_{x \to 1} f(x)=\lim_{n \to \infty} f(a_n) \\
=\lim_{n \to \infty} f(x_0)=f(x_0) \\
\Rightarrow \forall x_0,f(x_0)=f(1) \\
\Rightarrow f \text{ is constant function} 
\end{gathered}
$$

</div>



### T10

<div class='cbox'>

$$
\begin{gathered}
f(x+y)=f(x)+f(y),f(x) \text{ is continuous at } x=0 \\
\Rightarrow f\in C(R)
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
f(0+0)=f(0)+f(0)\Rightarrow f(0)=0 \\
f(x) \text{ is continuous at } x=0 \\
\Rightarrow \forall \epsilon_0,\exists \delta_0,\vert x \vert<\delta_0 \Rightarrow \vert f(x)-f(0) \vert <\epsilon_0 \\
\therefore \forall x_0, \\
\forall \epsilon,\text{let } \epsilon_0=\dfrac{\epsilon}{2} \Rightarrow \delta:=\delta_0 \\
\vert x-x_0 \vert <\delta \Rightarrow \\ 
\vert f(x)-f(x_0) \vert =\vert f(x_0+(x-x_0))-f(x_0) \vert \\
=\vert f(x_0)+f(x-x_0)-f(x_0) \vert  \\
=\vert f(x-x_0) \vert <\epsilon_0<\epsilon \\
\therefore \forall x_0, \lim_{x \to x_0} f(x)=f(x_0) \\
\Rightarrow f\in C(R)

\end{gathered}
$$

</div>



### T11

<div class='cbox'>

$$
\begin{gathered}
f:[0,+\infty) \Rightarrow R,f(2x)=f(x)\cos(x),f(x) \text{ is continuous at } x=0 \\
\Rightarrow f(x)=f(0)\dfrac{\sin(x)}{x} ,x\in [0,+\infty)
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\forall x_0, \\
\text{let } a_n=\dfrac{x_0}{2^{n-1}},x_0=a_1 \\
f(a_n)=f(a_{n+1})\cos(a_{n+1}) \\
\Rightarrow f(x_0)=f(a_1)=f(a_n)\prod _{i = 2} ^{n} \cos(a_i) \\
=f(a_n)\prod_{i=1}^{n-1}\cos \dfrac{x_0}{2^i}  \\
=f(a_n)\dfrac{\sin(x_0)}{2^{n-1}\sin\frac{x_0}{2^{n-1}}}  \\
\stackrel{\lim_{n \to \infty} }{\Longrightarrow}
f(x_0)=(\lim_{n \to \infty} f(a_n))\dfrac{\sin(x_0)}{\lim_{n \to \infty} 2^{n-1}\sin\frac{x_0}{2^{n-1}}}  \\
=f(0)\dfrac{\sin(x_0)}{x_0} \\
\therefore f(x)=f(0)\dfrac{\sin(x)}{x}  
\end{gathered}
$$

</div>
