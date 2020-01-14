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

    ''' 
    Exercise 1
    Return the cursor to the original state
    '''
    # Add code here

    print(employees.next())
    print(employees.next())
    print(employees.next())

    print("\n")

    ''' 
    Exercise 2
    Print all employees
    '''
    # print("Add code here")
    # print("\n")

    ''' 
    Exercise 3
    Print the document that contains the name Emma
    '''
    # print("Add code here")
    # print("\n")

client.close()
