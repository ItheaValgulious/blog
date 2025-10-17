---
title: Math Analysis Homework - Week 4
tags:
  - math-analysis
  - homework
  - math
date: 2025-10-13 17:49:46
---


# Math Analysis Homework - Week 4

## Class 1

### T1

<div class='cbox'>

$$
\begin{array}{l}
\left. \begin{array}{ll}
f\in C[a,b] \\
\forall x\in [a,b],\exists y\in [a,b], \vert f(y) \vert \le \dfrac{1}{2} \vert f(x) \vert 
\end{array} \right\} \\
\Rightarrow \exists \xi\in [a,b],f(\xi)=0
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\text{let } x_0\in [a,b], \\
\exists x_i\in[a,b] \ s.t.\ 
\vert f(x_i) \vert \le \dfrac{1}{2} \vert f(x_{i-1}) \vert  \\
x_i\in [a,b] \Rightarrow \exists \{ k_n \} \ s.t.\ 
\{ x_{k_n} \} \text{ is convergent}  \\
\Rightarrow \lim_{n \to \infty} x_{k_n}=X \\
\vert f(x_{k_n})\vert \le \dfrac{1}{2}  \vert f(x_{k_{n-1}})\vert
\Rightarrow  \vert f(x_{k_n})\vert\le \vert f(x_{0})\dfrac{1}{2^n}\vert  \\
\Rightarrow \lim_{n \to \infty} \vert f(x_{k_n})\vert=0 \\
\therefore \lim_{n \to \infty} \vert f(x_{k_n}) \vert =\vert f(\lim_{n \to \infty} x_{k_n}) \vert =\vert f(X) \vert =0
\\
\text{Q.E.D}
\end{array}
$$

</div>



### T2

<div class='cbox'>

$$
\begin{array}{l}
\left. \begin{array}{ll}
\psi\in C(R) \\
\lim_{x \to +\infty} \dfrac{\psi(x)}{x^n} =\lim_{x \to =-\infty} \dfrac{\psi(x)}{x^n} =0
\end{array} \right\} \\
\Rightarrow \begin{cases}
n \bmod 2=1 \Rightarrow \exists x_0,x_0^n+\psi(x_0)=0 \\
n \bmod 2=0 \Rightarrow \exists y,\forall x\in R,y^n+\psi(y)\le x^n+\psi(x)
\end{cases}

\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
f(x):=\dfrac{\psi(x)}{x^n} 
\end{array}
$$

(1):

$$
\begin{array}{l}
\text{if } \psi(0)=0 :  x_0=0 \\
\text{else } \psi(0)\ne 0, \\
\text{without lossing generality,let } \psi(0)=a<0 \\
\Rightarrow \lim_{x \to 0} \psi(x)=a<0 \\
\therefore \lim_{x \to 0^+} f(x) =\lim_{x \to 0^+} \dfrac{a}{x^n} =-\infty \\
\Rightarrow \text{let }M=-2,\exists x_1,f(x_1) <M=-2 \\
\lim_{x \to +\infty} f(x)=0 \\
\Rightarrow \text{let } \epsilon=0.5,\exists x_2,\vert f(x_2) \vert <\epsilon \\
f(x) \text{ is continuous in }(0,+\infty) \\
\stackrel{\text{ Intermediate Theorem }}{\Longrightarrow}\exists x_0,f(x_0)=-1,x_0^n+\psi(x_0)=0

\\
\text{Q.E.D}
\end{array}
$$

(2): 
$$
\begin{array}{l}
f(x)=x^n+\psi(x) \\
\lim_{x \to \infty} \dfrac{f(x)}{x^n} =1 \\
\text{let } \epsilon=0.1,\exists X,\vert x>X \vert \Rightarrow f(x)\in (0.9x^n,1.1x^n) \\
\exists y_1\in [-X,X],\forall x\in [-X,X],f(y_1)\le f(x) \\
\exists X_2,0.9X_2^n>f(y_1) \\
\exists y_2\in [-X_2,X_2],\forall x\in [-X_2,X_2],f(y_2)\le f(x) \\
\forall x\notin [-X_2,X_2],f(x)>0.9x^n>0.9X_2^n>f(y_1)\ge f(y_2) \\
\therefore \forall x,f(y_2)\le f(x)\\
\text{Q.E.D}
\end{array}
$$

