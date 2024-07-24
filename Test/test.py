import netCDF4
import numpy as np
import yaml
import matplotlib.pyplot as plt

#geos1 = netCDF4.Dataset('c48_spsa_t00.spsa.20170201_2200z.nc4')
#geos2 = netCDF4.Dataset('c48_spsa_t00.spsa.20170201_2300z.nc4')
sat = netCDF4.Dataset("satellite directory/nnr_001.SNPP04_L3a.db_ocean.20170101_0000z.nc4")

tau_sat = sat.variables["tau_"][0,0,:,:]
print(tau_sat)
#LWI_plot = plt.contourf(f.variables['LWI'][0,:,:])
sat_plot = plt.contourf(tau_sat)

#plt.show()

f1 = netCDF4.Dataset("scratch/MyFirstGeosRun.tavg2d_aer_x.20000415_0000z.nc4")
f2 = netCDF4.Dataset('scratch/MyFirstGeosRun.tavg2d_aer_x.20000415_0100z.nc4')


tau1 = f1.variables['TOTEXTTAU'][0,:,:]
tau2 = f2.variables['TOTEXTTAU'][0,:,:]
cost = np.mean((tau1 - tau2)**2)
#print(cost)

with open("params.yml","r") as f:
    params_dict = yaml.safe_load(f)

with open("params.yml","w") as f:
    yaml.safe_dump(params_dict,f,default_flow_style=False)




