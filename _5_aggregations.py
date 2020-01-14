from _1_create_client import create_connection

client = create_connection()

with client:
    db = client.testdb

    '''
    Exercise 1
    Calculate the total salary.
    '''

    '''
    Exercise 2
    Calculate the sum of the salaries of William and Emma.
    '''
