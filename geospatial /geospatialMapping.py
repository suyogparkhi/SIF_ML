import geopandas as gpd
import leafmap


geojson_file = 'india-soi.geojson'
parquet_output = 'india-soi.parquet'

gdf = gpd.read_file(geojson_file)


gdf.to_parquet(parquet_output, index=False, compression='snappy')

print(f"Parquet file '{parquet_output}' created successfully.")


m = leafmap.Map()


parquet_file = 'india-soi.parquet'
census_gdf = gpd.read_parquet(parquet_file)


m.add_gdf(census_gdf, layer_name='Census Data', fill_color='red', opacity=0.5)


html_content = m.to_html()
with open("map_with_census1.html", "w") as html_file:
    html_file.write(html_content)