</div>



### T3

<div class='cbox'>

$$
\begin{array}{l}
\left. \begin{array}{ll}
f\in C(R),\lim_{x \to \infty} f(x)=+\infty \\
\min f(x)=f(a)<a
\end{array} \right\} \\
\Rightarrow \exists x_1,x_2,f(f(x_i))=f(a)
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\exists X,\vert x \vert >X \Rightarrow f(x)>2a \\
\Rightarrow \exists X_1<a,X_2>a,f(X_1)>a,f(X_2)>a \\

\left. \begin{array}{ll}
f(a)<a \\
f(X_1)>a \\
f(x) \text{ is continuous} 
\end{array} \right\}  \\
\stackrel{\text{ Intermediate Theorem }}{\Longrightarrow} \\
\exists x_1\in [X_1,a],f(x_1)=a,f(f(x_1))=f(a) \\

\left. \begin{array}{ll}
f(a)<a \\
f(X_2)>a \\
f(x) \text{ is continuous} 
\end{array} \right\} \\
\stackrel{\text{ Intermediate Theorem }}{\Longrightarrow} \\
\exists x_2\in [a,X_2],f(x_2)=a,f(f(x_2))=f(a) 
\\
\text{Q.E.D}
\end{array}
$$

</div>



### T4

<div class='cbox'>

$$
\begin{array}{l}
f:C[a,b]\to R,D(f(x))+D(x)=1,(D(x)=[x\in Q]) \\
\Rightarrow f\notin C[a,b]
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\text{By Contradiction}  \\
\forall [x_1,x_2] \\
\stackrel{ \text{Intermediate Theorem}  }{\Longrightarrow} \\
\forall y\in [f(x_1),f(x_2)],\exists x_0,f(x_0)=y \\
\{ f(x) \vert x\in Q\cap [x_1,x_2] \} \supset \{ y \vert y\in Q^C \cap [f(x_1),f(x_2)] \}  \\ 
\Rightarrow [f(x_1),f(x_2)] \text{ is countable}  \\
\text{Ridiculous!}\\
\text{Q.E.D} 
\end{array}
$$

</div>



### T5

<div class='cbox'>

$$
\begin{array}{l}
f\in C[0,2a],f(0)=f(2a),a>0 \\
\Rightarrow \exists \xi\in [0,a],f(\xi)=f(\xi+a)
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\text{if } f(a)=0,\xi=a \\
\text{else: }  f(a)\ne 0 \\
\text{without lossing generality,let } f(a)>0 \\
\text{let } g(x)\in C[a,2a]= f(x)-f(x-a) \\
g(a)>0,g(2a)<0  \\
\stackrel{\text{ Intermediate Theorem }}{\Longrightarrow} \exists \xi,g(\xi)=0=f(\xi)=f(\xi-a) \\
\text{Q.E.D}
\end{array}
$$

</div>



### T6

<div class='cbox'>

$$
\begin{array}{l}
\left. \begin{array}{ll}
f\in C[a,b] \\
\{ x_n \} ,x_i\in[a,b]
\end{array} \right\} \\
\Rightarrow \exists \xi\in [\min_{i\in [1,n]} \{ x_i \} ,\max_{i\in[1,n]} \{ x_i \} ]:f(\xi)=\dfrac{1}{n} \sum _{i = 1} ^{n}  f(x_i)
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
L:=\min_{i\in [1,n]} \{ x_i \} ,R:=\max_{i\in[1,n]} \{ x_i \}  \\
f\in C[a,b] \stackrel{\text{ Extreme Value Theorem }}{\Longrightarrow} \exists x_1,x_2\in [L,R], \\
\forall x\in [L,R],f(x_1)\le f(x)\le f(x_2) \\
\dfrac{1}{n} \sum _{i = 1} ^{n}  f(x_i)\in [f(x_1),f(x_2)] \\
\stackrel{\text{ Intermediate Theorem }}{\Longrightarrow}\exists \xi,f(\xi)=\dfrac{1}{n} \sum _{i = 1} ^{n}  f(x_i)
\\
\text{Q.E.D}
\end{array}
$$

