
<div class='dbox'>

复向量空间

略

</div>


**2.2 Integration as a Linear Functional**
（本节主要为讨论性内容，核心结论如下）
对于任何正测度 $\mu$，${L}^1(\mu)$ 是一个向量空间，且映射 $f \mapsto \int_X f d\mu$ 是 ${L}^1(\mu)$ 上的一个线性泛函。

F. Riesz 定理的一个特定形式：
对于 $I=[0,1]$ 上所有连续复函数构成的向量空间 $C$，对 $C$ 上的每一个正线性泛函 $\Lambda$，都对应一个 $I$ 上的有限正 Borel 测度 $\mu$，使得
$$ \Lambda f = \int_I f d\mu \quad (f \in C). $$

**2.3 Definitions**
设 $X$ 是一个拓扑空间。
(a) 集合 $E \subset X$ 称为**闭集**，如果其补集 $E^c$ 是开集。
(b) 集合 $E \subset X$ 的**闭包** $\bar{E}$ 是包含 $E$ 的 $X$ 中最小的闭集。
(c) 集合 $K \subset X$ 称为**紧集**，如果 $K$ 的每一个开覆盖都包含一个有限子覆盖。特别地，如果 $X$ 本身是紧的，则称 $X$ 为紧空间。
(d) 点 $p \in X$ 的**邻域**是包含 $p$ 的 $X$ 的任意开子集。
(e) $X$ 称为 **Hausdorff 空间**，如果满足：若 $p \in X, q \in X$ 且 $p \neq q$，则存在 $p$ 的邻域 $U$ 和 $q$ 的邻域 $V$ 使得 $U \cap V = \varnothing$。
(f) $X$ 称为**局部紧**的，如果 $X$ 的每一点都有一个闭包为紧集的邻域。

**2.4 Theorem**
设 $K$ 是拓扑空间 $X$ 中的紧集，$F$ 是闭集。如果 $F \subset K$，则 $F$ 是紧集。

**Corollary**
如果 $A \subset B$ 且 $B$ 具有紧闭包，则 $A$ 也具有紧闭包。

**2.5 Theorem**
设 $X$ 是 Hausdorff 空间，$K \subset X$，$K$ 是紧集，且 $p \in K^c$。则存在开集 $U$ 和 $W$ 使得 $p \in U$，$K \subset W$，且 $U \cap W = \varnothing$。

**Corollary**
(a) Hausdorff 空间的紧子集是闭集。
(b) 如果 $F$ 是 Hausdorff 空间中的闭集，$K$ 是紧集，则 $F \cap K$ 是紧集。

**2.6 Theorem**
如果 $\{K_\alpha\}$ 是 Hausdorff 空间中紧子集的集合，且 $\bigcap_\alpha K_\alpha = \varnothing$，则 $\{K_\alpha\}$ 的某个有限子集也有空交集。

**2.7 Theorem**
设 $U$ 是局部紧 Hausdorff 空间 $X$ 中的开集，$K \subset U$，且 $K$ 是紧集。则存在一个闭包为紧集的开集 $V$，使得
$$ K \subset V \subset \bar{V} \subset U. $$

**2.8 Definition**
设 $f$ 是拓扑空间上的实（或广义实）函数。
如果对于每个实数 $\alpha$，集合 $\{x: f(x) > \alpha\}$ 是开集，则称 $f$ 是**下半连续**的。
如果对于每个实数 $\alpha$，集合 $\{x: f(x) < \alpha\}$ 是开集，则称 $f$ 是**上半连续**的。

**2.9 Definition**
拓扑空间 $X$ 上的复函数 $f$ 的**支集 (support)** 是集合 $\{x: f(x) \neq 0\}$ 的闭包。
$X$ 上所有支集为紧集的连续复函数的集合记为 $C_c(X)$。

**2.10 Theorem**
设 $X$ 和 $Y$ 是拓扑空间，且 $f: X \to Y$ 是连续的。如果 $K$ 是 $X$ 的紧子集，则 $f(K)$ 是紧集。

**Corollary**
任意 $f \in C_c(X)$ 的值域是复平面的紧子集。

