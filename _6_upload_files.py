from _1_create_client import create_connection

client = create_connection()
contacts_database = client.contactsdb

contacts_collection_csv = contacts_database["contacts_csv"]
contacts_collection_json = contacts_database["contacts_json"]
contacts_collection_raw_xml = contacts_database["raw_xml"]
contacts_collection_xml = contacts_database["contacts_xml"]


def import_csv_file():
    # Import csv file into MongoDB
    return


def import_json_file():
    # Import json into MongoDB
    return


def import_xml_file():
    # Insert the raw XML into MongoDB raw_xml collection
    # Then parse XML to JSON and insert into the contacts_collection_xml collection
    return


def main():
    # import_csv_file()
    # import_json_file()
    # import_xml_file()
    return


if __name__ == "__main__":
    main()
