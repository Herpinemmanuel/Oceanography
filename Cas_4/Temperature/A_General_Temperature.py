import numpy as np
import matplotlib.pyplot as plt 
import cartopy.crs as ccrs 

from xmitgcm import open_mdsdataset 
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
plt.ion()

dir1 = '/homedata/bderembl/runmit/test_southatlgyre3'

ds1 = open_mdsdataset(dir1,iters='all',prefix=['T'])

nt = 0
nz = 0

# Cartography T 

plt.figure(1)
ax = plt.subplot(projection=ccrs.PlateCarree());
ds1['T'].where(ds1.hFacC>0)[nt,nz,:,:].plot.pcolormesh('XC', 'YC', ax=ax);
plt.title('Cas 4 : Temperature')
ax.coastlines()
gl = ax.gridlines(draw_labels=True, alpha = 0.5, linestyle='--');
gl.xlabels_top = False
gl.ylabels_right = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
plt.savefig('T_Temperature_cas4'+'.png')
plt.clf()

# Averages

Average_T = ds1['T'].mean().values
print('Average of Temperature')
print(Average_T,'°C')
Average_T_mask = ds1['T'].where(ds1.hFacC>0).mean().values
print('Average of Temperature without continents')
print(Average_T_mask,'°C')
