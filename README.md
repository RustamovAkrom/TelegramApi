# TelegramApi 
**Django DRF**

### ***Runing Commands:***

1. Create Enviroment.
~~~bash
python3 -m venv env
source env/bin/activate
~~~
2. Pip install python enterpretator requirements.txt
~~~bash
pip3 install -r requirements.txt
~~~
3. Create `.env` file in workdir and add code for example on `.env-example`.
~~~sh
#!/bin/bash/
#### SECRET KEYS ####
SECRET_KEY="..." # your django secret key

#### DEBUG ####
DEBUG="True" # default True

#### Database ####
NAME="..." # database name
USER="..." # database user
PASSWORD="..." # database password
HOST="localhost" # database host default localhost
PORT=5432 # database port default 5432

#### TEST AUTHENTICATIE JWT TOKEN ##### 
AUTHENTICATION_TOKEN="..." # JWT token
~~~
4. Create all tables in database.
~~~bash
python3 manage.py makemigrations
python3 manage.py migrate
~~~
5. Create super user.
~~~bash
python3 createuser.py
~~~
5. Run
~~~bash
python3 manage.py runserver
~~~