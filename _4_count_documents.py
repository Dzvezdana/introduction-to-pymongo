from _1_create_client import create_connection
from pymongo import DESCENDING

client = create_connection()

with client:
    db = client.testdb

    '''
    Exercise 1
    Count the number of documents in the collection
    '''
    # n_employee_data = # Add code here
    # print("There are {} employees".format(n_employee_data))
    # print("\n")

    '''
    Exercise 2
    Find employees with salary higher than 45000 euros
    '''
    # expensive_employees = # Add code here
    # for employee in expensive_employees:
    #     print('{0} {1}'.format(
    #         employee['name'],
    #         employee['salary']))
    # print("\n")

    '''
    Exercise 3
    Select only the _id and name fields from the returned documents
    '''
    # employee_data = # Add code here
    # for employee in employee_data:
    #     print(employee)
    # print("\n")

    '''
    Exercise 4
    Sort the employee using their salary in descending way
    '''
    # employee_data = # Add code here
    # for employee in employee_data:
    #     print('{0} {1}'.format(
    #         employee['name'],
    #         employee['salary'])
    #     )

    '''
    Exercise 5
    Skip every second document and print the first 3 results
    '''
    # employee_data = # Add code here
    # for employee in employee_data:
    #     print('{0}: {1}'.format(employee['name'], employee['salary']))
