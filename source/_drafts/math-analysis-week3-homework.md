---
title: Math Analysis Homework - Week 3
tags: [math-analysis,homework]
---

# Math Analysis Homework - Week 3

## Class 1

### T1

<div class='cbox'>

$$
\begin{array}{l}
\text{Calculate left/right limits of }f(x)=\dfrac{2^{\frac{1}{x} }-1}{2^{\frac{1}{x} } +1}  (x_0=0)
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
x\to 0^+,\dfrac{1}{x} \to +\infty,\lim_{x \to 0^+} = f(x)=\dfrac{1-2^{-\frac{1}{x}}}{1+2^{-\frac1x}}=1 \\
x\to 0^-,\dfrac{1}{x} \to -\infty,2^{\frac{1}x}\to 0,\lim_{x \to 0^-} f(x)=-1 
\end{array}
$$

</div>

### T2

<div class='cbox'>

$$
\begin{array}{l}
\lim_{x \to 0} \dfrac{\sqrt{ 1+x } -\sqrt{ 1-x } }{x}  
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\sqrt{1+x}-1\sim\dfrac{x}{2} \\
\lim_{x \to 0} \dfrac{\sqrt{ 1+x } -\sqrt{ 1-x } }{x} \\
=\lim_{x \to 0}\dfrac{(\sqrt{ 1+x }-1) -(\sqrt{ 1-x }-1) }{x} \\
=\lim_{x \to 0}\dfrac{\frac{x}{2}+\frac{x}{2}}{x}  \\
=1
\end{array}
$$

</div>


### T3

<div class='cbox'>

$$
\begin{array}{l}
\lim_{x \to 1} \dfrac{\sum _{i = 1} ^{m}  x^i -m}{x-1} 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\text{let } f_m(x)=\dfrac{\sum _{i = 1} ^{m}  x^i-m}{x-1}  \\
\lim_{x \to 1} f_1(x)=1 \\
f_n(x)-f_{n-1}(x)=\dfrac{x^m-1}{x-1}=\sum _{i = 0} ^{m-1}  x^i \\
\therefore \lim_{x \to 1} f_n(x)=\lim_{x \to 1} f_1(x)+\sum _{i = 2} ^{n}  f(i)-f(i-1) \\
=1+\sum _{i = 2} ^{n}  i \\
=\dfrac{n(n+1)}{2}   
\end{array}
$$

</div>

### T4

<div class='cbox'>

$$
\begin{array}{l}
\lim_{n \to \infty} \prod_{i=1}^n \cos\dfrac{x}{2^i} 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\prod _{i = 1} ^{n}  \cos\dfrac{x}{2^i}  \\
=\dfrac{\sin\dfrac{x}{2^n}\prod _{i = 1} ^{n}  \cos\dfrac{x}{2^i}}{\sin\dfrac{x}{2^n} } \\
=\dfrac{sin(x)}{2^n\sin\dfrac{x}{2^n} } \\
\sin\dfrac{x}{2^n} \sim\dfrac{x}{2^n}  \\
\Rightarrow \lim_{n \to \infty} \dfrac{sin(x)}{2^n\sin\dfrac{x}{2^n} } \\
=\dfrac{\sin(x)}{x} 
\end{array}
$$

</div>


### T5

<div class='cbox'>

$$
\begin{array}{l}
\lim_{x \to \infty} (\sin\dfrac{1}{x} +\cos\dfrac{1}{x} )^x 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\lim_{x \to \infty} (\sin\dfrac{1}{x} +\cos\dfrac{1}{x} )^x  \\
=\lim_{x \to \infty} e^{x\ln(\sin\frac{1}{x}+\cos\frac1x)} \\
=e^{\lim_{x \to \infty} x\ln(\sin\frac{1}{x}+\cos\frac1x)} \\
=e^{\lim_{x \to \infty} x(\sin\frac{1}{x}+(\cos\frac1x-1))} \\
=e^{\lim_{x \to \infty} x(\frac{1}{x}+(1-\frac{1}{2x^2} -1))} \\
=e
\end{array}
$$

