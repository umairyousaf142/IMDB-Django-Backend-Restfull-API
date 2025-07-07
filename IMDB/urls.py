from django.contrib import admin
from django.urls import path, include
from IMDB_API import views

urlpatterns = [
    path('', views.api_root),
    path('admin/', admin.site.urls),
    path('api/', include('IMDB_API.urls')),
]

