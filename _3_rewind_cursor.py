from _1_create_client import create_connection

client = create_connection()

with client:
    db = client.testdb

    # Gets all data of collection
    employees = db.employee_data.find()

    # find returns a Cursor, use list to see the content
    # print("Content of employee_data": "Your code goes here")

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
