# Bondeson《Computational Electromagnetics》第8章

> **Source:** Anders Bondeson, Thomas Rylander, Pär Ingelström, *Computational Electromagnetics*, Springer 2005  
> **PDF:** pages 204-221 of 231 (231 total)

---

## Summary and Overview

8 Summary and Overview
successful hybrid methods oﬀer possibilities to treat signiﬁcantly larger classes
of problems.
One of the major challenges in CEM is to model systems that are elec-
trically large, that is, for which the spatial extent D is many wavelengths λ
in three dimensions. In this setting, it is useful to compare how the number
of ﬂoating-point operations and the memory requirements for the diﬀerent
methods scale with the wave frequency f for a system of ﬁxed spatial extent
(where we will consider objects with geometrical features that are on the order
of the wavelength or larger). Table 8.1 summarizes the scalings with frequency
for the methods treated in this book and the MLFMA extension of the MoM.
FEM/FDTD MoM-matrix MoM-MLFMA
Nitf 2
Nitf log f
Nitf 4
Nitf 2 log f
Table 8.1. Scalings for the number of operations with frequency f and the number
of iterations Nit.
It should be pointed out that there are multipliers in front of the scalings in
Table 8.1, and that these coeﬃcients can be quite signiﬁcant. For instance, the
multiplier is large for the MLFMA (which is a version of the MoM), so that the
application problems need to be quite large before this method is competitive.
However, the MLFMA is the most competitive full-wave method for very
large scale scattering problems, e.g., to compute the radar cross section for an
entire aircraft. In this chapter, we present a more detailed discussion of these
scalings. Also, we brieﬂy discuss a selection of other methods. There is a large
number of numerical algorithms in CEM, and it is beyond the scope of this
book to give a complete account.
8.1 Diﬀerential Equation Solvers
Diﬀerential equation solvers are used for both frequency- and time-domain
computations. They can be applied to both driven problems and eigenvalue
problems.
For diﬀerential equation solvers in frequency domain, one often uses iter-
ative solvers (especially in three dimensions), and brief introductions to this
subject are given in Appendices A and B. Generally, the number of iterations
needed for convergence scales as the square root of the condition number κ
of the matrix, where the condition number is the ratio of largest to smallest
eigenvalues of the matrix. The smallest eigenvalues of the curl-curl or Laplace
operator are independent of the resolution. The largest eigenvalues of these
second-order operators scale as 1/h2; see, e.g., (3.17). Given that the frequency
8.1 Diﬀerential Equation Solvers
f dictates the cell size h ∝1/f, the largest eigenvalue of a second-order oper-
ator scales as f 2. Therefore, the condition number κ = λmax/λmin ∝f 2, and
generally, the number of iterations scales as √κ = f. The matrix generated
by a diﬀerential equation formulation is sparse, so the number of operations
per iteration is proportional to the number of unknowns, i.e., ∝f 2 and ∝f 3
for 2D and 3D problems, respectively. Therefore, for frequency-domain FEM
(or ﬁnite diﬀerence methods) the total number of operations scales as f 3 in
2D and f 4 in 3D (for a single frequency).
For the diﬀerential equation solvers in time domain, the time-step varies
as h ∝1/f, and for a ﬁxed time interval the number of time-steps scales
as 1/∆t ∝f. Therefore, the number of operations for time-domain methods
(such as the FDTD) and the frequency-domain methods (e.g., FEM) scales as
f × f 2 = f 3 in 2D and f × f 3 = f 4 in 3D. But the time-domain method gives
a complete frequency spectrum, as compared to a standard frequency-domain
method that requires one computation for a single frequency.
In the following, unless stated otherwise, we focus on the scalings for 3D
methods.
8.1.1 Finite-Diﬀerence Time-Domain
To keep a certain relative phase error, the FDTD needs a certain number of
points per wavelength λ/h; 1% phase error requires about 18 cells per wave-
length. To keep this accuracy, the number of cells in any direction, D/h, scales
as f, while the maximum time-step scales as ∆t ∝h ∝f −1. Consequently, the
total number of operations scales as f 4. If one asks for a ﬁxed absolute phase
error across the whole system, the number space steps scales as f 3/2, and the
number of operations becomes O(f 6). In this case, higher-order methods are
more advantageous. So far, higher-order methods are not used very much for
electromagnetic problems, but work in this area is underway.
Time-domain methods generate time sequences that can be Fourier trans-
formed to give a full frequency spectrum in O(f 4) operations. This, plus the
simplicity of the FDTD, are the main reasons for its popularity. The ma-
jor drawback of the FDTD is that it is tied to structured grids, which force
oblique boundaries to appear as “staircases.”
8.1.2 Finite-Volume Time-Domain
Finite volume time-domain (FVTD) methods generate discrete equations by
integrating the Amp`ere and Faraday laws over each grid cell [88, 57]:
ϵEn+1 −En
dV =
ˆn × Hn+ 1
2 dS −
Jn+ 1
2 dV,
µHn+ 1
2 −Hn−1
dV = −
ˆn × EndS,
8 Summary and Overview
where superscripts indicate time. Two grids are used: the “primary” and
“dual” grids. The electric ﬁeld is deﬁned on the vertices of the primary grid
(cells Vh), and the magnetic ﬁeld is deﬁned on those of the dual grid (cells
Ve), the vertices of which are the centers of the primary cells. Unlike the
FDTD, the FVTD does not conserve electric and magnetic charges. Madsen
and Ziolkowski [44, 57] constructed an “FDTD correction” to accomplish this.
The FVTD is explicit and therefore eﬃcient, as long as the cells are of
reasonably uniform size; otherwise, very small time-steps are required, and
they degrade the performance of the method. The primary grid can be made of
tetrahedra, which gives the method good ability to model complex geometry. A
drawback of the FVTD is the appearance of a weak “late time” instability [44,
57, 89]. This can be prevented by adding dissipation, which, however, may
decrease the accuracy of the algorithm. The operation count scales the same
way as for the FDTD.
8.1.3 Finite Element Method
The ﬁnite element method easily handles complex geometry, and FEM is
used both in frequency- and time-domain analyses. Together with standard
iterative solvers, a frequency-domain calculation requires O(f 4) operations
per frequency. The scaling in time-domain calculations is the same as for the
FDTD, but time-domain FEM typically involves at least a factor of 10 more
operations.
A valuable property of the ﬁnite element method, in comparison to the
FVTD, is that both the mass matrix and the stiﬀness matrix are symmetric
and real, which guarantees that the eigenvalues ω2 of ∇× µ−1∇× E = ω2ϵE
are real. Combined with a suitable time-stepping scheme, this leads to a stable
algorithm. The symmetric, or reciprocal, property of the FEM appears not
to hold for ﬁnite volume discretizations. In fact, lack of symmetry is a likely
explanation of the late-time instability observed for many schemes.
8.1.4 Transmission Line Method
Transmission line methods (TLM) work with combinations of electric and
magnetic ﬁelds, represented as pulses propagating on a 3D grid of transmission
lines. At the intersections, the nodes, the pulses are scattered according to
scattering matrices S. By imposing the condition that S be unitary, energy
conservation can be enforced, and hence stability achieved.
TLM based on so-called expanded nodes was described by Hoefer [35].
An improved, symmetrical condensed node was introduced by Johns [40].
Celuch-Marcysiak and Gwarek [16] proved the equivalence of a transmission
line network with a circuit model for a nonuniform grid in 2D. An equivalence
with an FDTD formulation was established on a uniform 3D grid by Chen et
al. [17].
8.2 Integral Equation Solvers
8.1.5 Finite Integration Technique
The ﬁnite integration technique [84] (FIT) is based on the integral represen-
tation of Maxwell’s equations. The FIT reduces to the FDTD scheme on grids
consisting of cubes, and for that case, the derivation of the FIT is very similar
to the integral representation in Section 5.2.4. The ﬁelds are represented in
terms of electric and magnetic voltages (organized in the vectors ¯e and ¯h,
respectively). These are related to the electric and magnetic ﬂuxes (organized
in the vectors ¯¯d and ¯¯b, respectively) by the constitutive relations (expressed
as ¯¯d = Mϵ¯e and ¯h = Mµ−1 ¯¯b). Maxwell’s equations (in source-free space) can
then be written in the form
C¯e = −d
¯¯b,
C¯h = d
¯¯d.
For wave problems, the time derivatives are discretized in the leap-frog sense.
Here, C and C are the curl operators (matrices with elements 0 or ±1) on the
primary and dual meshes, respectively. Similarly, Gauss’s law can be stated
D¯¯d = q, and the condition of solenoidal magnetic ﬂux density as D¯¯b = 0,
where D and D represent the divergence on the primary and dual meshes,
respectively. The matrix corresponding to the gradient operator is then the
transpose of the divergence matrix. The matrix operators correctly repro-
duce well-known properties; for example, the zero divergence of the curl is
DC = 0 and the zero curl of the gradient is C DT = 0. This allows for var-
ious manipulations; for example, the vector wave equation can be written as
CMµ−1C¯e + Mϵ∂2¯e/∂t2 = 0.
Weiland and coworkers [78, 69] have investigated stable local reﬁnement
and nonorthogonal meshes for the FDTD scheme. The property C = CT is
important for stability, and the (typically) diagonal matrices Mϵ and Mµ−1
allow for explicit time-stepping. Thus, the FIT has the same scalings as the
FDTD, but it allows for curved meshes and local reﬁnement combined with
stable time-stepping.
8.2 Integral Equation Solvers
For integral equations, the number of unknowns is much smaller than for
volume discretizations such as FDTD or FEM, but the matrix is dense. The
integral formulation is nevertheless superior for large problems because of
a rather recent development called the fast multipole method (FMM). The
hierarchical version of this method is called the MLFMA, multilevel fast mul-
tipole algorithm [19]. The operation count then becomes ∝Nitf log f in 2D
and Nitf 2 log f in 3D. This is superior to the diﬀerential equation solvers if
Nit < O(f 2), which is generally the case. The drawback of the MLFMA is
8 Summary and Overview
that it is quite complicated to program, and in particular, to parallelize. In-
tegral equation methods, or the method of moments, solve either the EFIE,
MFIE, or the CFIE [51] on surfaces of conductors and dielectrics.
8.2.1 Frequency-Domain Integral Equations
In frequency-domain formulations, both the EFIE and the MFIE may suf-
fer from internal resonance; this can be avoided by using a suitable linear
combination of the two equations: the CFIE.
A main advantage of the MoM is the low number of unknowns, which scale
with frequency as O(f 2). The drawback is that the matrix is dense. Therefore,
if one attempts direct solution by LU decomposition, the operation count
has a very unfavorable O(f 6) scaling. In geometries that are only partly 3D,
this can be improved on by Fourier transformation in the main direction of
symmetry [42] or by using the Toepliz property of the MoM matrix to apply
CG-FFT techniques [51]. However, for truly 3D problems other methods for
solving the linear system are needed.
Iterative solvers, such as the conjugate gradient (CG) method or Krylov
methods, improve the scaling. The iterative algorithms are based on matrix–
vector multiplications, and with a dense matrix a conventional multiplication
takes O(f 4) operations. The total operation count then becomes O(Nitf 4),
where the number of iterations Nit can be hard to predict. Song and Chew [72]
report Nit ∝f 1/2 for problems with only closed surfaces. Thus, the scaling
becomes f 4.5 for each frequency, which is not competitive with diﬀerential
equation solvers. However, recently several methods have been developed to
reduce the number of operations for a matrix–vector multiplication, that is,
in computing the ﬁeld from given sources.
Fast Multipole Methods
A very successful scheme to replace the matrix multiplication is the fast mul-
tipole method (FMM) introduced by Rokhlin [58, 59] and developed into the
multilevel fast multipole algorithm (MLFMA) by a group at the University
of Illinois [73].
The FMM is described in an accessible way in [20]. The ﬁrst step is to
divide the simulation region into boxes, each containing a moderate number of
grid cells. Fields from grid cells in the same, or an adjacent, box are computed
in the standard way. The ﬁelds produced by sources farther away are computed
by ﬁrst generating a multipole expansion for the sources, then projecting this
onto a set of plane waves in the observation box, from which one obtains the
ﬁelds at each observation point. The savings come from the fact that only a
moderate number L of terms are needed in the multipole expansion. A semi-
empirical formula for the number of terms needed to achieve double precision
accuracy is L = kD + 10 ln(π + kD), and the required number of plane waves
scales as L2. Minimizing the total number of operations, one ﬁnds that the
8.2 Integral Equation Solvers
optimum number of elements per box scales as the square root of the total
number of elements N and that the total operation count scales as N 3/2.
The MLFMA repeats this algorithm in a hierarchical way on all scales and
achieves a scaling O(N log N). This algorithm has been implemented in the
FISC code [74].
A nice analogy of the FMM is a telephone network. If every one of N
customers is connected by a direct line to every other customer, the number
of connections scales as N 2. However, by introducing “hubs,” the number of
connections can be reduced. To make a telephone call, a customer (the source
point) calls the local hub (the multipole expansion), which calls another hub
(the plane waves), which ﬁnally calls the recipient of the call (the observation
point).
We can conclude that for 3D problems the FMM gives an O(f 3) and the
MLFMA an O(f 2 log f) scaling for the operation count per iteration. These
represent signiﬁcant reductions from the O(f 4) scaling for straightforward
matrix–vector multiplication. If the number of iterations scales as f 1/2, the
frequency-domain MoM is clearly competitive with time-domain diﬀerential
equation solvers for large problems. However, it takes a problem of signiﬁcant
size for the FMM or MLFMA to be competitive, with at least several thousand
unknowns. The FMM and MLFMA also imply large savings in storage because
the full matrix is never stored.
Other Fast Methods
The impedance matrix localization technique (IML) [14, 15] is a matrix alge-
bra routine that transforms to a basis for the source distribution that radiates
into narrow beams. This makes the MoM matrix sparse. The method can be
incorporated in existing MoM programs to sparsify an already computed ma-
trix.
Also, wavelet transforms have been used in MoM calculations [81, 28].
Wavelet transforms work excellently in static problems where the integral ker-
nel is nonoscillatory, and reduce the operation count to O(N log N). For elec-
trically large systems (D ≫λ) with oscillatory kernels, Wagner and Chew [81]
found that the standard wavelet transform reduces the number of operations
only to βN 2, with β ≈0.1. More recently, Golik [28] tested discrete wavelet
packet similarity transformations together with thresholding of the matrix el-
ements. As the system size was increased, with a ﬁxed number of cells per
wavelength, the number of nonzero matrix elements scaled more slowly than
N 2; the numerical results suggested an O(N 4/3) scaling.
8.2.2 Time-Domain Integral Equations
Time-domain integral equations (TDIE) is a relatively new area of research.
The ﬁrst approaches straightforwardly discretized the time-domain form of
8 Summary and Overview
the EFIE [63, 54] and the MFIE [71] in space and time. The time-domain
MFIE can be written as
2πJ(r, t) = 2πˆn × Hi(r, t) + ˆn ×
J(r ′, τ) + R
∂J(r ′, τ)
R2 dS′,
(8.1)
where τ = t −R/c is the retarded time and R = |r −r ′|. In the discretized
version, the solution has to be saved over the time that it takes a light wave
to traverse the entire simulation region, so the storage requirement for the
solution scales as f 3 (as for a volume discretization). The matrix storage scales
as f 4, so that for very large problems the matrix may have to be recomputed,
or some fast scheme is needed for the ﬁeld calculation. The operation count
scales as f 5, which is worse than for diﬀerential equation solvers.
The early TDIE algorithms were unstable and required dissipation for
stability [71, 80]. This problem appears to have been overcome recently for
the EFIE by a variational formulation together with strict FEM techniques
both in space and time [1].
Another TDIE solver has been developed by Walker and coworkers [10,
24] for the MFIE. Applying ﬁnite element techniques to (8.1), Bluck and
Walker [10] derived an algorithm that is somewhat implicit. The algorithm
needs to be implicit, because on every new time-level, “new,” or unknown,
currents enter into the surface integral in (8.1) within regions of radius c∆t
around each observation point. The resulting implicit algorithm was found
to be stable if the time-step exceeds the time it takes a light wave to tra-
verse the largest spatial element. (The degree of implicitness increases with
the time-step.) This code has been used to compute scattering data when the
scatterer is illuminated by a short pulse of duration ∝f −1; see [24]. In this
mode of operation, the operation count scales very favorably with frequency.
This is because the number of elements, both in the region where one needs
to integrate (illuminated source points) and in the region where the resulting
ﬁeld is signiﬁcant (illuminated observation points), scales only as f. It is su-
perﬂuous to calculate near-vanishing ﬁelds in the nonilluminated regions, and
this strongly reduces the operation count if the incoming pulse is short (and
the scattering surface is convex so that there are no multiple reﬂections).
8.3 Hybrid Methods
The diﬀerent basic techniques used in CEM all have their strengths and lim-
itations. One way to achieve performance that is better than two individual
methods is to combine them into a so-called hybrid method. This can be dif-
ﬁcult but very useful once a good and reliable formulation is found. There is
a vast number of hybrid methods, and here we mention only a few of them in
order to introduce the concept of hybridization.
8.3 Hybrid Methods
The FDTD is eﬃcient, but has diﬃculties with complex geometry. There-
fore, hybrid methods have been formulated to combine eﬃciency with the abil-
ity to treat complex geometry. The hybrid schemes combine the FDTD with
either an FVTD [88, 57, 89] or time-domain FEM [86, 47]. These methods
typically experience late-time instabilities [89, 47]. Rylander and Bondeson
formulated a stable hybrid scheme [60] that combines the FDTD with FEM
on unstructured meshes. Where the structured and unstructured grids join,
the mass and stiﬀness matrices are constructed in a special way to preserve
symmetry. This makes it straightforward to achieve stability without dissipa-
tion. The scheme uses an implicit solver on the unstructured grid. It has been
veriﬁed that the algorithm is stable for time-steps up to the stability limit of
the FDTD. The advanced TLM, FIT, and hybrid FEM-FDTD are eﬃcient
and stable solvers that can handle complex geometry. The FEM-FDTD com-
bination may have an advantage in being more easily coupled to standard grid
generators and is more adequate for adaptive mesh reﬁnement.
When diﬀerential equation solvers are applied to problems in unbounded
geometries, the computational region must be truncated. Several methods for
radiative boundary conditions have been formulated for diﬀerential equations
solvers, where the perfectly matched layers [8, 52] is the preferred choice in
most cases. For electrically very large problems, the volume discretizing solvers
ﬁnd competition from recently developed integral equation methods, which are
well suited to analyze objects in free-space. For open-region problems that in-
volve objects with complicated materials, it can be useful to use a FEM for
the object and its immediate surrounding, combined with a MoM for the re-
maining free-space environment. It is feasible to construct frequency-domain
formulations that combine the MoM and FEM. These are often referred to as
ﬁnite element–boundary integral formulations, or FE-BI for short. The FE-BI
formulation by Botha and Jin [12] is based on variational principles for the
continuous quantities, and it yields symmetric matrices that preserve reci-
procity explicitly, which reﬂects important properties of Maxwell’s equations.
Large Linear Systems
A.1 Sparse Matrices
Many CEM problems require the solution of large linear systems of equa-
tions. This is generally the case for the ﬁnite element method (FEM), both
for frequency- and time-domain applications. In realistic 3D applications, the
number of unknowns can be in the range of tens of thousands to several
millions. For the largest systems, direct inversion is seldom possible, and it-
erative methods are needed. Here, we will introduce some routines for large
linear systems.
Below, we give a MATLAB function that assembles the sparse system
that we solved using Gauss–Seidel iterations in the capacitance calculation in
Chapter 3. The study was then limited to a 50 × 50 grid. With the assembled
system we can use more eﬃcient methods and therefore use higher resolutions.
For this 2D problem, the direct solver invoked by “\” in MATLAB performs
very well.
We write the discretized problem as Af = s and use the MATLAB function
setAs listed below to set A and s. Note that this script was written so as to
make very few references to the sparse matrix. This is faster than referencing
the individual elements in the sparse matrix, because each reference requires
a function call, which is quite slow.
% --------------------------------------------------------------
% Set up matrix A and right-hand side s
% --------------------------------------------------------------
function [A, s] = setAs(a, b, c, d, n, m)
% Arguments:
width of inner conductor
= height of inner conductor
width of outer conductor
= height of outer conductor
= number of points in the x-direction (horizontal)
= number of points in the y-direction (vertical)
A Large Linear Systems
% Returns:
= matrix on sparse storage format
= right-hand side on sparse storage format
hx = 0.5*c/n;
% Grid size in x-direction
na = round(0.5*a/hx);
% Number of cells for half width of
% inner conductor
hy = 0.5*d/m;
% Grid size in y-direction
= round(0.5*d/hy);
% Number of cells for half height of
% outer conductor
mb = round(0.5*b/hy);
% Number of cells for half height of
% inner conductor
= 1;
% Potential on inner conductor
The upper right corner is discretized
--------------------+
------------+
| d/2
| b/2
(Dimensions)
The nodes are numbered like this
% (m-1)hy| (m-1)n+1 (m-1)n+2 (m-1)n+3
2n+1
2n+2
2n+3
--------------------------------------> x
2 hx
(n-1)hx
(Discretization)
= n * m;
% Total number of unknowns.
cx = hxˆ-2;
cy = hyˆ-2;
% Generate a matrix with N = m*n rows (-> nodes on the grid),
% and five columns, one for each nonzero diagonal of A.
% The first column gives contribution from nodes beneath.
% The second column gives contribution from nodes to the left.
A.1 Sparse Matrices
% The third column gives self-contribution.
% The fourth column gives contribution from nodes to the right.
% The fifth column gives contribution from nodes above.
% The following lines assume some knowledge of MATLAB.
If you
% feel uncertain, insert the ’keyboard’ command.
This causes
% MATLAB to stop.
Then execute lines by ’dbstep’ and examine
% the result.
C = repmat([cy cx -2*(cx+cy) cx cy], N, 1);
% Find indices of nodes that are not surrounded by four interior
% nodes.
idx0R = n:n:N-n;
% Nodes with
V = 0 to the right
idxNB = na+2:n;
% Nodes with dV/dy = 0 beneath
idxNL = 1+n*(mb+1):n:N;
% Nodes with dV/dx = 0 to the left
idx1C = repmat((1:na+1)’, 1, mb+1) + repmat((0:n:n*mb),na+1,1);
% ’x-index + n*(y-index-1)’ for all
idx1C = idx1C(:)’;
% nodes on (or inside) the inner
% conductor where V = 1
% and convert to row vector
C(idx1C,[1 2 4 5]) = 0;
C(idx1C, 3) = 1;
C(idx0R, 4) = 0;
C(idxNB, 5) = 2*cy;
C(idxNL, 4) = 2*cx;
C(idxNL, 2) = 0;
% Find the nonzero elements (si) of each column and the
% corresponding row indices (ii).
Do not include elements
% corresponding to nodes outside the grid.
[i1,j,s1] = find(C(n+1:end,
1)); % The first ’nc’ nodes have no
% neighbors beneath
[i2,j,s2] = find(C(1+1:end,
2)); % The first node has no
% neighbor to the left
[i3,j,s3] = find(C(
1:end,
3));
[i4,j,s4] = find(C(
1:end-1, 4)); % The last node has no
% neighbor to the right
[i5,j,s5] = find(C(
1:end-n, 5)); % The last ’nc’ nodes have no
% neighbors above
% Put the elements (si) into a sparse matrix. The first input
% are row indices, the second is column indices and the third
% is the elements.
A = sparse([i1+n; i2+1; i3; i4; i5], ...
[i1; i2; i3; i4+1; i5+n], ...
[s1; s2; s3; s4; s5], N, N);
A Large Linear Systems
s = sparse(idx1C’, 1, p, N, 1);
A.2 Solvers for Large Sparse Systems of Equations
As we already mentioned, the 2D discretized Laplace equation can be solved
in MATLAB by direct inversion f = A\s. For 2D problems, direct methods
are generally very competitive, unless the problems are very large. However,
for 3D problems, iterative solvers are often more eﬃcient. We will here give a
brief overview of solvers for sparse linear systems of equations that are used
in CEM.
A.2.1 Direct Solvers
In direct methods, a complete factorization (e.g., an LU decomposition) of
the matrix A is done. Clever reordering of the rows and the columns of A
plays an important role; a good reordering scheme can reduce the operation
count and the memory requirements for the factorization by more than an
order of magnitude. In MATLAB, one can, for example, use column approxi-
mate minimum degree permutation, colamd (for nonsymmetric matrices), or
symmetric approximate minimum degree permutation, symamd (for symmet-
ric matrices), to reorder matrices. However, when the backslash operator “\”
is invoked, this is done automatically.
A major advantage of direct methods compared to iterative methods is
that since a complete factorization is done, additional right-hand sides can be
solved for with low additional cost. Another advantage is that direct methods
generally are less sensitive to ill conditioning and can be used where many
iterative methods fail to converge.
However, both time and memory requirements scale unfavorably with
problem size; hence direct methods become prohibitively expensive for very
large problems. Often the memory requirements are the limiting factor.
Eﬃcient, freely available algorithms for direct factorization and reordering
of sparse matrices include UMFPACK [22], SuperLU [23], TAUCS [79], and
METIS [41].
A.2.2 Iterative Solvers
The matrices that result from ﬁnite element discretizations of Poisson’s equa-
tion (1.3) or the time-domain version of the curl-curl equation (6.72) are
symmetric and positive deﬁnite. For such systems, iterative so-called Krylov
methods (see Appendix B) generally work very well.
However, to speed up the convergence of the iterative algorithm, it is very
useful to precondition the matrix. The idea of preconditioning is to ﬁnd an
approximate inverse of A, say M−1, and multiply Af = s by the approximate
A.2 Solvers for Large Sparse Systems of Equations
inverse from the left. If M−1A ≈I, the iterative solver will converge much
faster. The choice of preconditioner generally has a much stronger eﬀect on
the speed of convergence than the choice of Krylov method. A choice that
often works well is the so-called incomplete LU decomposition, in which M =
LU ≈A, with L a lower triangular and U an upper triangular matrix. Then
M−1 = U−1L−1, which is inexpensive to apply if L and U are sparse. When
A is symmetric, the factorization can be made such that U = LT , and this is
called incomplete Cholesky decomposition. The degree of incompleteness can
be speciﬁed by how much ﬁll-in is allowed in L and U, that is, how many
extra nonzero elements L and U have in comparison with A. In MATLAB,
this is controlled by setting a relative tolerance below which elements in L
and U are dropped. This tolerance is chosen as a compromise between good
accuracy of the decomposition (favored by a small tolerance) and minimizing
memory and CPU time for a matrix multiplication (which is favored by a high
tolerance).
Also in the case with incomplete factorizations, it is strongly recommended
to reorder the rows and columns of A before the incomplete factorization is
computed.
Another, less complicated, preconditioner is symmetric successive overre-
laxation (SSOR) [6], in which the preconditioning matrix M never is stored
explicitly. Hence the memory requirements are smaller when SSOR is used as
a preconditioner instead of some incomplete factorization of A.
An important note is that for the time-harmonic version of the curl-curl
equation, and for low-frequency eddy current computations (Section 6.6.3),
the null-space of the curl operator causes problems for the Krylov methods,
and therefore more advanced preconditioners [43, 25, 26] are required.
Reliable implementations of Krylov methods and preconditioners are avail-
able, e.g., in the PETSc library [5]. Also MATLAB provides implementations
of many popular Krylov methods.
A.2.3 Multigrid Methods
The multigrid (MG) method [31, 85] was introduced about four decades ago,
but has only very recently been applied to Maxwell’s equations [34]. The MG
method can be used either as an iterative solver on its own, or as a very
eﬃcient preconditioner for iterative Krylov methods. It greatly improves the
convergence rate of iterative solvers for large sparse matrices that occur in
diﬀerential equation formulations. In fact, the convergence rate can be made
independent of the cell size h, rather than to scale as some power of h.
The underlying principle is the observation that for the Laplace equation,
the “short-wavelength error” (which varies on the scale of the grid) is re-
duced quickly by local operations (known as smoothers) such as Jacobi or
Gauss–Seidel iterations; see Section 3.1.1. However, the long-wavelength error
is reduced much more slowly by the smoothers. Since such error has short
wavelength with respect to a coarser grid, one expects that this error can be
A Large Linear Systems
reduced more rapidly on a coarse grid. Therefore, the basic idea of MG is to
introduce a hierarchy of grids, starting from the ﬁnest one, and try to improve
the solution on the ﬁner grid by looking for a correction from the coarser grid.
Optimally, the coarsest grid has only a small number of cells, and a direct
solver can be used at a low computational cost.
So far, MG is used mostly for electrostatic and magnetostatic problems [67,
56] and transient eddy current problems. Generally, MG is among the most
eﬃcient solvers [31, 56] for Laplace-type equations. However, little research
on MG has been devoted to fully electromagnetic problems, such as time-
harmonic problems for eddy current computations [7, 33]. Certain diﬃculties
(due to the null-space of the curl-curl operator) are encountered when this
method is applied to the full Maxwell’s equations. For wave problems, another
complicating aspect is that the coarsest grid must resolve the wavelength
λ ∝1/f, which limits the hierarchy of grids and therefore the recursive MG
algorithm.
A.3 Capacitance Calculation on Larger Grids
With the more eﬃcient solvers we can extend the capacitance calculation of
Section 3.1 to much larger grids. Results for grids up to 400 by 400 are shown
in Table A.1.
n h × 102
C [pF/m]
2.000
90.78080 583
1.000
90.68006 976
0.500
90.64044 979
0.333
90.62961 567
0.250
90.62481 230
Table A.1. Capacitance vs. cell size for ﬁnite diﬀerence solution on larger grids.
One can estimate the order of convergence from formula (2.4) for 100, 200,
and 400 points, and the order of convergence in h comes out as 1.341. This
is close to the asymptotic result 4/3, which occurs for the 270o corners. If we
do polynomial ﬁts to h4/3, the extrapolated value is 90.6145 pF/m. It should
be pointed out that a higher-order ﬁt to noninteger powers of h, such as h4/3,
is not an optimal representation, because the regular parts of the solution
contribute errors that scale as h2. Nevertheless, the extrapolation has added
three ﬁgures of accuracy. If we tried to achieve this accuracy by a single
calculation with uniform reﬁnement of the grid, we would have to decrease h
by more than a factor of 100, and the execution time would increase by at
least 1003, that is, one million times. Evidently, extrapolation can be a very
A.3 Capacitance Calculation on Larger Grids
eﬃcient way of increasing the accuracy. In the chapter on ﬁnite elements, we
show that the accuracy can also be improved by adaptive grid reﬁnement,
which aims at increasing the resolution in regions where the solution varies
rapidly.
Krylov Methods
Here, we will discuss some iterative methods for solving large linear systems
of equations
Ax = b.
(B.1)
For large 3D problems, it is generally too demanding to use a direct solver.
Iterative, so-called Krylov methods are often a much better choice for these
problems. Multigrid methods, which we discussed very brieﬂy in Section A.2.3,
have proven even more eﬃcient for many problems but will not be discussed
here.
B.1 Projection Methods
In projection methods, one minimizes the residual
r = b −Ax
(B.2)
by an approach similar to the Galerkin and Petrov–Galerkin methods for
ﬁnite elements. The vector x will be constructed as a sum of basis vectors
v; x = x0 + m
i=1 viyi, and y is an array of coeﬃcients. This can be written
compactly by introducing the matrix V = (v1, v2, . . . , vm) and the column
vector y = (y1, y2, . . . , ym)T :
x = x0 + Vy.
(B.3)
The vectors v1, v2, . . . , vm span a space Km of “basis” vectors. Similarly, one
chooses a space Lm of “test” vectors w1, w2, . . . , wm and demands that on
the mth step of the iteration the residual rm be orthogonal to all vectors in
Lm. If Km = Lm, this is Galerkin’s method; otherwise, it is a Petrov–Galerkin
method.
The most important part of the iteration is the choice of the search direc-
tions v1, v2, . . . , vm. The simplest case is that in which A is real and symmet-
ric. The old-fashioned “steepest descent” method chooses the increment di-
rections vi in the gradient direction of the error functional (x−xexact)T A(x−
B Krylov Methods
xexact), on every step of the iteration. It turns out that this is a bad strategy.
When the matrix A is positive deﬁnite and symmetric, the number of iter-
ations for the steepest descent method scales as the condition number of A,
that is, the ratio of largest to smallest eigenvalues, κ = λmax/λmin.
B.2 Krylov Methods
A better strategy is to generate the increment directions as r0, Ar0, A2r0,
. . . , Am−1r0, where r0 is the ﬁrst residual. Then K is called a Krylov space.
The Arnoldi algorithm does exactly this and projects out components of the
new v’s to keep them orthonormal.
Choose a vector v1 of norm 1
For j = 1, 2, . . . , m, Do:
hij = (Avj, vi) for i = 1, 2, . . . , j
wj = Avj −j
i=1 hijvi
hj+1,j = (wj, wj)1/2
If hj+1,j = 0 then Stop
vj+1 = wj/hj+1,j
EndDo
GMRES is Arnoldi’s method followed by a minimization of (r, r). This is a
reliable method, and it has the nice property that the error decreases mono-
tonically with the iteration number. The disadvantage of GMRES is that one
needs to store all the incremental directions v1, . . . , vm to do the minimiza-
tions. Therefore, it can become very memory-demanding if the number of
iterations is large. To circumvent the memory problem, one can restart GM-
RES after a certain number of iterations (typically 5 to 50). However, at the
restart, orthogonality is lost.
There are cleverer ways of generating the incremental directions v. The
standard method, which assumes that A is symmetric, is the Lanczos method.
Here it suﬃces to save three increment directions.
Choose a start vector v1 of norm 1.
Set β1 = 0, v0 = 0
For j = 1, 2, . . . , m, Do:
wj = Avj −βjvj−1
αj = (wj, vj)
wj = wj −αjvj
βj+1 = (wj, wj)1/2. If βj+1 = 0 then Stop
vj+1 = wj/βj+1
EndDo
This makes all the vectors vi, i = 1, 2, . . . , orthogonal (in inﬁnite-precision
B.3 Nonsymmetric A
arithmetic). With ﬁnite precision, orthogonality may be lost if the iteration
runs many steps. Consequently, the iteration may have to be restarted.
A method that is related to the Lanczos method is the conjugate gradient
(CG) method, where one keeps going in orthogonal directions. At least with
inﬁnite-precision arithmetic, this method can guarantee convergence when
the number of steps equals the number of unknowns. The CG method for a
symmetric A can be written as follows:
Compute r0 = b −Ax0, p0 = r0
For j = 0, 1, . . . , until convergence, Do:
αj = (rj, rj)/(Apj, pj)
xj+1 = xj + αjpj
rj+1 = rj −αjApj
βj = (rj+1, rj+1)/(rj, rj)
pj+1 = rj+1 + βjpj
EndDo
An advantage of the CG method is that one does not store the whole history of
incremental directions. For positive deﬁnite symmetric matrices, the required
number of iterations for CG is proportional to the square root of the condition
number of the matrix.
B.3 Nonsymmetric A
Lanczos Biorthogonalization
The symmetric Lanczos algorithm can be extended to nonsymmetric matrices.
The biorthogonal Lanczos algorithm constructs a pair of biorthogonal bases
v1, Av1, . . . , Am−1v1,
w1, AT w1, . . . , (AT )m−1w1,
with the orthogonality property (vi, wj) = δij. The procedure can be written
as follows:
Choose two vectors v1, w1 such that (v1, w1) = 1.
Set β1 = δ1 = 0, v0 = w0 = 0
For j = 1, 2, . . . , m, Do:
αj = (Avj, wj)
ˆvj+1 = Avj −αjvj −βjvj−1
ˆwj+1 = AT vj −αjwj −δjwj−1
δj+1 = |(ˆvj+1, ˆwj+1)|1/2. If δj+1 = 0 Stop
βj+1 = (ˆvj+1, ˆwj+1)/δj+1
wj+1 = ˆwj+1/βj+1, vj+1 = ˆvj+1/δj+1
EndDo
