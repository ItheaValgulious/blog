---
title: Math Analysis Homework - Week 8
tags: [math,math-analysis,homework]
---

# Math Analysis Homework - Week 8

## Class 1

### T1

<div class='cbox'>

$$
\begin{gathered}
\int \dfrac{x+1}{x^3+2x^2-x-2} dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=\int \dfrac{x+1}{(x+1)(x-1)(x+2)}dx  \\
=\int \dfrac{1}{3} (\dfrac{1}{x-1} -\dfrac{1}{x+2}) dx \\
=\dfrac{1}{3} \ln \vert \dfrac{x-1}{x+2} \vert  +C
\end{gathered}
$$

</div>



### T2

<div class='cbox'>

$$
\begin{gathered}
\int \dfrac{x-1}{(x^2+2x+3)^2} dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\text{let } u=x^2+2x+3 \\
ans=\dfrac{1}{2} \int \dfrac{du}{u^2} -2\int \dfrac{dx}{(x^2+2x+3)^2} \\
=-\dfrac{1}{2(x^2+2x+3)} -2\int \dfrac{dx}{((x+1)^2+{\sqrt 2}^2)^2}    \\
\text{let } x+1=\sqrt 2\tan v \\
ans=-\dfrac{1}{2(x^2+2x+3)} -2\int \dfrac{\sqrt 2 \sec^2 v}{4\sec^4 v}dv \\
=-\dfrac{1}{2(x^2+2x+3)} -\dfrac{\sqrt 2}{2}\int \dfrac{1+\cos 2v}{2}  dv \\
=-\dfrac{1}{2(x^2+2x+3)} -\dfrac{\sqrt 2}{4} \arctan\dfrac{x+1}{\sqrt 2} -\dfrac{1}{2}\dfrac{x+1}{x^2+2x+3}  +C
\end{gathered}
$$

</div>



### T3

<div class='cbox'>

$$
\begin{gathered}
\int \dfrac{x^4}{x^4+5x^2+4} dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=\int (1-\dfrac{5x^2+4}{(x^2+4)(x^2+1)} )dx \\
=\int (1-(\dfrac{16}{3(x^2+4)}-\dfrac{1}{3(x^2+1)} ))dx \\
=x-\dfrac{8}{3} \arctan\dfrac{x}{2} -\dfrac{1}{3} \arctan x+C
\end{gathered}
$$

</div>



### T4

<div class='cbox'>

$$
\begin{gathered}
\int \dfrac{1}{\sin x+\tan x} dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=\dfrac{1}{4} \int \dfrac{(1+\tan^2(\dfrac{x}{2}))(1-\tan^2(\dfrac{x}{2}))}{\tan \dfrac{x}{2} } dx \\
=\dfrac{1}{4} \int (\cot \dfrac{x}{2} -\tan^3\dfrac{x}{2} )dx \\
\int \tan^3 xdx \\
=\int \sec^2 x\tan xdx-\int \tan xdx \\
=\dfrac{\tan^2 x}{2} -\ln \sec x+C \\
Ans=\dfrac{1}{2} \ln \sin \dfrac{x}{2} -\dfrac{\tan^2 \dfrac{x}{2} }{4} +\dfrac{1}{2} \ln \sec \dfrac{x}{2} +C
\end{gathered}
$$

</div>



### T5

<div class='cbox'>

$$
\begin{gathered}
\int \dfrac{\sin 2x}{\sin^4 x+\cos^4 x} dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=\int \dfrac{\sin 2x}{(\sin^2 x+\cos^2 x)^2-\dfrac{1}{2} \sin^2 2x} dx \\
=\int \dfrac{\sin 2x}{\dfrac{1}{2} +\dfrac{1}{2} \cos^2 2x} dx \\
=-\int \dfrac{d\cos 2x}{1+\cos^2 2x} dx \\
=-\arctan \cos 2x+C
\end{gathered}
$$

</div>



### T6

<div class='cbox'>

