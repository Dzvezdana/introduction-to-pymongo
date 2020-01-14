from _1_create_client import create_connection

'''
Let's create our first collection and learn some basic database management operations.
'''
employee_data = [
    {'name': 'Jane', 'salary': 52692},
    {'name': 'Daniel', 'salary': 65117},
    {'name': 'Anthony', 'salary': 8500},
    {'name': 'William', 'salary': 29000},
    {'name': 'Emma', 'salary': 340000},
    {'name': 'Christopher', 'salary': 22700},
    {'name': 'Olivia', 'salary': 41700},
    {'name': 'Isabella', 'salary': 19600}
]

# Create the connection
client = create_connection()


def insert_in_collection():
    '''
    Exercise 1
    Create the employee_data collection.
    How many documents does it contain?
    '''
    print("Insert data in collection...")
    # insert_result = # Create the collection here
    return insert_result


with client:
    # Set database name to work with.
    # If it doesn't exist, it will be created as soon as one document is added.
    db = client.testdb

    insert_result = insert_in_collection()
    # Confirms that insert is successful
    print("Is insert successful: ", insert_result.acknowledged)
    print("\n")

    '''
    Exercise 2
    Print the existing database names
    '''
    # print("Database names: ", "Add code here")
    # print("\n")

    '''
    Exercise 3
    List collections names
    '''
    # print("Collections names: ", "Add code here")
    # print("\n")

    '''
    Exercise 4
    Update an existing document.
    Update Williams salary to 10 000
    '''
    # update_result = # Add code here
    # Confirm the change
    # print(list(db.employee_data.find({'name': 'William'})))
    # print("\n")

    '''
    Exercise 5
    Insert a new document with update.
    Create new employee Gonzalez, whose salary is 13000
    '''
    # insert_result = # Add code here
    # Confirm the change
    # print(list(db.employee_data.find({'name': 'Gonzalez'})))

# Close the connection
client.close()
