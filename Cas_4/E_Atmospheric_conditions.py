import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

from xmitgcm import open_mdsdataset
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

dir0 = '/homedata/bderembl/runmit/test_southatlgyre3'

ds0 = open_mdsdataset(dir0,iters='all',prefix=['cheapAML'])

# Average of Atmospheric Temperature

Average_Tair = ds0.CH_TAIR.mean().values
print('Case 4 : Average of Atmospheric Temperature')
print(Average_Tair,'°C')
Average_Tair_mask = ds0.CH_TAIR.where(ds0.hFacC>0).mean().values
print('Case 4 : Average of Atmospheric Temperature without continents')
print(Average_Tair_mask,'°C')

# Uwind et Vwind : Winds

Average_Uwind = ds0.CH_Uwind.mean().values
print('Case 4 : Average of Atmospheric Zonal component - Uwind')
print(Average_Uwind,'m/s')
Average_Uwind_mask = ds0.CH_Uwind.where(ds0.hFacW>0).mean().values
print('Case 4 : Average of Atmospheric Zonal component without continents')
print(Average_Uwind_mask,'m/s')

Average_Vwind = ds0.CH_Vwind.mean().values
print('Case 4 : Average of Atmospheric Meridional component - Vwind')
print(Average_Vwind,'m/s')
Average_Vwind_mask = ds0.CH_Vwind.where(ds0.hFacS>0).mean().values
print('Case 4 : Average of Atmospheric Meridional component without continents')
print(Average_Vwind_mask,'m/s')

