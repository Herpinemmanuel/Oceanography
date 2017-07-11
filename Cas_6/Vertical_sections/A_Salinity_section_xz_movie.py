import numpy as np
import matplotlib.pyplot as plt

from xmitgcm import open_mdsdataset
plt.ion()

dir1 = '/homedata/bderembl/runmit/test_southatlgyre6'

ds1 = open_mdsdataset(dir1,iters='all',prefix=['S'])

ny = 100
nt = 0
while (nt < 1000) :
  nt=nt+1
  print(nt)
  plt.figure(1)
  ds1['S'].where(ds1.hFacC>0)[nt,:,ny,:].plot.pcolormesh('XC','Z',vmin=30,vmax=39)
  plt.text(-60,-4000,nt)
  plt.title('Vertical Section (xz) of Salinity (YC = 30S)')
  if (nt < 10):
      plt.savefig('Salinity_Vertical_section_xz_Cas6-'+'00'+str(nt)+'.png')
      plt.clf()
  elif (nt > 9) and (nt < 100):
      plt.savefig('Salinity_Vertical_section_xz_Cas6-'+'0'+str(nt)+'.png')
      plt.clf()
  else:
      plt.savefig('Salinity_Vertical_section_xz_Cas6-'+str(nt)+'.png')
      plt.clf()
