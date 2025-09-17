---
title: Linea Algebra Homework - Class 1
tags:
  - linear-algebra
  - homework
date: 2025-09-15 20:33:30
---


# Linear Algebra Class1 Homework


#### T2

<div class='cbox'>

Going around a triangle from $(0,0)$ to $(5,0)$ to $(0,12)$ to $(0,0)$, what are those three vectors $\boldsymbol{u}, \boldsymbol{v}, \boldsymbol{w}$? What is $\boldsymbol{u}+\boldsymbol{v}+\boldsymbol{w}$? What are their lengths $\|\boldsymbol{u}\|$, $\|\boldsymbol{v}\|$, and $\|\boldsymbol{w}\|$? The length squared of a vector $\boldsymbol{u} = (u_1, u_2)$ is $\|\boldsymbol{u}\|^2 = u_1^2 + u_2^2$.

</div>

<div class='pbox'>

$$
\begin{array}{c}
\begin{cases}
u=\begin{bmatrix}
5\\
0\\
\end{bmatrix}\\
v=\begin{bmatrix}
-5\\
12\\
\end{bmatrix}\\
w=\begin{bmatrix}
0\\
-12\\
\end{bmatrix}
\end{cases}\\
u+v+w=\boldsymbol{0}\\
\vert\vert u \vert\vert =5\\
\vert\vert v \vert\vert =13\\
\vert\vert w \vert\vert =12\\

\end{array}
$$

</div>





#### T3

<div class='cbox'>

Describe geometrically (line, plane, or all of $\mathbf{R}^3$) all linear combinations of
- (a) $\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$ and $\begin{bmatrix} 3 \\ 6 \\ 9 \end{bmatrix}$
- (b) $\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}$ and $\begin{bmatrix} 0 \\ 2 \\ 3 \end{bmatrix}$
- (c) $\begin{bmatrix} 2 \\ 0 \\ 0 \end{bmatrix}$ and $\begin{bmatrix} 0 \\ 2 \\ 2 \end{bmatrix}$ and $\begin{bmatrix} 2 \\ 2 \\ 3 \end{bmatrix}$

</div>

<div class='pbox'>

##### (a):

a line with direction vector $\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$

##### (b):

a plane through the origin

##### (c):

all the 3d space

</div>


#### T5

<div class='cbox'>

If $\boldsymbol{v}+\boldsymbol{w} = \begin{bmatrix} 5 \\ 1 \end{bmatrix}$ and $\boldsymbol{v}-\boldsymbol{w} = \begin{bmatrix} 1 \\ 5 \end{bmatrix}$, compute and draw the vectors $\boldsymbol{v}$ and $\boldsymbol{w}$.

</div>

<div class='pbox'>

$$
\begin{array}{c}
v=\begin{bmatrix} 3 \\ 3 \end{bmatrix}\\
w=\begin{bmatrix} 2 \\ -2 \end{bmatrix}\\
\end{array}
$$

</div>





#### T7

<div class='cbox'>

Compute $\boldsymbol{u}+\boldsymbol{v}+\boldsymbol{w}$ and $2\boldsymbol{u}+2\boldsymbol{v}+\boldsymbol{w}$. How do you know $\boldsymbol{u}, \boldsymbol{v}, \boldsymbol{w}$ lie in a plane?
$$ \boldsymbol{u} = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} \quad \boldsymbol{v} = \begin{bmatrix} -3 \\ 1 \\ -2 \end{bmatrix} \quad \boldsymbol{w} = \begin{bmatrix} 2 \\ -3 \\ -1 \end{bmatrix} $$
These lie in a plane because $\boldsymbol{w} = c\boldsymbol{u} + d\boldsymbol{v}$. Find $c$ and $d$.

</div>

<div class='pbox'>

$$
\begin{array}{c}
u+v+w=0\\
2u+2v+w=\begin{bmatrix}
-2\\-3\\-1
\end{bmatrix}
\\
\begin{cases}
c=-1\\
d=-1
\end{cases}


\end{array}
$$

</div>



#### T11

<div class='cbox'>

If three corners of a parallelogram are $(1,1)$, $(4,2)$, and $(1,3)$, what are all three of the possible fourth corners? Draw those three parallelograms.

</div>

<div class='pbox'>

$(4,0),(4,4),(-2,2)$

a triangle with another three outer vertices

</div>



#### T13

<div class='cbox'>

