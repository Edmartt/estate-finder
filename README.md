# ESTATE FINDER

## Requirements

- Python 3.11
- Flask
- MySQL
- Docker


This project is in charge of making queries to a real estate database to show users the properties according to their status: pre-sale, for sale, and sold.

Users are able to filter the properties by: year of construction, city and state.

I've started to solve this problem by designing diagram with the best structure (according to me) for this microservice


After that, I have created the classes and methods that I will need, in the business logic structure, and finally, after having defined this aspect that I consider essential, I have moved on to create the directories and base files that constitute the project.


This is the prototype diagram:

![](https://github.com/Edmartt/estate-finder/blob/main/assets/prototype.png)

This is the final project structure:

`
.
├── config.py
├── docker-compose.yml
├── Dockerfile
├── README.md
├── run.py
└── src
    ├── auth
    │   ├── http_authentication.py
    │   ├── __init__.py
    │   └── jwt.py
    ├── database
    │   ├── database_interface.py
    │   ├── __init__.py
    │   └── mysql.py
    ├── estate
    │   ├── data_access_layer
    │   │   ├── data_access_implementation.py
    │   │   └── data_access_interface.py
    │   ├── estate_errors
    │   ├── http_estate.py
    │   ├── __init__.py
    │   ├── models
    │   │   └── estate.py
    │   ├── routes.py
    │   └── utils
    │       └── __init__.py
    └── __init__.py
`

I have tried to follow the vertical slice architecture, because it provides flexibility and is easy to maintain over time.
