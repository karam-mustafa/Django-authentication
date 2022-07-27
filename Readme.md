# Django Projects - Allauth

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Prerequisites](#Prerequisites)
- [Installing](#Installing)




## About <a name = "about"></a>

The project is an example of the Allauth package usage with Google and Microsoft.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them.

```
Python 3.9
Pipenv
```

### Installing

A step by step series of examples that tell you how to get a development env running.

Create Workplace *projectname* (Linux)

```
$ mkdir projectname
```

Create Virtual Enviroment
navigate to *projectname*

```
$ Python -m pip install pipenv
$ Python -m pipenv install
```

Activate Virtual Enviroment

```
$ Python -m pipenv shell
$ python -m pip install pipenv
```
Install python packages 

```
$ Python -m pipenv install
```

Change Djnago Secret Key in  Settings

```
SECRET_KEY='your secret key'
```

Run Database Migration 
```
$ python manage.py migrate
```

Add your social providers through admin panel
```
Go to http://localhost:8000/admin
```

Run Django Server 
```
$ python manage.py runserver
```

Please use the "app" application to build your customized views.

**For Testing:**

Google Auth: Go to http://localhost:8000/auth/google (Use the Access Token)

Microsoft Auth: Go to http://localhost:8000/auth/ms (Use the Access Token)

Check Auth: Go to http://localhost:8000/auth/secure

**Useful Links:**

Google Playground: https://developers.google.com/oauthplayground/