</div>



### T7

<div class='cbox'>

$$
\begin{array}{l}
f\in C(R),\forall \text{open interval } I,f(I) \text{ is open interval} \\
\Rightarrow f(x) \text{ is monotonic} 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\text{By Contradiction} \\
\text{if } \exists x_1<x_2<x_3,f(x_2)\le \min(f(x_1),f(x_3)) \\
\Rightarrow \exists x_4\in (x_1,x_2),\forall x\in[x_1,x_2],f(x_4)\ge f(x) \\
\text{let } I=(x_1,x_2),f(I)=\{ f(x) \vert x\in I \} . \\
\text{but } f(x_4)\in f(I),f(x_4) = \sup f(I),f(I) \text{ is not open}. \\
\text{Ridiculous!}  \\
\Rightarrow \not\exists x_1<x_2<x_3,f(x_2)\le \min(f(x_1),f(x_3)) \\
\text{same for} \not\exists x_1<x_2<x_3,f(x_2)\ge \max(f(x_1),f(x_3)) \\
\therefore \forall x_1<x_2<x_3,f(x_2)\in (f(x_1),f(x_3)) \\
\therefore f(x) \text{ is monotonic} 
\end{array}
$$

</div>



### T8

<div class='cbox'>

$$
\begin{array}{l}
f\in C(R),\lim_{x \to \infty} f(f(x))=\infty     \\
\Rightarrow \lim_{x \to \infty} f(x)=\infty
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\text{By Contradiction} \\
\exists M,a_n,\vert a_n \vert >n,\vert f(a_n) \vert <M \\ 
\Rightarrow \exists k_i,f(a_{k_i}) \text{ is convergent}  \\
\Rightarrow \lim_{n \to \infty} f(a_{k_i})=A<M \\
\lim_{n \to \infty} f(f(a_n))=\infty \\
\Rightarrow \lim_{n \to \infty} f(f(a_{k_i}))=\infty \\
\Rightarrow \lim_{n \to \infty} f(f(a_{k_i})) \\
=f(\lim_{n \to \infty} f(a_{k_i})) \\
=M \\
\text{Ridiculous!} \\
\text{Q.E.D}
\end{array}
$$

</div>



### T9

<div class='cbox'>

$$
\begin{array}{l}
\forall x,y\in R,\vert f(x)-f(y) \vert \le k \vert x-y \vert ,0<k<1 \\
\Rightarrow \begin{cases}
x-f(x) \text{ is increasing}  \\
\exists! \xi\in R,f(\xi)=\xi
\end{cases}

\end{array}
$$

</div>

<div class='pbox'>

(1)

$$
\begin{array}{l}
\forall x_1>x_2 \\
(x_1-f(x_1))-(x_2-f(x_2)) \\
=(x_1-x_2)-(f(x_1)-f(x_2)) \\
\ge (x_1-x_2)-k \vert x_1-x_2 \vert  \\
\ge 0
\\
\text{Q.E.D}
\end{array}
$$

(2)

$$
\begin{array}{l}
g(x)=x-f(x) \\
\text{by (1) } g(x) \text{ is increasing}  \\
\forall x>0, \\
g(x)-g(0) \\
=(x-0)-(f(x)-f(0)) \\
\ge (1-k)x \\
\Rightarrow \lim_{x \to +\infty} g(x)-g(0)\ge \lim_{x \to +\infty} (1-k)x \\
\Rightarrow \lim_{x \to +\infty} g(x)=+\infty \\
\text{same for } \lim_{x \to -\infty} g(x)=-\infty \\
\left. \begin{array}{ll}
\lim_{x \to +\infty} g(x)=+\infty \\
\lim_{x \to -\infty} g(x)=-\infty \\
g(x) \text{ is continuous}  \\
g(x) \text{ is increasing} 
\end{array} \right\} \\
\stackrel{\text{ Intermediate Theorem }}{\Longrightarrow} \\
\exists! \xi \in R,g(\xi)=0,f(\xi)=\xi \\
\end{array}
$$

</div>

## Class 2

### T1

<div class='cbox'>

