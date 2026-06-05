# Parallelization of MLFMA on Distributed Memory Computers / 分布式内存计算机上MLFMA的并行化

> **中英双语版**

**Source:** Chew, *Fast and Efficient Algorithms in CEM*, Chapter 4 — Sanjay Velamparambil, Jiming Song, and Weng Cho Chew
**来源：** Chew《计算电磁学中的快速高效算法》第4章

---

## 4.1 Introduction / 引言

Integral equation methods are widely used for the solution of electromagnetic scattering problems. The method of moments (MoM) converts the integral equation into a dense linear system. Direct methods (LU) require O(N³) operations, while iterative methods require O(N²) per matrix-vector product, both prohibitive for large problems.
积分方程方法广泛用于电磁散射问题的求解。矩量法(MoM)将积分方程转换为稠密线性系统。直接法(LU分解)需要O(N³)操作，而迭代方法每次矩阵-矢量乘积需要O(N²)，两者对于大规模问题都不可行。

MLFMA reduces the computational complexity of a matrix-vector multiply to O(N log N). Using MLFMA-accelerated MoM codes, researchers have solved very large-scale problems [2,3].
MLFMA将矩阵-矢量乘法的计算复杂度降低到O(N log N)。使用MLFMA加速的MoM代码，研究人员已求解了非常大尺度的问题[2,3]。

Advances in supercomputing have demonstrated that the future of high-performance computing lies in distributed memory parallel computing. To exploit this technology for extremely large-scale EM problems, distributed memory versions of MLFMA must be developed.
超级计算的进展表明，高性能计算的未来在于分布式内存并行计算。为了利用这一技术求解极端大规模电磁问题，必须开发分布式内存版本的MLFMA。

We have developed a parallel version of dynamic MLFMA called **ScaleME (Scalable Multipole Engine)**. ScaleME is a portable implementation using the Message Passing Interface (MPI) for communication. It is implemented as an application-independent kernel that can be retrofitted into existing applications.
我们开发了动态MLFMA的并行版本，称为**ScaleME（可扩展多极子引擎）**。ScaleME是使用消息传递接口(MPI)进行通信的可移植实现。它被实现为与应用程序无关的内核，可改造到现有应用中。

---

## 4.2 The MPI Programming Model / MPI编程模型

Message passing is a programming paradigm used widely on parallel computers. Each computing node consists of a processor and memory, connected through a network. Exchange of data between nodes is made through explicit messages.
消息传递是并行计算机上广泛使用的编程范式。每个计算节点由一个处理器和内存组成，通过网络连接。节点间的数据交换通过显式消息进行。

MPI is a standardized and portable message passing system designed to function on a wide variety of parallel computers. The MPI standard defines the user interface, syntax, and semantics of message passing functionalities, including point-to-point communication (send, receive) and collective communications (broadcast, etc.).
MPI是一种标准化、可移植的消息传递系统，旨在各种并行计算机上运行。MPI标准定义了消息传递功能的用户接口、语法和语义，包括点对点通信（发送、接收）和集合通信（广播等）。

In developing the parallel MLFMA, we have assumed the **single program multiple data (SPMD)** paradigm, where the same executable runs on all processors but execution graphs may vary.
在开发并行MLFMA时，我们采用了**单程序多数据(SPMD)**范式，即所有处理器运行相同的可执行文件，但执行图可能不同。

---

## 4.3 Mathematical Preliminaries / 数学预备

The basic principle behind FMM is to decompose the computation of matrix-vector products into two parts: nearby interactions (direct MoM) and well-separated interactions (using asymptotic representation of radiated fields).
FMM背后的基本原理是将矩阵-矢量乘积的计算分解为两部分：附近相互作用（直接MoM）和远距相互作用（使用辐射场的渐近表示）。

### 4.3.1 Diagonal Forms of Radiation Fields / 辐射场的对角形式

The radiation field outside a sphere containing all sources can be represented using outgoing multipole expansions. The key is the diagonal translation operator that allows efficient translation of radiation patterns between group centers.
包含所有源的球外辐射场可以用出射多极子展开表示。关键是允许在组中心之间高效传输辐射方向图的对角传输算子。

---

## 4.4 The Parallel MLFMA / 并行MLFMA

The general strategy of MLFMA is clustering basis functions at various spatial lengths and computing interactions with testing functions from sufficiently distant clusters using multipole expansions. For nearby interactions, direct computation is used.
MLFMA的一般策略是在不同空间尺度上对基函数进行聚类，并使用多极子展开计算与足够远聚类的测试函数的相互作用。对于附近的相互作用，使用直接计算。

