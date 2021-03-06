import numpy as np   
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import cartopy.crs as ccrs

from xmitgcm import open_mdsdataset 
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
plt.ion()

dir0 = '/homedata/bderembl/runmit/test_southatlgyre'

ds0 = open_mdsdataset(dir0,prefix=['T'])

nt = 0
nz = 0
while (nt < 50) :
    nt = nt+1
    print(nt)
    plt.figure(1)
    ax = plt.subplot(projection=ccrs.PlateCarree());
    ds0['T'][nt,nz,:,:].plot.pcolormesh('XC', 'YC',ax=ax,vmin=-10,vmax=35,cmap='ocean')
    plt.title('Case 1 : Temperature ')
    plt.text(5,5,nt,ha='center',wrap=True)
    ax.coastlines()
    gl = ax.gridlines(draw_labels=True, alpha = 0.5, linestyle='--');
    gl.xlabels_top = False
    gl.ylabels_right = False
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    if (nt < 10):
        plt.savefig('Temperature_cas1-'+'00'+str(nt)+'.png')
        plt.clf()
    elif (nt > 9) and (nt < 100):
        plt.savefig('Temperature_cas1-'+'0'+str(nt)+'.png')
        plt.clf()
    else:
        plt.savefig('Temperature_cas1-'+str(nt)+'.png')
        plt.clf()
