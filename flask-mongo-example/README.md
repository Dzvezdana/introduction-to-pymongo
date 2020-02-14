### Designing REST API with Python-Flask and MongoDB

This project demonstrates how to design REST API with Python-Flask and MongoDB.

Here are the tools we’ll need to build our APIs:

* Python 3.7
* [Postman](https://www.postman.com/)
* MongoDB
* Docker

##### Create your local environment

```bash
virtualenv -p python3 venv # Create the environment
source venv/bin/activate   # Activate the environment
```

##### Install dependencies

```python
pip3 install -r requirements.txt
```

##### Start the MongoDB Server

Let's start MongoDB using Docker.

```bash
docker run -d -p 27017-27019:27017-27019 --name mongodb mongo:latest
```

##### Start the application

```bash
python run-app.py
```

Once the application is started, go to [localhost](http://0.0.0.0:80/).
We'll use [Postman](https://www.postman.com/) to explore the APIs.

#### POST Example
[![POST](https://i.postimg.cc/dt98gDRv/POST.png)](https://postimg.cc/WhhFkNff)

IP:
```bash
http://0.0.0.0:80/api/v1/users
```

Body:
```json
[
  { 
    "id":1,
    "name": "Dana",
    "email": "dana@me",
    "phone": "223305",
    "location": "NL"
  }
]
```

#### GET Example
[![GET](https://i.postimg.cc/pLTn7CXY/GET.png)](https://postimg.cc/Yh59L1Fh)

IP:
```bash
http://0.0.0.0:80/api/v1/users/1
```

#### UPDATE Example
[![UPDATE](https://i.postimg.cc/SRknG7v9/UPDATE.png)](https://postimg.cc/bDVYyb8Y)

IP:
```bash
http://0.0.0.0:80/api/v1/users/1
```

Body:
```python
{"$set": {"name": "New Name"}}
```

#### DELETE Example
[![DELETE](https://i.postimg.cc/cJPYf3W7/DELETE.png)](https://postimg.cc/DWd8T88m)

IP:
```bash
http://0.0.0.0:80/api/v1/users/1
```

*Adapted from*: https://github.com/Moesif/moesif-flask-mongo-example