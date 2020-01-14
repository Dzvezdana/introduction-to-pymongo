import csv
import json
from lxml import etree as et
from xmljson import yahoo as yh
import pandas as pd
import folium
from folium import plugins

from _1_create_client import create_connection

client = create_connection()
contacts_database = client.contactsdb

contacts_collection_csv = contacts_database["contacts_csv"]
contacts_collection_json = contacts_database["contacts_json"]
contacts_collection_xml = contacts_database["contacts_xml"]
bicycle_availability_collection = contacts_database["availability_map"]


def import_csv_file():
    # Import csv file into MongoDB
    df = open('./data/telefoniaBCN.csv')
    csv_data = csv.reader(df, delimiter=',')

    # Skip headers
    csv_data.__next__()

    for i in csv_data:
        contacts_collection_csv.insert_one({
            "timestamp_": i[0],
            "Senyal": i[1],
            "net_type": i[2],
            "Activitat": i[3],
            "NOM_MUNI": i[4],
            "Year": i[5],
            "Month": i[6],
            "Hour": i[7],
            "Carrier": i[8],
            "weekday": i[9],
            "Lat": i[10],
            "Lng": i[11]
        })


def import_json_file():
    # Import json into MongoDB
    json_data = json.loads(open('./data/dataset.json').read())
    contacts_collection_json.insert_many(json_data)


def import_xml_file():
    # initialize XML parser and parse file
    parser = et.XMLParser(remove_blank_text=False, ns_clean=False)
    xml = et.parse('./data/dataset.xml', parser=parser)
    root = xml.getroot()

    # Insert the raw XML into MongoDB raw_xml collection
    xml_blob = et.tostring(root).decode("UTF-8")
    xml_document = {"xml_blob": xml_blob}
    contacts_database.raw_xml.insert_one(xml_document)

    # Parse XML to JSON and insert into the contacts_collection_xml collection
    parsed = yh.data(root)
    parsed_doc = json.loads(json.dumps(parsed))
    contacts_collection_xml.insert_one(parsed_doc)


def import_bicycle_file():
    # Import JSON into MongoDB
    json_data = json.loads(open('./data/availability_map.json').read())
    bicycle_availability_collection.insert_many(json_data)


def main():
    # import_csv_file()
    # import_json_file()
    # import_xml_file()
    # import_bicycle_file()

    # The number of bikes is String instead of Integer.
    bikes_list = list(bicycle_availability_collection.distinct('bikes'))
    for num in bikes_list:
        bicycle_availability_collection.update_many({'bikes': num},
                                                    {'$set': {'bikes': int(num)}})

    # Loading database query in pandas dataframe so we can visualize it
    filters = {'status': 'OPN', 'bikes': {'$gte': 3}}
    fields = {'_id', 'lat', 'lon', 'bikes', 'slots'}
    query = list(bicycle_availability_collection.find(filters, fields))
    df = pd.DataFrame(query)

    center_lat = 51.2194
    center_lon = 4.4025

    location_map = folium.Map(location=[center_lat, center_lon],
                              zoom_start=16,
                              width=800,
                              height=600
                              )

    longitude = len(df)
    for i in range(longitude):
        lng = float(df.iloc[i][3])
        lat = float(df.iloc[i][2])
        description = 'Bikes: ' + \
                      str(df.iloc[i][1]) + \
                      '<br> Empty slots: ' + \
                      str(df.iloc[i][4])
        folium.Marker([lat, lng],
                      popup=description,
                      icon=folium.Icon(color='red')).add_to(location_map)

    location_map.save('index.html')

    lats = []
    lngs = []
    totals = []
    for i in range(longitude):
        lats.append(float(df.loc[i]['lat']))
        lngs.append(float(df.loc[i]['lon']))
        totals.append(float(df.loc[i]['bikes']))

    # Visualization data adapted from https://colab.research.google.com/github/Giffy/MongoDB_PyMongo_Tutorial/blob/master/2_1_Mobile_coverage.ipynb
    location_map.add_child(plugins.HeatMap(
        zip(
            lats,
            lngs,
            totals),
        radius=12))

    location_map.save('index2.html')


if __name__ == "__main__":
    main()
