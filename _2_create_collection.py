from _1_create_client import create_connection

'''
Let's create our first collections and learn some basic database management operations.

Notice how the last document contains one extra field 'age' that no other document has.
This would not be possible in Relational Databases. In relational databases if we needed 
the field 'age' in only one row of the table, we would have to add it as a column and 
insert Null in all remaining rows.
'''
employee_data = [
    {'name': 'Jane', 'salary': 52692},
    {'name': 'Daniel', 'salary': 65117},
    {'name': 'Anthony', 'salary': 8500},
    {'name': 'William', 'salary': 29000},
    {'name': 'Emma', 'salary': 340000},
    {'name': 'Christopher', 'salary': 22700},
    {'name': 'Olivia', 'salary': 41700},
    {'name': 'Isabella', 'salary': 19600},
    {'name': 'Mike', 'salary': 1600, 'age': 19}
]

client = create_connection()

with client:
    # Set database name to work with.
    # If it doesn't exist, it will be created as soon as one document is added.
    db = client.testdb

    # Create the employee_data collection.
    # How many documents does it contain? Nine documents.
    print("Insert data in collection...")
    insert_result = db.employee_data.insert_many(employee_data)
    db.employee_data.count()

    # Confirms that insert is successful
    print("Is insert successful: ", insert_result.acknowledged)
    print("\n")

    # Show existing database names
    print("Database names: ", client.list_database_names())
    print("\n")

    # List collections names
    print("Collections names: ", db.list_collection_names())
    print("\n")

    # Update an existing document
    update_result = db.employee_data.update_one(
        {'name': "William"},
        {'$set': {'salary': 10000}}
    )
    print(list(db.employee_data.find({'name': 'William'})))
    print("\n")

    # Insert a new document with update
    # Upsert will update the document if it already exists
    insert_result = db.employee_data.update_one(
        {'name': 'Gonzalez'},
        {'$set': {'salary': 13000}}, upsert=True)
    print(list(db.employee_data.find({'name': 'Gonzalez'})))
