from _1_create_client import create_connection

client = create_connection()

with client:
    db = client.testdb

    # Gets all data of collection
    # find returns a Cursor, use list it to see the content
    employees = db.employee_data.find()

    print(employees.next())
    print(employees.next())
    print(employees.next())

    # Return the cursor to the original state
    employees.rewind()  # Rewinds the cursor to its unevaluated state.

    print(employees.next())
    print(employees.next())
    print(employees.next())

    print("\n")

    # Print all employees
    print(list(employees))
    print("\n")

    # Print data for Emma
    print(list(db.employee_data.find({'name': "Emma"})))

client.close()
