import numpy as np
import matplotlib.pyplot as plt 
import cartopy.crs as ccrs 

from xmitgcm import open_mdsdataset 
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
plt.ion()

dir1 = '/homedata/bderembl/runmit/test_southatlgyre3'

ds1 = open_mdsdataset(dir1,iters='all',prefix=['S'])

nt = -1                                 #Last iteration
nx = np.array(len(ds1['S'].XC)/2)                                 
ny = np.array(len(ds1['S'].YC)/2)

print(nx)  #280
print(ny)  #100

# Vertical Section of Salinity

plt.figure(1)
ax = plt.subplot(projection=ccrs.PlateCarree());
ds1['S'].where(ds1.hFacC>0)[nt,:,:,100].plot.pcolormesh('XC','YC',ax=ax)
plt.title('Case 4 : Salinity (t = -1 ; YC = 30°S)')
ax.coastlines()
gl = ax.gridlines(draw_labels=True, alpha = 0.5, linestyle='--');
gl.xlabels_top = False
gl.ylabels_right = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
plt.savefig('S_Salinity_Vertical_section(x,z)_cas4'+'.png')
plt.clf()

plt.figure(2)
ax = plt.subplot(projection=ccrs.PlateCarree());
ds1['S'].where(ds1.hFacC>0)[nt,:,280,:].plot.pcolormesh('XC','YC',ax=ax)
plt.title('Case 4 : Salinity (t = -1 ; XC = 0°E)')
ax.coastlines()
gl = ax.gridlines(draw_labels=True, alpha = 0.5, linestyle='--');
gl.xlabels_top = False
gl.ylabels_right = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
plt.savefig('S_Salinity_Vertical_section(y,z)_cas4'+'.png')
plt.clf()
