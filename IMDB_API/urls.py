from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('list/', views.watchPlatformList.as_view(), name='movie_list'),
    path('list/<int:pk>/', views.watchPlatformListUpdate.as_view(), name='movie_detail'),
    path('stream/list/', views.StreamPlatformList.as_view(), name='stream_platform_list'),
    path('stream/list/<int:pk>/', views.streamPlateformUpdate.as_view(), name='stream_detail'),
    path('reviews/list', views.reviewList.as_view(), name='reviews'),
    path('reviews/list/<int:pk>/', views.reviewListUpdate.as_view(), name='review_detail'),
    path('api/list/<int:pk>/reviews/', views.reviewList.as_view(), name='reviews'),
]

urlpatterns = format_suffix_patterns(urlpatterns)