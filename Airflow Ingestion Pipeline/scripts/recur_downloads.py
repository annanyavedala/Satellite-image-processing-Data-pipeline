from datetime import datetime, timedelta
from airflow import DAG
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt

 # define the area of interest as a polygon
footprint_geojson = {
    "type": "Polygon",
    "coordinates": [[
        [-74.0204, 40.6997],
        [-74.0204, 40.7002],
        [-74.0197, 40.7002],
        [-74.0197, 40.6997],
        [-74.0204, 40.6997]
    ]]
}

# convert the GeoJSON polygon to WKT format
footprint_wkt = geojson_to_wkt(footprint_geojson)

# connect to the Copernicus SciHub API
#Enter username and password
api = SentinelAPI('', '', 'https://scihub.copernicus.eu/dhus')

    # define the date range for new data
start_date = datetime.today() - timedelta(days=1)  # yesterday
end_date = datetime.today()

    # search for new images within the given dates and AOI
products = api.query(footprint_wkt,
                         date=(start_date, end_date),
                         platformname='Sentinel-1',
                        producttype='GRD',
                        sensoroperationalmode='IW'
                        )

    # download new products

api.download_all(products, directory_path='/Users/annanya/airflow/recur_downloads')

