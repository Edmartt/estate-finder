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


#### Note

For requesting the api docs after running the project just go to `/api/docs` and you will see something like this:

![](https://github.com/Edmartt/estate-finder/blob/dev/assets/swagger.png)


This is the prototype diagram:

![](https://github.com/Edmartt/estate-finder/blob/dev/assets/prototype.png)

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


## Running Development Version With Flask

1. Clone the repo:

```
git clone https://github.com/Edmartt/estate-finder.git
```

2. Browse into the project directory

```
cd estate-finder
```

3. Create a virtual environment

```
python -m venv <virtual-environment-name>
```

4. Activate the virtual environment

```
source <virtual-environment-name>/bin/activate
```

5. Set the environment variables following the envrc.example file here ![.envrc.example](https://github.com/Edmartt/estate-finder/blob/dev/.envrc.example)

```
source .envrc
```

6. Run with

```
flask run
```

## Running with Docker

1. Build the image

```
docker build -t edmartt/estate-finder:beta .
```

2. create a .env file following the .env.example file in this repo

![.env.example](https://github.com/Edmartt/estate-finder/blob/dev/.env.example)

3. Run a container instance

```
docker run --rm -p 6100:5000 --env-file .env edmartt/estate-finder:beta
```

### Note

You can still take a look at the swagger docs in localhost:6000/api/docs, the only difference with the development version is that you can't make requests


### doubts during development


Do I need a sample json file?

For the development of the solution it was required to create a .json file with the data that I expected to receive from a client application, which I found a little strange because if you can only show the properties for sale, pre sale and sold, the ideal solution is to create a query from sql to bring only the records that match that criteria. Additionally, it is requested to filter the results optionally with three parameters that are the year, city and status, seeing that I am asked for a json of the expected data of a client left me with much doubt, but I thought it was a better solution to generate a documentation with swagger.

## Database concept

I was asked to extend the database from which I get the records for this microservice with an ER diagram to support likes to properties while keeping a history of likes for each registered user.

I ended up with this extended version because users can like any number of properties, but I thought also when they don't like it anymore for some reason, then I added to my table a field called 'active' to know with a new record if the property is already liked or not.

The like_history table takes into account the user who liked the property as well as the identifier of the property and the date of creation of the record. Each time you like a different property or stop liking it, a new record will be added and you will have access to a complete history of all the properties that have been liked by the users.

This is the final model:


![](https://github.com/Edmartt/estate-finder/blob/dev/assets/extended%20database.png)


Some improvements for this database that I thought of were the use of authentication systems such as Auth0 to handle authentication through a robust platform saving time in maintaining code or updating obsolete libraries. Although there is also an alternative of having a separate database with a microservice that handles the authentication of users, sending name and password that only serve in this microservice, but in response to a successful authentication returns a JWT whose signature is generated privately, and also the JWT is assigned a time of life and is a more secure mechanism to manage user access.

The latter alternative would involve maintenance, but would have full control of user data in a more secure way.


## Note

In addition to the already mentioned, something quite striking is that the passwords are stored in plain text, which is most insecure in case the database is compromised. The ideal is to add some encryption algorithm. There are implementations such as libraries that make use of bcrypt, which adds enough security to the passwords with hash functions that prevent the readability of the password and in case the database is compromised, access to user passwords would not be something easy at least with the paradigm of classical computing.
