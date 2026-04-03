---
title: Physics Note 1
tags: [physics,self-study]
---
# Physics Note 1

自己先读他一遍

## 力学

### 坐标系转化

#### 例: 球坐标系

#### 科里奥利力

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

### 功和能

#### 动能定理

$$
\begin{gathered}
F=\dfrac{d}{dt} (mv) \\
\int Fdx= \int \dfrac{d(mv)}{dt} dx\\
=\dfrac{1}{m} \int mvd(mv)  \\
=\dfrac{1}{2} mv^2|_{t_0}^{t_1}
\end{gathered}
$$

#### 保守力与势能与机械能守恒

与路径无关的力可以构造出势能的标量场.使得两点之间运动时该力的功等于势能差.势能场的梯度是力场.

**我们看成保守力的势能只能和动能等量转化**,一个质点的机械能守恒其实是每个 (保守力+动能守恒)相加 的结果.

#### 稳定平衡点与不稳定平衡点

总势能场求梯度是力场,所以在势能场的极值点处做泰勒展开(物理当然假设无限可微)取一阶项,就知道平衡点处微扰后是类似简谐的稳定在平衡点附近还是类似正反馈偏离平衡.

#### 质点系功能原理

刚才你把保守力视为力场的时候,你是固定了力的一端看另一端,才能产生静态的力场.

现在要考虑两端都在动的情况:不过你发现没有关系,由作用力反作用力的关系,你能知道:

$$
\begin{gathered}
\int Fdx_1-\int Fdx_2=\int F(dx_1-dx_2)
\end{gathered}
$$

对质点来说,你的力场不会旋转,那么其中$dx_1-dx_2$恰好是你固定这个力场在一个点后另一个点的相对位移.

但这么想不是很优雅:你需要破坏质点之间的对称.有没有更好的方法呢?

AI大人说,你应该把势能看成关于两者坐标的函数$E(\vec x_1,\vec x_2)$,然后从空间的平移对称性可以说明$E$必须只依赖$\vec x_1-\vec x_2$,从空间的旋转对称性,可以说明只依赖$\vec x_1-\vec x_2$的长度,从而任意两个点的势能都只和相对距离相关.

在这里对$E$求梯度还可以得到保守力一定是沿两质点方向的结论.(保守力一定是有心力.)

此时你的动能定理变成了:

$$
\begin{gathered}
\int F_1dx_1-F_1dx_2 \\
=E(x_1,x_2)-E(x_1+\Delta x_1,x_2+\Delta x_2) \\
=E(\|x_1-x_2\|)-E(\|x_1+\Delta x_1-x_2-\Delta x_2\|)
\end{gathered}
$$

现在同时对所有点对累加,一侧累加了所有内力的做工,一侧是系统总势能的变化.

这时候你又有了些疑问:无限个点的时候我直接用质量密度积起来凭啥是对的?然后你想了一下发现我们在学物理,所以$E$和$F$都关于点的位置连续,而密度必须连续且有界,又因为我们在高斯定理那里考虑过弱有界定理的事,所以对于空间中二次方的力都是可积的(因为$dV$关于半径是三次方),这是不是甚至保证了绝对可积可以交换积分号啊.

这些性质是普遍满足的,所以我们看起来总可以在次数不超过$2$的时候乱换积分号.

而这里你只是把做工加起来,势能加起来,不需要交换积分,所以就合法了.

### 动量

#### 动量定理

$$
\begin{gathered}
F=\dfrac{d}{dt} (mv) \\
\Rightarrow Fdt=d(mv) \\
\Rightarrow \int Fdt=\int mdv=m\Delta v \\
\end{gathered}
$$

#### 动量守恒

你在学质点系功能定理的时候意识到力还是对点对考虑比较好.而对每个点对显然$m_1dv_1+m_2dv_2=Fdt-Fdt=0$,然后你仍然是都累加起来得到动量守恒.

#### 质点系动量定理

内力已经动量守恒了,然后因为你$Fdt=\dfrac d{dt}(mx)$是线性的,所以你可以全累加起来,然后要交换求和或积分号,得到:

$$
\begin{gathered}
\int \sum Fdt=\int \sum m_idv_i \\
\int \sum mv dt \\
=\int \sum m\Delta x_{i,1}-x_{i,0} \\
=M [(\sum \dfrac{m_i}{M}\Delta x_{i,1})-(\sum \dfrac{m_i}{M}\Delta x_{i,0})] \\
\text{where } M=\sum_i m_i
\end{gathered}
$$

第一个式子是合外力冲量等于总动量变化量
第二个式子告诉你对动量积分得到于质心的位移

#### 恢复系数

定义为碰撞前后的相对速度比:$(v_1-v_2)=e(v_1'-v_2')$

$$
\begin{gathered}
\begin{cases}
mv_1+Mv_2=mv_1'+Mv_2' \\
v_1-v_2=e(v_1'-v_2')
\end{cases} \\
\Rightarrow 
\begin{cases}
v_1'=v_1-\dfrac{m_2}{m_1+m_2} (1+e)(v_1-v_2) \\
v_2'=v_2-\dfrac{m_1}{m_1+m_2} (1+e)(v_1-v_2)
\end{cases}

\end{gathered}
$$

### 角动量

#### 角动量定理

定义力矩$\vec M=\vec r\times \vec F$

角动量$\vec L=\vec r\times \vec p=m\vec r\times \vec v$.

感觉拿面积建立直觉还不如速度乘旋转半径好理解呢

$$
\begin{gathered}
\dfrac{dL}{dt} =\dfrac{dr}{dt} \times p+r\times\dfrac{dp}{dt} \\
=0+r\times F \\
=M
\end{gathered}
$$

(发现乘法法则对任意双线性的东西都是类似的).

自然你会得到当没有力矩的时候角动量守恒,也就是开普勒第二定律了.

#### 天体椭圆轨道

<div class='cbox'>

只被引力作用的两个天体围绕质心做椭圆运动

</div>

<div class='pbox'>

选定质心为原点,则无外力的情况下它是惯性系.

只有引力,过质心,所以角动量守恒,注意角动量向量有方向的垂直于旋转面,从而是平面运动,且天体满足$r\times \dot r=\dfrac Lm$,$L$为定值.

同时你可以拿机械能守恒再列一个$-\dfrac{GMm}{\|r\|}+\dfrac12m \dot r^2=E$为定值.

然后你把$r$的分量写开肯定是两个未知数两个方程,然后把一个变量消掉就开始积分吧()由于我们在学物理所以省略这些神秘的积分步骤,你会得到它是椭圆.

</div>

### 刚体定轴旋转

### 简谐运动的合成

### 受迫振动,阻尼

### 波的能量,干涉

### 多普勒效应