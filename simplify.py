from json import load, dump
from shapely.geometry import LineString, Point, Polygon
from sys import argv
from os.path import isfile


def simplify_geojson(input_file, output_file, tolerance=0.009):
    with open(input_file, 'r') as f:
        data = load(f)
    if 'features' in data:
        simplified_features = []
        for feature in data['features']:
            geometry = feature['geometry']
            if geometry['type'] == 'LineString':
                feature['geometry']['coordinates'] = LineString(
                    geometry['coordinates']).simplify(tolerance, preserve_topology=True).coords[:]
            elif geometry['type'] == 'Point':
                pass
            elif geometry['type'] == 'Polygon':
                simplified_exterior = LineString(geometry['coordinates'][0]).simplify(
                    tolerance, preserve_topology=True)
                simplified_interiors = [LineString(interior).simplify(
                    tolerance, preserve_topology=True) for interior in geometry['coordinates'][1:]]
                feature['geometry']['coordinates'] = [
                    simplified_exterior.coords[:]] + [i.coords[:] for i in simplified_interiors]
            elif geometry['type'] == 'MultiPolygon':
                simplified_polygons = []
                for polygon in geometry['coordinates']:
                    simplified_exterior = LineString(polygon[0]).simplify(
                        tolerance, preserve_topology=True)
                    simplified_interiors = [LineString(interior).simplify(
                        tolerance, preserve_topology=True) for interior in polygon[1:]]
                    simplified_polygons.append(
                        [simplified_exterior.coords[:]] + [i.coords[:] for i in simplified_interiors])
                feature['geometry']['coordinates'] = simplified_polygons
            else:
                print(
                    f'Warning: Unsupported geometry type "{geometry["type"]}"')
            simplified_features.append(feature)
        data['features'] = simplified_features
    with open(output_file, 'w') as f:
        dump(data, f)

def verifyArgv():
    try:
        if len(argv)<4:
            raise Exception("3 parameters required \n simplifier.py input.jeojson output.geojson accuracy percentage")
        elif not isfile(argv[1]):
            raise Exception(argv[1],"file not found. ")
        elif isfile(argv[2]):
            raise Exception(argv[2],"file is already exist. ")
        elif int(argv[3]) not in range(0,101):
            raise Exception("accuracy value should be in between 1-100. ")
        output_data = simplify_geojson(
    argv[1], argv[2], float(argv[3]))
    except Exception as e:
        print(e)

verifyArgv()
