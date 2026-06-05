# 程守洙《普通物理学》电磁学部分 第1章：电场

> **来源：** 谢处方等，《电磁场与电磁波》，第1章
> **提取方式：** 📷 扫描PDF → OCR → 人工清洗

---

## 1.1 电场 | Electric Field

# David K. Cheng《Field and Wave Electromagnetics》2nd Ed Chapter 1
 本笔记基于  文本清洗整理100% 来源于原书内容
## Chapter 1 — The Electromagnetic Model
### 1-1. Introduction
Electromagnetics is the study of the effects of **electric charges at rest and in motion**. From elementary physics we know there are two kinds of charges: positive and negative. Both are sources of electric fields. Moving charges produce a current, which gives rise to a magnetic field. $\mathbf{A}$ time-varying electric field is accompanied by a magnetic field, and vice versa — resulting in a coupled **electromagnetic field**. Under certain conditions, time-dependent electromagnetic fields produce waves that radiate from the source.
### 1-2. The Electromagnetic Model
#### Deductive vs. Inductive Approach
There are two fundamental approaches to developing a scientific subject:
- **Inductive approach**: Follows historical development — from simple experiments to general principles (e.g., Coulomb's law \rightarrow Gauss's law \rightarrow Maxwell's equations).
- **Deductive (axiomatic) approach**: Postulates a few fundamental relations for an idealized model; axioms are validated by their ability to predict consequences that agree with experiment.
This book uses the **deductive approach** because it is more elegant and enables orderly development.
#### Three Essential Steps in Building a Theory
1. **Define basic quantities** (source and field quantities).
2. **Specify the rules of operation** (vector algebra, vector calculus, partial differential equations).
3. **Postulate fundamental relations** (based on numerous experimental observations).
#### Charge as a Source Quantity
We use the symbol $q$ (or $Q$) to denote **electric charge**. Electric charge is a fundamental property of matter and exists only in positive or negative integral multiples of the charge on an electron:
$$q = \pm N e, \quad N = 1,2,3,\ldots$$
where $e = 1.602 \times 10^{-19}$ C.
**Example:** $\mathbf{A}$ coulomb is a very large unit — it takes $1 / (1.602 \times 10^{-19}) \approx 6.25 \times 10^{18}$ electrons to make up $-1$ C. Two $1$-C charges $1$ m apart exert a force of approximately $10^9$ N (about 1 million tons) on each other.
#### Charge Density Functions
For large-scale (macroscopic) theory, we use smoothed-out average density functions:
- **Volume charge density** (scalar):
$$\rho = \frac{\Delta q}{\Delta v} \quad \text{(C/m}^3\text{)}, \qquad \rho = \lim_{\Delta v \to 0} \frac{\Delta q}{\Delta v}$$
- **Surface charge density** (scalar):
$$\rho_s = \lim_{\Delta $\mathbf{S}$ \to 0} \frac{\Delta q}{\Delta S} \quad \text{(C/m}^2\text{)}$$
- **Line charge density** (scalar):
$$\rho_\ell = \lim_{\Delta \ell \to 0} \frac{\Delta q}{\Delta \ell} \quad \text{(C/m)}$$
#### Current
Current is the rate of change of charge with respect to time:
$$I = \frac{dq}{dt} \quad \text{($\mathbf{A}$ = C/s)}$$
where $I$ may itself be time-dependent. The **volume current density** $\mathbf{J}$ (vector) relates to current $I$ through a surface:
$$I = \int_$\mathbf{S}$ \mathbf{J} \cdot d\mathbf{S} \quad \text{($\mathbf{A}$)}$$
### 1-3. SI Units and Universal Constants
The book uses the **rationalized SI (MKSA) system** — rationalized because the factor $4\pi$ does not appear in Maxwell's equations (it appears instead in Coulomb's law). See **Appendix $\mathbf{A}$** for the complete table of fundamental and derived quantities.
**Fundamental SI units:** meter (m), kilogram (kg), second (s), ampere ($\mathbf{A}$).
Key universal constants (free space):
| Constant | Symbol | Value |
|---|---|---|
| Speed of light | $c$ | $2.998 \times 10^8$ m/s |
| Permittivity of free space | $\varepsilon_0$ | $8.854 \times 10^{-12}$ $\mathbf{F}$/m |
| Permeability of free space | $\mu_0$ | $4\pi \times 10^{-7}$ $\mathbf{H}$/m |
$$\varepsilon_0 = \frac{1}{\mu_0 c^2}$$
### Review Questions (Chapter 1)
1. What is the difference between the inductive and deductive approaches in electromagnetics?
2. What are the three essential steps in building a theory on an idealized model?
3. What is the principle of conservation of electric charge?
4. Distinguish between volume charge density, surface charge density, and line charge density.
5. Define current and volume current density.
---