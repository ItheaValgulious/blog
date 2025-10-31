---
title: Math Analysis Homework - Week 6
tags: [math-analysis,math,homework]
---

# Math Analysis Homework - Week 6

## Class 1

### T1

<div class='cbox'>

analysis the function's convexity and inflection point

$$
\begin{array}{l}
f(x)=\dfrac{1-x^2}{1+x} 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
f(x)=1-x (x\ne -1) \\
f''(x)=0 \\
\Rightarrow \text{convex  in } (-\infty,-1),(-1,+\infty) \\
\forall x \ne -1,x \text{ is a inflection point} 
\end{array}
$$

</div>



### T2

<div class='cbox'>

$$
\begin{array}{l}
a,b>0 \Rightarrow  \\
(a+b)\ln \dfrac{a+b}{2} \le a\ln a+b\ln b
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
f(x)=x\ln x \\
f''(x)=\dfrac{1}{x} \ge 0 \Rightarrow f \text{ is convex in } (0,+\infty) \\
\Rightarrow f(a)+f(b)\ge 2f(\dfrac{a+b}{2} )  \\
\Rightarrow (a+b)\ln \dfrac{a+b}{2} \le a\ln a+b\ln b
\end{array}
$$

</div>



### T3

<div class='cbox'>

$$
\begin{array}{l}
p,q>0;a,b\ge 0 \Rightarrow  \\
(\dfrac{a}{p} )^p(\dfrac{b}{q} )^q\le (\dfrac{a+b}{p+q} )^{p+q}
\end{array}
$$

</div>

<div class='pbox'>

$ab=0$显然成立,考虑$a,b\ne 0$.

$$
\begin{array}{l}
(\dfrac{a}{p} )^p(\dfrac{b}{q} )^q\le (\dfrac{a+b}{p+q} )^{p+q} \\
\Leftrightarrow 
p\ln a-p\ln p +q\ln b-q\ln q\le (p+q)(\ln (a+b)-\ln (p+q)) \\
\Leftrightarrow 
p(\ln a-\ln (a+b)+\ln(p+q)-\ln p)+q(\ln b-\ln (a+b)+\ln (p+q)-\ln q)\le 0 \\ \\
\xLeftrightarrow{\text{let } x=\dfrac{p}{p+q} ,y=\dfrac{a}{a+b} }
\\
 x(\ln y-\ln x)+(1-x)(\ln (1-y)-\ln (1-x))\le 0 \\
f(y)=x\ln y+(1-x)\ln (1-y) \\
f'(y)=\dfrac{x}{y}-\dfrac{1-x}{1-y}=\dfrac{x-y}{y(1-y)}  \\
\Rightarrow \operatorname{sign} f'(y)=-\operatorname{sign} (y-x),f(x) \text{ is a maximum } \\
\Rightarrow f(y)\le f(y)=0 \\
\\
\text{Q.E.D}
\end{array}
$$

</div>

### T4

<div class='cbox'>

$$
\begin{array}{l}
\lambda_i>0,x_i>0,\sum _{i = 1} ^{n}  \lambda_i=1 \\
\Rightarrow \prod _{i = 1} ^{n}  x_i^{\lambda_i}\le \sum _{i = 1} ^{n}  \lambda_i x_i
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\ln(\sum _{i = 1} ^{n}  \lambda_ix_i)\ge \sum _{i = 1} ^{n}  \lambda_i\ln(x_i)=\ln \prod _{i = 1} ^{n}  x_i^{\lambda_i}\\
\text{Q.E.D}
\end{array}
$$

</div>



### T5

<div class='cbox'>

$$
\begin{array}{l}
f(x) \text{ is convex in } [a,b],\exists c\in (a,b):f(a)=f(c)=f(b) \\
\Rightarrow \forall x\in [a,b],f(x)=f(a)
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\forall x<c, \\
\begin{cases}
\dfrac{f(x)-f(c)}{x-c} \le \dfrac{f(c)-f(b)}{c-b} =0 \\
\dfrac{f(x)-f(c)}{x-c} \ge \dfrac{f(c)-f(a)}{c-a} =0
\end{cases} \\
\Rightarrow f(x)=f(c) \\
\text{same for } \forall x>c,f(x)=c \\
\Rightarrow \forall x\in [a,b],f(x)=f(a)
\end{array}
$$

</div>



### T6

<div class='cbox'>