$$
\begin{array}{l}
\lim_{h \to 0} \dfrac{f^2(x_0+2h)-f^2(x_0-h)}{h} 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\lim_{h \to 0} \dfrac{f^2(x_0+2h)-f^2(x_0-h)}{h}  \\
=\lim_{h \to 0} \dfrac{(f(x_0+2h)+f(x_0-h))(f(x_0+2h)-f(x_0-h))}{h} \\
=\lim_{h \to 0} 2f(x_0)\dfrac{f(x_0+2h)-f(x_0)+f(x_0)-f(x_0-h)}{h}   \\
=4f(x_0)\lim_{h \to 0} \dfrac{f(x_0+2h)-f(x_0)}{2h} +2f(x_0)\dfrac{f(x_0)-f(x_0-h)}{h}   \\
=6f(x_0)f'(x_0)
\end{array}
$$

</div>



### T2

<div class='cbox'>

$$
\begin{array}{l}
\lim_{x \to x_0} \dfrac{xf(x_0)-x_0f(x)}{x-x_0} 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\lim_{x \to x_0} \dfrac{xf(x_0)-x_0f(x)}{x-x_0}  \\
=\lim_{\delta \to 0} \dfrac{(x_0+\delta)f(x_0)-x_0f(x_0+\delta)}{\delta}  \\
=\lim_{\delta \to 0} \dfrac{(x_0+\delta)f(x_0)-x_0f(x_0)}{\delta} +\dfrac{x_0f(x_0)-x_0f(x_0+\delta)}{\delta}  \\
=f(x_0)-x_0f'(x_0)
\end{array}
$$

</div>




### T3

<div class='cbox'>

$$
\begin{array}{l}
\text{solve } f \\ s.t.\\ 
f(x+y)=f(x)f(y),f'(0)=1
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
f(x+0)=f(x)f(0) \Rightarrow f(0)=1 \\
f(x+y)=f(x)f(y) \\
\stackrel{ \frac{d}{dx} }{\Longrightarrow}f'(x+y)=f'(x)f(y) \\
\stackrel{ f(x+y)=f(x)f(y) }{\Longrightarrow}\dfrac{f'(x+y)}{f(x+y)} =\dfrac{f'(x)}{f(x)}  \\
\stackrel{ f(0)=f'(0) }{\Longrightarrow}f(x)=f'(x) \\
\Rightarrow \dfrac{f'(x)}{f(x)} =1 \\
\Rightarrow \ln(f(x))'=1 \\
\Rightarrow \ln(f(x))=x+C \\
\Rightarrow f(x)=e^{x+C} \\
\stackrel{ f(0)=1 }{\Longrightarrow}C=0 \\
\Rightarrow  f(x)=e^x
\end{array}
$$

</div>




### T4

<div class='cbox'>

$$
\begin{array}{l}
\left. \begin{array}{ll}
f(x)\in C[a,b],f(a)=f(b)=0 \\
f'_+(a)f'_-(b)>0
\end{array} \right\} \\
\Rightarrow \exists \xi\in (a,b):f(\xi)=0
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
f'_+(a)>0 \Rightarrow \lim_{\Delta x \to 0}  \dfrac{f(a+\Delta x)-f(a)}{\Delta x}>0  \\
\Rightarrow \lim_{\Delta x \to 0}  f(a+\Delta x)>0 \\
\exists x_1\in N^*(a),x_1>a,f(x_1)>0 \\
\text{same for } \exists x_2 \in N^*(b),x_2<b,f(x_2)<0 \\
\stackrel{\text{ Intermediate Theorem }}{\Longrightarrow}\exists \xi \in [x_1,x_2],f(\xi)=0
\end{array}
$$

</div>




### T5

<div class='cbox'>

$$
\begin{array}{l}
f(x)=\vert x-a \vert g(x) \\
g(x) \text{ is continuous at } x=a \\
\text{solve under what condition } f \text{ is differentiable at } x=a
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
f \text{ is differentiable at } x=a \\
\Leftrightarrow \lim_{\Delta x \to 0} \dfrac{f(a+\Delta x)}{\Delta x} \text{ exists}   \\
\lim_{\Delta x \to 0^+} \dfrac{f(a+\Delta x)}{\Delta x} \\
=\lim_{\Delta x \to 0} \dfrac{\vert \Delta x \vert g(a+\Delta x)}{\Delta x} \\
=g(a) \\
\text{same for } \lim_{\Delta x \to 0^-} \dfrac{f(a+\Delta x)}{\Delta x} = -g(a) \\
\text{thus } f \text{ is differentiable at } x=a \\
\Leftrightarrow \lim_{\Delta x \to 0} \dfrac{f(a+\Delta x)}{\Delta x} \text{ exists} \\
\Leftrightarrow 
g(a)=-g(a) \\
\Leftrightarrow  g(a)=0
\end{array}
$$

</div>





### T6

<div class='cbox'>

$$
\begin{array}{l}
\left. \begin{array}{ll}
f(x) \text{ is continuous at } x=0 \\
f(0)=0 \\
\lim_{x \to 0} \dfrac{f(2x)-f(x)}{x} = A
\end{array} \right\} 
\Rightarrow f'(0)=A
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\text{without lossing generality, let } A>0,x>0 \\
f'(x)=\lim_{x \to 0} \dfrac{f(x)-f(0)}{x} =\lim_{x \to 0} \dfrac{f(x)}{x}  \\
\lim_{x \to 0} \dfrac{f(2x)-f(x)}{Ax} =1 \\
\Rightarrow \forall \epsilon,\exists \delta, f(2x)-f(x)  \in ((1-\epsilon)Ax,(1+\epsilon)Ax)\\
\Rightarrow f(x) = f(\dfrac{x}{2^n} )+\sum _{i = 1} ^{n}  f(\dfrac{x}{2^{i-1}})-f(\dfrac{x}{2^i} )  \\
\in (f(\dfrac{x}{2^n} )+Ax(1-\epsilon) \sum _{i = 1} ^{n}  \dfrac{1}{2^i},f(\dfrac{x}{2^n} )+Ax(1+\epsilon) \sum _{i = 1} ^{n}  \dfrac{1}{2^i}) \\
\lim_{n \to \infty} f(x)\in [Ax(1-\epsilon),Ax(1+\epsilon)] \\

