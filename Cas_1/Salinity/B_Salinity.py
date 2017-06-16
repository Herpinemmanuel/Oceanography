import numpy as np   
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import cartopy.crs as ccrs

from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
from xmitgcm import open_mdsdataset 
plt.ion()

dir0 = '/homedata/bderembl/runmit/test_southatlgyre'

ds0 = open_mdsdataset(dir0,prefix=['S'])

nt = 0
nz = 0

while (nt < 50) :
    nt = nt+1
    print(nt)
    plt.figure(2)
    ax = plt.subplot(projection=ccrs.PlateCarree());
    ds0['S'][nt,nz,:,:].plot.pcolormesh('XC', 'YC', ax=ax,vmin=25,vmax=45,cmap='ocean');
    plt.title('Case 1 : Salinity ')
    plt.text(5,5,nt,ha='center',wrap=True)
    ax.coastlines()
    gl = ax.gridlines(draw_labels=True, alpha = 0.5, linestyle='--');
    gl.xlabels_top = False
    gl.ylabels_right = False
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    if (nt < 10):
        plt.savefig('Salinity_Cas1-'+'00'+str(nt)+'.png')
        plt.clf()
    elif (nt > 9) and (nt < 100):
        plt.savefig('Salinity_Cas1-'+'0'+str(nt)+'.png')
        plt.clf()
    else:
        plt.savefig('Salinity_Cas1-'+str(nt)+'.png')
        plt.clf()