$$
\begin{array}{l}
\left. \begin{array}{ll}
a<b<c<d \\
f(x) \text{ is convex in } [a,c] \text{ and }  [b,d] \\
\end{array} \right\} \\
\Rightarrow f(x) \text{ is convex in [a,d]} 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\forall x_1,x_2 \in [a,d] \\
\text{if } x_1,x_2\in [a,c] \\
f(\lambda x_1+(1-\lambda)x_2)\le \lambda  f(x_1)+(1-\lambda)f(x_2) \\
\text{same for } x_1,x_2\in[b,d] \\
\text{else } x_1\in [a,b),x_2\in (c,d] \\
\text{let } m=\lambda x_1+(1-\lambda)x_2 \\
\text{if } m \in [a,c] \\
\dfrac{f(x_1)-f(c)}{x_1-c} \le \dfrac{f(x_1)-f(x_2)}{x_1-x_2}  \\
\Rightarrow 
f(m)\le \mu f(x_1)+(1-\mu)f(c) \\
=f(x_1)+\dfrac{f(x_1)-f(c)}{x_1-c} (m-x_1) \\
\le f(x_1)+\dfrac{f(x_1)-f(x_2)}{x_1-x_2} (m-x_1) \\
=\lambda f(x_1)+(1-\lambda)f(x_2)  \\
\text{same for } m\in[c,d] \\
\therefore f \text{ is convex in } [a,d]
\end{array}
$$

</div>



### T7

<div class='cbox'>

$$
\begin{array}{l}
f(x) \text{ is convex in } I \\
\Leftrightarrow \forall c\in I,\exists a,f(x)\ge a(x-c)+f(c)
\end{array}
$$

</div>

<div class='pbox'>

反向:
$$
\begin{array}{l}
\forall x_1<x_2,\lambda \in (0,1) \\
\text{let } x_3=\lambda x_1+(1-\lambda)x_2,k=\dfrac{f(x_1)-f(x_2)}{x_1-x_2}  \\
\exists a, \\ s.t.\\ 
\begin{cases}
f(x_1)\ge a(x_1-x_3)+f(x_3) \\
f(x_2)\ge a(x_2-x_3)+f(x_3) \\
\end{cases} \\
\Rightarrow 
\begin{cases}
a\le \dfrac{f(x_1)-f(x_3)}{x_1-x_3}  \\
a\ge \dfrac{f(x_2)-f(x_3)}{x_2-x_3} 
\end{cases} \\
\Rightarrow \dfrac{f(x_1)-f(x_3)}{x_1-x_3} \ge \dfrac{f(x_2)-f(x_3)}{x_2-x_3}  \\
\Leftrightarrow f(x_3)\le \lambda f(x_1)+(1-\lambda)f(x_2)



\end{array}
$$

正向:

$$
\begin{array}{l}
\text{let } S=\{ \dfrac{f(x)-f(c)}{x-c} \vert x<c  \}  \\
T=\{ \dfrac{f(x)-f(c)}{x-c} \vert x>c  \}  \\
\forall s\in S,t\in T:s<t \\
\Rightarrow \sup S\le \inf T \\
\text{let } a\in [\sup S,\inf T] \\
\Rightarrow \begin{cases}
\forall x<c,\dfrac{f(x)-f(c)}{x-c} <a \\
\forall x>c,\dfrac{f(x)-f(c)}{x-c} >a
\end{cases} \\
\Rightarrow \forall x,f(x)>a(x-c)
\end{array}
$$

</div>

[think] 就是直接构造$a$而不是其他的什么奇怪思路.

### T8

<div class='cbox'>

$$
\begin{array}{l}
f(x) \text{ is convex in } [a,b] \\
\Rightarrow \forall x\in[a,b],f(x)\le \max(f(a),f(b))
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\text{let } m=\max(f(a),f(b)) \\
\lambda=\dfrac{x-a}{b-a} \\
\Rightarrow 
f(x)\le \lambda f(a)+(1-\lambda)f(b) \\
\le \lambda m + (1-\lambda) m \\
=m \\
\text{Q.E.D}

\end{array}
$$

</div>

### T9

<div class='cbox'>

$$
\begin{array}{l}
f(x) \text{ is convex in } [a,b] \\
\Rightarrow f(x) \text{ is bounded in } [a,b]
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\text{According to T8,} f(x)\le M_1=\max (f(a),f(b)) \\ \text{let } c\in (a,b) \\
\forall x<c,\dfrac{f(c)-f(x)}{c-x} \le \dfrac{f(b)-f(c)}{b-c}  \\
\Rightarrow f(x)\ge f(c)-\dfrac{f(b)-f(c)}{b-c} (c-x) \\
\ge f(c)-\dfrac{f(b)-f(c)}{b-c} (c-a)=M_2 \\
\text{same for } x>c,f(x)\ge f(c)-\dfrac{f(c)-f(a)}{c-a} (b-c)=M_3 \\
\Rightarrow \vert f(x) \vert \le \max (\vert M_1 \vert ,\vert M_2 \vert ,\vert M_3 \vert) =M
\end{array}
$$

