# Unagi blog

A Django-based blog application.

## Description

Here is the source code for my blog, which I will be updating regularly from now.

It is nothing more than Django and it is kept quite simple. I use the Django admin panel to create and update blog posts. I also made a custom preview of the
article I am writing on the admin panel using simple vanilla JS and HTML.

## Stack

- Django
- Postgres
- JS

## Contact

For any questions or feedback, please contact [lucas.beley@hotmail.fr](mailto:lucas.beley@hotmail.fr).


## Launch

Install dependencies if not already done.
```sh
pip install -r requirements.txt
```

Setup the env file using the `.env.dist` file.
```sh
cp .env.dist .env       # update it if required
```

For dev purpose, you can run the docker-compose file to setup a database.
```sh
docker-compose up -d
```

Then, simply runserver
```sh
cd unagi/
python manage.py runserver --settings unagi.settings_dev
```