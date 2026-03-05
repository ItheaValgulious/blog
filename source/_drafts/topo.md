---
title: Topo Basic Note
tags: [math,topo,note]
---
# Topo Basic Note

<div class='cbox'>

$\beta$是集合$X$上的拓扑基,$U\subset X$是$\beta$生成的拓扑中的开集等价于$\forall x\in U,\exists B_x\in \beta,s.t.\ x\in B_x\subset U$

</div>

<div class='pbox'>

左推右:$U$是一些$B_x$的并,所以$x\in U$一定有$x$属于某个$B_x$.

右推左:把所有$B_x$并起来.

</div>

<div class='cbox'>

对拓扑$(X,T)$中的一个开集族$A$,若对$X$中任意开集$U$,$\forall x\in U$,都有$\exists V_x\in A,x\in V_x\subset U$,则$A$是一个拓扑基,且生成的恰好是$(X,T)$

</div>

<div class='pbox'>

验证:显然对所有的$x$你可以找到一个$V$包含他,显然任意两个$V_1,V_2\in A,V_1\subset V_2$是开集可以找到$x\in (V_1\cap V_2)\in A$,是拓扑基.

显然你用开集不可能生成不是开集的东西,显然所有开集都有$U=\bigcup_{x\in U}V_x$,就行了.

</div>