</div>

## Class 2

### T1

<div class='cbox'>

$$
\begin{array}{l}
\lim_{x \to \frac{\pi}{2} } \dfrac{\ln \sin(x)}{(\pi-2x)^2} 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\lim_{x \to \frac{\pi}{2} } \dfrac{\ln \sin(x)}{(\pi-2x)^2}  \\
=\lim_{x \to \frac{\pi}{2} } \dfrac{\dfrac{\cos x}{\sin x} }{4(2x-\pi)}  \\
=\lim_{x \to \frac{\pi}{2} } \dfrac{\cos x}{4(2x-\pi)}  \\
=\lim_{x \to \frac{\pi}{2} } \dfrac{-\sin x}{8} \\
=-\dfrac{1}{8}  
\end{array}
$$

</div>



### T2

<div class='cbox'>

$$
\begin{array}{l}
\lim_{x \to 1^-} \ln x\ln(1-x)
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\lim_{x \to 1^-} \ln x\ln(1-x) \\
=\lim_{x \to 1^-} \ln(1+(x-1))\ln(1-x) \\
=\lim_{x \to 1^-} (x-1)\ln(1-x) \\
=\lim_{x \to 1^-} \dfrac{\ln(1-x)}{\dfrac{1}{x-1} }  \\
=\lim_{x \to 1^-} \dfrac{-\dfrac{1}{1-x} }{-\dfrac{1}{(x-1)^2} } =0
\end{array}
$$

</div>



### T3

<div class='cbox'>

$$
\begin{array}{l}
\lim_{x \to \infty} x[(1+\dfrac{1}{x} )^x-e]
\end{array}
$$

</div>

<div class='pbox'>


$$
\begin{array}{l}
\lim_{x \to \infty} x[(1+\dfrac{1}{x} )^x-e] \\
=\lim_{x \to \infty} \dfrac{(1+\dfrac{1}{x} )^x-e}{\dfrac{1}{x} }  \\
=\lim_{x \to 0} \dfrac{e^{\frac{\ln (x+1)}x}-e}{x}  \\
=\lim_{x \to 0} e^{\frac{\ln (1+x)}{x} } \cdot \dfrac{\frac{x}{1+x}-\ln(1+x)}{x^2}  \\
=\lim_{x \to 0} e \dfrac{\dfrac{1}{(1+x)^2} -\dfrac{1}{1+x} }{2x}  \\
=-\dfrac{1}{2} e
\end{array}
$$

</div>



### T4

<div class='cbox'>

$$
\begin{array}{l}
\lim_{x \to 0} {\left( \dfrac{(1+x)^\frac1x}{e}  \right)}^{\frac{1}{x}}
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\lim_{x \to 0} \exp \dfrac{1}{x} {\left( \dfrac{1}{x} \ln(1+x)-1 \right)}  \\
=\lim_{x \to 0} \exp \dfrac{\ln(1+x)-x}{x^2}  \\
=\exp \lim_{x\to 0}\dfrac{\ln(1+x)-x }{x^2}  \\ \\
=\exp \lim_{x\to 0}\dfrac{\dfrac{1}{1+x} -1}{2x} 
=e^{-\frac12}
\end{array}
$$

</div>



### T5

<div class='cbox'>

