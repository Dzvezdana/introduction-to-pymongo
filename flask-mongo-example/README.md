### Designing RESTful API with Python-Flask and MongoDB

This project demonstrates how to design RESTful API with Python-Flask and MongoDB.

Here are the tools we’ll need to build our APIs:

* Python 3.7
* [Postman](https://www.postman.com/)
* MongoDB

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

##### POST Example
[![POST](https://i.postimg.cc/dt98gDRv/POST.png)](https://postimg.cc/WhhFkNff)

##### GET Example
[GET](https://postimg.cc/Yh59L1Fh)

##### DELETE Example
[DELETE](https://postimg.cc/DWd8T88m)

##### UPDATE Example
[UPDATE](https://postimg.cc/bDVYyb8Y)

*Adapted from*: https://github.com/Moesif/moesif-flask-mongo-example