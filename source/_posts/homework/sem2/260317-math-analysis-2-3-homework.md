---
title: Math Analysis Homework - Sem 2 Week 3
tags:
  - math-analysis
  - homework
  - math
date: 2026-03-17 13:20:32
---

# Math Analysis Homework - Sem 2 Week 3

### T1

<div class="cbox">

**1.** 求下列幂级数的收敛域:
(2) $\sum_{n=1}^\infty \left(1+\frac{1}{n}\right)^{n^2} x^n$;

</div>

<div class="pbox">

$$
\begin{gathered}
R=1/\limsup_{n\to \infty} \sqrt[n]{(1+\dfrac1n)^{n^2}} \\
=1/\limsup_{n\to \infty} (1+\dfrac{1}{n} )^n \\
=\frac1e \\
\text{when } x=\pm\frac1e, \\
\ln [(1+\dfrac{1}{n} )^{n^2}x^n] \\
=\ln [((1+\dfrac{1}{n} )^n\frac1e)^n] \\
=n(n\ln(1+\dfrac1n)-1) \\
\to -\dfrac12 \\
\lim_{n \to \infty} |(1+\dfrac{1}{n} )^{n^2} x^n|=\dfrac{1}{e^\frac12} \ne 0,
\text{not convergent}  \\
\text{thus the convergent range is } (-\dfrac{1}{e} ,\dfrac{1}{e} )
\end{gathered}
$$

</div>

### T2

<div class="cbox">

**1.** 求下列幂级数的收敛域:
(6) $\sum_{n=1}^\infty \left(\frac{a^n}{n} + \frac{b^n}{n^2}\right) x^n, a>0, b>0$;

</div>

<div class="pbox">

$$
\begin{gathered}
R=1/\limsup_n \sqrt[ n ]{ \dfrac{a^n}{n} +\dfrac{b^n}{n^2}  } =\dfrac1{\max(a,b)} \\
\end{gathered}
$$

设通项为$c_n,f(x)=\sum_{n=1}^\infty c_nx^n$

若$a\ge b$:
若$x=\dfrac1a$时有 $\lim_{n \to \infty} \dfrac{c_nx^n}{\dfrac1n}=1$,由比较判别法知发散.

$x=-\dfrac1a$时:

$$
\begin{gathered}
f(x)=\sum _{n = 1} ^{\infty}  c_{2n}x^{2n}+c^{2n+1}x^{2n+1} \\
=\sum _{n = 1} ^{\infty}  (\dfrac{1}{2n} -\dfrac{1}{2n+1}) +\dfrac{b^{2n}}{a^{2n}}(\dfrac{1}{2n} - \dfrac{a}{b(2n+1)^2} ) 
\end{gathered}
$$

其中第一部分收敛,第二部分括号里有界所以也收敛,于是收敛.

若$b>a$,$x=\pm \dfrac1b$:
$$
\begin{gathered}
\lim_{n \to \infty} \dfrac{|\dfrac{a^n}{n} +\dfrac{b^n}{n^2} x^n |}{\dfrac{1}{n^2} } =1 \\
\end{gathered}
$$

由比较判别法知绝对收敛.

故收敛域为:

$$
\begin{gathered}
\begin{cases}
[-\dfrac{1}{b} ,\dfrac{1}{b} ],b>a \\
[-\dfrac{1}{a} ,\dfrac{1}{a} ),a\ge b
\end{cases}

\end{gathered}
$$


</div>

### T3

<div class="cbox">

**1.** 求下列幂级数的收敛域:
(8) $\sum_{n=1}^\infty \frac{n!}{n^n} x^n$;

</div>

<div class="pbox">

$$
\begin{gathered}
\lim_{n \to \infty} \dfrac{c_{n}}{c_{n-1}}=\lim_{n \to \infty}  n\dfrac{(n-1)^{n-1}}{n^n}  =\lim_{n \to \infty} (1-\dfrac{1}{n} )^{n-1}=\frac1e \\
\Rightarrow R=e
\end{gathered}
$$

$x\pm e$时:

$$
\begin{gathered}
\lim_{n \to \infty} \dfrac{n!}{n^n} e^n
=\lim_{n \to \infty} \dfrac{e^n}{n^n} \sqrt{ 2n\pi } (\dfrac{n}{e} )^n=\sqrt{ 2\pi n } \ne 0
\end{gathered}
$$
不收敛.

于是收敛域为$(-e,e)$

</div>

### T4

<div class="cbox">

**2.** 设 $\sum_{n=0}^\infty a_n x^n$ 和 $\sum_{n=0}^\infty b_n x^n$ 的收敛半径分别为 $r_1$ 和 $r_2$, 证明:

