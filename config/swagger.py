from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


swager_urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/v1/swager-ui/", SpectacularSwaggerView.as_view(), name="schema"),
    path("api/v1/reodoc/", SpectacularRedocView.as_view(), name="redoc")
]