# Bank Storage Watcher

This site allows to receive information about visits by employees of a bank storage and analyze the duration of a visit. 
The site was developed using the [Django](https://www.djangoproject.com/) web framework and uses [PostgreSQL](https://www.postgresql.org/) database for its work.

## How to install

For site to work, you need to install **Python 3.6+** and then install all dependencies:

```bash

$ pip install -r requirements.txt

```

## Used environment variables

* **DATABASE_URL** - a database URL(must be in form **postgresql://user:password@host:port/database**)
* **DJANGO_SECRET_KEY** - a [secret key](https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-SECRET_KEY)
* **DJANGO_DEBUG_MODE** - turn on/off [debug mode](https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-DEBUG) (Default: **off**)
* **DJANGO_TIME_ZONE** - setting of [time zone](https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-TIME_ZONE) (Default: **Europe/Moscow**)

## How to launch on localhost

In the project directory, create a text file named **.env** with the following contents:

```

DJANGO_SECRET_KEY=your_secret_key
DATABASE_URL=postgresql://user:password@host:port/database

```

and then run the following command:

```bash

$ python manage.py runserver

```

After that you can visit to main page on [http://localhost:8000/](http://localhost:8000/). 

# Project Goals

The code is written for educational purposes - this is a lesson in the course on Python and web development on the site [Devman](https://dvmn.org).