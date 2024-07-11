REST_FRAMEWORK = {
    # Render
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],

    # Parser
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ],

    # Authentication
    'DEFAULT_AUTHENTICATION_CLASSES': [
        "rest_framework_simplejwt.authentication.JWTAuthentication", 
    ],

    # Permission
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],

    # Default Rest Framework Schema
    'DEFAULT_SCHEMA_CLASS':"drf_spectacular.openapi.AutoSchema",

    # Pagination
    'DEFAULT_PAGINATION_CLASS': None,
    'PAGE_SIZE': None,

    'DEFAULT_FILTER_BACKENDS': [],
    # Filtering
    'SEARCH_PARAM': 'search',
    'ORDERING_PARAM': 'ordering',

    # Authentication
    'UNAUTHENTICATED_USER': 'django.contrib.auth.models.AnonymousUser',
    'UNAUTHENTICATED_TOKEN': None,

}

if not "config.settings.DEBUG":
    REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] = ["rest_framework.permissions.IsAuthenticated", ]



SPECTACULAR_SETTINGS = {
    "SWAGGER_UI_DIST": "SIDECAR",
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
    "TITLE": "Django Rest API",
    "DESCRIPTION": "Django Rest Telegram Api",
    "VERSION": "v1"
}

SPECTACULAR_SETTINGS_ACTIVE = True # Activator 
SWAGERS_MULTILANGUAGES = True # swaggers multilanguage activator