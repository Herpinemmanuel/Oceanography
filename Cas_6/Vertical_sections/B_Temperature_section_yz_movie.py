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
  
  # Vertical Sections xz of Temperature
  plt.figure(1)
  ds1['T'].where(ds1.hFacC>0)[nt,:,:,nx].plot()
  #plt.pcolormesh('XC','YC','Z',vmin=30,vmax=39)
  plt.title('Vertical Section (xz) of Temperature (YC = 30S)')
  plt.text(-60,-4000,nt)
  if (nt < 10):
   plt.savefig('Temperature_Vertical_section_xz_Cas6-'+'00'+str(nt)+'.png')
   plt.clf()
  elif (nt > 9) and (nt < 100):
   plt.savefig('Temperature_Vertical_section_xz_Cas6-'+'0'+str(nt)+'.png')
   plt.clf()
  else:
   plt.savefig('Temperature_Vertical_section_xz_Cas6-'+str(nt)+'.png')
   plt.clf()
