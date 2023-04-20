import numpy as np
import pyroSAR
from pyroSAR import identify
from pyroSAR import snap
from pyrosar_modified_util import geocode
import os 


output_dir='/Users/annanya/airflow/recur_downloads'
files = os.listdir(output_dir)
if len(files)>0:
    name= output_dir+'/'+files[0]
    print(identify(name))

    #Preprocessing of the sar image which outputs the sigma0 values
    geocode(infile=name, outdir='/Users/annanya/airflow/outputs/outdir_new_TF_extra', t_srs=4326, geocoding_type='Range-Doppler', removeS1ThermalNoise=True, polarizations='all', shapefile=None,
    scaling='linear',refarea='sigma0', speckleFilter='Gamma Map', test=False, removeS1BorderNoise=False)
else:
    print('No new files')




