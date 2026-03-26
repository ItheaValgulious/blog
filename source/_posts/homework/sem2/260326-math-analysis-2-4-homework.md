---
title: Math Analysis Homework - Sem 2 Week 4
tags:
  - math-analysis
  - math
  - homework
date: 2026-03-26 10:31:25
---

# Math Analysis Homework - Sem 2 Week 4

### T1

<div class="cbox">

**1.** 将下列函数在指定点展开成泰勒级数：
(3) $\frac{1}{x^2}, x = 1$;

</div>

<div class="pbox">

$$
\begin{gathered}
f(x)=x^{-2}  \\
f^{(n)}= (-1)^n (n+1)! x^{-2-n}
\Rightarrow  \\
f(x)=\sum _{i = 0} ^{\infty}  \dfrac{f^{(i)}(1)}{i!} (x-1)^i \\
=1+\sum _{i = 1} ^{\infty}(-1)^i(i+1)(x-1)^i
\end{gathered}
$$

余项为

$$
\begin{gathered}
R_n(x)=(-1)^{n}(n+1)(\theta x+1-\theta)^{-2-n} (x-1)^n \\
=(-1)^n (n+1)  (\dfrac{x-1}{\theta x+1-\theta} )^n \dfrac{1}{(\theta x+1-\theta)^2} 
\end{gathered}
$$

则$|x-1|<1$时收敛.$x=2,0$通项极限不为$0$显然发散.

</div>

### T2

<div class="cbox">

**1.** 将下列函数在指定点展开成泰勒级数：
(5) $\ln (1 + x + x^2 + x^3), x = 0$;

</div>

<div class="pbox">

$$
\begin{gathered}
f(x)=\ln(\dfrac{1-x^4}{1-x} )=\ln(1-x^4)-\ln(1-x) \\
=\sum _{i = 1} ^{\infty} \dfrac{x^i}{i} -\sum _{i = 1} ^{\infty}  \dfrac{x^{4i}}{i}  \\
=\sum _{i = 1} ^{\infty}  a_ix^i,a_i=\begin{cases}
\dfrac{1}{i} -\dfrac{1}{4i} ,i=4k,k\in \{ Z \}  \\
\dfrac{1}{i} ,\text{otherwise}
\end{cases}
\end{gathered}
$$

两个$\ln$的级数收敛域均为$(-1,1)$,故收敛于为$(-1,1)$

</div>

### T3

<div class="cbox">

**3.** 求函数 $f(x) = \arctan \frac{2x}{1-x^2}$ 在 $x=0$ 处的幂级数展开式，并求 $\sum_{n=0}^{\infty} \frac{(-1)^n}{2n+1}$ 的值.

</div>

<div class="pbox">

$$
\begin{gathered}
f'(x)=\dfrac{2}{1+x^2}  \\
=\sum _{i = 0} ^{\infty} 2\cdot (-1)^ix^{2i} \\
\Rightarrow f(x)=\int f'(x)=\sum _{i = 0} ^{\infty}  \dfrac{2\cdot (-1)^i x^{2i+1}}{2i+1} ,x\in (-1,1)
\end{gathered}
$$

由莱布尼茨判别法知级数在$x=1$时收敛,由阿贝尔定理知级数的和函数$s(x)$连续,故所求即 $s(1)=\lim_{x \to 1} s(x)=\lim_{x \to 1} f(x)=\dfrac\pi2$

</div>

### T4

<div class="cbox">

**4.** 设函数 $f(x) = \frac{1}{1-x-x^2}$，记 $a_n = \frac{f^{(n)}(0)}{n!}$. 证明：
- (1) 级数 $\sum_{n=0}^{\infty} \frac{1}{a_n}$ 收敛；
- (2) $a_0 = a_1 = 1, a_{n+2} = a_{n+1} + a_n, n=0, 1, 2, \cdots$；
- (3) 级数 $\sum_{n=0}^{\infty} \frac{a_{n+1}}{a_n a_{n+2}}$ 收敛，并求其和.

</div>

<div class="pbox">

计算得$a_0=a_1=1$.

$$
\begin{gathered}
f(x)(1-x-x^2)=1 \\
\Rightarrow \forall n\ge 2,0=(f(x)(1-x-x^2))^{(n)}|_{x=0} \\
=\sum _{i = 0} ^{n}  f^{(n-i)}(0)((1-x-x^2)^{(i)}|_{x=0})\binom ni \\
=f^{(n)}(0)-nf^{n-1}(0)+\dfrac{n(n-1)}{2} \cdot -2 f^{n-2}(0) \\
=n!a_n-n!a_{n-1}-n!(a_{n-2}) \\
=0 \\
\Rightarrow a_n=a_{n-1}+a_{n-2}
\end{gathered}
$$

故$a_n=a_{n-1}+a_{n-2}>2a_{n-2}$,则$\dfrac1{a_n}<\dfrac12\dfrac1{a_{n-2}}$,由比较判别法知奇数项,偶数项均绝对收敛,故(1)中级数收敛.

(3):

