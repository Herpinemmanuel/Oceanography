import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import xgcm
import cartopy.crs as ccrs

from xmitgcm import open_mdsdataset
from matplotlib.mlab import bivariate_normal
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

dir0 = '/homedata/bderembl/runmit/test_southatlgyre3'

ds0 = open_mdsdataset(dir0,iters='all',prefix=['U','V'])

grid = xgcm.Grid(ds0)
print(grid)

# sn² = (du/dx-dv/dy)²
Sn = (grid.diff(ds0.U.where(ds0.hFacW>0)*ds0.dyC, 'X') + grid.diff(ds0.V.where(ds0.hFacW>0)*ds0.dxC, 'Y'))/ds0.rAz
Sn_carree = Sn**2
print(Sn_carree)

# Ss² = (dv/dx+du/dy)²
Ss = (grid.diff(ds0.V.where(ds0.hFacS>0)*ds0.dyC, 'X') + grid.diff(ds0.U.where(ds0.hFacW>0)*ds0.dxC, 'Y'))/ds0.rAz
Ss_carree = Ss**2
print(Ss_carree)

# Vorticity² = (dv/dx-du/dy)²
Vorticity = (-grid.diff(ds0.U.where(ds0.hFacW>0)*ds0.dxC, 'Y') + grid.diff(ds0.V.where(ds0.hFacS>0)*ds0.dyC, 'X'))/ds0.rAz
Vor_carree = Vorticity**2

Okubo_weiss_criterion = Sn_carree + Ss_carree - Vor_carree

i = 0
nz = 0


while (i < 1000) :
   i=i+1
   print(i)
   plt.figure(1)
   #CS = plt.contour(X, Y, Z)
   #plt.clabel(CS, inline=1, fontsize=10)
   ax = plt.subplot(projection=ccrs.PlateCarree());
   Okubo_weiss_criterion[i,nz,:,:].plot.pcolormesh('XG','YG', ax=ax,cmap='ocean')
   plt.title('Case 6 : Okubo Weiss Criterion')
   plt.text(5,5,i,ha='center',wrap=True)
   ax.coastlines()
   gl = ax.gridlines(draw_labels=True, alpha = 0.5, linestyle='--');
   gl.xlabels_top = False
   gl.ylabels_right = False
   gl.xformatter = LONGITUDE_FORMATTER
   gl.yformatter = LATITUDE_FORMATTER
   if (i < 10):
     plt.savefig('Okubo_weiss_cas6-'+'00'+str(i)+'.png')
     plt.clf()
   elif (i > 9) and (i < 100):
     plt.savefig('Okubo_weiss_cas6-'+'0'+str(i)+'.png')
     plt.clf()
   else:
     plt.savefig('Okubo_weiss_cas6-'+str(i)+'.png')
     plt.clf()
