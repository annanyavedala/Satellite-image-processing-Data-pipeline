from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
import logging
logging.basicConfig(level=logging.DEBUG)

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
#Add the api username and password
api = SentinelAPI('', '', 'https://scihub.copernicus.eu/dhus')

# search for Sentinel-1 products that intersect with the area of interest and time range
products = api.query(footprint_wkt,
                     date=('20220101', '20221231'),
                     platformname='Sentinel-1',
                     producttype='GRD',
                     sensoroperationalmode='IW', 
                     limit=1
                    )
#In order to download all the images, we will just have to get rid of the limit parameter
# download the products in zip format
# product_id = list(products.keys())[0]
api.download_all(products, directory_path='/Users/annanya/airflow/downloads')