注意到:

$$
\begin{gathered}
S_n=\sum _{n = 0} ^{N}  \dfrac{a_{n+1}}{a_na_{n+2}}  \\
=\sum _{n = 0} ^{N}  \dfrac{1}{a_n} -\dfrac{1}{a_{n+2}}  \\
=2-\dfrac{1}{a_{N+1}} -\dfrac{1}{a_{N+2}}  \\
\Rightarrow S=\lim_{n \to \infty} S_n =2
\end{gathered}
$$

</div>

### T5

<div class="cbox">

**5.** (1) 证明：函数项级数
$$\sin x + \sum_{n=1}^{\infty} \frac{(2n-1)!! \sin^{2n+1} x}{(2n)!! (2n+1)}$$
在区间 $\left[0, \frac{\pi}{2}\right]$ 上一致收敛于和函数 $x$.

(2) 证明 $\sum_{n=1}^{\infty} \frac{1}{(2n-1)^2} = \frac{\pi^2}{8}$ 和 $\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}$.

</div>

<div class="pbox">

$$
\begin{gathered}
f(x)=\arcsin(x) \\
\Rightarrow f'(x)=\dfrac{1}{\sqrt{ 1-x^2 } } \\
=(1-x^2)^{-\frac12} \\
=1+\sum _{n = 1} ^{\infty} \dfrac{(2n-1)!!}{(2n)!!} x^{2n},\forall x\in[0,1)
\end{gathered}
$$

逐项积分得:

$$
\begin{gathered}
\arcsin(x)=x+\sum _{n = 1} ^{\infty}  \dfrac{(2n-1)!!}{(2n)!!(2n+1)} x^{2n+1},\forall x\in [0,1]
\end{gathered}
$$

且为一致收敛.

故原式一致收敛到$\arcsin(\sin x)=x$

(2):

注意到

$$
\begin{gathered}
\int_0^{\frac\pi2} \sin^{2n+1}(x)=\dfrac{(2n)!!}{(2n+1)!!}
\end{gathered}
$$

于是

$$
\begin{gathered}
\int_0^{\frac\pi2} \arcsin(\sin x)=\sum _{n = 0} ^{\infty}  \dfrac{(2n-1)!!}{(2n)!!(2n+1)} \int_0^{\frac\pi2}\sin^{2n+1}dx \\
=\sum _{n = 0} ^{\infty}  \dfrac{(2n-1)!!}{(2n)!!(2n+1)}\dfrac{(2n)!!}{(2n+1)!!} \\
=\sum _{n = 0} ^{\infty}  \dfrac{1}{(2n+1)^2}  \\
=\int_0^{\frac\pi2}xdx \\
=\dfrac{\pi^2}8
\end{gathered}
$$

于是显然有:

$$
\begin{gathered}
\sum _{n = 1} ^{\infty}  \dfrac{1}{n^2}-\sum _{i = 1} ^{\infty}  \dfrac{1}{(2n)^2}=\dfrac{\pi^2}{8}  \\
\Rightarrow \sum _{n = 1} ^{\infty}  \dfrac{1}{n^2} =\dfrac{\pi^2}{6} 
\end{gathered}
$$

</div>

### T6

<div class="cbox">

**7.** 利用斯特林公式解决下列问题：
- (1) 求极限 $\lim_{n \to \infty} \sqrt[n^2]{n!}$；
- (2) 证明：当 $n \to \infty$ 时，$\ln(n!) \sim n \ln n$；
- (3) 判断级数 $\sum_{n=2}^{\infty} \frac{1}{\ln(n!)}$ 的敛散性.

</div>

<div class="pbox">

(1):

$$
\begin{gathered}
\lim_{n \to \infty} \sqrt[ n^2 ]{ n! }  \\
=\lim_{n \to \infty} \exp \dfrac{1}{n^2} \ln(n!) \\
=\lim_{n \to \infty} \exp \dfrac{1}{n^2} \ln (\sqrt{2n\pi}(\dfrac{n}{e})^n e^{\frac{\theta_n}{12n}} ) \\
=\lim_{n \to \infty} \exp\dfrac{1}{n} (\ln n-1) \\
=e
\end{gathered}
$$

(2):

$$
\begin{gathered}
\lim_{n \to \infty} \dfrac{\ln n!}{n\ln n}  \\
=\lim_{n \to \infty} \dfrac{\ln (\sqrt{2n\pi}(\dfrac{n}{e})^n e^{\frac{\theta_n}{12n}})}{n\ln n}  \\
=\lim_{n \to \infty} \dfrac{n\ln(n-1)+\ln(\sqrt{ 2n\pi } )+\frac{\theta_n}{12n}}{n\ln n}=1 
\end{gathered}
$$

(3):

$\sum _{n = 2} ^{\infty} \dfrac{1}{\ln(n!)}$和$\sum _{n = 2} ^{\infty}  \dfrac{1}{n\ln n}$同敛散,从而与$\int_2^\infty \dfrac1{x\ln x}dx$同敛散,故发散.

</div>