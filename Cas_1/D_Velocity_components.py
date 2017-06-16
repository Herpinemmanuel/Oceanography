import numpy as np    
import matplotlib.pyplot as plt 
from xmitgcm import open_mdsdataset  

import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
plt.ion() 

dir1 = '/homedata/bderembl/runmit/test_southatlgyre'

ds1 = open_mdsdataset(dir1,prefix=['U','V'])

nt = -1
nz = 0

# Cartography U et V

plt.figure(1)
ax = plt.subplot(projection=ccrs.PlateCarree());
ds1['U'][nt,nz,:,:].plot.pcolormesh('XG', 'YC', ax=ax);
plt.title('Case 1 : Zonal Component - U')
ax.coastlines()
gl = ax.gridlines(draw_labels=True, alpha = 0.5, linestyle='--');
gl.xlabels_top = False
gl.ylabels_right = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
plt.savefig('U_Zonal_component_cas1'+'.png')
plt.clf()

plt.figure(2)
ax = plt.subplot(projection=ccrs.PlateCarree());
ds1['V'][nt,nz,:,:].plot.pcolormesh('XC', 'YG', ax=ax);
plt.title(' Case 1 : Meridional Component - V')
ax.coastlines()
gl = ax.gridlines(draw_labels=True, alpha = 0.5, linestyle='--');
gl.xlabels_top = False
gl.ylabels_right = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
plt.savefig('V_Meridional_Component_cas1'+'.png')
plt.clf()

# Averages

Average_U = ds1.U.mean().values
print('Case 1 : Average of Zonal Component - U')
print(Average_U,'m/s')
Average_U_mask = ds1.U.where(ds1.hFacW>0).mean().values
print('Case 1 : Average of Zonal Component without continents')
print(Average_U_mask,'m/s')

Average_V = ds1.V.mean().values
print('Case 1 :Average of Meridional Component - V')
print(Average_V,'m/s')
Average_V_mask = ds1.V.where(ds1.hFacS>0).mean().values
print('Case 1 : Average of Meridional Component without continents')
print(Average_V_mask,'m/s')
