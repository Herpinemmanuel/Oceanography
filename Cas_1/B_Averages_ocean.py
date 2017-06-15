#Averages of U,V,W,T,S and ETA

import numpy as np                  
import matplotlib.pyplot as plt

from xmitgcm import open_mdsdataset
          
dir0 = '/homedata/bderembl/runmit/test_southatlgyre'                            #Case 1 : 38 iterations

ds0 = open_mdsdataset(dir0,prefix=['Eta','U','V','W','T','S'])

print(ds0)

Average_ETA = ds0['Eta'].mean().values
print('Average of Ocean Surface Height Anomaly ')
print(Average_ETA,'m')
#Average_ETA_mask = ds0.Eta.where(ds0.hFacC>0).mean().values
#print('Average of Ocean Surface Height Anomaly without continents')
#print(Average_ETA_mask,'m')

Average_T = ds0['T'].mean().values
print('Average of Ocean Temperature')
print(Average_T,'°C')
#Average_T_mask = ds0['T'].where(ds0.hFacC>0).mean().values
#print('Average of Ocean Temperature without continents')
#print(Average_T_mask,'°C')

Average_S = ds0['S'].mean().values
print('Average of Ocean Salinity')
print(Average_S,'psu')
#Average_S_mask = ds0.S.where(ds0.hFacC>0).mean().values
#print('Average of Ocean Salinity without continents')
#print(Average_S_mask,'psu')

Average_U = ds0['U'].mean().values
print('Average of Meridional component of Ocean Velocity')
print(Average_U,'m/s')
#Average_U_mask = ds0.U.where(ds0.hFacW>0).mean().values
#print('Average of Meridional component of Ocean Velocity without continents')
#print(Average_U_mask,'m/s')

Average_V = ds0['V'].mean().values
print('Average of Zonal component of Ocean Velocity')
print(Average_V,'m/s')
#Average_V_mask = ds0.V.where(ds0.hFacS>0).mean().values
#print('Average of Meridional component of Ocean Velocity without continents')
#print(Average_V_mask,'m/s')

Average_W = ds0['W'].mean().values
print('Average of Vertical component of Ocean Velocity')
print(Average_W,'m/s')
#Average_W_mask = ds0.W.where(ds0.hFacS>0).mean().values
#print('Average of Vertical component of Ocean Velocity without continents')
#print(Average_W_mask,'m/s')
