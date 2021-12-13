from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('arbs/', include('arbs.urls')),
    path('admin/', admin.site.urls),
]