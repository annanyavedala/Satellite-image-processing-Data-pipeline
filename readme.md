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

   
