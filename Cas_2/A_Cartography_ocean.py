import numpy as np                                                        #Working with arrays
import matplotlib.pyplot as plt                                           #Plotting curves
import cartopy.crs as ccrs                                                #Maps Longitude-Latitude

from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
from xmitgcm import open_mdsdataset                                       #Reading datas

plt.ion() #or plt.show() at the end of script                             #Interactive mode

dir0 = '/homedata/bderembl/runmit/test_southatlgyre2'                      #Path to directory

ds0 = open_mdsdataset(dir0,prefix=['U','V','W','T','S','Eta'])            #Case 2 : 110 iterations

print(ds0)                                                                 #Whrite ds0 object

nt1 = 0                                                                   #First iteration
nt2 = -1                                                                  #Last iteration
nz = 0                                                                    #Altitude level : 60 levels

#ETA : Surface Height Anomaly
plt.figure(1)
ax = plt.subplot(projection=ccrs.PlateCarree());
ds0.Eta[nt1,:,:].plot.pcolormesh('XC', 'YC', ax=ax);
plt.title('ETA : Surface Height Anomaly (t=0)')
ax.coastlines()
gl = ax.gridlines(draw_labels=True, alpha = 0.5, linestyle='--');
gl.xlabels_top = False
gl.ylabels_right = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
plt.savefig('Cartography_ETA_cas2'+'.png')                               #Save figure
plt.clf()                                                                #Clear figure

#T : Temperature
plt.figure(2)
ax = plt.subplot(projection=ccrs.PlateCarree());
ds0['T'].where(ds0.hFacC>0)[nt1,nz,:,:].plot.pcolormesh('XC', 'YC', ax=ax);
plt.title('T : Temperature (t=0 ; z=0)')
ax.coastlines()
gl = ax.gridlines(draw_labels=True, alpha = 0.5, linestyle='--');
gl.xlabels_top = False
gl.ylabels_right = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
plt.savefig('Cartography_T_cas2'+'.png')
plt.clf()

#S : Salinity
plt.figure(3)
ax = plt.subplot(projection=ccrs.PlateCarree());
ds0['S'][nt1,nz,:,:].plot.pcolormesh('XC', 'YC', ax=ax);
plt.title('S : Salinity (t=0 ; z=0)')
ax.coastlines()
gl = ax.gridlines(draw_labels=True, alpha = 0.5, linestyle='--');
gl.xlabels_top = False
gl.ylabels_right = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
plt.savefig('Cartography_S_cas2'+'.png')
plt.clf()

#U : Meridional component of Sea water Velocity
plt.figure(4)
ax = plt.subplot(projection=ccrs.PlateCarree());
ds0['U'][nt2,nz,:,:].plot.pcolormesh('XG', 'YC', ax=ax);
plt.title('U : Meridional component of Sea water Velocity (t=-1 ; z=0)')
ax.coastlines()
gl = ax.gridlines(draw_labels=True, alpha = 0.5, linestyle='--');
gl.xlabels_top = False
gl.ylabels_right = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
plt.savefig('Cartography_U_cas2'+'.png')
plt.clf()

#V : Zonal component of Sea water Velocity
plt.figure(5)
ax = plt.subplot(projection=ccrs.PlateCarree());
ds0['V'][nt2,nz,:,:].plot.pcolormesh('XC', 'YG', ax=ax);
plt.title('V : Zonal component of Sea water Velocity (t=-1 ; z=0)')
ax.coastlines()
gl = ax.gridlines(draw_labels=True, alpha = 0.5, linestyle='--');
gl.xlabels_top = False
gl.ylabels_right = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
plt.savefig('Cartography_V_cas2'+'.png')
plt.clf()

#W : Vertical component of Sea water Velocity
plt.figure(6)
ax = plt.subplot(projection=ccrs.PlateCarree());
ds0['W'][nt2,nz,:,:].plot.pcolormesh('XC', 'YC', ax=ax);
plt.title('W : Vertical component of Sea water Velocity (t=-1 ; z=0)')
ax.coastlines()
gl = ax.gridlines(draw_labels=True, alpha = 0.5, linestyle='--');
gl.xlabels_top = False
gl.ylabels_right = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
plt.savefig('Cartography_W_cas2'+'.png')
plt.clf()
