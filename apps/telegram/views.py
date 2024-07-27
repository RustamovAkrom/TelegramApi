from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _


class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request):
        text = _("Welcome to my site.")
        return render(request, "index.html", {"text": text})
