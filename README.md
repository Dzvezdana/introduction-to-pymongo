# Introduction to PyMongo

This directory contains a set of basic examples for new MongoDB users.
Clone the repository and create a new *exercises* branch.

You can find the documentation here:

* [MongoDB](https://docs.mongodb.com/manual/)
* [Pymongo](https://api.mongodb.com/python/current/)

[**Exercise 1 - Making a Connection**](https://github.com/Dzvezdana/introduction-to-pymongo/blob/master/_1_create_client.py)

The first step when working with PyMongo is to create a MongoClient.

[**Exercise 2 - Creating a Collection**](https://github.com/Dzvezdana/introduction-to-pymongo/blob/master/_2_create_collection.py)

Let's create our first collections and learn some basic database management operations.

[**Exercise 3 - Cursors in MongoDB**](https://github.com/Dzvezdana/introduction-to-pymongo/blob/master/_3_rewind_cursor.py)

What is Cursor in MongoDB? When the `db.collection.find ()` function is used to search for documents in the collection, 
the result returns a pointer to the collection of documents returned which is called a cursor.

By default, the cursor will be iterated automatically when the result of the query is returned. 
But one can also explicitly go through the items returned in the cursor one by one. 
Let's see how we can do it in this exercise.

[**Exercise 4 - Count Documents**](https://github.com/Dzvezdana/introduction-to-pymongo/blob/master/_4_count_documents.py)

Let's learn how to count and sort documents! 


[**Exercise 5 - Aggregations**](https://github.com/Dzvezdana/introduction-to-pymongo/blob/master/_6_aggregations.py)

Aggregation operations process data records and return computed results. 
Aggregation operations group values from multiple documents together, and can perform a variety of operations on the 
grouped data (like finding the average, the sum etc.). 
They return a single result.

[**Exercise 6 - File conversion**](https://github.com/Dzvezdana/introduction-to-pymongo/blob/master/_6_upload_files.py)

Uploading a JSON is quite straight forward in MongoDB. But what if the data has another format like CSV or XML?
Then we first need to convert the file to a format MongoDB understands.
Let's learn how to do this in the following exercise.

The data you need to upload is located in the [data folder](https://github.com/Dzvezdana/introduction-to-pymongo/tree/master/data). 
Upload `dataset.json`, `dataset.xml` and `telefoniaBCN.csv`. You don't have to upload the `availability_map.json` file yet. 
We gonna use the for the next exercise.

*Note*: Don't use the shell to upload the files.

*Hint 1*: You can use the csv module to read the csv file. We need to create a dictionary from the csv.

*Hint 2*: I used [lxml](https://lxml.de/) to process the XML file in Python and [xmljson](https://pypi.org/project/xmljson/)
to convert the XML file to JSON. Of course this is just one way how this can be done and you can take a different approach.

*Hint 3*: Be careful: depending on the parser you're gonna use, you might end up with one JSON for the whole XML file. 
However, you need to insert as many documents in the collection as ids. So you need to select array field from the final output. 

[**Exercise 7 - Analyzing Bicycle Data**](https://github.com/Dzvezdana/introduction-to-pymongo/blob/master/_7_bicycle_data.py)

In this short exercise we will analise the rent bicycle availability in Antwerp, Belgium. I created two simple maps
that show the renting locations, and the number of available bikes, as well as a heat map. To generate the maps
you need to do simple data processing first.

*Note*: The visualization code was adapted from https://colab.research.google.com/github/Giffy/MongoDB_PyMongo_Tutorial/blob/master/2_1_Mobile_coverage.ipynb
