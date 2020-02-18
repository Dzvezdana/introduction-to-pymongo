from _1_create_client import create_connection

client = create_connection()

with client:
    db = client.test_database

    # Gets all data of collection
    employees = db.employees.find()

    # find returns a Cursor, use list to see the content
    # print("Content of employee_data": "Your code goes here")

    print(employees.next())
    print(employees.next())
    print(employees.next())

    ''' 
    Exercise 1
    Return the cursor to the original state
    '''
    employees.rewind()

    print(employees.next())
    print(employees.next())
    print(employees.next())

    print("\n")

    ''' 
    Exercise 2
    Print all employees
    '''
    #employees = db.employees.find()
    #print(list(employees)) #convert cursor into a list
    # print("\n")

    ''' 
    Exercise 3
    Print the document that contains the name Emma
    '''
    emma = db.employees.find(({'name': 'Emma'}))
    print(list(emma))

    # print("\n")

client.close()
