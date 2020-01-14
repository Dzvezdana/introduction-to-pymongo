from pymongo import MongoClient

'''
Exercise 1: Import PyMongo and establish connection.
'''


def create_connection():
    # uri - defines the connection parameters
    uri = 'mongodb://localhost:27017/'
    # Start client to connect to MongoDB server
    client = MongoClient(uri)
    return client


if __name__ == '__main__':
    client = create_connection()
    print("Show details about the client...")
    print(client.stats)
    client.close()
