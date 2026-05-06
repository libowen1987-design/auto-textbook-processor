#!/usr/bin/env python3
"""Paul Ch2: FCC/CISPR emission limits visualization."""
import numpy as np; import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt

f_cond = np.linspace(0.15, 30, 1000)
f_rad = np.linspace(30, 1000, 1000)
limit_B = np.piecewise(f_rad, [f_rad<88, (f_rad>=88)&(f_rad<216), (f_rad>=216)&(f_rad<960), f_rad>=960], [40,43.5,46,49])
limit_A = np.piecewise(f_rad, [f_rad<88, (f_rad>=88)&(f_rad<216), (f_rad>=216)&(f_rad<960), f_rad>=960], [39,43.5,46.4,49.5])
fig, axes = plt.subplots(1,2,figsize=(14,5))
ax=axes[0]; ax.step(f_cond, [48]*len(f_cond),'b-',where='mid')
ax.fill_between(f_cond,0,48,alpha=0.1,color='red',label='FAIL')
ax.fill_between(f_cond,48,60,alpha=0.1,color='green',label='PASS')
ax.set(xlabel='f (MHz)',ylabel='dBμV',title='FCC Class B Conducted',xlim=(0.15,30),ylim=(0,60))
ax.legend(); ax.grid(True,alpha=0.3)
ax=axes[1]; ax.plot(f_rad,limit_B,'b-',lw=2,label='Class B @3m')
ax.plot(f_rad,limit_A,'r--',lw=2,label='Class A @10m')
ax.set(xlabel='f (MHz)',ylabel='dBμV/m',title='FCC Radiated Limits',xlim=(30,1000),ylim=(30,60))
ax.legend(); ax.grid(True,alpha=0.3)
plt.tight_layout(); plt.savefig('../figures/paul_ch2_fcc_limits.png',dpi=150); plt.close()
print('✅ FCC limits plot done')