**2.11 Notation**
记号 $K \prec f$ 表示 $K$ 是 $X$ 的紧子集，$f \in C_c(X)$，对所有 $x \in X$ 有 $0 \le f(x) \le 1$，且对所有 $x \in K$ 有 $f(x)=1$。
记号 $f \prec V$ 表示 $V$ 是开集，$f \in C_c(X)$，$0 \le f \le 1$，且 $f$ 的支集包含于 $V$。
记号 $K \prec f \prec V$ 表示同时满足上述两个条件。

**2.12 Urysohn's Lemma**
设 $X$ 是局部紧 Hausdorff 空间，$V$ 是 $X$ 中的开集，$K \subset V$，且 $K$ 是紧集。则存在 $f \in C_c(X)$ 使得
$$ K \prec f \prec V. $$

**2.13 Theorem**
设 $V_1, \dots, V_n$ 是局部紧 Hausdorff 空间 $X$ 的开子集，$K$ 是紧集，且
$$ K \subset V_1 \cup \dots \cup V_n. $$
则存在函数 $h_i \prec V_i$ ($i=1, \dots, n$) 使得
$$ h_1(x) + \dots + h_n(x) = 1 \quad (x \in K). $$
集合 $\{h_1, \dots, h_n\}$ 称为 $K$ 上从属于覆盖 $\{V_1, \dots, V_n\}$ 的单位分解。

**2.14 The Riesz Representation Theorem**
设 $X$ 是局部紧 Hausdorff 空间，$\Lambda$ 是 $C_c(X)$ 上的正线性泛函。则在 $X$ 中存在一个包含所有 Borel 集的 $\sigma$-代数 $\mathfrak{M}$，并且在 $\mathfrak{M}$ 上存在唯一的正测度 $\mu$，它在下述意义下表示 $\Lambda$：
(a) 对每一个 $f \in C_c(X)$，$\Lambda f = \int_X f d\mu$，
且具有以下附加性质：
(b) 对每一个紧集 $K \subset X$，$\mu(K) < \infty$。
(c) 对每一个 $E \in \mathfrak{M}$，$\mu(E) = \inf\{\mu(V): E \subset V, V \text{ open}\}$.
(d) 对每一个开集 $E$ 以及每一个满足 $\mu(E) < \infty$ 的 $E \in \mathfrak{M}$，关系
$$ \mu(E) = \sup\{\mu(K): K \subset E, K \text{ compact}\} $$
成立。
(e) 如果 $E \in \mathfrak{M}$，$A \subset E$，且 $\mu(E)=0$，则 $A \in \mathfrak{M}$。

**2.15 Definition**
定义在局部紧 Hausdorff 空间 $X$ 的所有 Borel 集构成的 $\sigma$-代数上的测度 $\mu$ 称为 $X$ 上的 **Borel 测度**。如果 $\mu$ 是正测度，Borel 集 $E \subset X$ 称为**外正则**的，如果它具有定理 2.14 中的性质 (c)；称为**内正则**的，如果它具有定理 2.14 中的性质 (d)。如果 $X$ 中的所有 Borel 集既是外正则又是内正则的，则称 $\mu$ 是**正则**的。

**2.16 Definition**
拓扑空间中的集合 $E$ 称为 **$\sigma$-紧**的，如果 $E$ 是可数个紧集的并。
测度空间中的集合 $E$（带有测度 $\mu$）称为具有 **$\sigma$-有限测度**，如果 $E$ 是可数个满足 $\mu(E_i) < \infty$ 的集合 $E_i$ 的并。

**2.17 Theorem**
设 $X$ 是局部紧、$\sigma$-紧的 Hausdorff 空间。如果 $\mathfrak{M}$ 和 $\mu$ 如定理 2.14 中所述，则 $\mathfrak{M}$ 和 $\mu$ 具有以下性质：
(a) 如果 $E \in \mathfrak{M}$ 且 $\epsilon > 0$，则存在闭集 $F$ 和开集 $V$ 使得 $F \subset E \subset V$ 且 $\mu(V-F) < \epsilon$。
(b) $\mu$ 是 $X$ 上的正则 Borel 测度。
(c) 如果 $E \in \mathfrak{M}$，则存在集合 $A$ 和 $B$ 使得 $A$ 是 $F_\sigma$ 集，$B$ 是 $G_\delta$ 集，$A \subset E \subset B$，且 $\mu(B-A)=0$。

