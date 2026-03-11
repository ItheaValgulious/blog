---
title: Discrete Math Note
tags:
  - note
  - discrete
  - math
date: 2026-03-06 11:02:03
---

# Discrete Math Note

## Mysteries

- 空图指的是荒漠
- $(\varnothing,\varnothing)$不是图
- 单点不是路径(path)
- "邻接矩阵不能表示重边"        

## 20260306

<div class='cbox'>

对任意六个点的图$G$:$G$或$\overline{G}$至少有一个包含$K_3$子图.

</div>

<div class='pbox'>

先转化成完全图红蓝染色.

随便拿一个点,一定有至少3条同色,拿出3条中对应的3个点,若它们之中的某条边颜色与这3条相同则完事,否则它们之中的3条边子集构成$K_3$,完成.

</div>

## 20260310

<div class='cbox'>

若简单图中每个点度数都大于$3$,则图中一定存在有弦的回路

称一个简单回路中连接两个不相邻节点的边是弦

</div>

<div class='pbox'>

它给的证法是考虑拿一个极长简单路,那么你端点上的邻接点必须都在这条路上,于是离着近的那条就会是离着远的那条成的环的弦.

</div>