$$
\begin{array}{l}
\left. \begin{array}{ll}
f(x)\in C^2(a,+\infty) \\
\lim_{x \to +\infty} (f(x)+2f'(x)+f''(x))=l
\end{array} \right\} \\
\Rightarrow \begin{cases}
\lim_{x \to +\infty} f(x)=l \\
\lim_{x \to +\infty} f'(x)=\lim_{x \to +\infty} f''(x)=0
\end{cases}
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\text{let } F(x)=e^xf(x) \\
\Rightarrow 
\begin{cases}
F'(x)=e^x(f(x)+f'(x)) \\
F''(x)=e^x (f(x)+2f'(x)+f''(x))
\end{cases} \\
\Rightarrow \lim_{x \to +\infty} \dfrac{F''(x)}{e^x}=l \\
\lim_{x \to +\infty} \dfrac{F(x)}{e^x}  \\
=\lim_{x \to +\infty} \dfrac{F'(x)}{e^x} \\
=\lim_{x \to +\infty} \dfrac{F''(x)}{e^x} =l \\
\Rightarrow 
\begin{cases}
\lim_{x \to +\infty} f(x)=l \\
\lim_{x \to +\infty} f'(x)=\lim_{x \to +\infty} \dfrac{F'(x)}{e^x} -f(x)=0 \\
\lim_{x \to +\infty} f''(x)=\lim_{x \to +\infty} \dfrac{F''(x)}{e^x} -2f'(x)-f(x)=0
\end{cases}



\end{array}
$$

</div>



### T6

<div class='cbox'>

$$
\begin{array}{l}
\exists f''(x_0),f'(x_0)\ne 0 \\
\text{calc } \lim_{x \to x_0} {\left( \dfrac{1}{f(x)-f(x_0)} -\dfrac{1}{(x-x_0)f'(x_0)}  \right)} 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\lim_{x \to x_0} {\left( \dfrac{1}{f(x)-f(x_0)} -\dfrac{1}{(x-x_0)f'(x_0)}  \right)}  \\
=\lim_{x \to x_0} \dfrac{(x-x_0)f'(x_0)-(f(x)-f(x_0))}{(f(x)-f(x_0))(x-x_0)f'(x_0)} \\
=\lim_{x \to x_0} \dfrac{f'(x_0)-f'(x)}{f'(x_0)(f(x)+xf'(x)-x_0f'(x)-f(x_0))} \\
=\lim_{x \to x_0} \dfrac{-f''(x)}{f'(x_0)(2f'(x)+(x-x_0)f''(x))} \\
=-\dfrac{f''(x_0)}{2(f'(x_0))^2}
\end{array}
$$

</div>



### T7

<div class='cbox'>

$$
\begin{array}{l}
\vert x \vert <1,\arcsin x=\dfrac{x}{\sqrt{1-\theta^2x^2}} ,\theta\in (0,1) \\
\text{calc } \lim_{x \to 0}\theta
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\theta^2=\dfrac{1}{x^2} -\dfrac{1}{\arcsin^2(x)}  \\
=\dfrac{\arcsin^2(x)-x^2}{x^2\arcsin^2(x)}  \\
\text{let } t=\arcsin(x),x=\sin t \\
\Rightarrow \theta^2=\dfrac{t^2-\sin^2 t}{t^2\sin^2 t}  \\
\lim_{x \to 0} \theta^2 \\
=\lim_{t \to 0} \dfrac{t^2-\sin^2t}{t^2\sin^2t}  \\
=\lim_{t \to 0} \dfrac{t^2-\sin^2 t}{t^4}   \\
=\lim_{t \to 0} \dfrac{2t-\sin 2t}{4t^3}  \\
=\lim_{t \to 0} \dfrac{1-\cos2t}{6t^2}  \\
=\lim_{t \to 0} \dfrac{t^2}{3t^2} \\
=\dfrac{1}{3} \\
\Rightarrow \lim_{x \to 0} \theta = \dfrac{\sqrt 3}{3} 
\end{array}
$$

</div>

## Class 3

### T1

![alt text](../imgs/math-analysis-week6-homework/img-1761888263357.png)

### T2

<div class='cbox'>

$$
\begin{array}{l}
\text{calc } \vert S \vert \\
\vert S \vert = \{ x \vert \ln x-\dfrac{x}{e} =k,x\in(0,+\infty) \} 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\text{let } f(x)=\ln x-\dfrac{x}{e}  \\
f'(x)=\dfrac{1}{x} -\dfrac{1}{e}  \\
\Rightarrow \begin{cases}
x<e \Rightarrow f'(x)>0,f(x) \text{ is increasing}  \\
x>e \Rightarrow f'(x)<0,f(x) \text{ is decreasing}  \\
f(e)=0 \text{ is maximum of } f \\
\end{cases} \\
\left. \begin{array}{ll}
\lim_{x \to +\infty} f(x)=-\infty \\
\lim_{x \to 0^+} f(x)=-\infty    \\
\end{array} \right\} \\
\Rightarrow \begin{cases}
\vert S \vert =0,k>0 \\
\vert S \vert =1,k=0 \\
\vert S \vert =2,k<0
\end{cases}

\end{array}
$$

</div>



### T3

<div class='cbox'>

$$
\begin{array}{l}
x>0 \Rightarrow \exists !x_0,kx+\dfrac{1}{x_0^2} =1 \\
\text{solve } k
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\text{let } f(x)=\dfrac{x^2-1}{x^3} \\
f'(x)=\dfrac{3-x^2}{x^4} \\
\Rightarrow \begin{cases}
x<\sqrt 3 \Rightarrow f'(x)>0,f(x) \text{ is increasing}  \\
x>\sqrt 3 \Rightarrow f'(x)<0,f(x) \text{ is decreasing}  \\
f(\sqrt 3)=\dfrac{2\sqrt 3}{9} \text{ is maximum} 
\end{cases} \\
\begin{cases}
\lim_{x \to 0^+} f(x)=-\infty \\
\lim_{x \to +\infty} f(x)=0
\end{cases} \\
\Rightarrow k \in \{ \dfrac{2\sqrt 3}{9}  \} \cup (-\infty,0]


\end{array}
$$

</div>


