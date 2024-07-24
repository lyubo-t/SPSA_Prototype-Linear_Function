dset ^../../nnr_042_MYD04_061/Level3/Y%y4/M%m2/nnr_042.MYD04_L3a.ocean.%y4%m2%d2_%h200z.nc4
title Gridded MODIS Aerosol Retrievals
options template
undef 999.999
dtype netcdf
xdef 1152 linear -180 0.3125
ydef 721 linear -90 0.25
zdef 5 levels 870 660 550 470 440
tdef 99999 linear 00Z04JUL2002 3Hr
vars 8
tau=>tau  5  t,z,y,x  Aerosol Optical Depth
tau_=>tau_  5  t,z,y,x  Aerosol Optical Depth (Revised)
tau_fine=>tau_fine  5  t,z,y,x  Aerosol Optical Depth (Fine Mode)
count_tau=>count_tau  5  t,z,y,x  Aerosol Optical Depth Obs Count
count_tau_=>count_tau_  5  t,z,y,x  Aerosol Optical Depth (Revised) Obs Count
cloud=>cloud  0  t,y,x  Cloud Fraction
ae=>ae  0  t,y,x  Angstrom Exponent 440-870
ae_=>ae_  0  t,y,x  Angstrom Exponent 440-870 (Revised)
endvars