</div>


### T6

<div class='cbox'>

$$
\begin{array}{l}
\lim_{x \to 0} x \lbrack \dfrac{1}{x}  \rbrack 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\left. \begin{array}{ll}
x\lbrack \dfrac{1}{x}  \rbrack \in (1-x,1] \\
\lim_{x \to 0} 1-x=\lim_{x \to 1} 1=1
\end{array} \right\} \\
\stackrel{\text{Squeeze Theorem}}{\Longrightarrow}
\lim_{x \to 0} x \lbrack \dfrac{1}{x}  \rbrack =1 
\end{array}
$$

</div>


### T7

<div class='cbox'>

$$
\begin{array}{l}
\lim_{x \to \infty} (\dfrac{1+x}{3+x}  )^x
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
(\dfrac{1+x}{3+x}  )^x
=(1-\dfrac{2}{x+3} )^x \\
\text{let } t=-\dfrac{x+3}{2},x=-2t-3  \\
(1+\dfrac{2}{x+3} )^x=(1+\dfrac{1}{t} )^{-2t-3} \\
\therefore \lim_{x \to \infty} (1+\dfrac{2}{x+3} )^x \\
=\lim_{t \to \infty} (1+\dfrac{1}{t} )^{-2t} \\
=e^{-2}
\end{array}
$$

</div>


### T8

<div class='cbox'>

$$
\begin{array}{l}
\lim_{x \to 0} (\dfrac{a^x+b^x+c^x}{3} )^\frac{1}{x}
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\lim_{x \to 0} (\dfrac{a^x+b^x+c^x}{3} )^\frac{1}{x} \\
=\exp \lim_{x \to 0} \dfrac{\ln(\dfrac{a^x+b^x+c^x}{3} )}{x}  \\
=\exp \lim_{x\to 0}\dfrac{(\dfrac{a^x+b^x+c^x}{3} )-1}{x} \\
a^x=e^{x\ln(a)}=1+x\ln(a)+o(x) \\
\therefore
=\exp \lim_{x \to 0} \dfrac{x\ln a+x\ln b+x\ln c}{x} \\
=\exp \dfrac{\ln(abc)}{3} \\
=\sqrt[ 3 ]{ abc }  

\end{array}
$$

</div>


### T9

<div class='cbox'>

$$
\begin{array}{l}
\lim_{x \to 0} \dfrac{x\tan^4x}{\sin^3x(1-\cos x)} 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\lim_{x \to 0} \dfrac{x\tan^4x}{\sin^3x(1-\cos x)}  \\
=\lim_{x \to 0} \dfrac{x\sin x}{\cos^3x(1-\cos x)}  \\
=\lim_{x \to 0} \dfrac{x^2}{\cos^3x\dfrac{x^2}{2} }  \\
=2
\end{array}
$$

</div>

### T10


<div class='cbox'>

$$
\begin{array}{l}
\lim_{x \to 0} \dfrac{\sqrt{ 1+x^4 } -1}{1-\cos^2x} 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\lim_{x \to 0} \dfrac{\sqrt{ 1+x^4 } -1}{1-\cos^2x}  \\
=\lim_{x \to 0} \dfrac{x^4}{2x^2} \\
=\lim_{x \to 0} \dfrac{x^2}{2}  \\
=0 
\end{array}
$$

</div>


### T11

<div class='cbox'>

solve a,b:

