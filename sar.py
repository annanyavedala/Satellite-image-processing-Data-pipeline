import numpy as np
import pyroSAR
from pyroSAR import identify
from pyroSAR import snap
from overriden_util import geocode


name='S1A_IW_GRDH_1SDV_20221204T194951_20221204T195025_046186_0587A8_3411.SAFE.zip'
print(identify(name))


geocode(infile=name, outdir='./outdir_new_TF', t_srs=4326, geocoding_type='Range-Doppler', removeS1ThermalNoise=True, 
polarizations='all', shapefile=None,scaling='linear',refarea='sigma0', speckleFilter='Gamma Map', test=False, 
removeS1BorderNoise=False)
print('Done')


