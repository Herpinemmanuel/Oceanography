import numpy as np
import matplotlib.pyplot as plt

from xmitgcm import open_mdsdataset
plt.ion()

dir1 = '/homedata/bderembl/runmit/test_southatlgyre6'

ds1 = open_mdsdataset(dir1,iters='all',prefix=['S'])

nt = 0
nx = 280

while (nt < 1000) :
  nt=nt+1
  print(nt)
  plt.figure(1)
  ds1['S'].where(ds1.hFacC>0)[nt,:,:,nx].plot.pcolormesh('YC','Z',vmin=32,vmax=38)
  plt.text(-45,-4500,nt)
  plt.title('Vertical Section (yz) of Salinity (XC = 0E)')
  if (nt < 10):
     plt.savefig('Salinity_section_yz_Cas6-'+'00'+str(nt)+'.png')
     plt.clf()
  elif (nt > 9) and (nt < 100):
     plt.savefig('Salinity_section_yz_Cas6-'+'0'+str(nt)+'.png')
     plt.clf()
  else:
     plt.savefig('Salinity_section_yz_Cas6-'+str(nt)+'.png')
     plt.clf()