$$
\begin{array}{l}
\lim_{x \to +\infty} (\sqrt{ x^2-x+1 } -ax-b)=0
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\sqrt{ x^2-x+1 }=\sqrt{(x-\dfrac{1}{2} )^2+\dfrac{3}{4} } \\
\text{let } t=x-\dfrac{1}{2}  \\
\lim_{x \to \infty} \sqrt{ x^2-x+1 } -(x-\dfrac{1}{2} ) \\
=\lim_{x \to \infty} \sqrt{ t^2+\dfrac{3}{4}  }-\sqrt{ t^2 }  \\
=\lim_{x \to \infty} \dfrac{3}{4(\sqrt{t^2+\frac{3}{4}}+\sqrt{t^2})}   \\
=0
\end{array}
$$

</div>

### T12

<div class='cbox'>

$$
\begin{array}{l}
f(x_0^-)<f(x_0^+) \Rightarrow \exists \delta>0,\forall x\in (x_0-\delta,x_0),\forall y\in (x_0,x_0+\delta),f(x)<f(y)
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\lim_{x \to x_0^-} f(x)<\lim_{x \to x_0^+} f(x) \\
\text{let } \epsilon=\dfrac{f(x_0^+)-f(x_0^-)}{3} ,\exists \delta=\min(\delta_1,\delta_2) \\ s.t.\\ 
\forall x\in (x_0-\delta,x_0), \vert f(x)-f(x_0^-) \vert <\epsilon, \\
\forall y\in (x_0,x_0+\delta), \vert f(y)-f(x_0^+) \vert <\epsilon \\
\therefore f(x)<f(x_0^-)+\epsilon<f(x_0^+)-\epsilon<f(y)
\end{array}
$$

</div>

### T13

<div class='cbox'>

$$
\begin{array}{l}
f \text{ is periodic function} ,\lim_{x \to \infty} f(x)=0 \\
\Rightarrow f(x)=0
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\text{let } T \text{ is a period of } f \\
\forall x_0,\epsilon,
\exists X>x_0 \ s.t.\ 
x>X \Rightarrow f(x)<\epsilon \\
\text{let } n=\lbrack \dfrac{X-x_0}{T} +100 \rbrack  \\
\Rightarrow  f(x_0)=f(x_0+nT)<\epsilon \\
\Rightarrow \lim_{x \to x_0} f(x)=0 \\
\Rightarrow f(x)=0
\end{array}
$$

</div>

### T14

<div class='cbox'>

$$
\begin{array}{l}
\left. \begin{array}{ll}
f(x),x\in(0,1) \\
x\to 0^+ \Rightarrow f(x)=o(1) \\
f(x)-f(\dfrac{x}{2} )=o(x)
\end{array} \right\}
\Rightarrow x\to 0^+ ,f(x)=o(x)
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\forall \epsilon, \\
\text{let }\epsilon_1=\dfrac{\epsilon}{8}\\
\exists \delta \ s.t.\ 
x<\delta \Rightarrow 
f(x)-f(\dfrac{x}{2} )<\epsilon_1x \\
\therefore
f(x)=f(\dfrac{x}{2^n} )+\sum _{i = 0} ^{n-1}  f(\dfrac{x}{2^i} )-f(\dfrac{x}{2^{i+1}} )  \\
<f(\dfrac{x}{2^n} )+\sum _{i = 0} ^{n-1}  \dfrac{\epsilon_1x}{2^i}  \\
<f(\dfrac{x}{2^n} )+2\epsilon_1x \\
\therefore f(x)=\lim_{n \to \infty} f(x) \\
\le \lim_{n \to \infty} f(\dfrac{x}{2^n} )+2\epsilon_1x \\
=2\epsilon_1x \\
<\epsilon x \\ 
\Rightarrow x\to 0^+ \Rightarrow  f(x)=o(x) 
\end{array}
$$

</div>

### T15

<div class='cbox'>

$$
\begin{array}{l}
\left. \begin{array}{ll}
a,b>1,f(x) \text{ is bounded in } N^*(0) \\
f(ax)=bf(x)
\end{array} \right\} \\
\Rightarrow \lim_{x \to 0} f(x)=f(0)
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
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
\end{array}
$$

</div>

