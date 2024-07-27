INSTALLED_PACKAGES_APPS = [
    "jazzmin",
    "rest_framework",
    "drf_yasg",
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "modeltranslation",
    "phonenumber_field",
]

DEFAULT_DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

PROJECT_DJANGO_APPS = [
    "apps.telegram.apps.TelegramConfig",
    "apps.shared.apps.SharedConfig",
    "apps.account.apps.AccountConfig",
]
