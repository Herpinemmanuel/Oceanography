import numpy as np

from xmitgcm import open_mdsdataset 

dir0 = '/homedata/bderembl/runmit/test_southatlgyre6'
i = 108

ds = open_mdsdataset(dir0,iters=i,prefix=['etan'])
ds['ETAN'].to_netcdf('ETA_Surface_Height_Anomaly-'+'0000'+str(i)+'.nc')  

while (i < 500000):
    i = int(i+216)
    print(i)
    if (i > 100) and (i < 999):
        ds0 = open_mdsdataset(dir0,iters=i,prefix=['etan'])
        ds0['ETAN'].to_netcdf('ETA_Surface_Height_Anomaly-'+'0000'+str(i)+'.nc')  
    elif (i > 1000) and (i < 9999):
        ds1 = open_mdsdataset(dir0,iters=i,prefix=['etan'])
        ds1['ETAN'].to_netcdf('ETA_Surface_Height_Anomaly-'+'000'+str(i)+'.nc')  
    elif (i > 10000 ) and (i < 99999):
        ds2 = open_mdsdataset(dir0,iters=i,prefix=['etan'])
        ds2['ETAN'].to_netcdf('ETA_Surface_Height_Anomaly-'+'00'+str(i)+'.nc')
    else:
        ds3 = open_mdsdataset(dir0,iters=i,prefix=['etan'])
        ds3['ETAN'].to_netcdf('ETA_Surface_Height_Anomaly-'+str(i)+'.nc')