$$
\begin{gathered}
\int \dfrac{1}{1+\sqrt[3]{1+x}} dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\text{let } t=\sqrt[ 3 ]{ 1+x },x=t^3-1 \\
ans=\int \dfrac{3t^2dt}{t+1}  \\
=3\int (t-1+\dfrac{1}{t+1}) dt \\
=3(\dfrac{t^2}{2}-t+\ln(t+1))+C \\
=\dfrac{3}{2} (1+x)^{\frac23}-3(1+x)^{\frac13}+3\ln(1+\sqrt[ 3 ]{ 1+x } )+C
\end{gathered}
$$

</div>



### T7

<div class='cbox'>

$$
\begin{gathered}
\int \dfrac{1}{x\sqrt{1+x^2}} dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\text{let } x=\tan t \\
ans=\int \dfrac{\sec^2 t}{\tan t \sec t} dt \\
=\int \csc t dt \\
=\ln \vert \csc t-\cot t \vert +C \\
=\ln \vert \dfrac{\sqrt{ x^2+1 } -1}{x}  \vert +C
\end{gathered}
$$

</div>



### T8

<div class='cbox'>

$$
\begin{gathered}
\int \dfrac{1}{x+\sqrt{x^2+x+1}} dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\text{let } \sqrt{x^2+x+1}=x+t \\
x^2+x+1=x^2+2xt+t^2 \\
x=\dfrac{t^2-1}{1-2t}  \\
\Rightarrow ans=\int \dfrac{1}{2\dfrac{t^2-1}{1-2t} +t} \dfrac{2t(1-2t)+2(t^2-1)}{(1-2t)^2} dt \\
=\int \dfrac{t^2-t+1}{(t-2)(t-\dfrac{1}{2} )} dt \\
=\int (1+\dfrac{1}{2} (\dfrac{4}{t-2} -\dfrac{1}{t-\frac12} ))dt \\
=t+2\ln(t-2)-\dfrac{1}{2} \ln (t-\dfrac{1}{2} )+C \\
=\sqrt{x^2+x+1}-x+2\ln(\sqrt{x^2+x+1}-x-2) \\
-\dfrac{1}{2} \ln(\sqrt{x^2+x+1}-x-\dfrac{1}{2} )+C
\end{gathered}
$$

</div>



### T9

<div class='cbox'>

$$
\begin{gathered}
\int \dfrac{1}{(1+e^x)^2}dx 
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\text{let }t=e^x \\
=\int \dfrac{1}{t(1+t)^2}dt \\
=\int (\dfrac{1}{t} -\dfrac{1}{(1+t)^2} -\dfrac{1}{1+t}) dx \\
=\ln \dfrac{t}{t+1} +\dfrac{1}{1+t} +C \\
=\ln \dfrac{e^x}{1+e^x} +\dfrac{1}{1+e^x} +C
\end{gathered}
$$

</div>



### T10

<div class='cbox'>

$$
\begin{gathered}
\int x\ln\dfrac{1+x}{1-x} dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=\int ((1+x)\ln(1+x)-\ln(1+x)+(1-x)\ln(1-x)-\ln(1-x))dx \\
\int x\ln xdx=\dfrac{x^2\ln x}{2} -\dfrac{x^2}{4} +C \\
\int \ln xdx=x\ln x-x+C \\
\Rightarrow ans=\dfrac{(1+x)^2}{4} (2\ln (1+x)-1)-(1+x)\ln(1+x)+(1+x) \\
-\dfrac{(1-x)^2}{4} (2\ln(1-x)-1)+(1-x)\ln(1-x)-(1-x) +C\\
=\dfrac{x^2-1}{2} \ln\dfrac{1+x}{1-x} +x+C
\end{gathered}
$$

</div>



### T11

<div class='cbox'>

