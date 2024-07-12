import os

from pathlib import Path

from dotenv import load_dotenv

from config._config_ import *

from django.utils.translation import gettext_lazy as _

load_dotenv(".env")

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = os.getenv("DEBUG") in ["true", "True", "1"]

ALLOWED_HOSTS = []

INSTALLED_APPS = INSTALLED_PACKAGES_APPS + DEFAULT_DJANGO_APPS + PROJECT_DJANGO_APPS


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'django.middleware.locale.LocaleMiddleware', # translation middleware
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "config.urls"

TEMPLATES_DIR = BASE_DIR.joinpath("templates")

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR.joinpath("db.sqlite3"),
    }
}

# DATABASES = {
#     "default": {
#        "ENGINE": "django.db.backends.postgresql",
#        "NAME": os.getenv("NAME"),
#        "USER": os.getenv("USER"),
#        "PASSWORD": os.getenv("PASSWORD"),
#        "HOST": os.getenv("HOST"),
#        "PORT": os.getenv("PORT"),
#        "CONN_MAX_AGE": 600,  # Время жизни соединения (в секундах)

#     }
# }


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "account.User"

LANGUAGES  = (
    ("en", _("English")),
    ("ru", _("Russia")),
    ("uz", _("Uzbek")),
)

LOCALE_PATHS = [
    BASE_DIR.joinpath("locale"),
]

LANGUAGE_CODE = "en"

TIME_ZONE = "Asia/Tashkent"

USE_I18N = True
USE_L10N = True

USE_TZ = True

PHONENUMBER_REGION = "UZ" # defaul region phone

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR.joinpath("staticfiles")
STATICFILES_DIRS = [BASE_DIR.joinpath("static")]

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR.joinpath("media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTHENTICATION_TOKEN = os.getenv("AUTHENTICATION_TOKEN") # null True

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE

# Logging
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': 'debug.log',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     },
# }