(1) $\sum_{n=0}^\infty (a_n + b_n) x^n$ 的收敛半径 $r \ge \min\{r_1, r_2\}$, 且当 $r_1 \neq r_2$ 时, 有 $r = \min\{r_1, r_2\}$; 当 $r_1 = r_2$ 时, $r$ 可能大于 $r_1$;

(2) $\sum_{n=0}^\infty (a_n b_n) x^n$ 的收敛半径 $r \ge r_1 r_2$.

</div>

<div class="pbox">

(1):

$$
\begin{gathered}
R_a=\limsup_{n\to \infty} \sqrt[n]{|a_n|} =\dfrac1{r_1} \\
R_b=\limsup_{n\to \infty} \sqrt[n]{|b_n|} =\dfrac1{r_2} \\
R=\limsup_{n\to \infty} \sqrt[n]{|a_n+b_n|} \le \sqrt[ n ]{ 2\max(|a_n|,|b_n|) } \\
\Rightarrow R \le \max(R_a,R_b) \\
\Rightarrow r \ge \min(r_1,r_2) \\
\text{when } r_1 \ne r_2, \\
\text{assume } r_1 < r_2, \\
R=\limsup_{n\to \infty} \sqrt[n]{|a_n+b_n|}  \\
\ge \limsup_{n\to \infty} \sqrt[n]{|a_n|} =R_a \\
\Rightarrow r \le r_1 \Rightarrow r=r_1 \\
\text{when } r_1=r_2, \\
\text{let  } a_n=1,b_n=-1,r=\infty>r_1=r_2=1 \\
\end{gathered}
$$

(2):

$$
\begin{gathered}
\limsup _{n\to \infty} \sqrt[n]{|a_nb_n|} \le \limsup_{n\to \infty} \sqrt[n]{|a_n|}\cdot \limsup_{n\to \infty} \sqrt[n]{|b_n|} =\dfrac{1}{r_1r_2}  \\
\Rightarrow  r \ge r_1r_2
\end{gathered}
$$

对上极限的不等号,考虑取$a_nb_n$取最大值的子列为$a_{n_k}b_{n_k}$,则显然 $\lim_{k\to \infty} \sqrt[n_k]{|a_{n_k}b_{n_k}|} = \lim_{k\to \infty} \sqrt[n_k]{|a_{n_k}|}\cdot \sqrt[n_k]{|b_{n_k}|} \le \limsup \sqrt[n]{|a_n|}\cdot \limsup \sqrt[n]{|b_n|}$.

</div>

### T5

<div class="cbox">

**3.** 设 $f(x) = \sum_{n=0}^\infty a_n x^n$ 在 $(-r, r)$ 中收敛, 且 $\sum_{n=0}^\infty \frac{a_n}{n+1} r^{n+1}$ 收敛. 证明: 无论 $\sum_{n=0}^\infty a_n x^n$ 在 $x=r$ 处是否收敛, 都有
$$ \int_0^r f(x)dx = \sum_{n=0}^\infty \frac{a_n}{n+1} r^{n+1} $$
并由此证明
$$ \int_0^1 \frac{\ln \frac{1}{1-x}}{x} dx = \sum_{n=1}^\infty \frac{1}{n^2} $$

</div>

<div class="pbox">

(1):

由优级数判别法,$\forall x\in [-l,l]\subset (-r,r)$, 有 

$$
\begin{gathered}
\sum _{n = 0} ^{\infty} a_n|x|^n \le (\sum _{n = 0} ^{\infty} a_nr^n(\dfrac{l}{r} )^n) \\
\end{gathered}
$$

其中因为$a_nr^n$收敛到$0$所以有界,优级数绝对收敛,所以幂级数$f$内闭一致收敛.于是可以逐项积分,得到$\forall r'\in (-r,r)$:

$$
\begin{gathered}
\lim_{r' \to r} \int_0^{r'} f(x)dx = \lim_{r' \to r} \sum_{n=0}^\infty \int_0^{r'} a_n x^n dx = \lim_{r' \to r} \sum_{n=0}^\infty \frac{a_n}{n+1} (r')^{n+1}
\end{gathered}
$$

此时已知右边的级数在闭区间上收敛所以一致收敛所以连续,于是即

$$
\begin{gathered}
\int_0^r f(x)dx = \sum_{n=0}^\infty \frac{a_n}{n+1} r^{n+1}
\end{gathered}
$$

(2):

$$
\begin{gathered}
\int_0^1 \dfrac{\ln \frac{1}{1-x}}{x} dx  \\
=\int_0^1 \sum _{n = 0} ^{\infty}  \dfrac{x^n}{n+1} dx \\
\end{gathered}
$$

注意到该级数的收敛于为$(-1,1)$,而我们知道 $\sum_n \dfrac1{n^2}$收敛,于是

