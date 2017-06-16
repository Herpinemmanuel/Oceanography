import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

from xmitgcm import open_mdsdataset
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

dir0 = '/homedata/bderembl/runmit/test_southatlgyre'

ds0 = open_mdsdataset(dir0,iters='all',prefix=['cheapAML'])

# Average of Atmospheric Temperature

Average_Tair = ds0.CH_TAIR.mean().values
print('Case 1 : Average of Atmospheric Temperature')
print(Average_Tair,'°C')
Average_Tair_mask = ds0.CH_TAIR.where(ds0.hFacC>0).mean().values
print('Case 1 : Average of Atmospheric Temperature without continents')
print(Average_Tair_mask,'°C')

# Uwind et Vwind : Winds

Average_Uwind = ds0.CH_Uwind.mean().values
print('Case 1 : Average of Atmospheric Zonal component - Uwind')
print(Average_Uwind,'m/s')
Average_Uwind_mask = ds0.CH_Uwind.where(ds0.hFacW>0).mean().values
print('Case 1 : Average of Atmospheric Zonal component without continents')
print(Average_Uwind_mask,'m/s')

Average_Vwind = ds0.CH_Vwind.mean().values
print('Case 1 : Average of Atmospheric Meridional component - Vwind')
print(Average_Vwind,'m/s')
Average_Vwind_mask = ds0.CH_Vwind.where(ds0.hFacS>0).mean().values
print('Case 1 : Average of Atmospheric Meridional component without continents')
print(Average_Vwind_mask,'m/s')

# Specific Humidity

Average_CH_QAIR = ds0.CH_QAIR.mean().values
print('Average of Specific Humidity')
print(Average_CH_QAIR, 'kg_WATER/kg_DRYAIR')

Average_CH_QAIR_mask = ds0.CH_QAIR.where(ds0.hFacC>0).mean().values
print('Average of Specific Humidity without continents')
print(Average_CH_QAIR_mask, 'kg_EAU/kg_AIRSEC')

# Surface Heating

Average_CH_QNET = ds0.CH_QNET.mean().values
print('Average of Surface Heating')
print(Average_CH_QNET, 'W/m²')

Average_CH_QNET_mask = ds0.CH_QNET.where(ds0.hFacC>0).mean().values
print('Average of Surface Heating without continents')
print(Average_CH_QNET_mask, 'W/m²')

# Latent Heat

Average_CH_LH = ds0.CH_LH.mean().values
print('Average of Latent Heat ')
print(Average_CH_LH, 'W/m²')

Average_CH_LH_mask = ds0.CH_LH.where(ds0.hFacC>0).mean().values
print('Average of Latent Heat without continents')
print(Average_CH_LH_mask, 'W/m²')

# Sensible Heat

Average_CH_SH = ds0.CH_SH.mean().values
print('Average of Sensible Heat')
print(Average_CH_SH,'W/m²')

Average_CH_SH_mask = ds0.CH_SH.where(ds0.hFacC>0).mean().values
print('Average of Sensible Heat without continents')
print(Average_CH_LH_mask,'W/m²')