**2.18 Theorem**
设 $X$ 是局部紧 Hausdorff 空间，且其中每个开集都是 $\sigma$-紧的。设 $\lambda$ 是 $X$ 上的任意正 Borel 测度，且对每个紧集 $K$ 都有 $\lambda(K) < \infty$。则 $\lambda$ 是正则的。

**2.19 Euclidean Spaces**
欧几里得 $k$ 维空间 $R^k$ 是所有坐标 $\xi_i$ 为实数的点 $x=(\xi_1, \dots, \xi_k)$ 的集合。
定义 $x+y$ 和 $\alpha x$。定义内积 $x \cdot y = \sum \xi_i \eta_i$ 和范数 $|x|=(x \cdot x)^{1/2}$。度量定义为 $\rho(x,y)=|x-y|$。
$R^k$ 中的开集是可数个不相交盒子的并。

**2.20 Theorem**
在 $R^k$ 的某个 $\sigma$-代数 $\mathfrak{M}$ 上存在唯一的正完备测度 $m$，具有以下性质：
(a) 对每个 $k$-维胞腔 (box/cell) $W$，$m(W) = \text{vol}(W)$。
(b) $\mathfrak{M}$ 包含 $R^k$ 中的所有 Borel 集；更确切地说，$E \in \mathfrak{M}$ 当且仅当存在 $A, B \subset R^k$ 使得 $A \subset E \subset B$，$A$ 是 $F_\sigma$，$B$ 是 $G_\delta$，且 $m(B-A)=0$。此外，$m$ 是正则的。
(c) $m$ 是平移不变的，即对每个 $E \in \mathfrak{M}$ 和每个 $x \in R^k$，有 $m(E+x) = m(E)$。
(d) 如果 $\mu$ 是 $R^k$ 上任意正的平移不变 Borel 测度，且对每个紧集 $K$ 都有 $\mu(K) < \infty$，则存在常数 $c$ 使得对所有 Borel 集 $E \subset R^k$ 有 $\mu(E) = c m(E)$。
(e) 对每一个 $R^k$ 到 $R^k$ 的线性变换 $T$，对应一个实数 $\Delta(T)$，使得对每个 $E \in \mathfrak{M}$，有 $m(T(E)) = \Delta(T)m(E)$。

**2.21 Remarks**
如果 $m$ 是 $R^k$ 上的 Lebesgue 测度，习惯上将 $L^1(m)$ 写为 $L^1(R^k)$。
如果 $k=1$，习惯上将 $\int f dm$ 写为 $\int_a^b f(x) dx$。
并非每个 Lebesgue 可测集都是 Borel 集。并非 $R^k$ 的每个子集都是 Lebesgue 可测的。

**2.22 Theorem**
如果 $A \subset R^1$ 且 $A$ 的每个子集都是 Lebesgue 可测的，则 $m(A)=0$。

**Corollary**
每一个正测度集合都有不可测子集。

**2.23 Determinants**
定理 2.20(e) 中的比例因子 $\Delta(T)$ 可以通过行列式进行代数解释：
$\Delta(T) = |\det T|$。

**2.24 Lusin's Theorem**
设 $f$ 是 $X$ 上的复可测函数，$\mu(A) < \infty$，若 $x \notin A$ 则 $f(x)=0$，且 $\epsilon > 0$。则存在 $g \in C_c(X)$ 使得
$$ \mu(\{x: f(x) \neq g(x)\}) < \epsilon. $$
此外，我们可以安排使得 $\sup_{x \in X} |g(x)| \le \sup_{x \in X} |f(x)|$。

**Corollary**
假设 Lusin 定理的条件满足且 $|f| \le 1$。则存在序列 $\{g_n\}$ 使得 $g_n \in C_c(X)$，$|g_n| \le 1$，且
$$ f(x) = \lim_{n \to \infty} g_n(x) \quad \text{a.e.} $$

**2.25 The Vitali-Caratheodory Theorem**
设 $f \in L^1(\mu)$，$f$ 是实值函数，且 $\epsilon > 0$。则在 $X$ 上存在函数 $u$ 和 $v$ 使得 $u \le f \le v$，$u$ 是上半连续且上有界的，$v$ 是下半连续且下有界的，并且
$$ \int_X (v-u) d\mu < \epsilon. $$