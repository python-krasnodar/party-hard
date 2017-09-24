# Party Hard

An example of an application on Django.

## About application

This application allows us to invite friends from the social network vkontakte. The user who came to the page of the site will be offered to log in through the social network vkontakte. After authorization, if he has not previously responded to the invitation, it will be proposed to confirm or decline participation in the party. If he previously answered a question, he will be asked to delete and answer again.

The party organizer can view all of these answers. Also, the organizer will receive email notifications about all actions of other users.

In repository https://github.com/memclutter/party-hard-devops, collected everything necessary to deploy the project.

## Requirements

This project uses the following third-party dependencies:

* Python 3.6
* Django 1.11
* PostgreSQL 9.6
* RabbitMQ 3.5.7

## Local deployment

Create a virtual environment:

```sh
virtualenv -p python3.6 .venv
source .venv/bin/activate
pip instal -r requirements.txt
```

Create an `.env` file with content similar to the `.env.dist` file. It will be necessary to substitute your secret data to connect to the PostgreSQL database (`DATABASE_URL`) and the message broker RabbitMQ (`CELERY_BROKER_URL`). 

Go to https://vk.com/editapp?act=create and select "Website", set the name. Received "Application ID" and "Secure Key" should be written in the file .env (`SOCIAL_AUTH_VK_OAUTH2_KEY`, `SOCIAL_AUTH_VK_OAUTH2_SECRET`). 

Applying Migrations to the Database.

```sh
cd app
./manage.py migrate
```

Load fixture data (optional).

```sh
./manage.py loaddata dictionaries/drinks.json
```

Run local web server

```sh 
./manage.py runserver
```

and in the other console we run `celery`

```sh 
celery -A config worker -l info
```
