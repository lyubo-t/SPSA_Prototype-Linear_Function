import netCDF4
import numpy as np
import yaml
from subprocess import call
import os

#####################
#read parameters file
#####################
with open('RC/SS2G_instance_SS.rc') as f:
    params = yaml.safe_load(f)

#create theta vector from parameters file
with open("params.yml","r") as f:
    params_dict = yaml.safe_load(f)

theta_dict = params_dict['params']
theta_values = []

for key in params_dict['params']:
    theta_values.append(theta_dict[key])
theta = np.array(theta_values)
p = len(theta)

###################
#first half of SPSA
#(create theta_plus and theta_minus)
###################
meta_values = []
for key in params_dict['metaparams']:
    meta_values.append(params_dict['metaparams'][key])


k = meta_values[0]
a = meta_values[1]
A = meta_values[2]
c = meta_values[3]
alpha = meta_values[4]
gamma = meta_values[5]

ak = a/(A+k+1)**alpha
ck = c/(k+1)**gamma
delta = np.ones(p) - 2*(np.random.randint(1,3,p) -1)
thetaplus = theta + ck*delta
thetaminus = theta - ck*delta

#write params onto SS2G_instance_SS
#with open("RC/SS2G_instance_SS.rc","w") as f:
#    yaml.safe_dump(params_dict,f,sort_keys=False)


#################################
#execute GEOS once for theta_plus
#################################
BASH_COMMAND = ["bash"]
GEOS_COMMAND = BASH_COMMAND + ["gcm_run.j"]
#call(GEOS_COMMAND) #theta_plus


###################
#read scratch files
###################
GEOS_FILE_PATTERN = 'MyFirstGeosRun.tavg2d_aer_x.2000'
SCRATCH_DIR = 'scratch/'

def open_netcdf(file):
    f = netCDF4.Dataset(file)
    return f 

geos_output1 = np.empty(0,'float32')
for root,dirs,files in os.walk(SCRATCH_DIR):
    for file in files:
        if GEOS_FILE_PATTERN in file: 
            geos_file = open_netcdf(SCRATCH_DIR+file)
            geos_tau = geos_file.variables['TOTEXTTAU'][0,:,:] 
            geos_output1 = np.append(geos_output1,geos_tau)
    break

####################
#read satellite data
####################
SAT_DIR = 'satellite directory/'
SAT_FILE_PATTERN = 'nnr_001.SNPP04_L3a.db_ocean.2017'

sat_data = np.empty(0,'float32')
for root,dirs,files in os.walk(SAT_DIR):
    for file in files:
        if SAT_FILE_PATTERN in file: 
            sat_file = open_netcdf(SAT_DIR+file)
            sat_tau = sat_file.variables['tau_'][0,0,:,:]
            #*add this*    remap satellite data to dimensions of GEOS
            sat_data = np.append(sat_data,sat_tau)
    break

###################################
#execute GEOS again for theta_minus
###################################
#call(GEOS_COMMAND) #theta_minus
def open_netcdf(file):
    f = netCDF4.Dataset(file)
    return f 

geos_output2 = np.empty(0,'float32')
for root,dirs,files in os.walk(SCRATCH_DIR):
    for file in files:
        if GEOS_FILE_PATTERN in file: 
            geos_file = open_netcdf(SCRATCH_DIR+file)
            geos_tau = geos_file.variables['TOTEXTTAU'][0,:,:] 
            geos_output2 = np.append(geos_output2,geos_tau)
    break

###############
#calculate loss
###############
def loss(yp,yt):
    cost = 0
    if len(yp) == len(yt):
        cost = np.mean((yp - yt)**2) 
        return cost
    else:
        #print("The values of GEOS output and satellite data don't match up")
        return 0
yplus = loss(sat_data,geos_output1)
yminus = loss(sat_data,geos_output2)

####################
#second half of SPSA
#(update theta vector)
####################
ghat = (yplus - yminus)/(2*ck*delta)
theta = theta - ak*ghat
k += 1  

####################################
#save new parameters onto params.yml
####################################
for key in theta_dict.keys():
    for i in np.arange(len(theta)):
        theta_dict[key] = float(theta[i])

params_dict['params'] = theta_dict
params_dict['metaparams']['k'] = k
print(params_dict)

with open("params.yml","w") as f:
    yaml.safe_dump(params_dict,f,sort_keys=False)

