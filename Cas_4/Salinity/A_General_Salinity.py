import numpy as np    
import matplotlib.pyplot as plt 
import cartopy.crs as ccrs

from xmitgcm import open_mdsdataset 
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
plt.ion()  

dir1 = '/homedata/bderembl/runmit/test_southatlgyre3'

ds1 = open_mdsdataset(dir1,prefix=['S'])

nt = 0
nz = 0

# Cartography S : Salinity

plt.figure(1)
ax = plt.subplot(projection=ccrs.PlateCarree());
ds1['S'][nt,nz,:,:].plot.pcolormesh('XC', 'YC', ax=ax);
plt.title('Case 4 : Salinity')
ax.coastlines()
gl = ax.gridlines(draw_labels=True, alpha = 0.5, linestyle='--');
gl.xlabels_top = False
gl.ylabels_right = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
plt.savefig('S_General_Salinity_cas4'+'.png')
plt.clf()

# Averages

Average_S = ds1.S.mean().values
print('Average of Salinity')
print(Average_S,'psu')
Average_S_mask = ds1.S.where(ds1.hFacC>0).mean().values
print('Average of Salinity without continents')
print(Average_S_mask,'psu')