$$
\begin{gathered}
=\sum _{n = 0} ^{\infty}  \dfrac{1}{n+1} \int_0^1 x^n dx \\
=\sum _{n = 0} ^{\infty}  \dfrac{1}{(n+1)^2} \\
=\sum _{n = 1} ^{\infty}  \dfrac{1}{n^2}
\end{gathered}
$$


</div>

### T6

<div class="cbox">

**4.** 求下列幂级数的和函数, 并指出等式成立的范围:
(6) $f(x)=\sum_{n=1}^\infty \frac{2n+1}{n!} x^{2n}$;

</div>

<div class="pbox">

收敛半径为

$$
\begin{gathered}
R=\dfrac{1}{\limsup_{n\to \infty} \sqrt[ n ]{ \dfrac{2n+1}{n!} } } =\infty
\end{gathered}
$$

由T5,因为$\forall X\in R$,级数:

$$
\begin{gathered}
\sum _{n = 1} ^{\infty}  \dfrac{\dfrac{2n+1}{n!} }{2n+1} x^{2n+1}=xe^{x^2}-x
\end{gathered}
$$

收敛,所以

$$
\begin{gathered}
\int_0^X f(x)dx \\
=\int_0^X \sum_{n=1}^\infty \frac{2n+1}{n!} x^{2n} dx \\
=\sum_{n=1}^\infty \frac{2n+1}{n!} \int_0^X x^{2n} dx \\
=\sum _{n = 1} ^{\infty}  \dfrac{X^{2n+1}}{n!}  \\
=Xe^{X^2}-X
\end{gathered}
$$

于是

$$
\begin{gathered}
f(x)=\dfrac{d}{dx} \int_0^X f(x)dx \\
        =\dfrac{d}{dx} (Xe^{X^2}-X) \\
=e^{X^2}+2X^2e^{X^2}-1 \\
\end{gathered}
$$

对任意$x$成立.

</div>

### T7

<div class="cbox">

**4.** 求下列幂级数的和函数, 并指出等式成立的范围:
(9) $f(x)=\sum_{n=1}^\infty (-1)^{n-1} n^2 x^n$;

</div>

<div class="pbox">

$$
\begin{gathered}
R=1/\limsup_{n\to \infty} \sqrt[n]{n^2} =1 \\
\forall X\in (-1,1),
\int_0^X \dfrac1x fdx=\sum _{n = 1} ^{\infty} \int_0^x (-1)^{n-1} n^2 x^{n-1} dx \\
=\sum _{n = 1} ^{\infty} (-1)^{n-1} n X^n \\
\int_0^Y \dfrac1X(\int_0^X \dfrac{1}{x} fdx) dX \\
=\sum _{n = 1} ^{\infty}  (-1)^{n-1}Y^{n} \\
=\dfrac{Y}{1+Y}\\
\end{gathered}
$$

所以

$$
\begin{gathered}
\int \dfrac1x(\int \dfrac1x f)=\dfrac{x}{1+x}\\
\Rightarrow f(x)=\dfrac{x(1-x)}{(1+x)^3} 
\end{gathered}
$$

当$x\in (-1,1)$时成立.

</div>

### T8

<div class="cbox">

**5.** 利用幂级数求下列级数的和:
(2) $\sum_{n=2}^\infty \frac{1}{(n^2-1)2^n}$;

</div>

<div class="pbox">

设

$$
\begin{gathered}
f(x)=\sum _{n = 2} ^{\infty}  \dfrac{1}{(n+1)(n-1   )} x^{n-1} \\
=\sum _{n = 2} ^{\infty}  \dfrac{1}{2} (\dfrac{1}{n-1} -\dfrac{1}{n+1} ) x^{n-1} \\
=\dfrac{1}{2} \sum _{n = 1} ^{\infty}  \dfrac{x^n}{n}-\dfrac{1}{2} x^{-2}\sum _{n = 3} ^{\infty}  \dfrac{x^n}{n}  \\
=-\dfrac{1}{2} \ln (1-x)+\dfrac{1}{2} x^{-2}(\ln (1-x)+\dfrac{x^2}{2} +\dfrac{x}{1} )
\end{gathered}
$$

其中$\ln (1-x)$的收敛域是$(-1,1)$.

于是

$$
\begin{gathered}
Ans=\dfrac12f(\dfrac{1}{2} )=\dfrac{5}{8} -\dfrac{3}{4} \ln 2
\end{gathered}
$$

</div>

### T9

<div class="cbox">

**5.** 利用幂级数求下列级数的和:
(3) $\sum_{n=1}^\infty \frac{n(n+2)}{2^{2(n+1)}}$;

</div>

<div class="pbox">

$$
\begin{gathered}
\text{let } f(x)=\sum _{n = 2} ^{\infty}  (n-1)(n+1)x^n \\
\end{gathered}
$$

由比值法易知收敛半径为$1$,当$x<\dfrac12$时一致收敛可逐项积分:

