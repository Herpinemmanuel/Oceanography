import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import xgcm
import cartopy.crs as ccrs

from xmitgcm import open_mdsdataset
from matplotlib.mlab import bivariate_normal
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

dir0 = '/homedata/bderembl/runmit/test_southatlgyre'

ds0 = open_mdsdataset(dir0,iters='all',prefix=['U','V'])

grid = xgcm.Grid(ds0)
print(grid)

Vorticity = (-grid.diff(ds0.U.where(ds0.hFacW>0)*ds0.dxC, 'Y') + grid.diff(ds0.V.where(ds0.hFacS>0)*ds0.dyC, 'X'))/ds0.rAz
print('Vorticity')

i = 0
nz = 0

while (i < 50) :
    i=i+1
    print(i)
    plt.figure(1)
    ax = plt.subplot(projection=ccrs.PlateCarree());
    Vorticity[i,nz,:,:].plot.pcolormesh('XG','YG', ax=ax,vmin=-0.00020,vmax=0.00020,cmap='ocean')
    plt.title('Case 1 : Vorticity')
    plt.text(5,5,i,ha='center',wrap=True)
    ax.coastlines()
    gl = ax.gridlines(draw_labels=True, alpha = 0.5, linestyle='--');
    gl.xlabels_top = False
    gl.ylabels_right = False
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    if (i < 10):
        plt.savefig('Vorticity_cas1-'+'00'+str(i)+'.png')
        plt.clf()
    elif (i > 9) and (i < 100):
        plt.savefig('Vorticity_cas1-'+'0'+str(i)+'.png')
        plt.clf()
    else:
        plt.savefig('Vorticity_cas1-'+str(i)+'.png')
        plt.clf()
