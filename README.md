# PROPERTY FINDER

## Requirements

- Python 3.11
- Flask
- MySQL
- Docker


This project is in charge of making queries to a real estate database to show users the properties according to their status: pre-sale, for sale, and sold.

Users are able to filter the properties by: year of construction, city and state.

I've started to solve this problem by designing diagram with the best structure (according to me) for this microservice


After that, I have created the classes and methods that I will need, in the business logic structure, and finally, after having defined this aspect that I consider essential, I have moved on to create the directories and base files that constitute the project.


#### Note

For requesting the api docs after running the project just go to `/api/docs` and you will see something like this:

![](https://github.com/Edmartt/estate-finder/blob/main/assets/swagger.png)


This is the prototype diagram:

![](https://github.com/Edmartt/estate-finder/blob/main/assets/prototype.png)

This is the final project structure:

```
├── config.py
├── docker-compose.yml
├── Dockerfile
├── filter_data.json
├── README.md
├── requirements.txt
├── run.py
└── src
    ├── auth
    │   ├── http_authentication.py
    │   ├── __init__.py
    │   └── jwt.py
    ├── database
    │   ├── database_interface.py
    │   ├── __init__.py
    │   └── mysql_connection.py
    ├── estate
    │   ├── data_access_layer
    │   │   ├── data_access_implementation.py
    │   │   ├── data_access_interface.py
    │   │   └── __init__.py
    │   ├── estate_errors
    │   │   ├── errors.py
    │   │   └── __init__.py
    │   ├── http_estate.py
    │   ├── __init__.py
    │   ├── models
    │   │   ├── estate.py
    │   │   └── __init__.py
    │   ├── routes.py
    │   └── utils
    │       ├── filter_validator.py
    │       └── __init__.py
    ├── __init__.py
    └── static
        └── swagger.yaml
```

I have tried to follow the vertical slice architecture, because it provides flexibility and is easy to maintain over time.


## Running

clone the repo:

```
git clone https://github.com/Edmartt/estate-finder.git
```
browse into the project directory

```
cd estate-finder
```

create a virtual environment

```
python -m venv <virtual-environment-name>
```

activate the virtual environment

```
source <virtual-environment-name>/bin/activate
```

set the environment variables following the envrc.example file

```
source .envrc
```

and run with

```
flask run
```



### doubts during development


Do I need a sample json file?

For the development of the solution it was required to create a .json file with the data that I expected to receive from a client application, which I found a little strange because if you can only show the properties for sale, pre sale and sold, the ideal solution is to create a query from sql to bring only the records that match that criteria. Additionally, it is requested to filter the results optionally with three parameters that are the year, city and status, seeing that I am asked for a json of the expected data of a client left me with much doubt, but I thought it was a better solution to generate a documentation with swagger.
