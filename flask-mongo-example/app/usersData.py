"""This module will serve the API request."""

import ast
from importlib.machinery import SourceFileLoader
import json

from flask import request, jsonify

from app import app
from config import client


# Import the helpers module
helper_module = SourceFileLoader('*', './app/helpers.py').load_module()

# Select the database
db = client.restfulapi
# Select the collection
collection = db.users


@app.route("/")
def get_initial_response():
    """Welcome message for the API."""
    # Message to the user
    message = {
        'apiVersion': 'v1.0',
        'status': '200',
        'message': 'Welcome to the Flask API'
    }
    # Making the message looks good
    resp = jsonify(message)
    # Returning the object
    return resp


@app.route("/api/v1/users", methods=['POST'])
def create_user():
    """ Function to create new users. """
    try:
        # Create new users
        try:
            body = ast.literal_eval(json.dumps(request.get_json()))
        except:
            # Bad request as request body is not available
            # Add a message for debugging purpose
            return "", 400

        record_created = collection.insert(body)

        # Prepare the response
        if isinstance(record_created, list):
            # Return list of id of the newly created item
            return jsonify([str(v) for v in record_created]), 201
        else:
            # Return id of the newly created item
            return jsonify(str(record_created)), 201
    except:
        # Error while trying to create the resource
        # Add a message for debugging purpose
        return "", 500


@app.route("/api/v1/users/<user_id>", methods=['GET'])
def fetch_user(user_id):
    """ Function to fetch a user. """
    s = collection.find_one({'id': int(user_id)})
    if s:
        s["_id"] = str(s["_id"])
        output = dict(s)
    else:
        output = "No such id"
    return jsonify({'result': output})


@app.route("/api/v1/users/<user_id>", methods=['POST'])
def update_user(user_id):
    """ Function to update the user. """
    try:
        # Get the value which needs to be updated
        try:
            body = ast.literal_eval(json.dumps(request.get_json()))
        except:
            # Bad request as the request body is not available
            # Add a message for debugging purpose
            return "", 400

        # Updating the user
        records_updated = collection.update_one({"id": int(user_id)}, body)

        # Check if resource is updated
        if records_updated.modified_count > 0:
            # Prepare the response as resource is updated successfully
            return "", 200
        else:
            # Bad request as the resource is not available to update
            # Add a message for debugging purpose
            return "", 404
    except:
        # Error while trying to update the resource
        # Add a message for debugging purpose
        return "", 500


@app.route("/api/v1/users/<user_id>", methods=['DELETE'])
def remove_user(user_id):
    """ Function to remove the user. """
    try:
        # Delete the user
        delete_user = collection.delete_one({"id": int(user_id)})

        if delete_user.deleted_count > 0:
            # Prepare the response
            return "", 204
        else:
            # Resource Not found
            return "", 404
    except:
        # Error while trying to delete the resource
        # Add a message for debugging purpose
        return "", 500


@app.errorhandler(404)
def page_not_found(e):
    """ Send a message to the user with notFound 404 status. """
    # Message to the user
    message = {
        "err":
            {
                "msg": "This route is currently not supported. Please refer API documentation."
            }
    }
    # Making the message looks good
    resp = jsonify(message)
    # Sending OK response
    resp.status_code = 404
    # Returning the object
    return resp
