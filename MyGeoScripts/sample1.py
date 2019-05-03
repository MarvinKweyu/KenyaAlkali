import geopandas as gpd

shapefile = '../Data/ne_110m_admin_0_countries.shp'

# read shapefile using geopandas
gdf = gpd.read_file(shapefile)[['ADMIN','ADM0_A3','geometry']]

# rename columns
gdf.columns = ['country', 'country_code', 'geometry']
gdf.head()
# print("hello")
