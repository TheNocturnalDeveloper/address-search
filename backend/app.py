from flask import Flask, request, abort
from flask_cors import CORS, cross_origin
import shapefile

import re
import csv
from pathlib import Path

place_data_path = str(Path("places/gis_osm_places_free_1.shp"))
place_data = shapefile.Reader(place_data_path)
place_fields = place_data.fields[1:]
place_field_names = [field[0] for field in place_fields]

road_data_path = str(Path("roads/gis_osm_roads_free_1.shp"))
road_data = shapefile.Reader(road_data_path)
road_fields = road_data.fields[1:]
road_field_names = [field[0] for field in road_fields]

zip_data_path = str(Path('zip/zip_codes.csv'))


def get_place_by_name(name):
    """
        loops through the data in the place shp file
        until it finds a place with a matching name.
    """
    for row in place_data.iterShapeRecords():
        record = row.record

        # hamlets seem to be named after streets
        # skipping them will yield better results
        if record["fclass"] == "hamlet":
            continue

        if name.casefold() in record["name"].casefold():
            return dict(zip(place_field_names, record))

    return None


def get_road_by_name(name):
    """
        loops through the data in the road shp file
        until it finds a road with a matching name.
    """
    for row in road_data.iterShapeRecords():
        record = row.record
        if name.casefold() in record["name"].casefold():
            return dict(zip(road_field_names, record))
    return None


def get_area_by_zip(zip):
    """
        loops through the data in the zip csv file
        until it finds a matching zip code.
    """
    # dict reader doesn't reset iterator,
    # this means that the file has to be opened on every search
    zip_data = csv.DictReader(open(zip_data_path, 'r'))

    for row in zip_data:
        if zip.casefold() in row["nl_sixpp"].casefold():
            return row
    return None


# 1-4 numbers followed by at most 2 letters
zip_code = "[0-9]{1,4}[A-Za-z]{0,2}"
zip_code_regex = re.compile(zip_code)

app = Flask(__name__)
cors = CORS(app)
app.config.from_object('config')


@app.route('/')
@cross_origin()
def index():
    query = request.args.get("query", "")

    if zip_code_regex.fullmatch(query) is not None:
        area = get_area_by_zip(query)
        if area is not None:
            area.update({"type": "zip"})
            return area

    place = get_place_by_name(query)
    if place is not None:
        place.update({"type": "place"})
        return place

    road = get_road_by_name(query)
    if road is not None:
        road.update({"type": "road"})
        return road

    abort(404)
