from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns
from ._config_ import rest_framework


schema_view = get_schema_view(
    openapi.Info(
        title="Blog Api",
        default_version="v1",
        description="Document Telegram Api",
        terms_of_service="https://example.com/terms/",
        contact=openapi.Contact(email="akromjonrustamov56@gmail.com"),
    ),
    public=True,
)

if rest_framework.SWAGERS_MULTILANGUAGES:
    if rest_framework.SPECTACULAR_SETTINGS_ACTIVE:
        
        swager_urlpatterns = i18n_patterns(
            path(_("schema/"), SpectacularAPIView.as_view(), name="schema"),
            path(_("swagger-ui/"), SpectacularSwaggerView.as_view(), name="swagger-ui"),
            path(_("reodoc/"), SpectacularRedocView.as_view(), name="redoc")
        )

    else:
        swager_urlpatterns = i18n_patterns(
            path(_("swagger-ui/"), schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
            path(_("redoc/"), schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
        )

else:
    if rest_framework.SPECTACULAR_SETTINGS_ACTIVE:
            
        swager_urlpatterns = [
            path("schema/", SpectacularAPIView.as_view(), name="schema"),
            path("swagger-ui/", SpectacularSwaggerView.as_view(), name="swagger-ui"),
            path("reodoc/", SpectacularRedocView.as_view(), name="redoc")
        ]

    else:
        swager_urlpatterns = [
            path("swagger-ui/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
            path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
        ]
