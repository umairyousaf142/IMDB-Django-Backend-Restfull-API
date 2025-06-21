from django.shortcuts import render, HttpResponse
from .serializers import *


def movie_list(request):

    stream_movies = stramPlatform.objects.all()
    serialized = streamPlatformSerializer(stream_movies, many=True)
    if request.method == 'GET':
        return HttpResponse(serialized.data, content_type='application/json')

def movie_detail(request, pk):
    movies = watchList.objects.get(pk=pk)
    serialized = watchListSerializer(movies)
    if request.method == 'GET':
        return HttpResponse(serialized.data, content_type='application/json')
    return HttpResponse(f"This is the detail view for movie with ID: {pk}.")