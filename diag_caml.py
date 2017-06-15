#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from xmitgcm import open_mdsdataset
import scipy.io.netcdf as netcdf
import f90nml
import glob,os,re
import intergrid

import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
plt.ion()

dir0 = '/home/bderembl/runmit/test_southatlgyre'

#ERA files
dir0_era = '/home/bderembl/work/MITgcm/myrun/southatlgyre/input/files/era/'

# read mitgcm input
nml_mit = f90nml.read(dir0+ 'data')

#ds = open_mdsdataset(dir0,iters=25920)
ds_v = open_mdsdataset(dir0,prefix=['U','V','T','S','Eta'])
ds_a = open_mdsdataset(dir0,prefix=['cheapAML'])

#print(ds)

deltat = nml_mit['parm03']['deltat']
times = deltat*ds_v['time']

n1,n2,si_y,si_x = ds_v['T'].shape


lon_g,lat_g = np.meshgrid(ds_v['XC'].data,ds_v['YC'].data) 


xx = np.zeros((si_x*si_y,2))
xx[:,0] = lat_g.flat
xx[:,1] = lon_g.flat

# select iteration
it_m = 5
# initial state not stored:
it_a = it_m - 1 

# 4 points/day in era
it_era = times[it_m]/21600

#####################################
# read ERA                          #
#####################################

vars2 = ['u10', 'v10','t2', 'd2', 'ssrd', 'strd']
nvars = len(vars2)

allfiles1 = sorted(glob.glob(dir0_era + vars2[0] + '*'));
nb_files = len(allfiles1);


f1 = netcdf.netcdf_file(allfiles1[0],'r')
lat_i = f1.variables['lat'][:].copy().squeeze()
lon_i = f1.variables['lon'][:].copy().squeeze()
f1.close()

lat_i = lat_i[::-1]
lon_i =np.where(lon_i > 180, lon_i - 360,lon_i)

lon_i2,lat_i2 = np.meshgrid(lon_i,lat_i) 
lo = np.array([ np.min(lat_i), np.min(lon_i)])  # lowest lat, lowest lon
hi = np.array([ np.max(lat_i), np.max(lon_i) ])   # highest lat, highest lon

si_t_all = 0

psi_out = np.zeros((nvars,si_y,si_x))
flag_done = 0
for nv in range(0,nvars):

  allfiles1 = sorted(glob.glob(dir0_era + vars2[nv] + '*'));
  nb_files = len(allfiles1);


  for nfi in range(0,nb_files):
    
    file1 = allfiles1[nfi]
    f = netcdf.netcdf_file(file1,'r')

    time_e = f.variables['time'][:].copy().squeeze()
    si_t = len(time_e)
    f.close()

    if nv == 0:
      si_t_all = si_t_all + si_t

    if si_t_all > it_era and flag_done == 0:  

      flag_done = 1
      it2 = it_era - (si_t_all - si_t)
      f = netcdf.netcdf_file(allfiles1[0],'r')
      psi = f.variables[vars2[nv]][int(it2.data),:,:].copy().squeeze()
      psi = psi[::-1,:]
      f.close()
    
      interfunc = intergrid.Intergrid( 1.0*psi[:,:], lo=lo, hi=hi , verbose=0, order=3)
      psi_out[nv,:,:] = interfunc.at( xx).reshape(si_y,si_x)
  
    
      #modif unit
      if vars2[nv] == 't2':
        psi_out[nv,:,:] = psi_out[nv,:,:] - 273.16
      if vars2[nv] == 'd2':
        psi_out[nv,:,:] = 6.112*np.exp(17.67*(psi_out[nv,:,:] - 273.16)/(243.5 + (psi_out[nv,:,:] - 273.16)))*0.622/1000;
      if vars2[nv] == 'ssrd':
        psi_out[nv,:,:] = np.delete(np.diff(psi_out[nv,:,:],1,0), slice(4, None, 5),0)/6.0/60.0/60.0*0.94 #0.94:albedo (ssrd)
      if vars2[nv] == 'strd':
        psi_out[nv,:,:] = np.delete(np.diff(psi_out[nv,:,:],1,0), slice(4, None, 5),0)/6.0/60.0/60.0
  
  

# read mitgcm

var = 'CH_TAIR'
nt = -1

plt.figure()
ax = plt.subplot(projection=ccrs.PlateCarree());
ds_a[var][nt,:,:].plot.pcolormesh('XC', 'YC', ax=ax);
ax.coastlines();
gl = ax.gridlines(draw_labels=True, alpha = 0.5, linestyle='--');
gl.xlabels_top = False
gl.ylabels_right = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER


# read ERA