### Data Distribution / 数据分布

In the parallel implementation, the tree structure of MLFMA is distributed across processors. Nonempty boxes at each level are partitioned among processors. The key challenge is balancing the computational load while minimizing communication overhead.
在并行实现中，MLFMA的树结构分布在多个处理器上。每层的非空盒子在处理器之间划分。关键挑战是在最小化通信开销的同时平衡计算负载。

### The Communication Patterns / 通信模式

The parallel MLFMA requires three main communication patterns / 并行MLFMA需要三种主要的通信模式：

1. **Aggregation communication / 聚合通信**：Upward tree traversal — children send outgoing expansions to parent / 向上树遍历——子节点向父节点发送出射展开
2. **Translation communication / 传输通信**：Exchange of outgoing expansions between well-separated groups across processors / 跨处理器的远距组之间交换出射展开
3. **Disaggregation communication / 分发通信**：Downward tree traversal — parents send incoming expansions to children / 向下树遍历——父节点向子节点发送入射展开

### Dynamic Load Balancing / 动态负载平衡

Due to the non-uniform distribution of basis functions, static load balancing is insufficient. ScaleME implements dynamic load balancing strategies that redistribute work at runtime to maintain efficiency.
由于基函数的非均匀分布，静态负载平衡是不够的。ScaleME实现了动态负载平衡策略，在运行时重新分配工作以保持效率。

---

## 4.5 Implementation Issues / 实现问题

### Memory Management / 内存管理

Each processor stores only the MLFMA data for its partition of the tree. The near-field interaction matrix is stored as sparse blocks, distributed across processors.
每个处理器仅存储其树分区对应的MLFMA数据。近场相互作用矩阵以稀疏块形式存储，分布在处理器上。

### Scalability / 可扩展性

The parallel efficiency of ScaleME has been demonstrated on problems with millions of unknowns. Strong scaling and weak scaling results show good performance up to hundreds of processors.
ScaleME的并行效率已在百万未知数级别的问题上得到验证。强可扩展性和弱可扩展性结果显示在数百个处理器范围内具有良好的性能。

### Portability / 可移植性

ScaleME is designed to be portable across different platforms, from commodity Linux clusters to high-end supercomputers with specialized interconnects.
ScaleME被设计为跨不同平台可移植，从普通的Linux集群到具有专用互联的高端超级计算机。

---

## 4.7 Numerical Results / 数值结果

### 4.7.1 Radar Cross Section of Aircraft / 飞机的雷达截面

Parallel MLFMA has been used to compute the RCS of complex aircraft targets with over 10 million unknowns, achieving near-linear speedup on large parallel systems.
并行MLFMA已被用于计算具有超过1000万未知数的复杂飞机目标的RCS，在大型并行系统上实现了接近线性的加速比。

### 4.7.2 Scattering from Ships / 舰船散射

Large-scale ship scattering problems with complex geometry have been solved efficiently using the parallel MLFMA, demonstrating the robustness of the implementation.
使用并行MLFMA高效地求解了具有复杂几何形状的大规模舰船散射问题，展示了实现的稳健性。

---

## 4.9 Conclusions / 结论

Parallel MLFMA enables the solution of extremely large-scale EM scattering problems that are intractable on single processors. The ScaleME implementation provides a portable, scalable framework for distributed memory parallel computing in computational electromagnetics.
并行MLFMA使得求解在单处理器上无法处理的极端大规模电磁散射问题成为可能。ScaleME实现为计算电磁学中的分布式内存并行计算提供了可移植、可扩展的框架。

---

## References / 参考文献

[1] V. Rokhlin, "Rapid solution of integral equations of scattering theory in two dimensions," *J. Comput. Phys.*, vol. 86, pp. 414–439, 1990.
[2] J. M. Song and W. C. Chew, "Multilevel fast-multipole algorithm for solving combined field integral equations of electromagnetic scattering," *Microwave Opt. Technol. Lett.*, vol. 10, pp. 14–19, 1995.
[3] J. M. Song, C. C. Lu, and W. C. Chew, "Multilevel fast multipole algorithm for electromagnetic scattering by large complex objects," *IEEE Trans. Antennas Propagat.*, vol. 45, pp. 1488–1493, 1997.
[4] MPI Forum, "MPI: A Message-Passing Interface Standard," http://www.mpi-forum.org.
[5] W. C. Chew, J. M. Jin, E. Michielssen, and J. M. Song, *Fast and Efficient Algorithms in Computational Electromagnetics*, Artech House, 2001.
