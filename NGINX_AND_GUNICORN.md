Чтобы запустить Django проект на компьютере с Ubuntu и настроить его с Nginx, выполните следующие шаги:

### 1. Установите зависимости

```bash
sudo apt update
sudo apt install python3-pip python3-dev libpq-dev nginx curl
```

### 2. Установите и настройте виртуальное окружение

```bash
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv
mkdir ~/myproject
cd ~/myproject
virtualenv myprojectenv
source myprojectenv/bin/activate
```

### 3. Установите Django и Gunicorn

```bash
pip install django gunicorn
```

### 4. Создайте Django проект

```bash
django-admin startproject myproject .
```

### 5. Настройте базу данных (при необходимости)

Если вы используете PostgreSQL, установите и настройте её:

```bash
sudo apt install postgresql postgresql-contrib
```

Создайте базу данных и пользователя:

```sql
CREATE DATABASE myproject;
CREATE USER myprojectuser WITH PASSWORD 'password';
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
```

Настройте `settings.py` для использования PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

### 6. Выполните миграции и создайте суперпользователя

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 7. Настройте Gunicorn для сервера

Создайте файл Gunicorn systemd service:

```bash
sudo nano /etc/systemd/system/gunicorn.service
```

Добавьте следующее:

```ini
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=your_user
Group=www-data
WorkingDirectory=/home/your_user/myproject
ExecStart=/home/your_user/myproject/myprojectenv/bin/gunicorn --workers 3 --bind unix:/home/your_user/myproject/myproject.sock myproject.wsgi:application

[Install]
WantedBy=multi-user.target
```

Замените `your_user` на ваше имя пользователя. Сохраните и закройте файл.

Запустите и включите Gunicorn:

```bash
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

### 8. Настройте Nginx

Создайте файл конфигурации для Nginx:

```bash
sudo nano /etc/nginx/conf.d/nginx.conf
```

Добавьте следующее:

```nginx
server {
    listen 80;
    server_name your_domain_or_IP;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/your_user/myproject;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/your_user/myproject/myproject.sock;
    }
}
```

Сохраните и закройте файл.

Активируйте конфигурацию Nginx:

```bash
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

### 9. Настройте брандмауэр

Разрешите трафик на порты HTTP и HTTPS:

```bash
sudo ufw allow 'Nginx Full'
```

### 10. Проверьте проект

Теперь ваш Django проект должен быть доступен по вашему доменному имени или IP-адресу.

Поздравляю! Вы настроили Django проект на Ubuntu с использованием Nginx.

Чтобы настроить Nginx и Gunicorn для вашего Django проекта, следуйте этим шагам:
---
### 1. Установите зависимости

```bash
sudo apt update
sudo apt install python3-pip python3-dev libpq-dev nginx curl
```

### 2. Создайте и активируйте виртуальное окружение

```bash
mkdir ~/myproject
cd ~/myproject
python3 -m venv myprojectenv
source myprojectenv/bin/activate
```

### 3. Установите Django и Gunicorn

```bash
pip install django gunicorn
```

### 4. Создайте Django проект

```bash
django-admin startproject myproject .
```

### 5. Настройте базу данных (если необходимо) и выполните миграции

Если вы используете PostgreSQL, настройте `settings.py` и выполните миграции:

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6. Настройте Gunicorn

Создайте файл сервиса Gunicorn:

```bash
sudo nano /etc/systemd/system/gunicorn.service
```

Добавьте следующее:

```ini
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=your_user
Group=www-data
WorkingDirectory=/home/your_user/myproject
ExecStart=/home/your_user/myproject/myprojectenv/bin/gunicorn --workers 3 --bind unix:/home/your_user/myproject/myproject.sock myproject.wsgi:application

[Install]
WantedBy=multi-user.target
```

Замените `your_user` на ваше имя пользователя. Сохраните и закройте файл.

Запустите и включите Gunicorn:

```bash
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

### 7. Настройте Nginx

Создайте файл конфигурации для Nginx:

```bash
sudo nano /etc/nginx/sites-available/myproject
```

Добавьте следующее:

```nginx
server {
    listen 80;
    server_name your_domain_or_IP;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/your_user/myproject;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/your_user/myproject/myproject.sock;
    }
}
```

Сохраните и закройте файл.

Активируйте конфигурацию Nginx:

```bash
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

### 8. Настройте брандмауэр

Разрешите трафик на порты HTTP и HTTPS:

```bash
sudo ufw allow 'Nginx Full'
```

### 9. Настройка статических файлов

Настройте `settings.py` для работы со статическими файлами:

```python
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
```

Соберите статические файлы:

```bash
python manage.py collectstatic
```

Теперь ваш Django проект должен быть доступен по вашему доменному имени или IP-адресу.

### 10. Проверка и отладка

Если возникнут проблемы, проверьте журналы Nginx и Gunicorn:

```bash
sudo journalctl -u nginx
sudo journalctl -u gunicorn
```

Следуя этим шагам, вы сможете настроить и запустить ваш Django проект с использованием Gunicorn и Nginx на Ubuntu.