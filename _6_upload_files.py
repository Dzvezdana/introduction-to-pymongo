import csv
import json
from lxml import etree as et
from xmljson import yahoo as yh

from _1_create_client import create_connection

client = create_connection()
contacts_database = client.contactsdb

contacts_collection_csv = contacts_database["contacts_csv"]
contacts_collection_json = contacts_database["contacts_json"]
contacts_collection_raw_xml = contacts_database["raw_xml"]
contacts_collection_xml = contacts_database["contacts_xml"]


def import_json_file():
    # Import json into MongoDB
    json_data = json.loads(open('./data/dataset.json').read())
    contacts_collection_json.insert_many(json_data)


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


def import_xml_file():
    # Initialize XML parser and parse the file
    parser = et.XMLParser(remove_blank_text=False, ns_clean=False)
    xml = et.parse('./data/dataset.xml', parser=parser)
    root = xml.getroot()

    # Insert the raw XML into MongoDB raw_xml collection
    xml_blob = et.tostring(root).decode("UTF-8")
    xml_document = {"xml_blob": xml_blob}
    contacts_collection_raw_xml.insert_one(xml_document)

    # Parse XML to JSON and insert into the contacts_collection_xml collection.
    parsed = yh.data(root)
    parsed_doc = json.loads(json.dumps(parsed))
    contacts_collection_xml.insert_many(parsed_doc['dataset']['record'])


def main():
    # import_json_file()
    # import_csv_file()
    import_xml_file()


if __name__ == "__main__":
    main()
