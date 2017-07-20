import numpy as np
import matplotlib.pyplot as plt

from xmitgcm import open_mdsdataset
plt.ion()

dir1 = '/homedata/bderembl/runmit/test_southatlgyre6'

ds1 = open_mdsdataset(dir1,iters='all',prefix=['S','T'])

nt = 0

for ny in range(0,200,40):
    for nx in range(0,560,40):
        print(nx)
        print(ny)
        plt.figure(1)
        plt.plot(ds1['S'].where(ds1.hFacC>0)[nt,:,ny,nx],ds1['T'].where(ds1.hFacC>0)[nt,:,ny,nx])

plt.title('Diagram T-S')
plt.savefig('Diagramme_T_S'+'.png')
