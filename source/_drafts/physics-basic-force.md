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

### 狭义相对论

<div class='cbox'>

如何理解狭义相对论.

</div>

<div class='pbox'>

首先,他是要处理在两个有匀速相对运动的参考系下的变换,且由于两个参考系等价,这个变换应该是对称的,还要做到不改变物理规律.它解决的变换是B系是怎么样的,那么你在A系看B系是什么样的.

同时性原理:就是同一点同时发生的两件事在另一个系里也应该同时发生.(其实感觉这个也可以是保证因果链,避免果在因之前发生,看起来和保时序是等价的).我们很快发现它保障了可以定义一个点的时间.

光速不变原理:光速在每个系看起来是一样的.

然后一个推导过程是这样的:考虑B系相对A系有一个$(v,0)$的速度.

那么我们在B系$(0,0),(0,1)$分别放一个镜子,并让里面有一束光在这两个点之间来回,这相当于一个运行在$(0,0)$处的钟,我们叫他光钟.

那么根据同时性原理我们可以在$0$处进行计时:如果你在$t_1$时刻和$t_2$时刻接收到这个光,那么一件发生在$[t_1,t_2]$的事就有了时长属性$t_2-t_1$,这也是为什么它真的是一个钟.或者说,当我们想变换时间的时候我们需要先知道时间是什么,那么不妨定义成光钟计算出的时长.

那么我们发现,在$B$系下,显然每隔$t_1=\dfrac {2l}c$接到一次;而$A$系下,光速不变,但光速现在是斜着走的了,所以光速就成了$(v,\sqrt{c^2-v^2})$,竖直分量笑了,就成了每隔$t_2=\dfrac{2l}{\sqrt{c^2-v^2}}$,于是你就算出了时间的变换系数是$\gamma=\dfrac{t_2}{t_1}=\dfrac1{\sqrt{1-(\dfrac vc)^2}}$.

注意方向:$\dfrac {t_2}{t_1}$是说同一件事,在里面经过了$t_1$的时间,则在外面经过了$t_2$时间,因为$t_2>t_1$,所以我们说钟慢了.

然后你也可以再去考虑距离:因为光速相同,由速度的定义,相同时间里走过的路程也相同,所以你把光钟横着放,考虑光钟的长度即可.

然后你还是考虑长度为$x$的光钟,在B系下显然是要用$t_1=\dfrac{2x_1}c$,在A系下由于光速不变,系在跑,就成了$t_2=\dfrac {x_2}{v-c}-\dfrac {x_2}{v+c}$,令这两个时间相等得到$t_2=\gamma t_1$,化简得$x_2=\dfrac1{\gamma} x_1$

最后你再考虑不同位置的两个点的时间怎么算?即:B系下相隔$x$处的两个点的时间差:考虑在$\dfrac x2$处同时向两侧发两束光,那么它俩在$B$系下同时到达,这是一个$B$系下的同时的事件(但不同地点),而到$A$系看的话:你先把整个长度$\dfrac x2$变换过去成$\dfrac x{2\gamma}$,然后光在以$c$的速度跑,车在以$v$的速度跑,你就算出来时间是$\dfrac x{2\gamma}(\dfrac1{c-v}-\dfrac1{c+v})=\gamma \dfrac{vx}{c^2}$.

你用这三部分就可以推任意变换了:你认为$B$系的原点的时间是这个系的时间,那么变换$(x,t)$处的事件,自然就变成:$(\dfrac x{\gamma},\gamma t-\dfrac{\gamma vx}{c^2})$

如果你$x$这一维是沿运动方向为正的,那么这个$\Delta t$就该减上去了.

</div>

最后再简单说几个点:
- 为什么垂直于运动方向的时间和空间都不会变?因为你假设会变,那考虑两个圆环沿轴向彼此接近,它俩互相看对方都比自己大/小,就说不清谁会套到谁了.
- 如果一维空间?那很糟了,不过结论不会变,你可以用A和B之间互相发光推.

感觉把相对论拆成空间,时间,不同空间位置的时间差这三块看比洛伦兹更好记罢了()

### 功和能

#### 动能定理

<div class='cbox'>

做功等于动能变化量

</div>

<div class='pbox'>

$$
\begin{gathered}
F=\dfrac{d}{dt} (mv) \\
\int Fdx= \int \dfrac{d(mv)}{dt} dx\\
=\dfrac{1}{m} \int mvd(mv)  \\
=\dfrac{1}{2} mv^2|_{t_0}^{t_1}
\end{gathered}
$$

