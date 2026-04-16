<div class='cbox'>

平面图三角剖分图$G$最小度为$5$,则存在一条边$(u,v)$满足$d(u)=d(v)=5$或$\{d(u),d(v)\}=\{5,6\}$.

</div>

<div class='pbox'>

反证法,假设不存在.

给每个点赋予电量$c(v)=6-d(v)$,给每个面赋予电量$c(f)=6-2d(v)=0$,($d(f)$表示这个面的边界由几条边构成).

于是点上的总电量之和为

$$
\begin{gathered}
\sum_{v\in V}(6-d(v)) \\
=\sum _{v\in V} (6-d(v))+\sum _{f\in F} (6-2d(f)) \\
=6v(G)-2e(G)+6f(G)-4e(G) \\
=12
\end{gathered}
$$

然后重新分配电量:把每个$5$度点的电量平均分给它的每个邻居.设新电量为$c'(u)$则:
- $d(u)=5 \Rightarrow c'(u)=0$(不存在相邻的5度点,分完之后成了$0$)
- $d(u)=6 \Rightarrow c'(u)=0$(不会接收到5度点的电量,且原来为$0$)
- $d(u)\ge 7 \Rightarrow c'(u)\le c(u)+\dfrac15 \lbrack \dfrac{d(u)}{2}  \rbrack<0$.(这里除以$2$是因为是你是三角剖分图,所以$u$的邻居一定构成一个环,而不能有两个$5$度点相连,所以最多是$\dfrac {d(u)}2$)

你发现所有点的电量都成负的了.

所以如果不存在那两种边,你流动总电量从正的变成负的了,所以矛盾.就证明完了.


</div>


<div class='cbox'>

每个平面图中都存在与至多两个$12^+$度点相邻的$5^-$度点.

</div>

<div class='pbox'>




</div>


<div class='cbox'>

证明若一个图没有三元环,则其有不超过$\dfrac{n^2}4$条边,当$K_{\frac n2,\frac n2}$取等.

</div>

<div class='pbox'>

设$N(u)$表示$u$的所有相邻点.

考虑任取一条边$(u,v)$,则$N(u)\cap N(v)=\varnothing$,于是$d(u)+d(v)\le n$.

把每条边的式子加起来,得到:

$$
\begin{gathered}
\sum _{(u,v)\in E} d(u)+d(v)\le e(G)n
\end{gathered}
$$

因为

$$
\begin{gathered}
\sum _{(u,v)\in E} d(u)+d(v) \\
=\sum _{u\in V} d(u)^2
\end{gathered}
$$

由柯西不等式

$$
\begin{gathered}
\begin{cases}
(\sum _{u\in V} d(u)^2)n\ge 4e(G)^2
\end{cases}
\end{gathered}
$$

联立得$4e(G)^2\le e(G)n^2$,就得到$e(G)\le \dfrac{n^2}4$.

</div>

