from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *


def movie_list(request):

    stream_movies = stramPlatform.objects.all()
    serialized = streamPlatformSerializer(stream_movies, many=True)
    # if request.method == 'GET':
    return JsonResponse(serialized.data, safe = False)

def movie_detail(request, pk):

    movies = watchList.objects.get(pk=pk)
    serialized = watchListSerializer(movies)
    return JsonResponse(serialized.data)



class StreamPlatformList(APIView):
    def get(self, request):
        
        stream_platforms = stramPlatform.objects.all()

        serialized = streamPlatformSerializer(stream_platforms, many=True)
        
        return Response(serialized.data, status = status.HTTP_200_OK)
        

    def post(self, request):
        data = request.data
        serialized = streamPlatformSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


def stream_detail(request, pk):

    stream_platform = stramPlatform.objects.get(pk=pk)
    serialized = streamPlatformSerializer(stream_platform)
    return JsonResponse(serialized.data)