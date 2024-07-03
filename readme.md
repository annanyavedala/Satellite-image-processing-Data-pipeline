# Image Analysis Pipeline Project

## Overview

This project focuses on creating a comprehensive image analysis pipeline using Apache Airflow. It consists of two main components:
1. **SAR Image Analysis**: Using PyroSAR and other libraries to retrieve Synthetic Aperture Radar (SAR) images from satellites and calculate soil moisture content.
2. **Landsat 8 Image Analysis**: Retrieving images from the Landsat 8 satellite and calculating the Normalized Difference Water Index (NDWI).

## Project Structure

### SAR Preprocessing

The SAR preprocessing pipeline retrieves SAR images from satellites and processes them to calculate soil moisture content.

#### Files:
- **`overriden_auxil.py` and `overriden_util.py`**: Custom versions of the PyroSAR package source code, modified for our specific use case.
- **`sar.py`**: Script that imports the utility files and handles SAR image retrieval and processing.

#### How to Run:
1. Ensure you have the necessary dependencies installed.
2. Execute the SAR preprocessing script:
   ```bash
   python3 sar.py

This will start the download and preprocessing immediately.

#### Normalized Difference Water Index (NDWI)
This part of the project involves retrieving Landsat 8 satellite images and calculating the NDWI for the Area of Interest (AOI).

File:
**`NDWI.ipynb`**: Jupyter Notebook containing the code for NDWI calculation and AOI cropping.

How to Use:
Open the NDWI.ipynb file in Jupyter Notebook or Jupyter Lab.
Execute the cells to perform the NDWI calculation.

#### Airflow Ingestion Pipeline
Automates the SAR data ingestion process using Apache Airflow. Includes all necessary scripts and Directed Acyclic Graphs (DAGs) to manage the workflow.

Setup:
Ensure Apache Airflow is installed and configured.
Create the necessary output folders as specified in the code.
Deploy the DAGs and scripts to your Airflow instance.

 #### Prerequisites
Python 3.x
Apache Airflow
Jupyter Notebook or Jupyter Lab
PyroSAR and other required Python libraries

   
