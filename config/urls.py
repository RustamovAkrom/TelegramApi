from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

from .swagger import swager_urlpatterns


urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
]

urlpatterns_i18n = i18n_patterns(
    path(_("admin/"), admin.site.urls),
    path(_("api/v1/account/"), include("apps.account.urls")),
    path(_("api/v1/telegram/"), include("apps.telegram.urls")),
)

urlpatterns_i18n += swager_urlpatterns
urlpatterns += urlpatterns_i18n

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

