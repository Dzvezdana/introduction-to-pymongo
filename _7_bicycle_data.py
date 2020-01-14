import json
import pandas as pd
import folium
from folium import plugins

from _1_create_client import create_connection

client = create_connection()
contacts_database = client.contactsdb
bicycle_availability_collection = contacts_database["availability_map"]


def import_bicycle_file():
    # Import JSON into MongoDB
    json_data = json.loads(open("./data/availability_map.json").read())
    bicycle_availability_collection.insert_many(json_data)


def create_heatmap(df, longitude):
    center_lat = 51.2194
    center_lon = 4.4025
    location_map = folium.Map(
        location=[center_lat, center_lon], zoom_start=16, width=800, height=600
    )

    lats = []
    lngs = []
    totals = []
    for i in range(longitude):
        lats.append(float(df.loc[i]["lat"]))
        lngs.append(float(df.loc[i]["lon"]))
        totals.append(float(df.loc[i]["bikes"]))

    # Adapted from https://colab.research.google.com/github/Giffy/MongoDB_PyMongo_Tutorial/blob/master/2_1_Mobile_coverage.ipynb
    location_map.add_child(plugins.HeatMap(zip(lats, lngs, totals), radius=12))
    location_map.save("index.html")


def map_with_markers(df, longitude):
    center_lat = 51.2194
    center_lon = 4.4025
    location_map_m = folium.Map(
        location=[center_lat, center_lon], zoom_start=16, width=800, height=600
    )
    for i in range(longitude):
        lng = float(df.iloc[i][3])
        lat = float(df.iloc[i][2])
        description = (
            "Bikes: " + str(df.iloc[i][1]) + "<br> Empty slots: " + str(df.iloc[i][4])
        )
        folium.Marker(
            [lat, lng], popup=description, icon=folium.Icon(color="red")
        ).add_to(location_map_m)

    location_map_m.save("index2.html")


def main():
    import_bicycle_file()
    # The number of bikes is String instead of Integer.
    bikes_list = list(bicycle_availability_collection.distinct("bikes"))
    for num in bikes_list:
        bicycle_availability_collection.update_many(
            {"bikes": num}, {"$set": {"bikes": int(num)}}
        )

    # Loading database query in pandas dataframe so we can visualize it
    filters = {"status": "OPN", "bikes": {"$gte": 3}}
    fields = {"_id", "lat", "lon", "bikes", "slots"}
    query = list(bicycle_availability_collection.find(filters, fields))
    df = pd.DataFrame(query)

    longitude = len(df)
    create_heatmap(df, longitude)
    map_with_markers(df, longitude)


if __name__ == "__main__":
    main()
