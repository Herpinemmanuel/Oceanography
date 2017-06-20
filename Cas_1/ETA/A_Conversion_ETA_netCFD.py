import numpy as np

from xmitgcm import open_mdsdataset 

dir0 = '/homedata/bderembl/runmit/test_southatlgyre'
i = 0

while (i < 423360):
    i = int(i+2160)
    print(i)
    if (i > 1000) and (i < 9999):
        ds1 = open_mdsdataset(dir0,iters=i,prefix=['Eta'])
        ds1['Eta'].to_netcdf('ETA_Surface_Height_Anomaly-'+'00'+str(i)+'.nc')  
    elif (i > 10000 ) and (i < 99999):
        ds2 = open_mdsdataset(dir0, iters=i,prefix=['Eta'])
        ds2['Eta'].to_netcdf('ETA_Surface_Height_Anomaly-'+'0'+str(i)+'.nc')
    else:
        ds3 = open_mdsdataset(dir0, iters=i,prefix=['Eta'])
        ds3['Eta'].to_netcdf('ETA_Surface_Height_Anomaly-'+str(i)+'.nc')
