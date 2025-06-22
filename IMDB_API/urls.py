from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('list/', views.movie_list, name='movie_list'),
    path('list/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('stream/list/', views.StreamPlatformList.as_view(), name='stream_platform_list'),
    path('stream/list/<int:pk>/', views.stream_detail, name='stream_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)