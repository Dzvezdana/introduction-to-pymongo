from _1_create_client import create_connection
from pymongo import DESCENDING

client = create_connection()

with client:
    db = client.test_database

    '''
    Exercise 1
    Count the number of documents in the collection
    '''
    # n_employee_data = db.employees.count()
    # print("There are {} employees".format(n_employee_data))
    # 10
    # print("\n")

    '''
    Exercise 2
    Find employees with salary higher than 45000 euros
    '''
    # expensive_employees = db.employees.find({'salary':{'$gt': 45000}})
    # for employee in expensive_employees:
    #     print('{0} {1}'.format(
    #         employee['name'],
    #         employee['salary']))
    # print("\n")
    # Jane 52692
    # Daniel 65117
    # Emma 340000


    '''
    Exercise 3
    Select only the _id and name fields from the returned documents
    '''
    # employee_data = db.employees.find({}, {'name': 1, 'name': 1}) #
    # for employee in employee_data:
    #     print(employee)

    '''
    Exercise 4
    Sort the employee using their salary in descending way
    '''
    # employee_data = db.employees.find().sort('salary', -1)
    # for employee in employee_data:
    #     print('{0} {1}'.format(
    #         employee['name'],
    #         employee['salary'])
    #     )
# Emma 340000
# Daniel 65117
# Jane 52692
# Olivia 41700
# Christopher 22700
# Isabella 19600
# Gonzalez 13000
# William 10000
# Anthony 8500
# Mike 1600


    '''
    Exercise 5
    Skip the first 2 documents and then print the next 3 results
    '''
    employee_data = db.employees.find(skip=2, limit=3)
    for employee in employee_data:
        print('{0}: {1}'.format(employee['name'], employee['salary']))