\Rightarrow \lim_{x \to 0} \dfrac{f(x)}{x} =A
\end{array}
$$

</div>





### T7

<div class='cbox'>

$$
\begin{array}{l}
f(x) \text{ is differentiable at } x_0 \\
\Rightarrow \forall \{ a_n \} ,\{ b_n \} , \lim_{n \to \infty} a_n=x_0^-,\lim_{n \to \infty} b_n=x_0^+ \\
f'(x_0)=\lim_{n \to \infty} \dfrac{f(b_n)-f(a_n)}{b_n-a_n} 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\lim_{n \to \infty} \dfrac{f(b_n)-f(x_0)}{b_n-x_0} =\lim_{x \to x_0} \dfrac{f(x)-f(x_0)}{x-x_0}=f'(x_0)  \\
\text{same for } \dfrac{f(x_0)-f(a_n)}{x_0-a_n} =f'(x_0)  \\
\dfrac{f(b_n)-f(a_n)}{b_n-a_n}  \\
=\dfrac{f(b_n)-f(x_0)+f(x_0)-f(a_n)}{b_n-x_0+x_0-a_n} \\
\in (\dfrac{f(b_n)-f(x_0)}{b_n-x_0} ,\dfrac{f(x_0)-f(a_n)}{a_n-x_0} )
\stackrel{\text{ Squeeze Theorem }}{\Longrightarrow} \\
\lim_{n \to \infty} \dfrac{f(b_n)-f(a_n)}{b_n-a_n} =f'(x_0)

\end{array}
$$
</div>

## Class 3

Calc the following function's directive

### T1

<div class='cbox'>

$$
\begin{array}{l}
y=x\sin x+\dfrac{\sin x}{x} 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
y'=\sin(x)+x\cos(x)+\dfrac{x\cos x-\sin x}{x^2}  \\
=\sin x+x\cos x+\dfrac{\cos x}{x} -\dfrac{\sin x}{x^2} 
\end{array}
$$

</div>



### T2

<div class='cbox'>

$$
\begin{array}{l}
y=\dfrac{xe^x-1}{\sin x} 
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
y'=\dfrac{(x+1)e^x\sin x-(xe^x-1)\cos x}{\sin^2 x} \\
=\dfrac{(x+1)e^x}{\sin x} -\dfrac{(xe^x-1)\cos x}{\sin^2 x}  
\end{array}
$$

