SAR PREPROCESSING

The overriden_auxil and the overriden_util python files are the tweaked source codes of the pyroSAR package that helped us perform the preprocessing for our specific use case. The sar.py file imports these utility files.
Please run the sar.py file using 'python3 sar.py' and the download will immediately begin.



NORMALISED DIFFERENCE WATER INDEX

The NDWI.ipynb consists of the code that was used to calculate the NDWI and to crop the Area of Interest.



AIRFLOW INGESTION PIPELINE

This has all the scripts and dags that are used to automate the SAR data ingestion process. Create the necessary output folders as written in the code while running the dag.
