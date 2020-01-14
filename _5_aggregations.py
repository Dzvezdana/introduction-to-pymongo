from _1_create_client import create_connection

client = create_connection()

with client:
    db = client.testdb

    # Calculate the total salary
    agr = [{'$group': {'_id': 1, 'all': {'$sum': '$salary'}}}]

    val = list(db.employee_data.aggregate(agr))
    print('The sum of the salary is {}.'.format(val[0]['all']))
    print("\n")

    # Use the match operator to select specific employee data to aggregate.
    agr = [{'$match': {'$or': [{'name': "William"}, {'name': "Emma"}]}},
           {'$group': {'_id': 1, 'sum2employee_data': {'$sum': "$salary"}}}]
    val = list(db.employee_data.aggregate(agr))
    print('The sum of the salaries of William and Emma is: {}'
          .format(val[0]['sum2employee_data']))
    print("\n")