</div>



### T3

<div class='cbox'>

$$
\begin{array}{l}
y=(x^3+1)^4
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
y'=4(x^3+1)^3 3x^2 \\
=12x^2(x^3+1)^3
\end{array}
$$

</div>



### T4

<div class='cbox'>

$$
\begin{array}{l}
y=e^{\sqrt{x^3+1}}
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
y'=e^{\sqrt{x^3+1}} \cdot \dfrac{3x^2}{2\sqrt {x^3+1}} 
\end{array}
$$

</div>



### T5

<div class='cbox'>

$$
\begin{array}{l}
y=2^{\sin(x^2)}+2^{\tan \frac{1}{x} }
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
y'=2^{\sin x^2+1}\ln 2 \cos x^2 x-2^{\tan \frac{1}{x}}\ln 2 \sec^2 \dfrac{1}{x} \dfrac{1}{x^2} 
\end{array}
$$

</div>



### T6

<div class='cbox'>

$$
\begin{array}{l}
y=\sin(\sin(\sin(\sqrt{x^2+1})))
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
y'=\cos(\sin(\sin(\sqrt{x^2+1})))\cos(\sin \sqrt{x^2+1})\cos (\sqrt {x^2+1})\dfrac{x}{\sqrt {x^2+1}} 
\end{array}
$$

</div>


### T7

<div class='cbox'>

$$
\begin{array}{l}
y=\arctan \dfrac{2x}{1-x^2} 
\end{array}
$$

</div>

<div class='pbox'>

arctan'=1/1+x^2

$$
\begin{array}{l}
y'=\dfrac{1}{1+(\dfrac{2x}{1-x^2} )^2}\dfrac{2(1-x^2)+4x^2}{(1-x^2)^2}   \\
=\dfrac{2}{(1+x^2)} 
\end{array}
$$

</div>



### T8

<div class='cbox'>

$$
\begin{array}{l}
y=\ln \sqrt{\dfrac{1+\cos x}{1-\cos x} }
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
\sqrt {\dfrac{1+\cos x}{1-\cos x} } \\
=\cot \dfrac{x}{2}  \\
\Rightarrow y=\ln \cot \dfrac{x}{2} \\
\Rightarrow y'=-\tan \dfrac{x}{2}  \csc^2 \dfrac{x}{2} \cdot \dfrac{1}{2}  \\
=-\dfrac{1}{2\sin \frac{x}{2}\cos \frac{x}{2}}  \\
=-\csc x

\end{array}
$$

</div>



### T9

<div class='cbox'>

$$
\begin{array}{l}
y=x^{a^a}+a^{a^x}+a^{x^a}
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
y'=a^ax^{a^a-1}+a^{a^x+x}\ln^2 a+ a^{x^a+1}\ln ax^{a-1}
\end{array}
$$

</div>



### T10

<div class='cbox'>

$$
\begin{array}{l}
y=\sin(f(\sin(x)))
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
y'=\cos(f(\sin(x)))f'(\sin x)\cos x
\end{array}
$$

</div>



### T11

<div class='cbox'>

$$
\begin{array}{l}
y={\left( \dfrac{\sin(f(x))}{x}  \right)} ^{f(f(x))} \\
\end{array}
$$

</div>

<div class='pbox'>

$$
\begin{array}{l}
y=\exp f(f(x)) (\ln \sin(f(x))-\ln x)  \\
={\left( \dfrac{\sin(f(x))}{x}  \right)} ^{f(f(x))} {\left( f'(f(x))f'(x)\ln\dfrac{\sin f(x)}{x} +f(f(x)) {\left( \dfrac{x}{\sin f(x)} \dfrac{xf'x \cos f(x)-\sin f(x)}{x^2}  \right)}  \right)}  \\
={\left( \dfrac{\sin(f(x))}{x}  \right)} ^{f(f(x))} {\left( f'(f(x))f'(x)\ln\dfrac{\sin f(x)}{x} +\dfrac{f(f(x))(xf'x\cos f x-\sin f x}{x\sin f x}   \right)}
\end{array}
$$

</div>













