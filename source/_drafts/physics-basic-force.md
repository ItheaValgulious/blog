---
title: Physics Note 1
tags: [physics,self-study]
---
# Physics Note 1

自己先读他一遍

## 力学

### 科里奥利力

[think] 这里的关键是,其实向量并不擅长表达旋转,所以表达出旋转坐标系下的某位置在真实系下的表达然后再求两次导是很麻烦的.但 一个量在旋转系和静止系下分别的导数的关系是简单的(指的是,同一个向量,选定旋转的基向量与固定的基向量的两种表示后得到的坐标求导的关系)

<div class='cbox'>

$$
\begin{gathered}
\dfrac{d}{dt} v_I=\dfrac{d}{dt} v_R + \omega \times v
\end{gathered}
$$

其中$I$表示静止系下看,$R$表示在旋转系下看.

</div>

<div class='pbox'>

直接写成$v_I=(r\cos t,r\sin t)v_R^{(0)}+(-r\sin t,r\cos t)v_R^{(1)}$,求导得:

$$
\begin{gathered}
\dot v_I= (r\cos \omega t,r\sin \omega t) \dot {v_R^{(0)}}+(-r\sin \omega t,r\cos \omega t)\dot {v_R^{(1)}} \\
+\dot{(r\cos \omega t,r\sin \omega t)}v_R^{(0)}+\dot{(-r\sin \omega t,r\cos \omega t)}v_R^{(1)} 
\end{gathered}
$$

整理一下就是$\dot v_R+\omega\times v$了.$\omega$顺时针向内逆时针向外,遵循右手螺旋定则.

</div>

于是就可以推了:

<div class='cbox'>

推导旋转坐标系与静止系的变换:

</div>

<div class='pbox'>

$$
\begin{gathered}
\dot r_I=\dot r_R+\omega \times r_R \\
\ddot r_I=(\ddot r_R+\dot \omega \times r_R+\omega \times \dot r_R)+\omega\times(\dot r_R+\omega \times r_R) \\
\Rightarrow a_I=(a_R)+(\dot \omega\times r_R)+(2\omega\times v_R)+(\omega\times(\omega\times r_R))
\end{gathered}
$$

其中第一项是原来的加速度,第二项是如果非匀速旋转导致的,第三项是科里奥利力导致的,第四项是离心力导致的($\omega\times(\omega\times r_R)$方向朝内,大小是$\omega^2|r_R|$).

</div>

### 引力的球壳公式

怎么喵的推起来这么麻烦?分出去开篇新文章了.

### 相对论

### 角动量定理

### 天体椭圆轨道

### 刚体定轴旋转

### 简谐运动的合成

### 受迫振动,阻尼

### 波的能量,干涉

### 多普勒效应