$$
\begin{gathered}
\int \arctan(1+\sqrt x)dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=x\arctan(1+\sqrt x)-\int x\dfrac{1}{2\sqrt x(1+(\sqrt x+1)^2)} dx \\
\text{let } t=\sqrt x \\
ans=x\arctan(1+\sqrt x)-\int \dfrac{t^2dt}{1+(1+t)^2}  \\
=x\arctan(1+\sqrt x)-\int (dt-\dfrac{d(t+1)^2}{1+(1+t)^2} ) \\
=x\arctan(1+\sqrt x)-t+\ln(1+(1+t)^2)+C \\
=x\arctan(1+\sqrt x)-\sqrt x+\ln(1+(1+\sqrt x)^2)+C
\end{gathered}
$$

</div>



### 12

<div class='cbox'>

$$
\begin{gathered}
\int \dfrac{x\sec^2 x}{(1+\tan x)^2} dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\int \dfrac{\sec^2x}{(1+\tan x)^2} dx \\
=\int \dfrac{d\tan x}{(1+\tan x)^2} \\
-\dfrac{1}{1+\tan x} +C \\
ans=-\dfrac{x}{1+\tan x} +\int \dfrac{dx}{1+\tan x}  \\
\int \dfrac{dx}{1+\tan x}  \\
=\int \dfrac{\cos x}{\cos x+\sin x} dx \\
=\dfrac{1}{2} \int \dfrac{(\cos x+\sin x)dx+d(\cos x+\sin x)}{\cos x+\sin x}  \\
=\dfrac{1}{2} \ln(\cos x+\sin x)+\dfrac{1}{2} x+C \\
\Rightarrow ans=-\dfrac{x}{1+\tan x} +\dfrac{1}{2} \ln(\cos x+\sin x)+\dfrac{1}{2} x+C
\end{gathered}
$$

</div>



### T13

<div class='cbox'>

$$
\begin{gathered}
\int \dfrac{x^2}{1+x^2} \arctan xdx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
\text{let }x=\tan t \\
ans=\int t\tan^2 tdt \\
\int \tan^2 dt=\int (\sec^2 t-1)dt \\
=\tan t-t+C \\
ans=t(\tan t-t)-\int (\tan t-t )dt \\
=t\tan t-\ln \sec t-\dfrac{t^2}{2} +C \\
=x\arctan x-\ln \sqrt{t^2+1}-\dfrac{1}{2} \arctan^2(t)+C
\end{gathered}
$$

</div>



### T14

<div class='cbox'>

$$
\begin{gathered}
\int  \dfrac{x+\sin x}{1+\cos x} dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
=\int {\left( \tan\dfrac{x}{2} +\dfrac{x}{1+\dfrac{1-\tan^2 \dfrac{x}{2}}{1+\tan^2 \dfrac{x}{2} }  }  \right)}  dx \\
=\int \tan\dfrac{x}{2} +\dfrac{x}{2} +\dfrac{\tan^2 \dfrac{x}{2} x}{2} dx \\
\text{let }  u=\dfrac{x}{2}  \\

ans=2\int (\tan u+u+u\tan^2 u )du \\
=2 {\left( \dfrac{x}{2} \tan \dfrac{x}{2} \right)} +C \\
=x\tan \dfrac{x}{2} +C
\end{gathered}
$$

</div>



### T15

<div class='cbox'>

$$
\begin{gathered}
f(x^2-1)=\ln \dfrac{x^2}{x^2-2} ,f(\phi(x))=\ln x \\
\text{calc } \int \phi(x)dx
\end{gathered}
$$

</div>

<div class='pbox'>

$$
\begin{gathered}
f(x)=\ln \dfrac{x+1}{x-1} ,x\ge -1 \\
f(\phi (x))=\ln x \\
\Leftrightarrow \dfrac{\phi(x)+1}{\phi(x)-1} =x,\phi (x)=\dfrac{x+1}{x-1}  \\
ans=\int \dfrac{x+1}{x-1} dx \\
=\int (1+\dfrac{2}{x-1}) dx \\
=x+2\ln(x-1)+C
\end{gathered}
$$

</div>




