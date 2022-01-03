from django.urls import path

from . import views

urlpatterns = [
    path('arbs', views.arbs, name='arbs'),
    path('scrape', views.scrape, name='scrape'),
]