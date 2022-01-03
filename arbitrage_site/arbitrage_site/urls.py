from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('statistics/', include('arbitrage_statistics.urls')),
    path('admin/', admin.site.urls),
]