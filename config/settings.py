import os

from pathlib import Path

from dotenv import load_dotenv

from config._config_ import *

from django.utils.translation import gettext_lazy as _

load_dotenv(".env")

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = os.getenv("DEBUG") in ["true", "True", "1"]

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

INSTALLED_APPS = DEFAULT_DJANGO_APPS + INSTALLED_PIP_APPS + PROJECT_CREATING_APPS


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

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR.joinpath("templates")],
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


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR.joinpath("db.sqlite3"),
    }
}


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": ...,
#         "USER": ...,
#         "PASSWORD": ...,
#         "HOST": ...,
#         "PORT": ...,
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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Tashkent"

USE_I18N = True
USE_L10N = True

USE_TZ = True

PHONENUMBER_REGION = "UZ"

STATIC_URL = "static/"
# STATIC_ROOT = BASE_DIR.joinpath("static")
STATICFILES_DIRS = [BASE_DIR.joinpath("static")]

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR.joinpath("media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

