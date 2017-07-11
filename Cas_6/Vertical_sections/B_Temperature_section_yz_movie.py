import numpy as np
import matplotlib.pyplot as plt 

from xmitgcm import open_mdsdataset
plt.ion()

dir1 = '/homedata/bderembl/runmit/test_southatlgyre6'

ds1 = open_mdsdataset(dir1,iters='all',prefix=['T'])

nx = 280
nt = 0
while (nt < 1000) :
  nt=nt+1
  print(nt)
  
  # Vertical Sections yz of Temperature
  plt.figure(1)
  ds1['T'].where(ds1.hFacC>0)[nt,:,:,nx].plot.pcolormesh('YC','Z',vmin=2,vmax=30)
  plt.title('Vertical Section (yz) of Temperature (XC = 0E)')
  plt.text(-45,-4500,nt)
  if (nt < 10):
   plt.savefig('Temperature_section_yz_Cas6-'+'00'+str(nt)+'.png')
   plt.clf()
  elif (nt > 9) and (nt < 100):
   plt.savefig('Temperature_section_yz_Cas6-'+'0'+str(nt)+'.png')
   plt.clf()
  else:
   plt.savefig('Temperature_section_yz_Cas6-'+str(nt)+'.png')
   plt.clf()