**Review Question.** In xyz space, where is the plane of all linear combinations of $\boldsymbol{i} = (1,0,0)$ and $\boldsymbol{i}+\boldsymbol{j} = (1,1,0)$?

</div>

<div class='pbox'>

equal to the linear combination of i and j($j=(0,1,0)$).

so it's the plane xOy

</div>



#### T17

<div class='cbox'>

What combination $c\begin{bmatrix} 1 \\ 2 \end{bmatrix} + d\begin{bmatrix} 3 \\ 1 \end{bmatrix}$ produces $\begin{bmatrix} 14 \\ 8 \end{bmatrix}$? Express this question as two equations for the coefficients c and d in the linear combination.

</div>

<div class='pbox'>

$$
\begin{cases}
    14=1c+3d\\
    8=2c+1d
\end{cases}
 \Rightarrow 
\begin{cases}
    c=2\\
    d=4
\end{cases}
$$

</div>

#### T19

<div class='cbox'>

Restricted only by $c \ge 0$ and $d \ge 0$ draw the "cone" of all combinations $c\boldsymbol{u}+d\boldsymbol{v}$.

a angle that has the origin as the vertex(we should paint all the points between u and v black)

</div>

#### T23

<div class='cbox'>

If you look at all combinations of those $\boldsymbol{u}, \boldsymbol{v}, \boldsymbol{w}$, is there any vector that can't be produced from $c\boldsymbol{u} + d\boldsymbol{v} + e\boldsymbol{w}$? Different answer if $\boldsymbol{u}, \boldsymbol{v}, \boldsymbol{w}$ are all in \_\_\_\_\_\_.

</div>

<div class='pbox'>

(1):no.

(2):a plane

</div>


### Challange Problems

#### T24

<div class='cbox'>

How many corners $(\pm 1, \pm 1, \pm 1, \pm 1)$ does a cube of side 2 have in 4 dimensions? What is its volume? How many 3D faces? How many edges? Find one edge.

</div>

<div class='pbox'>

(1):every component of every vertex's coordinate has two value, so there are $2^4=16$ vertices.

(2):volume: $2^4=16$

(3):every 3d faces means a restriction of one component, so $4*2=8$

(4):every edge means a restriction of three components, and the last component's two value represents two vertex it connects. so $\binom{4}{3}2^3=32$

</div>



#### T25

<div class='cbox'>

Find two different combinations of the three vectors $u = (1, 3)$ and $v = (2, 7)$ and $w = (1, 5)$ that produce $b = (0, 1)$. Slightly delicate question: If I take any three vectors $u, v, w$ in the plane, will there always be two different combinations that produce $b = (0, 1)$?

</div>

<div class='pbox'>

##### (1)

$w=-3u+2v,b=-2u+2v$.

so for each $t$

$$
\begin{cases}
u=-2-3t \\
v=2+2t \\
w=-t
\end{cases}
$$
is a solution

##### (2)

No. eg: $u=v=w=(1,0)$

Yes when there are two vectors in $\{u,v,w\}$ that are linearly dependent.

</div>



#### T26

<div class='cbox'>

The linear combinations of $v = (a, b)$ and $w = (c, d)$ fill the plane unless \_\_\_\_\_\_\_\_. Find four vectors $u, v, w, z$ with four nonzero components each so that their combinations $cu + dv + ew + fz$ produce all vectors in four-dimensional space.

</div>

<div class='pbox'>

###### (1)

$\exists k \ s.t.\ w=kv \text{ or } u=0 \text{ or } v=0$

##### (2)

$$
\begin{cases}
u=[1,1,1,2]\\
v=[1,1,2,1]\\
w=[1,2,1,1]\\
z=[1,1,1,1]\\
\end{cases}
$$

(do some elementary row operation on Identity Matrix)

</div>



#### T27

<div class='cbox'>

Write down three equations for $c, d, e$ so that $cu + dv + ew = b$. Write this also as a matrix equation $Ax = b$. Can you somehow find $c, d, e$ for this $b$?
$u = \begin{bmatrix} 2 \\ -1 \\ 0 \end{bmatrix} \quad v = \begin{bmatrix} -1 \\ 2 \\ -1 \end{bmatrix} \quad w = \begin{bmatrix} 0 \\ -1 \\ 2 \end{bmatrix} \quad b = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}$

</div>

<div class='pbox'>

$$
\begin{cases}
c=\dfrac{3}{4}\\
d=\dfrac{1}{2}\\
e=\dfrac{1}{4}
\end{cases}

$$

</div>




