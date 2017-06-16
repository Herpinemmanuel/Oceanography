import numpy as np
import matplotlib.pyplot as plt 

from xmitgcm import open_mdsdataset 
plt.ion()

dir1 = '/homedata/bderembl/runmit/test_southatlgyre'

ds1 = open_mdsdataset(dir1,iters='all',prefix=['S'])

Height = ds1.S.Z
print(Height)

nx = len(ds1.S.XC)/2
print(nx)
ny = len(ds1.S.YC)/2
print(ny)

nt = -1        #Last Iteration

# Vertical Section of Salinity
plt.figure(1)
ds1['S'].where(ds1.hFacC>0)[nt,:,210,:].plot()
plt.title('Case 1 : Salinity (t=-1 ; YC = 30S)')
plt.savefig('S_Salinity_Vertical_section_xz_cas1'+'.png')
plt.clf()

plt.figure(2)
ds1['S'].where(ds1.hFacC>0)[nt,:,:,560].plot()
plt.title('Case 1 : Salinity (t=-1 ; XC = 0E)')
plt.savefig('S_Salinity_Vertical_section_yz_cas1'+'.png')
plt.clf()