$$
\begin{gathered}
\int \dfrac1{x^3} \int f(x)  =\sum _{n = 2} ^{\infty}  x^{n-1}=\dfrac{1}{1-x}-1  \\
\Rightarrow f(x)=\dfrac{3-x}{(1-x)^3}x^2  \\
Ans=f(\dfrac{1}{4} )=\dfrac{11}{27} 
\end{gathered}
$$

</div>

### T10

<div class="cbox">

**6.** 证明:
(1) $y = \sum_{n=0}^\infty \frac{x^{4n}}{(4n)!}$ 满足 $y^{(4)} = y$;

(2) $y = \sum_{n=0}^\infty \frac{x^n}{(n!)^2}$ 满足 $xy'' + y' - y = 0$.

</div>

<div class="pbox">

(1):

对求导$i$次后的级数,$R_i=1/\lim_{n \to \infty}\dfrac{(n-i-1)!}{(n-i)!}=\infty$.收敛,内闭一致收敛,可以逐项求导,得到:

$$
\begin{gathered}
y^{(4)}=\sum _{n = 0} ^{\infty}  \dfrac{d^4}{ {dx}^4} \dfrac{x^{4n}}{(4n)!}=y 
\end{gathered}
$$

(2):

$R=1/\lim_{n \to \infty} \dfrac{((n-1)!)^2}{(n!)^2} =\infty$,收敛,一致收敛,可逐项求导.且

规定$0!=1,(-n)!=0$

$$
\begin{gathered}
xy''+y'-y \\
\sum _{n = 2} ^{\infty}  -\dfrac{x^n}{(n!)^2} +\dfrac{x^{n-1}}{n!(n-1)!} +x\dfrac{x^{n-2}}{n!(n-2)!} \\
=-\sum _{n = 0} ^{\infty}  \dfrac{x^n}{(n!)^2}  +\sum _{n = 0} ^{\infty}  x^{n-1}\dfrac{1}{((n-1)!)^2}  \\
=0
\end{gathered}
$$

</div>

### T11

<div class="cbox">

**7.** 设 $f(x) = \sum_{n=0}^\infty a_n x^n$ 的收敛半径 $r = +\infty$. 令 $f_n(x) = \sum_{k=0}^n a_k x^k$. 证明: $\{f[f_n(x)]\}$ 在 $[a, b]$ 上一致收敛于 $f[f(x)]$.

</div>

<div class="pbox">

因为$f_n(x)$每项连续,$f_n$一致收敛到$f$,于是$f$连续.所以$f$在$[a,b]$一致连续且有界.设界为$[A,B]$.

又有$f$在$[A,B]$上连续而一致连续.满足$\forall \epsilon_1>0,\exists \delta>0,\forall |x-y|<\delta,|f(x)-f(y)|<\epsilon_1$.

又因为$f(x)$一致收敛到$f_n(x)$,所以$\forall \epsilon_2>0,\exists N,\forall n>N,|f(x)-f_n(x)|<\epsilon_2$.

于是取$\epsilon_1=\epsilon,\epsilon_2=\delta$:

$$
\begin{gathered}
n>N \Rightarrow |f_n(x)-f(x)|<\delta \Rightarrow |f(f_n(x))-f(f(x))|<\epsilon
\end{gathered}
$$

得证.

</div>

### T12

<div class="cbox">

**8.** 设定项级数 $\sum_{n=0}^\infty a_n$ 发散, 且 $\lim_{n\to\infty} \frac{a_n}{a_0 + a_1 + \dots + a_n} = 0$. 证明: 幂级数 $\sum_{n=0}^\infty a_n x^n$ 的收敛半径 $r=1$.

</div>

<div class="pbox">

$$
\begin{gathered}
\sum _{n = 0} ^{\infty}  a_n 1^n=\sum _{n = 0} ^{\infty}  a_n=\infty
\end{gathered}
$$

故由Abel收敛定理知收敛半径$R\le 1$.

$\forall x\in (-1,1),x<1$:

设$S_n$为$a_n$部分和,则易知 $\lim_{n \to \infty} \dfrac{S_{n-1}}{S_n}=1$

$$
\begin{gathered}
\sum _{n = 0} ^{\infty}  a_nx^n \\
=a_0+\sum _{n = 1} ^{\infty}  (S_n-S_{n-1})x^n \\
=\sum _{n = 0} ^{\infty}  S_n(x^n-x^{n+1})+S_nx^n
\end{gathered}
$$

最后一项显然极限为$0$,对前面的部分

使用比值:

$$
\begin{gathered}
\lim_{n \to \infty} \dfrac{S_n}{S_{n-1}} \dfrac{x^n-x^{n+1}}{x^{n-1}-x^n}  \\
=1\cdot x<1
\end{gathered}
$$

故收敛.

故收敛域为$(-1,1)$,收敛半径为$1$.

</div>