</div>

#### 保守力与势能与机械能守恒

与路径无关的力可以构造出势能的标量场.使得两点之间运动时该力的功等于势能差.势能场的梯度是力场.

**我们看成保守力的势能只能和动能等量转化**,一个质点的机械能守恒其实是每个 (保守力+动能守恒)相加 的结果.

#### 稳定平衡点与不稳定平衡点

总势能场求梯度是力场,所以在势能场的极值点处做泰勒展开(物理当然假设无限可微)取一阶项,就知道平衡点处微扰后是类似简谐的稳定在平衡点附近还是类似正反馈偏离平衡.

#### 质点系功能原理

<div class='cbox'>

质点系总能量(动能+保守力势能)变化量等于非保守力和外力的做功.

</div>

<div class='pbox'>

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

而这里你只是把做功加起来,势能加起来,不需要交换积分,所以就合法了.

</div>

### 动量

#### 动量定理

<div class='cbox'>

冲量是动量变化量

</div>

<div class='pbox'>

$$
\begin{gathered}
F=\dfrac{d}{dt} (mv) \\
\Rightarrow Fdt=d(mv) \\
\Rightarrow \int Fdt=\int mdv=m\Delta v \\
\end{gathered}
$$

</div>


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

<div class='cbox'>

推导碰撞前后速度

</div>

<div class='pbox'>

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

</div>


### 角动量

#### 角动量定理

定义力矩$\vec M=\vec r\times \vec F$

角动量$\vec L=\vec r\times \vec p=m\vec r\times \vec v$.

感觉拿面积建立直觉还不如速度乘旋转半径好理解呢

<div class='cbox'>

角动量变化量等于力矩对时间积分

</div>

<div class='pbox'>

$$
\begin{gathered}
\dfrac{dL}{dt} =\dfrac{dr}{dt} \times p+r\times\dfrac{dp}{dt} \\
=0+r\times F \\
=M
\end{gathered}
$$

</div>



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

然后你把$r$的分量写开肯定是两个未知数两个方程,然后把一个变量消掉就开始积分吧()~~由于太麻烦~~由于我们在学物理所以省略这些神秘的积分步骤,你会得到它是椭圆.

</div>

### 刚体定轴旋转

三维刚体在定轴旋转时等价于压扁了的二维刚体.所以下面都研究二维刚体.

<div class='cbox'>

刚体转动的角动量

</div>

<div class='pbox'>

$$
\begin{gathered}
L=\int_{x\in V} x\times (\rho(x)dV)(\omega\times x) \\
x\times (\omega \times x)=x^2\omega \\
\Rightarrow L=\int x^2\omega \rho(x)dV \\
=\omega \int x^2\rho(x)dV \\
=\omega I
\end{gathered}
$$

这里$I$就是转动惯量.单位是$m^2\cdot kg$.

因为是二维的,所以$x\perp \omega$可以直接乘.

</div>

<div class='cbox'>

刚体转动的能量

</div>

<div class='pbox'>

$$
\begin{gathered}
E=\int_{x\in V} \dfrac12 (\rho(x)dV) (\omega\times x)^2 \\
=\dfrac 12(\int_{x\in V} \rho(x)dV x^2) \omega^2 \\
=\dfrac12 \omega^2 I
\end{gathered}
$$

</div>

转动惯量之间有关系,方便计算

<div class='cbox'>

平行轴定理:已知过质心的$l$的转轴对应的转动惯量为$I_l$,对与他平行的距离为$d$的轴$m$有:

$I_m=I_l+Md^2$

</div>

<div class='pbox'>

$$
\begin{gathered}
I_m=\int_{x\in V} ((x\times u_l)-d)^2 \rho(x)dV \\
=\int_{x\in V} (x\times u_l)^2 +\int_{x\in V} d^2\rho(x)dV-2\int_{x\in V} (x\times u_l)d \\
=I_l+Md^2-2\int_{x\in V} (x\times u_l)d
\end{gathered}
$$

其中$u_l$是$l$的方向单位向量.注意到因为原点取质心,所以最后一项是$0$,得证.

</div>

<div class='cbox'>

对二维刚体来说,垂直于平面的轴转动惯量等于平面上两条相交于它的垂直的轴的转动惯量之和:

$I_z=I_x+I_y$

</div>

<div class='pbox'>

较为显然:相当于取了个坐标系,然后勾股定理.

</div>



### 简谐运动的合成

### 受迫振动,阻尼

### 波的能量,干涉

### 多普勒效应