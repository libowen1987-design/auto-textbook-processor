"""
jin_ch12_examples.py
Jin CEM 2nd Ed., Chapter 12: Concluding Remarks
Examples: overview of CEM methods, comparison of applicability.
"""
import numpy as np
import matplotlib.pyplot as plt


def cem_methods_overview():
    """Visual comparison of CEM methods across problem size and complexity."""
    methods = [
        ("MoM (direct)", 1e3, 1e7, 0.1, 0.4),
        ("MoM (MLFMA)", 1e4, 1e8, 0.3, 0.6),
        ("FEM (direct)", 1e3, 1e7, 0.2, 0.5),
        ("FEM (iterative)", 1e4, 1e8, 0.3, 0.5),
        ("FDTD", 1e5, 1e9, 0.4, 0.7),
        ("PO/GTD", 1e7, 1e12, 0.6, 0.9),
        ("SBR", 1e6, 1e11, 0.5, 0.8),
    ]
    
    fig, ax = plt.subplots(figsize=(10, 5))
    
    for name, min_N, max_N, min_c, max_c in methods:
        x = [min_N, max_N]
        y = [min_c, max_c]
        ax.fill_between(x, y, alpha=0.3)
        ax.plot(x, y, lw=1.5, label=name)
        ax.text(np.sqrt(min_N*max_N), (min_c+max_c)/2, name,
                ha='center', va='center', fontsize=9, fontweight='bold')
    
    ax.set_xscale('log')
    ax.set_xlabel("Problem size (unknowns / cells)")
    ax.set_ylabel("Geometric complexity")
    ax.set_title("CEM Method Applicability Map")
    ax.set_ylim(0, 1)
    ax.grid(True, alpha=0.3, which='both')
    
    plt.tight_layout()
    plt.savefig("/home/ubuntu/.openclaw/workspace/textbooks/jin/figures/jin_ch12_fig_overview.png",dpi=150)
    plt.close()
    print("[OK] CEM methods overview plot saved.")


def method_selection_guide():
    """Simple decision tree for method selection."""
    print("="*55)
    print("CEM Method Selection Guide")
    print("="*55)
    print()
    print("  Is the problem electrically large?")
    print("    YES (>100 lambda) → Asymptotic methods:")
    print("      • PEC/curved surfaces → PO + PTD")
    print("      • Multiple reflections → SBR")
    print("      • Canonical geometries → GTD/UTD")
    print()
    print("    NO (electrically moderate/small):")
    print("      Is geometry complex/heterogeneous?")
    print("        YES → FDTD or FEM")
    print("          • Simple shapes, uniform grid → FDTD")
    print("          • Curved/irregular geometry → FEM")
    print("        NO → MoM (exterior) or FEM (interior)")
    print("          • Homogeneous objects → MoM (boundary only)")
    print("          • Inhomogeneous → FEM (volume)")
    print()
    print("  Time-domain vs frequency-domain?")
    print("    • Broadband response, transient → FDTD/FETD")
    print("    • Single frequency, steady-state → MoM/FEM")
    print()


def main():
    print();print("╔══════════════════════════════════════════╗")
    print("║  Jin CEM 2nd Ed. — Ch12 Code              ║")
    print("╚══════════════════════════════════════════╝");print()
    cem_methods_overview()
    method_selection_guide()
    print("All Ch12 examples done.")

if __name__=="__main__":
    main()
