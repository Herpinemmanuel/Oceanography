  
  
  
  
  
  
  
  
  
  plt.figure(2)
  ax = plt.subplot(projection=ccrs.PlateCarree());
  ds1['S'].where(ds1.hFacC>0)[nt,:,:,280].plot()
  plt.title('Vertical Section (yz) of Salinity (XC = 0E)')
  plt.text(5,5,nt,ha='center',wrap=True)
  ax.coastlines()
  gl = ax.gridlines(draw_labels=True, alpha = 0.5, linestyle='--');
  gl.xlabels_top = False
  gl.ylabels_right = False
  gl.xformatter = LONGITUDE_FORMATTER
  gl.yformatter = LATITUDE_FORMATTER
  if (nt < 10):
      plt.savefig('Salinity_Vertical_section_xz_Cas6-'+'00'+str(nt)+'.png')
      plt.clf()
   elif (nt > 9) and (nt < 100):
      plt.savefig('Salinity_Vertical_section_xz_Cas6'+'0'+str(nt)+'.png')
      plt.clf()
   else:
      plt.savefig('Salinity_Vertical_section_xz_Cas6'+str(nt)+'.png')
      plt.clf()
