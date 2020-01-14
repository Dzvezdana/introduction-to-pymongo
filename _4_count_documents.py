from _1_create_client import create_connection
from pymongo import DESCENDING

client = create_connection()

with client:
    db = client.testdb

    # Count the number of documents in the collection
    n_employee_data = db.employee_data.count_documents({})
    print("There are {} employees".format(n_employee_data))
    print("\n")

    # Find employees with salary higher than 45000 euros
    expensive_employees = db.employee_data.find({'salary': {'$gt': 45000}})
    for employee in expensive_employees:
        print('{0} {1}'.format(
            employee['name'],
            employee['salary']))
    print("\n")

    # Select only the _id and the name fields from the returned documents
    employee_data = db.employee_data.find({}, {'_id': 1, 'name': 1})

    for employee in employee_data:
        print(employee)
    print("\n")

    # Sort the employee data in descending way
    employee_data = db.employee_data.find().sort("salary", DESCENDING)

    for employee in employee_data:
        print('{0} {1}'.format(
            employee['name'],
            employee['salary'])
        )

    # Skip every second document and print the first 3 results.
    employee_data = db.employee_data.find().skip(2).limit(3)
    for employee in employee_data:
        print('{0}: {1}'.format(employee['name'], employee['salary']))
