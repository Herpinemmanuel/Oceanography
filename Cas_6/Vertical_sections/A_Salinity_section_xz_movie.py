import numpy as np
import matplotlib.pyplot as plt 

from xmitgcm import open_mdsdataset 


dir1 = '/homedata/bderembl/runmit/test_southatlgyre6'

ds1 = open_mdsdataset(dir1,iters='all',prefix=['S'])

Height = ds1.S.Z
print(Height)
nx = len(ds1.S.XC)/2
print(nx)
ny = len(ds1.S.YC)/2
print(ny)

nt = 0
while (nt < 1000) :
  nt=nt+1
  print(nt)
  # Vertical Sections xz of Salinity
  plt.figure(1)
  ds1['S'].where(ds1.hFacC>0)[nt,:,100,:].plot()
  plt.title('Vertical Section (xz) of Salinity (YC = 30S)')
  plt.text(5,5,nt,ha='center',wrap=True)
  if (nt < 10):
     plt.savefig('Salinity_Vertical_section_xz_Cas6-'+'00'+str(nt)+'.png')
     plt.clf()
  elif (nt > 9) and (nt < 100):
     plt.savefig('Salinity_Vertical_section_xz_Cas6-'+'0'+str(nt)+'.png')
     plt.clf()
  else:
     plt.savefig('Salinity_Vertical_section_xz_Cas6-'+str(nt)+'.png')
     plt.clf()
