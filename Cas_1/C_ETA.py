import numpy as np
import matplotlib.pyplot as plt 
import cartopy.crs as ccrs 

from xmitgcm import open_mdsdataset 
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
plt.ion()

dir1 = '/homedata/bderembl/runmit/test_southatlgyre'

ds1 = open_mdsdataset(dir1,iters='all',prefix=['Eta'])

nt = 0

# Cartography of ETA

plt.figure(1)
ax = plt.subplot(projection=ccrs.PlateCarree());
ds1.Eta[nt,:,:].plot.pcolormesh('XC', 'YC', ax=ax);
plt.title('Case 1 : ETA')
ax.coastlines()
gl = ax.gridlines(draw_labels=True, alpha = 0.5, linestyle='--');
gl.xlabels_top = False
gl.ylabels_right = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

plt.savefig('ETA_Surface_Height_Anomaly_cas1'+'.png')
plt.clf

# Averages

Average_ETA = ds1.Eta.mean().values
print('Average of Surface Height Anomaly ')
print(Average_ETA,'m')
Average_ETA_mask = ds1.Eta.where(ds1.hFacC>0).mean().values
print('Average of Surface Height Anomaly without continents')
print(Average_ETA_mask,'m')

# Temporal series

plt.figure(2)
x1 = ds1.Eta.mean(axis=[1,2])
Temporal_series =x1.plot()
plt.title('Case 1 : Temporal series of ETA')
plt.xlabel('Time')
plt.ylabel('Average of Surface Height Anomaly')
plt.savefig('Temporal_series_cas1'+'.png')
plt.clf()
