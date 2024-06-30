REST_FRAMEWORK = {}

if not "config.settings.DEBUG":
    REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] = ("rest_framework.permissions.IsAuthenticated", )

REST_FRAMEWORK['DEFAULT_SCHEMA_CLASS'] = "drf_spectacular.openapi.AutoSchema"
REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = ("rest_framework_simplejwt.authentication.JWTAuthentication", )



SPECTACULAR_SETTINGS = {
    "SWAGGER_UI_DIST": "SIDECAR",
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
    "TITLE": "Django Rest API",
    "DESCRIPTION": "Django Rest API",
}

