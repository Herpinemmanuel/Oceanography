import numpy as np
import matplotlib.pyplot as plt 

from xmitgcm import open_mdsdataset 
plt.ion()

dir1 = '/homedata/bderembl/runmit/test_southatlgyre'

ds1 = open_mdsdataset(dir1,iters='all',prefix=['T'])

Height = ds1.T.Z
print(Height)

nx = int(len(ds1.T.XC)/2)
print(nx)
ny = int(len(ds1.T.YC)/2)
print(ny)

nt = -1

# Vertical Section of Temperature
plt.figure(1)
ds1['T'].where(ds1.hFacC>0)[nt,:,ny,:].plot()
plt.title('Case 1 : Temperature (t=-1 ; YC = 30S)')
plt.savefig('T_Temperature_Vertical_section_xz_cas4'+'.png')
plt.clf()

plt.figure(2)
ds1['T'].where(ds1.hFacC>0)[nt,:,:,nx].plot()
plt.title('Case 1 : Temperature (t=-1 ; XC = 0E)')
plt.savefig('T_Temperature_Vertical_section_yz_cas4'+'.png')
plt.clf()
