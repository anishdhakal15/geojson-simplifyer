# Introduction
This script simplifies the geometry of a GeoJSON file using the "shapely" library. The script takes 3 command line arguments: the input file, output file, and a tolerance value. The tolerance value represents the maximum distance that the simplified geometry can deviate from the original geometry. The script uses the 'simplify' method from the shapely library which uses the Douglas-Peucker algorithm, to simplify the geometry and reduce the size of the file.

# Use Case
- Simplifying large GeoJSON files that are too big to be easily handled and visualized.
- Improving the performance of data visualization tools like Plotly, Leaflet, and D3, which often have limitations on the size of the data they can handle.
- Reducing the size of large data sets for faster rendering and better performance.

# Requirements
- Python 3
- shapely library
- json library

# How to Use
1. Install the required libraries by running "pip install shapely json"
2. Run the script by providing 3 command line arguments: input file, output file and tolerance value. 
3. The input file should be a valid GeoJSON file. The output file will be the simplified version of the input file. 
4. The tolerance value should be a decimal value between 0 and 1, representing the maximum distance that the simplified geometry can deviate from the original geometry. Default value is 0.009
5. The script will output the simplified GeoJSON file to the specified output file.

# Note
- The tolerance value is a critical factor in the simplification process, and the optimal value will depend on the specific data and the desired level of simplification. It's important to experiment with different tolerance values to find the best balance between file size reduction and accuracy. It's also worth noting that the tolerance ratio is varying depending on the data, so you might want to adjust it accordingly.
- This script currently only supports LineString, Point, Polygon, MultiPolygon geometries, if you want to support other geometries you can add it to the script.
- The script also includes an additional function 'verifyArgv' to check if the input, output files are valid but it's removed as it was not providing any useful information.
- The script can be used as a command line tool or can be integrated with other scripts to simplify geojson files in bulk.

Overall, this script is a useful tool for simplifying large GeoJSON files and can help improve the performance of data visualization tools. It's easy to use and can be integrated with other scripts to simplify large data sets in bulk.
