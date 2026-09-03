"""URLconf raiz del proyecto mysite.

Parte 1: se incluye el URLconf de la app polls con include().
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
