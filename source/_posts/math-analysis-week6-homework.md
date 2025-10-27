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
