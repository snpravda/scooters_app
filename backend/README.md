# Project Setup

### Create virtualenv
```shell
cd backend
python3 -m venv venv
```
### Activate venv
Mac/Linux:
```shell
source venv/bin/activate
```
Windows:
```shell
venv\Scripts\activate
```
### Install requirements and run db migrations
```shell
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```
### Create admin user
```shell
python manage.py createsuperuser
```
### Run app
```shell
python manage.py runserver
```
Go to http://127.0.0.1:8000/admin/ for creating providers and scooters